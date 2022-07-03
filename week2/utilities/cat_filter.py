import argparse
from collections import defaultdict
parser = argparse.ArgumentParser(description="Filter a fasttext training file by a label treshold")
parser.add_argument('--infile', type=argparse.FileType('r', encoding='UTF-8'), 
                      required=True)
parser.add_argument('--outfile', 
                      required=True)
parser.add_argument('--threshold', type=int, required=True)
args = parser.parse_args()

labeled_products = [line.split(" ") for line in args.infile.readlines()]

label2count = defaultdict(lambda: 0)

for line in labeled_products:
    label2count[line[0]] += 1

pruned_products = filter(lambda line: label2count[line[0]]>=args.threshold, labeled_products)
joined = map(lambda line: " ".join(line), pruned_products)

with open(args.outfile, 'w') as f:
    f.writelines(joined)
    f.close

