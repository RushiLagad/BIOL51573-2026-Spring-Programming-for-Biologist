# Programming for Biologists (BIOL 51573), Spring 2026

Coursework from BIOL 51573 at the University of Arkansas.

## parse_GFF.py

Pulls each gene's sequence out of a genome using its GFF3 annotation.

```bash
python parse_GFF.py genome.fasta annotation.gff3
```

It reads the genome FASTA, takes the start and end of each feature in the GFF3, slices out the sequence and writes everything to `covid_genes.fasta`. The helper functions are in `gff_functions.py`. `covid_genes.fasta` in this repo is the output from the SARS-CoV-2 genome used in class.
