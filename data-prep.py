import json

#parse comments file into dictionary
comments_file = open('data/comments.json')
comments_dict = json.load(comments_file)

#parse documents file into dictionary
documents_file = open('data/documents.json', 'r')
documents_dict = json.load(documents_file)

#show all keys in the comments_dict
print(comments_dict.keys())

#show all keys in the documents_dict
print(documents_dict.keys())

#show the first line of data in the comments_dict
#show the first line of data in the documents_dict

#use beautifulsoup to remove html encoding and tags
from bs4 import BeautifulSoup
soup = BeautifulSoup(columns[0]['0'])
print(soup.get_text())

#remove html encoding and tags from first 5 records
i = 0
while i < 5:
  if(columns[0][str(i)] != None):
    soup = BeautifulSoup(columns[0][str(i)])
    columns[0][str(i)] = soup.get_text()
  i += 1
  
#print the first 10 records
j = 0
while j < 20:
  print(j)
  if(columns[0][str(j)] != None):
    print(columns[0][str(j)])
  j += 1
  
#remove html encoding and tags from all records
for record in columns[0]:
  if(columns[0][record] != None):
    soup = BeautifulSoup(str(columns[0][record]))
    columns[0][record] = soup.get_text()
    
print(BeautifulSoup(str(columns[0]['13'])).get_text())