import random

fa = open("adjectives.txt", "r")
fn = open("nouns.txt", "r")

adjs = fa.read().split('\n')
nouns = fn.read().split('\n')


def get_pair(adjs, nouns):
    LEN_A = len(adjs)
    LEN_N = len(nouns)
    i_a = random.randint(0,LEN_A)
    i_n = random.randint(0,LEN_N)
    print('Risposta:', nouns[i_n], adjs[i_a].split('\t')[0])

while True:
    myin = input('Digita una domanda:\n')
    if myin == 'STOP':
        break
    else:
        #print('\nprocessing...\nLayers initialized')
        #print('generating answer...\n')
        get_pair(adjs, nouns)
        print('\n')


