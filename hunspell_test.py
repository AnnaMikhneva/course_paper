import itertools

patterns = """NounStem H? A?
NounStem H? B?
AdjStem I A?
AdjStem I B?
VerbStem D? E?
VerbStem F C?
PronStem A
TAMSuffixStem
PostStem A?
PossStem
AscStem A
AdjStem
NounStem G
VerbStem G
DemStem A?
DemStem B?"""
import re
dct = {}

latin = 'ABCDEFGHIJKLMNOPRQSTUVWXYZ'

for pattern in patterns.split('\n'):
    head = pattern.split()[0]

    if head not in dct:
        dct[head] = []
    for line in patterns.split('\n'):
        if pattern.split()[0] == head:
            for affix in pattern.split()[1:]:
                if affix.split('?')[0] not in dct[head]:
                    dct[head].append(affix.split('?')[0])

#print(dct)


with open('morphoanalyzator.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    match = re.findall(r'LEXICON .*?Stem\n((?:.|\n)*?)\n\n\n', content)
    stems = []
    for stem in match:
        item = stem.split('\n')
        stems.append(item)
    #print(match)
    #print(stems)
with open('wordlist.txt', 'w', encoding = 'utf-8') as word_file:
    for i in range(len(stems)):
        suffixes = ''.join(list(dct.values())[i])
        for word in stems[i]:
            word = word.split(":")
            if suffixes == '':
                word_file.write(word[1] + '\n')
            else:
                word_file.write(word[1] + '/' + suffixes + '\n')

# wc -l wordlist.txt > nama.dic
# sort wordlist.txt | uniq >> nama.dic


with open('morphoanalyzator.txt', 'r', encoding='utf-8') as file:
    content2 = file.read()
    match2 = re.findall(r'LEXICON .*?(Suffix|Marker)\n((?:.|\n)*?)\n\n', content2)
    suffixes = []
    for suf in match2:
        item2 = suf[1].split('\n')
        suffixes.append(item2)
    #print(match2)
    #print(suffixes)
with open('morphoanalyzator.txt', 'r', encoding='utf-8') as f:
    content3 = f.readlines()
    markers = []
    for fileline in content3:
        match3 = re.fullmatch(r'LEXICON .*(Suffix|Marker)\n', fileline)
        if match3:
            markers.append(fileline[8:-1])
    print(markers)
    for index, it in enumerate(markers):
        markers[index] = latin[index]
    print(markers)
with open('affix.txt', 'w', encoding = 'utf-8') as aff_file:
    for i in range(len(suffixes)):
        aff_file.write('SFX ' + markers[i] + " Y " + str(len(suffixes[i])) + '\n')
        for word in suffixes[i]:
            word = word.split(":")
            aff_file.write('SFX ' + markers[i] + ' 0 ' + word[1] +'\n')
        aff_file.write('\n')

# flex = {}
# i = 0
#
# for stem in dct:
#     for affix in dct[stem]:
#         if affix not in flex:
#             flex[affix] = ''
#         flex[affix] += latin[i]
#     print(stem, latin[i])
#     i += 1
#
# print(flex)
