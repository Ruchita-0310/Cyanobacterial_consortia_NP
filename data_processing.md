# Cyanobacterial Consortia MAGs: Long-read Metagenome Assembly and Genome Annotation
This document describes the workflow used to process Oxford Nanopore long reads and Illumina short reads from the DL1 soda lake metagenomic sample. The workflow includes basecalling, FASTQ conversion, long-read quality filtering, long-read assembly, hybrid polishing, MAG recovery, bin refinement, taxonomic classification, quality assessment, genome annotation, and coverage estimation.
## Overview
The sequencing run used the Ligation Sequencing Kit V14 (`SQK-LSK114`) and 1 µg of high molecular weight DNA. The run produced 73 POD5 files, corresponding to approximately 12.5 Gb of sequence data, with a read N50 of approximately 7.54 kb. Basecalling was performed with Dorado using the `sup` model and a minimum quality score of 8 on a GPU partition.
```text
POD5 files
   ↓
Dorado basecalling
   ↓
BAM to FASTQ conversion
   ↓
Long-read quality filtering with Chopper
   ↓
Long-read assembly with MetaMDBG
   ↓
Long-read polishing with Medaka
   ↓
Short-read polishing with Polypolish and Pypolca
   ↓
Binning and refinement with MetaWRAP
   ↓
Taxonomic classification with GTDB-Tk
   ↓
Genome quality assessment with CheckM2
   ↓
Genome annotation with MetaErg
   ↓
Coverage and sequencing depth estimation with CoverM
```
## Software used

| Step | Tools |
|---|---|
| Basecalling | Dorado |
| BAM to FASTQ conversion | bedtools |
| Long-read filtering | Chopper |
| Long-read assembly | MetaMDBG |
| Long-read polishing | Medaka |
| Short-read polishing | BWA-MEM, Polypolish, Pypolca |
| Binning and refinement | MetaWRAP, MetaBAT2, MaxBin2, CONCOCT |
| Taxonomic classification | GTDB-Tk v2.4.0 |
| Genome quality assessment | CheckM2 |
| Genome annotation | MetaErg |
| Coverage and sequencing depth | CoverM |

---
<details>
<summary><strong>1. Basecalling</strong> - Dorado</summary>

The Nanopore POD5 files were basecalled with Dorado using the `sup` model. A minimum quality score of 8 was applied during basecalling.

```bash
dorado basecaller \
    --min-qscore 8 \
    sup \
    pod5/ \
    > DL1_SodaLakes_basecalling.bam
```

Output:

```text
DL1_SodaLakes_basecalling.bam
```

</details>

---

<details>
<summary><strong>2. Convert BAM output to FASTQ</strong> - bedtools</summary>

The Dorado BAM output was converted to FASTQ using `bedtools bamtofastq`.

```bash
bedtools bamtofastq \
    -i DL1_SodaLakes_basecalling.bam \
    -fq DL1_SodaLakes_LongReads.fastq
```

Output:

```text
DL1_SodaLakes_LongReads.fastq
```

</details>

---

<details>
<summary><strong>3. Long-read quality control and filtering</strong> - Chopper</summary>

Long reads were filtered using Chopper. Reads were retained if they had a minimum quality score of 10 and a minimum length of 500 bp.

```bash
gunzip -c DL1_SodaLakes_LongReads.fastq.gz \
    | chopper -q 10 -l 500 \
    | gzip \
    > Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz
```

Output:

```text
Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz
```

</details>

---

<details>
<summary><strong>4. Long-read metagenome assembly</strong> - MetaMDBG</summary>

Filtered Nanopore reads were assembled using MetaMDBG.

```bash
metaMDBG asm \
    --out-dir metaMDBG_assembly_DL1 \
    --in-ont Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz \
    --threads 8
```

Output directory:

```text
metaMDBG_assembly_DL1/
```

</details>

---

<details>
<summary><strong>5. Long-read polishing</strong> - Medaka</summary>

The MetaMDBG contig file was decompressed before Medaka polishing. Medaka was run with the `--bacteria` option.

```bash
gzip -d metaMDBG_assembly_DL1/contigs.fasta.gz

medaka_consensus \
    -i Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz \
    -d metaMDBG_assembly_DL1/contigs.fasta \
    -o medaka.DL1.assembly.out \
    -t 6 \
    --bacteria
```

Output directory:

```text
medaka.DL1.assembly.out/
```

</details>

---

<details>
<summary><strong>6. Short-read polishing, step 1</strong> - BWA-MEM and Polypolish</summary>

Illumina short reads were mapped to the Medaka-polished assembly using BWA-MEM. The alignments were filtered and used for polishing with Polypolish.

```bash
bwa index medaka.DL1.assembly.out/consensus.fasta

bwa mem -t 16 -a \
    medaka.DL1.assembly.out/consensus.fasta \
    ../../../RB_6/SR/Li50127-RS-DL-1-RT_S16_R1.fastq.gz \
    > alignments_1.sam

bwa mem -t 16 -a \
    medaka.DL1.assembly.out/consensus.fasta \
    ../../../RB_6/SR/Li50127-RS-DL-1-RT_S16_R2.fastq.gz \
    > alignments_2.sam
```

Polypolish insert size filtering and polishing:

```bash
polypolish filter \
    --in1 alignments_1.sam \
    --in2 alignments_2.sam \
    --out1 filtered_1.sam \
    --out2 filtered_2.sam

polypolish polish \
    medaka.DL1.assembly.out/consensus.fasta \
    filtered_1.sam \
    filtered_2.sam \
    > medaka.polypolish.DL1.assembly.fasta
```

Output:

```text
medaka.polypolish.DL1.assembly.fasta
```

</details>

---

<details>
<summary><strong>7. Short-read polishing, step 2</strong> - Pypolca</summary>

