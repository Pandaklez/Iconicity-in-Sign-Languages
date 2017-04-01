import csv

s = csv.DictReader(open("data.csv"))

words = []
for row in s:
    word = row["word"]
    if word not in words:
        words.append(word)

print(len(words))
