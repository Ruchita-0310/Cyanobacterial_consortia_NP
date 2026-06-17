# Soda Lake Metagenome Assembly and MAG Analysis

This repository documents the workflow used to process Oxford Nanopore and Illumina sequencing data from a soda lake microbial community, generate a long-read metagenomic assembly, polish the assembly, recover metagenome-assembled genomes, classify bins, annotate genomes, and calculate sequencing depth and coverage.

The full step-by-step workflow is provided in:

[`data_analysis.md`](data_analysis.md)

## Workflow summary

```text
POD5 files
   ↓
Dorado basecalling
   ↓
BAM to FASTQ conversion
   ↓
Long-read quality filtering with Chopper
   ↓
Long-read metagenome assembly with MetaMDBG
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
## Repository structure
```text
.
├── README.md
└── data_analysis.md
```
## Main tools

| Step | Tools |
|---|---|
| Basecalling | Dorado |
| FASTQ conversion | bedtools |
| Long-read filtering | Chopper |
| Long-read assembly | MetaMDBG |
| Long-read polishing | Medaka |
| Short-read polishing | BWA-MEM, Polypolish, Pypolca |
| Binning and refinement | MetaWRAP, MetaBAT2, MaxBin2, CONCOCT |
| Taxonomic classification | GTDB-Tk |
| Genome quality assessment | CheckM2 |
| Genome annotation | MetaErg |
| Coverage estimation | CoverM |