The Polypolish-corrected assembly was further polished using Pypolca.

```bash
pypolca run \
    -a medaka.polypolish.DL1.assembly.fasta \
    -1 Li50127-RS-DL-1-RT_S16_R1.fastq.gz \
    -2 Li50127-RS-DL-1-RT_S16_R2.fastq.gz \
    -t 12 \
    -o medaka.polypolish.polca.DL1.assembly.fasta \
    --careful
```

Main output:

```text
medaka.polypolish.polca.DL1.assembly.fasta/pypolca_corrected.fasta
```

</details>

---

<details>
<summary><strong>8. Binning and bin refinement</strong> - MetaWRAP</summary>

Short reads were decompressed before running MetaWRAP binning. Binning was performed with MetaBAT2, MaxBin2, and CONCOCT, followed by MetaWRAP bin refinement.

Prepare short reads:

```bash
gunzip -c Li50127-RS-DL-1-RT_S16_R1.fastq.gz > DL1_SR_R1.fastq
gunzip -c Li50127-RS-DL-1-RT_S16_R2.fastq.gz > DL1_SR_R2.fastq
```

Run binning:

```bash
metawrap binning \
    -o Binning_pypolca_DL1 \
    -t 12 \
    -a medaka.polypolish.polca.DL1.assembly.fasta/pypolca_corrected.fasta \
    --metabat2 \
    --maxbin2 \
    --concoct \
    -m 40 \
    DL1_SR_R1.fastq \
    DL1_SR_R2.fastq
```

Run bin refinement:

```bash
metawrap bin_refinement \
    -o Refinement_pypolca_DL1 \
    -t 12 \
    -A Binning_pypolca_DL1/metabat2_bins/ \
    -B Binning_pypolca_DL1/maxbin2_bins/ \
    -C Binning_pypolca_DL1/concoct_bins/ \
    -c 50 \
    -x 10 \
    -m 40
```

Refined MAGs:

```text
Refinement_pypolca_DL1/metawrap_50_10_bins/
```

</details>

---

<details>
<summary><strong>9. Taxonomic classification</strong> - GTDB-Tk</summary>

Refined bins were classified using GTDB-Tk v2.4.0.

```bash
gtdbtk classify_wf \
    --genome_dir Refinement_pypolca_DL1/metawrap_50_10_bins/ \
    --out_dir gtdbtk_classify_wf \
    --cpus 8 \
    -x fa \
    --skip_ani_screen
```

Output directory:

```text
gtdbtk_classify_wf/
```

</details>

---

<details>
<summary><strong>10. Genome quality assessment</strong> - CheckM2</summary>

CheckM2 was used to estimate genome completeness and contamination.

```bash
checkm2 predict \
    -t 30 \
    -x fa \
    --input ./ \
    --output-directory ./CheckM2
```

Output directory:

```text
CheckM2/
```

</details>

---

<details>
<summary><strong>11. Genome annotation</strong> - MetaErg</summary>

Refined MAGs were annotated using MetaErg through a Singularity container. The MetaErg database directory and MAG directory were bound into the container.

```bash
\time singularity exec \
    --bind /work/ebg_lab/referenceDatabases/metaerg_db_V214:/databases \
    --bind /Refinement_pypolca_DL1/metawrap_50_10_bins:/data \
    --writable /work/ebg_lab/software/metaerg-v2.5.2/sandbox_metaerg_2.5.4/ \
    metaerg \
    --database_dir /databases \
    --contig_file /data \
    --file_extension .fa
```

</details>

---

<details>
<summary><strong>12. Coverage and sequencing depth</strong> - CoverM</summary>

CoverM was used to estimate coverage and sequencing depth for contigs, MAGs, and high-quality MAGs using both long reads and short reads.

### Long-read coverage

For the polished assembly:

```bash
coverm genome \
    --single Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz \
    --mapper minimap2-ont \
    --min-read-percent-identity 95 \
    --genome-fasta-files medaka.polypolish.polca.DL1.assembly.fasta/pypolca_corrected.fasta
```

For refined MAGs:

```bash
coverm genome \
    --single Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz \
    --mapper minimap2-ont \
    --min-read-percent-identity 95 \
    --genome-fasta-directory Refinement_pypolca_DL1/metawrap_50_10_bins/ \
    --genome-fasta-extension fa
```

For high-quality MAGs:

```bash
coverm genome \
    --single Filtered_500_10_DL1_SodaLakes_LongReads.fastq.gz \
    --mapper minimap2-ont \
    --min-read-percent-identity 95 \
    --genome-fasta-directory HQ_mags/ \
    --genome-fasta-extension fa
```

### Short-read coverage

For the polished assembly:

```bash
coverm genome \
    -1 /path/to/short/reads_R1.fastq.gz \
    -2 /path/to/short/reads_R2.fastq.gz \
    --mapper bwa-mem \
    --min-read-percent-identity 95 \
    --genome-fasta-files medaka.polypolish.polca.DL1.assembly.fasta/pypolca_corrected.fasta
```

For refined MAGs:

```bash
coverm genome \
    -1 /path/to/short/reads_R1.fastq.gz \
    -2 /path/to/short/reads_R2.fastq.gz \
    --mapper bwa-mem \
    --min-read-percent-identity 95 \
    --genome-fasta-directory Refinement_pypolca_DL1/metawrap_50_10_bins/ \
    --genome-fasta-extension fa
```

For high-quality MAGs:

```bash
coverm genome \
    -1 /path/to/short/reads_R1.fastq.gz \
    -2 /path/to/short/reads_R2.fastq.gz \
    --mapper bwa-mem \
    --min-read-percent-identity 95 \
    --genome-fasta-directory HQ_mags/ \
    --genome-fasta-extension fa
```

</details>
