import gzip
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
from pathlib import Path

fna_dirs = [fna_dir
            for fna_dir in Path('../raw_data/hmp-reference/ncbi_dataset/data/').iterdir()
            if fna_dir.is_dir()]

fna_dirs += [Path('../raw_data/jgi_gem_human/mags'),
            Path('../raw_data/EBI/human-gut-v2-0-1/fna'),
            Path('../raw_data/EBI/human-oral-v1-0/fna')]

output_table_name = 'files/output/all__genomes_GC_content.tsv'

cnt = 0
GC_content = dict()
for fna_dir in fna_dirs:
    for fna_file in fna_dir.iterdir():
        cnt += 1
        print(f'{cnt}. {fna_file}')
        with open(fna_file, 'rt') as handle:
            joined_seq = ''.join(str(record.seq)
                                 for record in SeqIO.parse(handle, 'fasta'))
            GC_content[fna_file.name] = gc_fraction(joined_seq)

with open(output_table_name, 'w') as out:
    out.write('Genome_name\tGC%\n')
    for name, gc in GC_content.items():
        out.write(f'{name}\t{100*gc}\n')
