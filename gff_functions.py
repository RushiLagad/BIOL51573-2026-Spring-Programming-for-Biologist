# gff_functions.py
# Module containing helper functions to parse FASTA and GFF3 files

def read_fasta(fasta_file):
    """
    Reads a genome FASTA file and returns the full DNA sequence as a string.
    Skips the first header line (starts with '>') and strips newline characters.
    """
    genome_sequence = ""

    with open(fasta_file, "r") as fh:
        for line in fh:
            # Skip the header line
            if line.startswith(">"):
                continue
            # Append each DNA line after stripping the newline
            genome_sequence += line.strip()

    return genome_sequence


def read_gff(gff_file, genome_sequence):
    """
    Reads and parses a GFF3 annotation file.
    Extracts:
      - The sequence ID from the last column (value after 'ID=')
      - The gene sequence using start and end coordinates (columns 4 and 5)
    Returns a list of (sequence_id, gene_sequence) tuples.
    """
    gene_records = []

    with open(gff_file, "r") as fh:
        for line in fh:
            # Skip comment/header lines
            if line.startswith("#"):
                continue

            line = line.strip()
            if not line:
                continue

            columns = line.split("\t")

            # GFF3 coordinates are 1-based and inclusive
            start = int(columns[3])
            end   = int(columns[4])

            # Extract the gene sequence from the genome (convert to 0-based index)
            gene_sequence = genome_sequence[start - 1 : end]

            # Extract sequence ID from the last column (e.g., "ID=cds-YP_009724389.1;...")
            attributes = columns[8]
            seq_id = ""
            for attribute in attributes.split(";"):
                if attribute.startswith("ID="):
                    seq_id = attribute.replace("ID=", "")
                    break

            gene_records.append((seq_id, gene_sequence))

    return gene_records


def write_output(gene_records, output_file="covid_genes.fasta"):
    """
    Writes extracted gene sequences to a FASTA-formatted output file.
    Each record is written as:
        >sequence_id
        SEQUENCE...
    """
    with open(output_file, "w") as out:
        for seq_id, gene_sequence in gene_records:
            out.write(f">{seq_id}\n")
            out.write(f"{gene_sequence}\n")

    print(f"Output written to: {output_file}")
