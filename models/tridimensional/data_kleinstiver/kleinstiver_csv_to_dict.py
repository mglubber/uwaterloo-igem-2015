"""
Convert CSV of Cas9 mutants from Klienstiver et al. (2015), Nature, doi:10.1038/nature14592 into dict format
Included for reproducibility of data preparation
"""
import os
import csv

from cas9_mutants import PI_domain, PI_sec_structure, aa_group

def mutant_csv_to_string(mutant_csv_row):
    """ Parses a row of mutations in the Kleinstiver CSV to a string describing a dictionary

    Args: mutant_csv_row is the output of an iteration of a csv.reader object reading from the Kleinstiver_mutants CSVs
    Returns:
        A string that writes out a Python dictionary with entries "pam", "backbone" and "mutants", where "mutants" is a
        sub-dictionary with entries aa_idx, sec_structure, aa_init, aa_mut, aa_group_init, aa_group_mut
    """
    dict_string = "    {'pam': '"+ mutant_csv_row[0] + "', 'backbone': '" + mutant_csv_row[1]
    dict_string += "',\n     'mutations': ["

    # Find indices of mutations and annotate
    for idx, aa_mut in enumerate(mutant_csv_row[2:]):
        if aa_mut != '0':
            aa_idx = idx + 1097                 # Index shifted to protein idx, rather than PI domain idx
            aa_init = PI_domain[idx]            # Lookup in PI domain sequence from UniProt
            aa_group_init = aa_group[aa_init]   # Amino acid grouping, e.g. polar, hydrophobic
            aa_group_mut = aa_group[aa_mut]     # Amino acid grouping, e.g. polar, hydrophobic

            # There is likely a cleverer way to organize/search through the secondary structure data, but we're only
            # doing this once
            sec_structure = 'none'
            for ss in PI_sec_structure:
                if PI_sec_structure[ss][0] <= aa_idx <= PI_sec_structure[ss][1]:
                    sec_structure = ss

            dict_string += "{'aa_idx': " + str(aa_idx) + ", 'sec_structure': '" + sec_structure + "', "
            dict_string += "'aa_init': '" + aa_init + "', 'aa_mut': '" + aa_mut + "',\n"
            dict_string += "                     'aa_group_init': '" + aa_group_init + "', 'aa_group_mut': '"
            dict_string += aa_group_mut + "'},\n                    "

    return dict_string

# Begin kleinstiver_string, which will be copied as the variable cas9_mutants in kleinstiver_dict
kleinstiver_string = "mutants_kleinstiver = [\n"

# Open CSV files of mutants. Each row contains a vector with 0 where there is no mutation and AA codes for mutations
with open(os.path.normpath("./Kleinstiver_mutants_NGA.csv")) as csvfile:
    mutants_NGA = csv.reader(csvfile, delimiter=',')
    mutants_NGA.next()  # skip header
    for mutant_csv_row in mutants_NGA:
        kleinstiver_string += mutant_csv_to_string(mutant_csv_row)
        kleinstiver_string = kleinstiver_string[:-22] # remove redundant comma & spaces
        kleinstiver_string += "]},\n"

with open(os.path.normpath("./Kleinstiver_mutants_NGC.csv")) as csvfile:
    mutants_NGC = csv.reader(csvfile, delimiter=',')
    mutants_NGC.next()  # skip header
    for mutant_csv_row in mutants_NGC:
        kleinstiver_string += mutant_csv_to_string(mutant_csv_row)
        kleinstiver_string = kleinstiver_string[:-22] # remove redundant comma & spaces
        kleinstiver_string += "]},\n"

kleinstiver_string = kleinstiver_string[:-2] # remove redundant comma
kleinstiver_string += "]"
print kleinstiver_string # the output of this print statement becomes kleinstiver_mutants in kleinstiver_dict
