"""
Python variables relevant to the Cas9 mutants described by Klienstiver et al. (2015), Nature, doi:10.1038/nature14592
Contains the variables:
    PI_domain: string, WT PI domain (AA 1099-1368) from UniProt (http://www.uniprot.org/uniprot/Q99ZW2) + AAs 1097, 1098
    PI_sec_structure: dict with format 'type_#' : (start, end), secondary structure within PI domain from UniProt
    aa_groups: dict, single letter codes of 20 amino acids and their groups, which are "hydrophobic", "acidic", "basic",
        "polar" and "specialcase". Note that the classifications of methionine (M), tryptophan (W) and tyrosine
        (Y) are ambiguous
    kleinstiver_mutants: list of dictionaries with keys "pam", "backbone" and "mutations". Each list entry is a
        different cas9 mutant from Kleinstiver et al. Generated from the CSVs using kleinstiver_csv_to_dict.py.
"""

PI_domain = ('KTEVQTGGFSKESILPKRNSDKLIARKKDWDPKKYGGFDSPTVAYSVLVVAKVEKGKSKKLKSVKELLGITIMERSSFEKNPIDFLEAKGYKEVKKDLIIKLPKY'
             'SLFELENGRKRMLASAGELQKGNELALPSKYVNFLYLASHYEKLKGSPEDNEQKQLFVEQHKHYLDEIIEQISEFSKRVILADANLDKVLSAYNKHRDKPIREQA'
             'ENIIHLFTLTNLGAPAAFKYFDTTIDRKRYTSTKEVLDATLIHQSITGLYETRIDLSQLGGD')

PI_sec_structure = {
    'helix_1': (981,1000),
    'helix_2': (1002,1004),
    'helix_3': (1005,1008),
    'beta_strand_1': (1009,1011),
    'helix_4': (1018,1021),
    'helix_5': (1031,1040),
    'turn_1': (1041,1043),
    'helix_6': (1044,1046),
    'beta_strand_2': (1048,1051),
    'beta_strand_3': (1057,1059),
    'beta_strand_4': (1062,1065),
    'turn_2': (1067,1069),
    'beta_strand_5': (1072,1075),
    'turn_3': (1076,1078),
    'helix_7': (1079,1087),
    'beta_strand_6': (1093,1096),
    'beta_strand_7': (1115,1117),
    'beta_strand_8': (1120,1123),
    'helix_8': (1128,1131),
    'beta_strand_9': (1139,1151),
    'turn_4': (1152,1155),
    'beta_strand_10': (1156,1167),
    'turn_5': (1168,1170),
    'helix_9': (1171,1176),
    'helix_10': (1178,1185),
    'helix_11': (1192,1194),
    'beta_strand_11': (1196,1198),
    'beta_strand_12': (1203,1205),
    'beta_strand_13': (1207,1209),
    'beta_strand_14': (1211,1218),
    'beta_strand_15': (1220,1222),
    'helix_12': (1230,1240),
    'helix_13': (1252,1261),
    'turn_6': (1262,1264),
    'helix_14': (1265,1279),
    'helix_15': (1284,1296),
    'turn_7': (1297,1299),
    'helix_16': (1302,1312),
    'turn_8': (1313,1316),
    'beta_strand_16': (1317,1320),
    'beta_strand_17': (1324,1328),
    'beta_strand_18': (1329,1331),
    'helix_17': (1341,1344),
    'beta_strand_19': (1345,1350),
    'beta_strand_20': (1352,1354),
    'beta_strand_21': (1356,1361),
    'helix_18': (1362,1365)
}

aa_group = {
    'R': 'basic',
    'K': 'basic',
    'H': 'basic',
    'D': 'acidic',
    'E': 'acidic',
    'Q': 'polar',
    'N': 'polar',
    'S': 'polar',
    'T': 'polar',
    'A': 'hydrophobic',
    'V': 'hydrophobic',
    'I': 'hydrophobic',
    'L': 'hydrophobic',
    'F': 'hydrophobic',
    'W': 'hydrophobic',
    'Y': 'hydrophobic',
    'M': 'hydrophobic',
    'P': 'special',
    'G': 'special',
    'C': 'special'
}

