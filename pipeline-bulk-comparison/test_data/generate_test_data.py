import os
import urllib.request
import gzip


inputs = [{'Genome': 'MGYG000012911',
  'FTP_download': 'ftp://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/human-gut/v2.0/all_genomes/MGYG0000039/MGYG000003937/genomes1/MGYG000012911.gff.gz'},
 {'Genome': 'MGYG000059903',
  'FTP_download': 'ftp://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/human-gut/v2.0/all_genomes/MGYG0000024/MGYG000002454/genomes1/MGYG000059903.gff.gz'},
 {'Genome': 'MGYG000064204',
  'FTP_download': 'ftp://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/human-gut/v2.0/all_genomes/MGYG0000024/MGYG000002478/genomes2/MGYG000064204.gff.gz'},
 {'Genome': 'MGYG000065573',
  'FTP_download': 'ftp://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/human-gut/v2.0/all_genomes/MGYG0000025/MGYG000002506/genomes2/MGYG000065573.gff.gz'},
 {'Genome': 'MGYG000072444',
  'FTP_download': 'ftp://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/human-gut/v2.0/all_genomes/MGYG0000025/MGYG000002506/genomes2/MGYG000072444.gff.gz'},
 {'Genome': 'MGYG000178727',
  'FTP_download': 'ftp://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/human-gut/v2.0/all_genomes/MGYG0000013/MGYG000001346/genomes4/MGYG000178727.gff.gz'},
 {'Genome': 'MGYG000199500',
  'FTP_download': 'ftp://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/human-gut/v2.0/all_genomes/MGYG0000000/MGYG000000060/genomes3/MGYG000199500.gff.gz'},
 {'Genome': 'MGYG000208235',
  'FTP_download': 'ftp://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/human-gut/v2.0/all_genomes/MGYG0000013/MGYG000001346/genomes5/MGYG000208235.gff.gz'},
 {'Genome': 'MGYG000276443',
  'FTP_download': 'ftp://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/human-gut/v2.0/all_genomes/MGYG0000025/MGYG000002506/genomes8/MGYG000276443.gff.gz'},
 {'Genome': 'MGYG000277295',
  'FTP_download': 'ftp://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/human-gut/v2.0/all_genomes/MGYG0000024/MGYG000002454/genomes3/MGYG000277295.gff.gz'}]


if __name__ == '__main__':
    os.makedirs('fna', exist_ok=True)
    for record in inputs:
        with urllib.request.urlopen(record['FTP_download']) as response:
            with gzip.GzipFile(fileobj=response) as gz:
                lines = gz.read().decode().split()
                for i, line in enumerate(lines):
                    if line.startswith('##FASTA'):
                        break
                with open(f"fna/{record['Genome']}.fna", 'w') as f:
                    f.write(''.join(lines[i+1:]))
    with open('summary.tsv', 'w') as f:
        f.write('id\tpath_fna\tpath_antismash\n')
        for record in inputs:
            f.write(f"{record['Genome']}\ttest_data/fna/{record['Genome']}.fna\t\n")
