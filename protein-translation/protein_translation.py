PATTERNS = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP',
}


def proteins(strand):
    split_strand = list()
    sequences = list()
    for index in range(0, len(strand), 3):
        split_strand.append(strand[index: index + 3])
    for protein in split_strand:
        if protein in PATTERNS.keys() and PATTERNS.get(protein) != 'STOP':
            sequences.append(PATTERNS.get(protein))
        elif PATTERNS.get(protein) == 'STOP':
            break
    return sequences


if __name__ == '__main__':
    sample = "UAGUGG"
    print(proteins(sample.upper()))