kleinstiver_mutants = [
    {
        'pam': 'NGA',
        'backbone': 'WT',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'I',
          'aa_group_init': 'polar', 'aa_group_mut': 'hydrophobic'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'WT',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1154, 'sec_structure': 'turn_4', 'aa_init': 'S', 'aa_mut': 'F',
          'aa_group_init': 'polar', 'aa_group_mut': 'hydrophobic'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'WT',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'WT',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1222, 'sec_structure': 'beta_strand_15', 'aa_init': 'K', 'aa_mut': 'R',
          'aa_group_init': 'basic', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'WT',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1300, 'sec_structure': 'none', 'aa_init': 'K', 'aa_mut': 'N',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'WT',
        'mutations': [
        {'aa_idx': 1330, 'sec_structure': 'beta_strand_18', 'aa_init': 'T', 'aa_mut': 'P',
          'aa_group_init': 'polar', 'aa_group_mut': 'special'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1317, 'sec_structure': 'beta_strand_16', 'aa_init': 'N', 'aa_mut': 'K',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1324, 'sec_structure': 'beta_strand_17', 'aa_init': 'F', 'aa_mut': 'I',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1344, 'sec_structure': 'helix_17', 'aa_init': 'D', 'aa_mut': 'E',
          'aa_group_init': 'acidic', 'aa_group_mut': 'acidic'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1179, 'sec_structure': 'helix_10', 'aa_init': 'I', 'aa_mut': 'M',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1146, 'sec_structure': 'beta_strand_9', 'aa_init': 'V', 'aa_mut': 'E',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'E',
          'aa_group_init': 'acidic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1230, 'sec_structure': 'helix_12', 'aa_init': 'S', 'aa_mut': 'F',
          'aa_group_init': 'polar', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1322, 'sec_structure': 'none', 'aa_init': 'A', 'aa_mut': 'S',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1111, 'sec_structure': 'none', 'aa_init': 'L', 'aa_mut': 'F',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1134, 'sec_structure': 'none', 'aa_init': 'F', 'aa_mut': 'T',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1190, 'sec_structure': 'none', 'aa_init': 'V', 'aa_mut': 'I',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1252, 'sec_structure': 'helix_13', 'aa_init': 'N', 'aa_mut': 'K',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1192, 'sec_structure': 'helix_11', 'aa_init': 'K', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1303, 'sec_structure': 'helix_16', 'aa_init': 'R', 'aa_mut': 'C',
          'aa_group_init': 'basic', 'aa_group_mut': 'special'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1151, 'sec_structure': 'beta_strand_9', 'aa_init': 'K', 'aa_mut': 'N',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1152, 'sec_structure': 'turn_4', 'aa_init': 'G', 'aa_mut': 'R',
          'aa_group_init': 'special', 'aa_group_mut': 'basic'},
        {'aa_idx': 1218, 'sec_structure': 'beta_strand_14', 'aa_init': 'G', 'aa_mut': 'R',
          'aa_group_init': 'special', 'aa_group_mut': 'basic'},
        {'aa_idx': 1329, 'sec_structure': 'beta_strand_18', 'aa_init': 'T', 'aa_mut': 'A',
          'aa_group_init': 'polar', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1148, 'sec_structure': 'beta_strand_9', 'aa_init': 'K', 'aa_mut': 'N',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1283, 'sec_structure': 'none', 'aa_init': 'A', 'aa_mut': 'T',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1249, 'sec_structure': 'none', 'aa_init': 'P', 'aa_mut': 'L',
          'aa_group_init': 'special', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1263, 'sec_structure': 'turn_6', 'aa_init': 'K', 'aa_mut': 'R',
          'aa_group_init': 'basic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1297, 'sec_structure': 'turn_7', 'aa_init': 'H', 'aa_mut': 'Y',
          'aa_group_init': 'basic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1125, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1143, 'sec_structure': 'beta_strand_9', 'aa_init': 'V', 'aa_mut': 'I',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1104, 'sec_structure': 'none', 'aa_init': 'G', 'aa_mut': 'R',
          'aa_group_init': 'special', 'aa_group_mut': 'basic'},
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1303, 'sec_structure': 'helix_16', 'aa_init': 'R', 'aa_mut': 'H',
          'aa_group_init': 'basic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1366, 'sec_structure': 'none', 'aa_init': 'G', 'aa_mut': 'V',
          'aa_group_init': 'special', 'aa_group_mut': 'hydrophobic'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1299, 'sec_structure': 'turn_7', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1155, 'sec_structure': 'turn_4', 'aa_init': 'K', 'aa_mut': 'R',
          'aa_group_init': 'basic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1364, 'sec_structure': 'helix_18', 'aa_init': 'Q', 'aa_mut': 'L',
          'aa_group_init': 'polar', 'aa_group_mut': 'hydrophobic'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1113, 'sec_structure': 'none', 'aa_init': 'K', 'aa_mut': 'N',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1177, 'sec_structure': 'none', 'aa_init': 'N', 'aa_mut': 'K',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1150, 'sec_structure': 'beta_strand_9', 'aa_init': 'E', 'aa_mut': 'K',
          'aa_group_init': 'acidic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1097, 'sec_structure': 'none', 'aa_init': 'K', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1141, 'sec_structure': 'beta_strand_9', 'aa_init': 'Y', 'aa_mut': 'F',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1173, 'sec_structure': 'helix_9', 'aa_init': 'S', 'aa_mut': 'F',
          'aa_group_init': 'polar', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1162, 'sec_structure': 'beta_strand_10', 'aa_init': 'E', 'aa_mut': 'D',
          'aa_group_init': 'acidic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1283, 'sec_structure': 'none', 'aa_init': 'A', 'aa_mut': 'V',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1168, 'sec_structure': 'turn_5', 'aa_init': 'I', 'aa_mut': 'N',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1218, 'sec_structure': 'beta_strand_14', 'aa_init': 'G', 'aa_mut': 'E',
          'aa_group_init': 'special', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1329, 'sec_structure': 'beta_strand_18', 'aa_init': 'T', 'aa_mut': 'A',
          'aa_group_init': 'polar', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1332, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGA',
        'backbone': 'R1335Q',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1148, 'sec_structure': 'beta_strand_9', 'aa_init': 'K', 'aa_mut': 'N',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1317, 'sec_structure': 'beta_strand_16', 'aa_init': 'N', 'aa_mut': 'D',
          'aa_group_init': 'polar', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1218, 'sec_structure': 'beta_strand_14', 'aa_init': 'G', 'aa_mut': 'R',
          'aa_group_init': 'special', 'aa_group_mut': 'basic'},
        {'aa_idx': 1257, 'sec_structure': 'helix_13', 'aa_init': 'L', 'aa_mut': 'F',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1100, 'sec_structure': 'none', 'aa_init': 'V', 'aa_mut': 'M',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1110, 'sec_structure': 'none', 'aa_init': 'I', 'aa_mut': 'V',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1156, 'sec_structure': 'beta_strand_10', 'aa_init': 'K', 'aa_mut': 'R',
          'aa_group_init': 'basic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1219, 'sec_structure': 'none', 'aa_init': 'E', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1250, 'sec_structure': 'none', 'aa_init': 'E', 'aa_mut': 'D',
          'aa_group_init': 'acidic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1256, 'sec_structure': 'helix_13', 'aa_init': 'Q', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1287, 'sec_structure': 'helix_15', 'aa_init': 'L', 'aa_mut': 'R',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1177, 'sec_structure': 'none', 'aa_init': 'N', 'aa_mut': 'E',
          'aa_group_init': 'polar', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1250, 'sec_structure': 'none', 'aa_init': 'E', 'aa_mut': 'K',
          'aa_group_init': 'acidic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1261, 'sec_structure': 'helix_13', 'aa_init': 'Q', 'aa_mut': 'K',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1148, 'sec_structure': 'beta_strand_9', 'aa_init': 'K', 'aa_mut': 'N',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1175, 'sec_structure': 'helix_9', 'aa_init': 'E', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1219, 'sec_structure': 'none', 'aa_init': 'E', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1352, 'sec_structure': 'beta_strand_20', 'aa_init': 'I', 'aa_mut': 'F',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1195, 'sec_structure': 'none', 'aa_init': 'I', 'aa_mut': 'L',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1149, 'sec_structure': 'beta_strand_9', 'aa_init': 'V', 'aa_mut': 'D',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1303, 'sec_structure': 'helix_16', 'aa_init': 'R', 'aa_mut': 'C',
          'aa_group_init': 'basic', 'aa_group_mut': 'special'},
        {'aa_idx': 1317, 'sec_structure': 'beta_strand_16', 'aa_init': 'N', 'aa_mut': 'K',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1119, 'sec_structure': 'none', 'aa_init': 'L', 'aa_mut': 'V',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1138, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'I',
          'aa_group_init': 'polar', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1219, 'sec_structure': 'none', 'aa_init': 'E', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1190, 'sec_structure': 'none', 'aa_init': 'V', 'aa_mut': 'I',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1301, 'sec_structure': 'none', 'aa_init': 'P', 'aa_mut': 'T',
          'aa_group_init': 'special', 'aa_group_mut': 'polar'},
        {'aa_idx': 1309, 'sec_structure': 'helix_16', 'aa_init': 'I', 'aa_mut': 'T',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1350, 'sec_structure': 'beta_strand_19', 'aa_init': 'Q', 'aa_mut': 'H',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1285, 'sec_structure': 'helix_15', 'aa_init': 'A', 'aa_mut': 'G',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'special'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1195, 'sec_structure': 'none', 'aa_init': 'I', 'aa_mut': 'L',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1202, 'sec_structure': 'none', 'aa_init': 'S', 'aa_mut': 'N',
          'aa_group_init': 'polar', 'aa_group_mut': 'polar'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1250, 'sec_structure': 'none', 'aa_init': 'E', 'aa_mut': 'D',
          'aa_group_init': 'acidic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1251, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1138, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'K',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1363, 'sec_structure': 'helix_18', 'aa_init': 'S', 'aa_mut': 'M',
          'aa_group_init': 'polar', 'aa_group_mut': 'hydrophobic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1292, 'sec_structure': 'helix_15', 'aa_init': 'S', 'aa_mut': 'I',
          'aa_group_init': 'polar', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1100, 'sec_structure': 'none', 'aa_init': 'V', 'aa_mut': 'E',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1111, 'sec_structure': 'none', 'aa_init': 'L', 'aa_mut': 'H',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'H',
          'aa_group_init': 'acidic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1296, 'sec_structure': 'helix_15', 'aa_init': 'K', 'aa_mut': 'M',
          'aa_group_init': 'basic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1366, 'sec_structure': 'none', 'aa_init': 'G', 'aa_mut': 'E',
          'aa_group_init': 'special', 'aa_group_mut': 'acidic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1255, 'sec_structure': 'helix_13', 'aa_init': 'K', 'aa_mut': 'M',
          'aa_group_init': 'basic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1104, 'sec_structure': 'none', 'aa_init': 'G', 'aa_mut': 'R',
          'aa_group_init': 'special', 'aa_group_mut': 'basic'},
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1157, 'sec_structure': 'beta_strand_10', 'aa_init': 'L', 'aa_mut': 'V',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1219, 'sec_structure': 'none', 'aa_init': 'E', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1242, 'sec_structure': 'none', 'aa_init': 'Y', 'aa_mut': 'F',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1330, 'sec_structure': 'beta_strand_18', 'aa_init': 'T', 'aa_mut': 'M',
          'aa_group_init': 'polar', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1262, 'sec_structure': 'turn_6', 'aa_init': 'H', 'aa_mut': 'P',
          'aa_group_init': 'basic', 'aa_group_mut': 'special'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1226, 'sec_structure': 'none', 'aa_init': 'L', 'aa_mut': 'I',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1229, 'sec_structure': 'none', 'aa_init': 'P', 'aa_mut': 'I',
          'aa_group_init': 'special', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1330, 'sec_structure': 'beta_strand_18', 'aa_init': 'T', 'aa_mut': 'K',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1219, 'sec_structure': 'none', 'aa_init': 'E', 'aa_mut': 'V',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1179, 'sec_structure': 'helix_10', 'aa_init': 'I', 'aa_mut': 'F',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1285, 'sec_structure': 'helix_15', 'aa_init': 'A', 'aa_mut': 'P',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'special'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'L',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1161, 'sec_structure': 'beta_strand_10', 'aa_init': 'K', 'aa_mut': 'I',
          'aa_group_init': 'basic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1155, 'sec_structure': 'turn_4', 'aa_init': 'K', 'aa_mut': 'T',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1191, 'sec_structure': 'none', 'aa_init': 'K', 'aa_mut': 'I',
          'aa_group_init': 'basic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1194, 'sec_structure': 'helix_11', 'aa_init': 'L', 'aa_mut': 'F',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'Q',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1339, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'P',
          'aa_group_init': 'polar', 'aa_group_mut': 'special'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335E+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1144, 'sec_structure': 'beta_strand_9', 'aa_init': 'L', 'aa_mut': 'P',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'special'},
        {'aa_idx': 1208, 'sec_structure': 'beta_strand_13', 'aa_init': 'N', 'aa_mut': 'S',
          'aa_group_init': 'polar', 'aa_group_mut': 'polar'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'E',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335T+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1191, 'sec_structure': 'none', 'aa_init': 'K', 'aa_mut': 'N',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'T',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335T+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1303, 'sec_structure': 'helix_16', 'aa_init': 'R', 'aa_mut': 'H',
          'aa_group_init': 'basic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'T',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335T+T1337R',
        'mutations': [
        {'aa_idx': 1195, 'sec_structure': 'none', 'aa_init': 'I', 'aa_mut': 'M',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1207, 'sec_structure': 'beta_strand_13', 'aa_init': 'E', 'aa_mut': 'K',
          'aa_group_init': 'acidic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1317, 'sec_structure': 'beta_strand_16', 'aa_init': 'N', 'aa_mut': 'K',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'T',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1350, 'sec_structure': 'beta_strand_19', 'aa_init': 'Q', 'aa_mut': 'H',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335T+T1337R',
        'mutations': [
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'T',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335T+T1337R',
        'mutations': [
        {'aa_idx': 1134, 'sec_structure': 'none', 'aa_init': 'F', 'aa_mut': 'L',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'Y',
          'aa_group_init': 'acidic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1192, 'sec_structure': 'helix_11', 'aa_init': 'K', 'aa_mut': 'R',
          'aa_group_init': 'basic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1207, 'sec_structure': 'beta_strand_13', 'aa_init': 'E', 'aa_mut': 'K',
          'aa_group_init': 'acidic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1218, 'sec_structure': 'beta_strand_14', 'aa_init': 'G', 'aa_mut': 'R',
          'aa_group_init': 'special', 'aa_group_mut': 'basic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'T',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'},
        {'aa_idx': 1342, 'sec_structure': 'helix_17', 'aa_init': 'V', 'aa_mut': 'V',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335T+T1337R',
        'mutations': [
        {'aa_idx': 1111, 'sec_structure': 'none', 'aa_init': 'L', 'aa_mut': 'H',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1197, 'sec_structure': 'beta_strand_11', 'aa_init': 'K', 'aa_mut': 'T',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1285, 'sec_structure': 'helix_15', 'aa_init': 'A', 'aa_mut': 'S',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'T',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335T+T1337R',
        'mutations': [
        {'aa_idx': 1114, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'G',
          'aa_group_init': 'basic', 'aa_group_mut': 'special'},
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'T',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335T+T1337R',
        'mutations': [
        {'aa_idx': 1162, 'sec_structure': 'beta_strand_10', 'aa_init': 'E', 'aa_mut': 'D',
          'aa_group_init': 'acidic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1195, 'sec_structure': 'none', 'aa_init': 'I', 'aa_mut': 'M',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1218, 'sec_structure': 'beta_strand_14', 'aa_init': 'G', 'aa_mut': 'R',
          'aa_group_init': 'special', 'aa_group_mut': 'basic'},
        {'aa_idx': 1309, 'sec_structure': 'helix_16', 'aa_init': 'I', 'aa_mut': 'V',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'T',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335T+T1337R',
        'mutations': [
        {'aa_idx': 1135, 'sec_structure': 'none', 'aa_init': 'D', 'aa_mut': 'N',
          'aa_group_init': 'acidic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1190, 'sec_structure': 'none', 'aa_init': 'V', 'aa_mut': 'I',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1285, 'sec_structure': 'helix_15', 'aa_init': 'A', 'aa_mut': 'V',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'hydrophobic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'T',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    },
    {
        'pam': 'NGC',
        'backbone': 'R1335T+T1337R',
        'mutations': [
        {'aa_idx': 1111, 'sec_structure': 'none', 'aa_init': 'L', 'aa_mut': 'H',
          'aa_group_init': 'hydrophobic', 'aa_group_mut': 'basic'},
        {'aa_idx': 1218, 'sec_structure': 'beta_strand_14', 'aa_init': 'G', 'aa_mut': 'R',
          'aa_group_init': 'special', 'aa_group_mut': 'basic'},
        {'aa_idx': 1297, 'sec_structure': 'turn_7', 'aa_init': 'H', 'aa_mut': 'D',
          'aa_group_init': 'basic', 'aa_group_mut': 'acidic'},
        {'aa_idx': 1335, 'sec_structure': 'none', 'aa_init': 'R', 'aa_mut': 'T',
          'aa_group_init': 'basic', 'aa_group_mut': 'polar'},
        {'aa_idx': 1337, 'sec_structure': 'none', 'aa_init': 'T', 'aa_mut': 'R',
          'aa_group_init': 'polar', 'aa_group_mut': 'basic'}
        ]
    }
]
