import csv
import re
#import pandas as pd

#df = pd.read_csv("cmpnd_open.csv")
#col = df.pattern
#print(type(col))
def funct(var):
    s = csv.DictReader(open("cmpnd_open.csv"))
    cc = []
    for row in s:
        content = row[var]
        cc.append(content)

    pattern_left = []
    pattern_right = []
    for el in cc:
        m = re.search('(.*?)&(.*)', el)
        if m != None:
            word1 = m.group(1)
            word2 = m.group(2)
            pattern_left.append(word1)
            pattern_right.append(word2)
        else:
            pattern_left.append('ok')
            pattern_right.append('ok')
    return pattern_left, pattern_right

def csv_dict_writer(fieldnames, data):
    with open("out.csv", "w") as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def indices(b):
    s = csv.DictReader(open("cmpnd_open.csv"))
    ind = []
    i = 0
    for el in b:
        if el != 'ok':
            ind.append(i)
        i += 1
    return ind

def reorder_data(ind, p_left, p_right, b_left, b_right, n_left, n_right):
    s = csv.DictReader(open("cmpnd_open.csv"))
    urls = []
    languages = []
    word = []
    non_iconic = []
    sem = []
    for row in s:
        wor = row['word']
        url = row['urls']
        lang = row['languages']
        non_ic = row['non_iconic']
        sema = row['semantic_field']
        sem.append(sema)
        non_iconic.append(non_ic)
        urls.append(url)
        word.append(wor)
        languages.append(lang)
    #print(len(word))
    data = []
    #print(len(data))
    urls = []
    languages = []
    word = []
    non_iconic = []
    sem = []
    pattern = []
    base = []
    #print(len(p_left))
    s = csv.DictReader(open("cmpnd_open.csv"))
    for row in s:
        wor = row['word']
        url = row['urls']
        lang = row['languages']
        non_ic = row['non_iconic']
        sema = row['semantic_field']
        pat = row['pattern']
        bas = row['base']
        base.append(bas)
        pattern.append(pat)
        sem.append(sema)
        non_iconic.append(non_ic)
        urls.append(url)
        word.append(wor)
        languages.append(lang)

    for j in ind:
        if n_left[j] == 'ok':
            data.append([word[j], sem[j], b_left[j], p_left[j], non_iconic[j], languages[j], urls[j]])
            data.append([word[j], sem[j], b_right[j], p_right[j], non_iconic[j], languages[j], urls[j]])
        else:
            data.append([word[j], sem[j], b_left[j], p_left[j], n_left[j], languages[j], urls[j]])
            data.append([word[j], sem[j], b_right[j], p_right[j], n_right[j], languages[j], urls[j]])
            
    for k in range(0, len(p_left)):
        if k not in ind:
            data.append([word[k], sem[k], base[k], pattern[k], non_iconic[k], languages[k], urls[k]])
    #print(len(data))
    #with open('out.csv', "w") as fl:

    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)

    csv_dict_writer(fieldnames, my_list)

def main():
    [p_left, p_right] = funct('pattern')
    [b_left, b_right] = funct('base')
    [n_left, n_right] = funct('non_iconic')
    #print(b_left)
    ind = indices(b_left)
    reorder_data(ind, p_left, p_right, b_left, b_right, n_left, n_right)

if __name__ == '__main__':
    main()
