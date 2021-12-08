# About ProcessCount

This repository constains the python script **total_posteriors_Count.py** to calculate the total gene presences, multi, gains, losses, expansions, contractions ocurring per each branch/node in a phylogenetic tree. 

Input file is the table resulting from Posteriors analysis made with the software Count:
http://www.iro.umontreal.ca/~csuros/gene_content/count.html

# Before running the script

Install the following python packages: argparse, pandas, re, math

# Running the script

./total_posteriors_Count.py --posteriors <Posteriors_from_Count.csv>

# Suggested citation

Paula Ramos-Silva, Mónica Serrano, Adriano O Henriques, From Root to Tips: Sporulation Evolution and Specialization in Bacillus subtilis and the Intestinal Pathogen Clostridioides difficile, Molecular Biology and Evolution, Volume 36, Issue 12, December 2019, Pages 2714–2736, https://doi.org/10.1093/molbev/msz175
