__author__ = "Paula Ramos-Silva"
__dateCreated__ = "25-11-2016"
__dateModified__ = "23-02-2024"

"""
Given a phylogenetic profile as input, COUNT computes posterior probabilities for every gene, including:
- gains, losses, expansions and contractions at tree edges
- presences and multiple members at tree nodes

This data is retrieved in a large table and processed here with total_posteriors_Count.py to estimate the total number
of gains, losses, presences, expansions, contractions and multiple presences in a readable format. 

usage: python total_posteriors_Count.py --posteriors [PATH TO POSTERIORS FILE]

References: 
1. Count - software for analysis of gene content evolution is available at 
http://www.iro.umontreal.ca/~csuros/gene_content/count.html

2. Miklós Csűös, Count: evolutionary analysis of phylogenetic profiles with parsimony and likelihood, Bioinformatics, 
Volume 26, Issue 15, August 2010, Pages 1910–1912, https://doi.org/10.1093/bioinformatics/btq315

3. Paula Ramos-Silva, Mónica Serrano, Adriano O Henriques, From Root to Tips: Sporulation Evolution and Specialization 
in Bacillus subtilis and the Intestinal Pathogen Clostridioides difficile, Molecular Biology and Evolution, Volume 36, 
Issue 12, December 2019, Pages 2714–2736, https://doi.org/10.1093/molbev/msz175

Tested with:
Python 2.7.1
Python 3.9.0

"""

import argparse
import pandas
import re
import math
import sys


def main():
    parser = argparse.ArgumentParser(description="Computes total presences, multi, gains, losses, expansions, "
                                                 "contractions from Posteriors - Count to Total_Posteriors_Count.txt")
    parser.add_argument('--posteriors', dest='posteriors',
                        help='path to csv file with posteriors, comment lines removed')

    args = parser.parse_args()

    posteriors_table = pandas.read_csv(args.posteriors, index_col=0, sep="\t", header=0)

    column_names = list(posteriors_table.columns.values)
    row_names = list(posteriors_table.index)

    column_types = [filter(lambda x: re.search(r':present', x), column_names),
                    filter(lambda x: re.search(r':multi', x), column_names),
                    filter(lambda x: re.search(r':gain', x), column_names),
                    filter(lambda x: re.search(r':loss', x), column_names),
                    filter(lambda x: re.search(r':expansion', x), column_names),
                    filter(lambda x: re.search(r':contraction', x), column_names)]

    for ct in column_types:
        count_total_by_node(row_names, ct, posteriors_table)


def count_total_by_node(rows, columns, posteriors):
    file = open('Total_Posteriors_Count.txt', 'a')
    for node in columns:

        total = 0

        for index in rows:

            if not math.isnan(posteriors.at[index, node]):
                total += float(posteriors.at[index, node])

        file.write('{}\t{}\n'.format(node, int(round(total))))
    file.close()


#########################

if __name__ == "__main__":
    usage = "python total_posteriors_Count.py -h"
    if len(sys.argv) == 1:
        print("Incorrect arguments.\nFor usage try: ", usage)
        sys.exit()
    main()
