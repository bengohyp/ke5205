import json
import ijson
import html
from bs4 import BeautifulSoup
from urllib.parse import urlparse
'''
#parse comments.json into dictionary
comments_file = open('data\comments.json')
comments_dict = json.load(comments_file)
'''
#parse comments.json into list
comments_file = open('data/comments.json')
text_generator = ijson.items(comments_file, 'text')
text_list = list(text_generator)
print(len(text_list[0]))
print(text_list[0]['0'])

#demo remove html tags and encoding using BeautifulSoup
soup = BeautifulSoup(text_list[0]['0'])
print(soup.get_text())

#function to check if string is a URL
def checkUrl(s):
    parse_result = urlparse(str(s))
    if parse_result.netloc == '' : return False
    else: return True

#check if beautified string is a URL
soup = BeautifulSoup(text_list[0]['0'])
print(checkUrl(soup))

#loop through 30 entries and beautify them
i = 0
while i < 30:
    print(i)
    if text_list[0][str(i)] != None:
        soup = BeautifulSoup(text_list[0][str(i)])
        print(soup.get_text())
    i += 1

for i in range(5):
    for key in comments[i]:
        print(key)
        print(comments[i][str(key)])
        i += 1


for index in range(0, len(documents)):
    if((type(documents[index]['title']) is None) or (type(documents[index]['title']) == type(None))) and ((type(documents[index]['text']) is None) or (type(documents[index]['text']) == type(None))):
      to_delete.append(index)


if ((type(comments_title['26']) is None) or (type(comments_title['26']) is type(None))):
    print('is None')


to_delete = []
for key in comments_title:
    if ((type(comments_title[str(key)]) is None) or (type(comments_title[str(key)]) is type(None))):
        to_delete.append(key)
for key in to_delete:
    del comments_title[str(key)]

keys = []
for i in comments_title_sanitized:
    keys.append(i)
for j in range(0,len(comments_title_sanitized)):
    print(comments_title_sanitized[keys[j]])

keys = []
for i in comments_text_sanitized:
    keys.append(i)
for j in range(0,len(keys)):
    print(comments_text_sanitized[keys[j]])