#parse out all protein ORF genes(CDS)from annotated FASTA file, then extract codon usage #take gb file as input, read by line, for CDS feature, extract the gene sequence, and write to a fasta file 
# mimivirus.gb does not contain transcription features, for other files in the future.. 
import os 
from Bio import SeqIO
print("Reading GenBank file and extracting CDS features...")
# initialize the input file
input_dir = "viral_genomes/"
input_file = os.path.join(input_dir, "Mimivirus.gb")
file_name = os.path.basename(input_file)
outfile_name = file_name.replace(".gb", "_cds.fasta")
output_dir = "outputs/"
# check input and output directories and files 
if not os.path.exists(input_file):
    print(f"Error: input file not found: {input_file}")
    exit(1)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
# CDS feature extraction and writing to output file 
print(f"Reading GenBank file {input_file} and extracting CDS features...")
count = 0
with open(f"{output_dir}/{outfile_name}", "w") as output_file:
    for record in SeqIO.parse(input_file, "genbank"):
        for feature in record.features:
            if feature.type == "CDS":
                # extract DNA sequence of the CDS feature
                cds_seq = feature.extract(record.seq)
                # extract quantifiers for gene id and product 
                gene_id = feature.qualifiers.get("locus_tag", ["unknown"])[0]
                product = feature.qualifiers.get("product", ["unknown"])[0]
                #writing to fasta file, with the gene id and product in the header
                output_file.write(f">{gene_id} {product}\n{cds_seq}\n")
                count += 1
print(f"Extracted {count} CDS features to outputs/{outfile_name}")
