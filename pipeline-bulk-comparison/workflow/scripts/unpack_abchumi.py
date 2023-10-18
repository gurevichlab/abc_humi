import os
import sys
import gzip
from Bio import SeqIO


def main():
    if len(sys.argv) < 3:
        print(f'Usage: {sys.argv[0]} databse.gbk.gz output_dir')
        return
    
    path_in = sys.argv[1]
    path_out = sys.argv[2]
    
    os.makedirs(path_out)
    
    with gzip.open(path_in, 'rt') as f:
        for record in SeqIO.parse(f, 'gb'):
            idx = record.id
            if idx.startswith('HMBGC'):
                with open(os.path.join(path_out, f'{idx}.gbk'), 'w') as fout:
                    fout.write(record.format('gb'))
    

if __name__ == '__main__':
    main()