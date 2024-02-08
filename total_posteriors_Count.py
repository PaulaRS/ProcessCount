__author__ = 'Paula Ramos-Silva'
# ======================================================================
# Print total presences, multi, gains, losses, expansions, contractions from Posteriors - Count
# Count software for analysis of gene content evolution is
# available at http://www.iro.umontreal.ca/~csuros/gene_content/count.html
#
# ======================================================================
#
# Tested with:
#  Python 2.7.1
#  Python 3.9.0
#
# Created 25-11-2016
# Updated 23-08-2022

import argparse
import pandas
import re
import math
import sys

def main():
    parser = argparse.ArgumentParser(description="Print total presences, multi, gains, losses, expansions, contractions from Posteriors - Count")
    parser.add_argument('--posteriors', dest='posteriors', help='csv file with posteriors file with comment lines removed')

    args = parser.parse_args()

    posteriors_table = pandas.read_csv(args.posteriors, index_col=0, sep="\t", header=0)

    column_names = list(posteriors_table.columns.values)
    row_names = list(posteriors_table.index)

    column_types = []
    column_types.append(filter(lambda x:re.search(r':present', x), column_names))
    column_types.append(filter(lambda x:re.search(r':multi', x), column_names))
    column_types.append(filter(lambda x:re.search(r':gain', x), column_names))
    column_types.append(filter(lambda x:re.search(r':loss', x), column_names))
    column_types.append(filter(lambda x:re.search(r':expansion', x), column_names))
    column_types.append(filter(lambda x:re.search(r':contraction', x), column_names))

    for ct in column_types:
        countTotalbyNode(row_names, ct, posteriors_table)


def countTotalbyNode(rows, columns, posteriorsdf):

    for node in columns:

        total = 0

        for index in rows:

            if not math.isnan(posteriorsdf.at[index, node]):

                total += float(posteriorsdf.at[index, node])

        print ('{}\t{}'.format(node, int(round(total))))


#########################

if __name__=="__main__":
    usage = "python total_posteriors_Count.py --posteriors <your_posteriors_table.csv>"
    if len(sys.argv) != 1:
        print("Incorrect arguments.\nUsage is : ", usage)
        sys.exit()
    main()
