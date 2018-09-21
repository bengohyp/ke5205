#!/usr/bin/python -tt

def show_progress_bar():
  import progressbar
  from time import sleep
  bar = progressbar.ProgressBar(maxval=100, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
  bar.start()
  for i in range(100):
    bar.update(i+1)
    sleep(0.1)
  bar.finish()

  
  
#extract_to_dict accepts a filepath to a json file and
#outputs a dictionary that contains all the values
def extract_to_dict(file_path):
  import json
  file = open(file_path)
  data_list = json.load(file)
  file.close()
  return data_list



#delete_empty takes in a dictionary and deletes the keys
#that are empty
def delete_empty(input_dict, key1, key2):
  to_delete = []
  for index in range(0, len(input_dict)):
    if((type(input_dict[index][str(key1)]) is None) or (type(input_dict[index][str(key1)]) == type(None))) and ((type(input_dict[index][str(key2)]) is None) or (type(input_dict[index][str(key2)]) == type(None))):
      to_delete.append(index)
  to_delete.reverse()
  for index in to_delete:
    del input_dict[index]
    
    

def remove_non_ascii(s): return "".join(i for i in s if ord(i)<128)



def cleanup_dict(input_dict, key1, key2):
  #delete empty records
  delete_empty(input_dict, key1, key2)
  import html
  import progressbar
  bar = progressbar.ProgressBar(maxval=len(input_dict), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
  count = 0
  bar.start()
  for index in range(0, len(input_dict)):
    bar.update(count)
    count += 1
    if((type(input_dict[index][str(key1)]) is None) or (type(input_dict[index][str(key1)]) == type(None))):
      pass
    else:
      #convert byte to unicode
      if(type(input_dict[index][str(key1)]) == bytes):
        input_dict[index][str(key1)] = input_dict[index][str(key1)].decode('utf-8')
      #remove non-ascii characters from strings
      input_dict[index][str(key1)] = remove_non_ascii(input_dict[index][str(key1)])
      #remove html encoding
      input_dict[index][str(key1)] = html.unescape(input_dict[index][str(key1)])
    if((type(input_dict[index][str(key2)]) is None) or (type(input_dict[index][str(key2)]) == type(None))):
      pass
    else:
      if(type(input_dict[index][str(key2)]) == bytes):
        input_dict[index][str(key2)] = input_dict[index][str(key2)].decode('utf-8')
      input_dict[index][str(key2)] = remove_non_ascii(input_dict[index][str(key2)])
      input_dict[index][str(key2)] = html.unescape(input_dict[index][str(key2)])



def checkUrl(s):
  from urllib.parse import urlparse
  parse_result = urlparse(str(s))
  if parse_result.netloc == '' : return False
  else: return True


  
#beautify_text accepts a dict and outputs a dict
#with all the html tags and encoding removed
def beautify_text(input_dict, key):
  #!pip install bs4
  from bs4 import BeautifulSoup
  import progressbar
  bar = progressbar.ProgressBar(maxval=len(input_dict), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
  count = 0
  bar.start()
  result = {}
  for index in range(0,len(input_dict)):
    bar.update(count)
    count += 1
    if (type(input_dict[index][str(key)]) is None) or (type(input_dict[index][str(key)]) == type(None)): 
      pass
    else:
      if(checkUrl(input_dict[index][str(key)])):
        result[index] = input_dict[index][str(key)]
      else:
        soup = BeautifulSoup(input_dict[index][str(key)])
        result[index] = soup.get_text()
    bar.finish()
  return result

    
def main():
  FILEPATH = 'data/documents.json'
  KEY1 = 'title'
  KEY2 = 'text'
  documents = {}
  documents = extract_to_dict(FILEPATH)
  cleanup_dict(documents, KEY1, KEY2)
  beautified_title = {}
  beautified_title = beautify_text(documents, KEY1)
  beautified_text = {}
  beautified_text = beautify_text(documents, KEY2)

if __name__ == '__main__':
  main()