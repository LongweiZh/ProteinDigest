import re


def double(a):
    return 2 * a


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
        if result_list != []:
            results[i - 1] = result_list
    return results


def protein_digest(seq, enzyme='trypsin', l_min=0, l_max=0, mw_min=0, mw_max=0, miss=5):
    seq = seq.upper()
    pattern_data = {"trypsin": re.compile(r'(?<=[KR])(?=[^P])')}
    pattern = pattern_data["trypsin"]
    slice = pattern.split(seq)
    peptide_list = peptide_slice(slice, miss)
    results = []
    for miss_number in peptide_list.keys():
        for peptide in peptide_list[miss_number]:
            i = 1
            a = Peptide(name=(str(miss_number)+"_"+str(i)), seq=peptide, miss=miss_number)
            results.append(a)
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
    mw_seq = sum(amino_acid_masses[aa] for aa in seq) + 18.01528
    return mw_seq

#a = 'AAKQQRCCKAARPAAR'
#slice = protein_digest(a,miss=5)
#for i in slice:
#    print(i.seq,i.miss,i.mw())

#print(mol_weight('QQR'))
#p = Peptide('a','QQR',5)
#print(p.mw())
