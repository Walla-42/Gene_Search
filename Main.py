import Function_Dictionary as dic
from Bio import SeqIO
import os

print(dic.select_chromosome('Test_Genomes_Sequences/plasmodiumfalciparum_genome.fna'))

Target=  "MASAPGLAFANITLMLDLPQLPAIFFVNVRNNFKIFMNEIKQKTVEGEDIFYPHNRINLQNKQINKMGRTRKYSNNKEWIFGNPF"
# This target protein is a protein sequence in the above genome coding for an ATP synthase-associated protein. It has 1 exon and will work with this code, returning 'Found gene at position: 302825
# The above gene is located on chromosome 3. Just copy and paste the NC_000521.4 Plasmodium falciparum 3D7 genome assembly, chromosome: 3 when prompted. 

fasta_file = 'selected_chromosome.fna'


for record in SeqIO.parse(fasta_file, 'fasta'):
    print('\033[1;33m' + f"Record being analyzed: {record.description}" + '\033[0m')
    dic.search_gene(record.seq, Target)

os.remove(fasta_file)

