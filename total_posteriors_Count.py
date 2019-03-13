__author__ = 'polvicia'

# Print total presences, multi, gains, losses, expansions, contractions from Posteriors - Count
# Count software for analysis of gene content evolution is
# available at http://www.iro.umontreal.ca/~csuros/gene_content/count.html
#
# Created 25-11-2016
# Last updated 26-01-2017

import argparse
import pandas
import re
import math

def main():

    parser = argparse.ArgumentParser(description="Print total presences, multi, gains, losses, expansions, contractions from Posteriors - Count")
    parser.add_argument('--posteriors', dest='posteriors', help='csv file with posteriors file with comment lines removed')

    args = parser.parse_args()

    posteriors_table = pandas.read_csv(args.posteriors, index_col=0, sep="\t", header=0)

    column_names = list(posteriors_table.columns.values)
    row_names = list( posteriors_table.index)

    column_presences = filter(lambda x:re.search(r':present', x), column_names)
    column_multiple =  filter(lambda x:re.search(r':multi', x), column_names)
    column_gains = filter(lambda x:re.search(r':gain', x), column_names)
    column_losses = filter(lambda x:re.search(r':loss', x), column_names)
    column_expansions = filter(lambda x:re.search(r':expansion', x), column_names)
    column_contractions = filter(lambda x:re.search(r':contraction', x), column_names)

    count_total_bynode(row_names, column_presences, posteriors_table)
    count_total_bynode (row_names, column_multiple, posteriors_table)
    count_total_bynode(row_names, column_gains, posteriors_table)
    count_total_bynode(row_names, column_losses, posteriors_table)
    count_total_bynode(row_names, column_expansions, posteriors_table)
    count_total_bynode(row_names, column_contractions, posteriors_table)

def count_total_bynode(rows, columns, posteriorsdf):

    for node in columns:

        total = 0

        for index in rows:

            if not math.isnan(posteriorsdf.at[index,node]):

                total += float(posteriorsdf.at[index,node])

        print '{}\t{}'.format(node, int(round(total)))


#########################

if __name__=="__main__": main()




