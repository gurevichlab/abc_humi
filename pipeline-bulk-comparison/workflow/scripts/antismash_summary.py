import os
import sys
import pandas as pd
import chompjs
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


def parse_regions_js(as_output_dir):
    fn = os.path.join(as_output_dir, 'regions.js')
    if not os.path.isfile(fn):
        return []
    
    with open(fn) as f:
        data = chompjs.parse_js_object(f.read())
    
    rows = []
    for rec in data:
        for i, r in enumerate(rec['regions']):
            gbk = f"{rec['seq_id']}.region{i+1:03}.gbk"
            rows.append({
                'Seq_ID': rec['seq_id'],
                'Anchor': r['anchor'],
                'GBK': gbk
            })
    return rows


def get_gbk_data(gbk_file):
    genome_record = SeqIO.read(gbk_file, "genbank")
    num_genes = len([feature for feature in genome_record.features if feature.type == "CDS"])
    for feature in genome_record.features:
        if feature.type == "region":
            # format [1:100](+)
            coords = list(map(int, str(feature.location)[1:-4].split(':')))
            gc = gc_fraction(genome_record.seq)
            return {'Length': max(coords) - min(coords),
                    'Gene_Count': num_genes,
                    'GC_BGC': f'{100 * gc:.2f}',
                    'From': coords[0],
                    'To': coords[1],
                    'BGC_Type': ','.join(feature.qualifiers['product']),
                    'Completeness': 'Fragmented' if feature.qualifiers['contig_edge'] == ['True'] else 'Complete'}


def scrap_as_files(as_output_dir):
    res = []
    for f in os.listdir(as_output_dir):
        if f.endswith('.gbk') and 'region' in f:
            _path = os.path.join(as_output_dir, f)
            gbk_data = get_gbk_data(_path)
            res.append({'GBK': f, **gbk_data})
    return res


def main():
    as_output_dir = sys.argv[1]
    df_regions = pd.DataFrame(parse_regions_js(as_output_dir), columns=['Seeq_ID', 'Anchor', 'GBK'])
    df_gbk = pd.DataFrame(scrap_as_files(as_output_dir), columns=['GBK', 'Length', 'From', 'To', 'BGC_Type', 'Completeness'])
    df_gbk = pd.merge(df_gbk, df_regions, on='GBK')
    df_gbk['Path_antismash'] = df_gbk['GBK'].map(lambda x: os.path.join(as_output_dir, x))
    df_gbk.to_csv(sys.argv[2], index=False, sep='\t')

if __name__ == '__main__':
    main()