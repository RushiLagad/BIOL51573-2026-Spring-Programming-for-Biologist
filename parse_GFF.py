# parse_GFF.py
# Main script to parse a genome FASTA + GFF3 file and extract gene sequences
# Usage: python parse_GFF.py covid.fasta covid_genes.gff3

import argparse
import gff_functions

def main():
    # --- Set up command-line argument parsing ---
    parser = argparse.ArgumentParser(
        description="Extract gene sequences from a genome FASTA using a GFF3 annotation file."
    )
    parser.add_argument("fasta_file", help="Path to the genome FASTA file (e.g., covid.fasta)")
    parser.add_argument("gff_file",   help="Path to the GFF3 annotation file (e.g., covid_genes.gff3)")
    args = parser.parse_args()

    # --- Step 1: Read the genome sequence from FASTA ---
    print(f"Reading genome from: {args.fasta_file}")
    genome_sequence = gff_functions.read_fasta(args.fasta_file)
    print(f"  Genome length: {len(genome_sequence)} bp")

    # --- Step 2: Parse the GFF3 file and extract gene sequences ---
    print(f"Parsing GFF3 file: {args.gff_file}")
    gene_records = gff_functions.read_gff(args.gff_file, genome_sequence)
    print(f"  Found {len(gene_records)} gene features")

    # --- Step 3: Write extracted sequences to output FASTA ---
    gff_functions.write_output(gene_records, output_file="covid_genes.fasta")


if __name__ == "__main__":
    main()
