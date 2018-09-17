import json

with open('data/comments.json', 'r') as file:
    comments_dict = json.load(file)
    
#print(comments_dict.keys())