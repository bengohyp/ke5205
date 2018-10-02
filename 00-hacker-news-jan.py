FILENAME01 = 'Hacker_News.hn_2018_01.csv'
FILEPATH = 'data/'
file01 = open(FILEPATH+FILENAME01, encoding='utf-8')

import csv
reader = csv.reader(file01)

titles_dict = {}
texts_dict = {}
count = 0
for row in reader:
  _id, by, dead, deleted, descendants, id, parent, score, text, time, timestamp, title, type, url = row
  if(title == ""): 
    pass
  else:
    titles_dict[str(count)] = title
  if(text == ""):
    pass
  else:
    texts_dict[str(count)] = text
  count += 1
print("Length of titles_dict = " + str(len(titles_dict)))
print("Length of texts_dict = " + str(len(texts_dict)))