import sys

in_txt = sys.argv[1]
target_gene_s = sys.argv[2]
target_gene_e = sys.argv[3]

def ismatch(g1, g2):
    for i in range(len(g1)):
        g1_list = fit_dict[g1[i]]
        g2_list = fit_dict[g2[i]]
        if list(set(g1_list) & set(g2_list)) == []:
            return False
    return True

def match_gene(source, target):
    length_source = len(source)
    length_target = len(target)
    for i in range(length_source - length_target):
        gene_ = source[i:i+length_target]
        if ismatch(gene_, target):
            print('the match gene is %s ' % gene_)
            print('the target gene is %s' % target)
            return True
    return False


fit_dict = [
    ('A', ['A']),
    ('C', ['C']),
    ('T', ['T']),
    ('G', ['G']),
    ('R',['A', 'G']),
    ('Y',['C', 'T']),
    ('M',['A', 'C']),
    ('K',['G', 'T']),
    ('S',['G', 'C']),
    ('W',['A', 'T']),
    ('H',['A', 'T', 'C']),
    ('B',['G', 'T', 'C']),
    ('V',['G', 'A', 'C']),
    ('D',['G', 'A', 'T']),
    ('N',['A', 'T', 'C', 'G'])]
fit_dict = dict(fit_dict)

input_txt = []
with open(in_txt, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().replace(' ', '')
        for s in line:
            if s.isalpha():
                input_txt.append(s.upper())

start_match = False
end_match = False

print(match_gene(input_txt, target_gene_s))
print(match_gene(input_txt, target_gene_e))
