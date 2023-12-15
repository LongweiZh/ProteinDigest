import re


class Peptide:
    def __init__(self, name, seq, miss):
        self.name = name
        self.seq = seq
        self.miss = miss

    def length(self):
        return len(self.seq)

    def mw(self):
        return mol_weight(self.seq)


def peptide_slice(slice, miss):
    results = {}
    for i in range(1, miss + 2):
        result_list = ["".join(slice[j:j + i]) for j in range(len(slice) - i + 1)]
        if result_list:
            results[i - 1] = set(result_list)
    return results


def protein_digest(seq, enzyme, l_min, l_max, mw_min, mw_max, miss):
    seq = seq.upper()
    pattern_data = {"Trypsin": re.compile(r'(?<=[KR])(?=[^P])'),
                    "Trypsin (C-term to K/R, even before P)": re.compile(r'(?<=[KR])(?=.)'),
                    "Lys C": re.compile(r'(?<=[K])(?=.)'),
                    "Lys N": re.compile(r'(?<=.)(?=K)'),
                    "CNBr": re.compile(r'(?<=[M])(?=.)'),
                    "Arg C": re.compile(r'(?<=[R])(?=[^P])'),
                    "Asp N": re.compile(r'(?<=.)(?=D)'),
                    "Glu C (bicarbonate)": re.compile(r'(?<=[E])(?=[^PE])'),
                    "Glu C (phosphate)": re.compile(r'(?<=[DE])(?=[^PE])'),
                    "Microwave-assisted formic acid hydrolysis (C-term to D)": re.compile(r'(?<=[D])(?=.)'),
                    "Pepsin (pH 1.3)": re.compile(r'(?<=[FL])(?=.)'),
                    "Pepsin (pH > 2)": re.compile(r'(?<=[FLWYAEQ])(?=.)'),
                    "Proteinase K": re.compile(r'(?<=[AFYWLIV])(?=.)'),
                    "Thermolysin": re.compile(r'(?<=[DE])(?=AFILMV)')}
    pattern = pattern_data[enzyme]
    slice = pattern.split(seq)
    peptide_list = peptide_slice(slice, miss)
    print('---splice-----')
    print(peptide_list)
    candidates = []
    results = []
    for miss_number in peptide_list.keys():
        for peptide in peptide_list[miss_number]:
            a = Peptide(name=peptide, seq=peptide, miss=miss_number)
            candidates.append(a)

    for candidate in candidates:
        if int(l_min) <= candidate.length() <= int(l_max) and int(mw_min) <= candidate.mw() <= int(mw_max):
            results.append(candidate)
    return results


def mol_weight(seq):
    amino_acid_masses = {
        'A': 71.03711,
        'R': 156.10111,
        'N': 114.04293,
        'D': 115.02694,
        'C': 103.00919,
        'E': 129.04259,
        'Q': 128.05858,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'L': 113.08406,
        'K': 128.09496,
        'M': 131.04049,
        'F': 147.06841,
        'P': 97.05276,
        'S': 87.03203,
        'T': 101.04768,
        'U': 150.95363,
        'W': 186.07931,
        'Y': 163.06333,
        'V': 99.06841,
    }
    mw_seq = round(sum(amino_acid_masses[aa] for aa in seq) + 18.01528,2)
    return mw_seq


# a = 'AFYWLIVAFYWLIV'
# slice = protein_digest(a, "Proteinase K", 1, 5, 0, 10000, 2)
# for i in slice:
#     print(i.seq, i.miss, i.mw())
