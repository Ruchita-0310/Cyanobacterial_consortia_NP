## Basecalling
The sequencing run was performed using the Ligation Sequencing Kit V14 (SQK-LSK114) and 1 µg of HMW DNA. 73 pod5 files were obtained (~12.5 Gb) an N50 aprrox 7.54Kb. For basecalling, I ran Dorado basecaller with the sup model and set a quality limit of 8 using GPU partition bigmem gpu:1
```
####### Run your script #########################
dorado basecaller --min-qscore 8 sup pod5/ > DL1_SodaLakes_basecalling.bam
```
## Convert .bam output to .fastq
```
####### Run your script #########################
bedtools bamtofastq -i DL1_SodaLakes_basecalling.bam -fq DL1_SodaLakes_LongReads.fastq
```
## Quality control for Long reads
Chopper
```
####### Run your script #########################
gunzip -c DL1_SodaLakes_LongReads.fastq.gz | chopper -q 10 -l 500 | gzip > Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz
```
## Long-read Assembly
MetaMDBG
```
####### Run your script #########################
metaMDBG asm --out-dir metaMDBG_assembly_DL1 --in-ont Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz --threads 8
```
## Polishing - MEDAKA
Unzip files before running MEDAKA
```
####### Run your script #########################
gzip -d metaMDBG_assembly_DL1/contigs.fasta.gz
medaka_consensus -i Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz -d metaMDBG_assembly_DL1/contigs.fasta \
-o medaka.DL1.assembly.out -t 6 --bacteria
```
## Polishing - Short reads
The first step is polishing using Polypolish
```
####### Run your script #########################
bwa index medaka.DL1.assembly.out/consensus.fasta
bwa mem -t 16 -a medaka.DL1.assembly.out/consensus.fasta ../../../RB_6/SR/Li50127-RS-DL-1-RT_S16_R1.fastq.gz > alignments_1.sam
bwa mem -t 16 -a medaka.DL1.assembly.out/consensus.fasta ../../../RB_6/SR/Li50127-RS-DL-1-RT_S16_R2.fastq.gz > alignments_2.sam

###### Polypolish insert size filter ############
polypolish filter --in1 alignments_1.sam --in2 alignments_2.sam --out1 filtered_1.sam --out2 filtered_2.sam
polypolish polish medaka.DL1.assembly.out/consensus.fasta filtered_1.sam filtered_2.sam > medaka.polypolish.DL1.assembly.fasta
```
The second step was using Pypolca.
```
####### Run your script #########################
pypolca run -a medaka.polypolish.DL1.assembly.fasta \
-1 Li50127-RS-DL-1-RT_S16_R1.fastq.gz -2 Li50127-RS-DL-1-RT_S16_R2.fastq.gz \
-t 12 -o medaka.polypolish.polca.DL1.assembly.fasta --careful
```
## Binning and Refinement
Using MetaWRAP
```
###### Run your script #########################
##GunZIp in case are in .gz
gunzip -c Li50127-RS-DL-1-RT_S16_R1.fastq.gz > DL1_SR_R1.fastq
gunzip -c Li50127-RS-DL-1-RT_S16_R2.fastq.gz > DL1_SR_R2.fastq

## BINNING ##
metawrap binning -o Binning_pypolca_DL1 -t 12 -a medaka.polypolish.polca.DL1.assembly.fasta/pypolca_corrected.fasta \
--metabat2 --maxbin2 --concoct -m 40 DL1_SR_R1.fastq DL1_SR_R2.fastq

## BIN REFINEMENT ##
metawrap bin_refinement -o Refinement_pypolca_DL1 -t 12 -A Binning_pypolca_DL1/metabat2_bins/ \
-B Binning_pypolca_DL1/maxbin2_bins/ -C Binning_pypolca_DL1/concoct_bins/ -c 50 -x 10 -m 40
```
## Taxonomic classification
GTDB-Tk v2.4.0
```
####### Run your script #########################
gtdbtk classify_wf --genome_dir Refinement_pypolca_DL1/metawrap_50_10_bins/ \
--out_dir gtdbtk_classify_wf --cpus 8 -x fa --skip_ani_screen
```
## CheckM2
```
####### Run your script #########################
checkm2 predict -t 30 -x fa --input ./ --output-directory ./CheckM2 
```
## Annotation
MetaErg
```
\time  singularity exec --bind /work/ebg_lab/referenceDatabases/metaerg_db_V214:/databases --bind /Refinement_pypolca_DL1/metawrap_50_10_bins:/data  --writable /work/ebg_lab/software/metaerg-v2.5.2/sandbox_metaerg_2.5.4/ metaerg --database_dir /databases --contig_file /data --file_extension .fa
```
## Coverage & sequencing depth
CoverM
```
#for long reads
#for contigs
coverm genome --single Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz --mapper minimap2-ont --min-read-percent-identity 95 --genome-fasta-files medaka.polypolish.polca.DL1.assembly.fasta/pypolca_corrected.fasta
#for MAGS
coverm genome --single Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz --mapper minimap2-ont --min-read-percent-identity 95 --genome-fasta--directory Refinement_pypolca_DL1/metawrap_50_10_bins/ --genome-fasta-extension fa
#for HQMAGs
coverm genome --single Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz --mapper minimap2-ont --min-read-percent-identity 95 --genome-fasta--directory HQ_mags/ --genome-fasta-extension fa
#for short reads
#for contigs
coverm genome -1 /path/to/short/reads -2 /path/to/short/reads --mapper bwa-mem --min-read-percent-identity 95 --genome-fasta-files medaka.polypolish.polca.DL1.assembly.fasta/pypolca_corrected.fasta
#for MAGS
coverm genome -1 /path/to/short/reads -2 /path/to/short/reads --mapper bwa-mem --min-read-percent-identity 95 --genome-fasta--directory Refinement_pypolca_DL1/metawrap_50_10_bins/ --genome-fasta-extension fa
#for HQMAGs
coverm genome -1 /path/to/short/reads -2 /path/to/short/reads --mapper bwa-mem --min-read-percent-identity 95 --genome-fasta--directory HQ_mags/ --genome-fasta-extension fa
```
