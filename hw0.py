from Bio import Entrez
import fileinput
def find_genes(sequence):
    genes = []
    in_gene = False
    gene_start = 0
    gene_name = ""
    for i in range(len(sequence)):
        codon = sequence[i:i+3]
        if codon == startCodon and not in_gene:
            in_gene = True
            gene_start = i
        elif codon in stopCodon and in_gene:
            in_gene = False
            gene_name = f"Gene_{len(genes) + 1}"
            genes.append((gene_start, i+3, gene_name))
    return genes

a = fileinput.input(files='input_fasta.fasta')

startCodon = 'ATG'
stopCodon = ['TAA', 'TAG', 'TGA']

gene_coordinates = []
for sequence in a:
    sequence = sequence.strip()
    if sequence.startswith('>'):
        continue
    genes_in_sequence = find_genes(sequence)
    for gene in genes_in_sequence:
        gene_coordinates.append(gene)
with open('output_genes.bed', 'w') as bed_file:
    for start, end, name in gene_coordinates:
        bed_file.write(f'{start}\t{end}\t{name}\n')
