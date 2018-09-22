#!/usr/bin/python3 -tt

import os
import json
import string
import nltk
from nltk import word_tokenize, FreqDist
from nltk.corpus import stopwords


# min_extract_to_dict accepts a file and outputs an dictionary that contains
# all the values of a specified key
def min_extract_to_dict(file_path, key):
    # !pip install ijson
    import ijson
    file = open(file_path)
    generator = ijson.items(file, key)
    data_list = list(generator)
    file.close()
    return data_list[0]


# delete_empty takes in a dictionary and deletes the keys that are empty
def delete_empty(input_dict):
    to_delete = []
    for key in input_dict:
        if ((type(input_dict[str(key)]) is None) or
                (type(input_dict[str(key)]) is type(None))):
            to_delete.append(key)
    for key in to_delete:
        del input_dict[str(key)]


def byte_to_unicode(input_dict, key):
    if(type(input_dict[str(key)]) == bytes):
        return input_dict[str(key)].decode('utf-8')


# remove_non_ascii takes a string and strips all non-ascii characters from it
# before returning a string
def remove_non_ascii(s):
    return "".join(i for i in s if ord(i) < 128)


# cleanup_dict takes a dictionary, removes all empty records, converts byte
# type to unicode, removes all non ascii characters, and remove html encoding
def cleanup_dict(input_dict):
    # delete empty records
    input_dict = delete_empty(input_dict)
    import html
    import progressbar
    bar = progressbar.ProgressBar(maxval=len(input_dict),
                                  widgets=[progressbar.Bar('=', '[', ']'), ' ',
                                  progressbar.Percentage()])
    count = 0
    bar.start()
    for key in input_dict:
        bar.update(count)
        count += 1
        # convert byte to unicode
        input_dict[str(key)] = byte_to_unicode(input_dict, key)
        # remove non-ascii characters from strings
        input_dict[str(key)] = remove_non_ascii(input_dict[str(key)])
        # remove html encoding
        input_dict[str(key)] = html.unescape(input_dict[str(key)])
        # sanitize with BeautifulSoup
        try:
            input_dict[str(key)] = BeautifulSoup(
                input_dict[str(key)]).get_text()
        except:
            print("Unable to process line " + key)
    bar.finish()


# checkUrl takes a string and checks if it is a properly formed URL address
def checkUrl(s):
    from urllib.parse import urlparse
    parse_result = urlparse(str(s))
    if parse_result.netloc == '':
        return False
    else:
        return True


# beautify_text accepts a dict and outputs a dict with all the html tags and
# encoding removed
def beautify_text(input_dict):
    # !pip install bs4
    from bs4 import BeautifulSoup
    import progressbar
    bar = progressbar.ProgressBar(maxval=len(input_dict),
                                  widgets=[progressbar.Bar('=', '[', ']'), ' ',
                                  progressbar.Percentage()])
    count = 0
    bar.start()
    result = {}
    for key in input_dict:
        bar.update(count)
        count += 1
        if(checkUrl(input_dict[str(key)])):
            result[str(key)] = input_dict[str(key)]
        else:
            soup = BeautifulSoup(input_dict[str(key)])
            result[str(key)] = soup.get_text()
        bar.finish()
    return result


def sanitize_dict(input_dict):
    import html
    from bs4 import BeautifulSoup
    import progressbar
    delete_empty(input_dict)
    bar = progressbar.ProgressBar(maxval=len(input_dict),
                                  widgets=[progressbar.Bar('=', '[', ']'), ' ',
                                  progressbar.Percentage()])
    count = 0
    bar.start()
    count += 1
    for key in input_dict:
        bar.update(count)
        count += 1
        if ((type(input_dict[str(key)]) is None) or 
                (type(input_dict[str(key)]) is type(None))):
            pass
        else:
            # convert byte to unicode
            if(type(input_dict[str(key)]) == bytes):
                input_dict[str(key)] = input_dict[str(key)].decode('utf-8')
            # remove non-ascii characters from strings
            input_dict[str(key)] = remove_non_ascii(input_dict[str(key)])
            # remove html encoding
            input_dict[str(key)] = html.unescape(input_dict[str(key)])
            # keep URL as-is
            if (checkUrl(input_dict[str(key)])):
                pass
            else:
                # sanitize with BeautifulSoup
                try:
                    input_dict[str(key)] = BeautifulSoup(
                        input_dict[str(key)]).get_text()
                except:
                    print("Unable to process line " + key)
    bar.finish()
    return input_dict

FILEPATH = 'data/comments.json'
KEY1 = 'title'
KEY2 = 'text'
comments_title = {}
comments_title = min_extract_to_dict(FILEPATH, KEY1)
comments_text = {}
comments_text = min_extract_to_dict(FILEPATH, KEY2)
# comments = extract_to_dict(FILEPATH)
comments_title_sanitized = {}
comments_title_sanitized = sanitize_dict(comments_title)
comments_text_sanitized = {}
comments_text_sanitized = sanitize_dict(comments_text)

# cleanup_dict(comments_title)
# cleanup_dict(comments_text)
# beautified_comments_title = {}
# beautified_comments_title = beautify_text(comments_title)
# beautified_comments_text = {}
# beautified_comments_text = beautify_text(comments_text)


# convert dictionary into token list
comments_title_tokens = []
for key in comments_title_sanitized:
    comments_title_tokens.extend(word_tokenize(comments_title_sanitized[str(key)]))
len(comments_title_tokens)
comments_title_tokens[:20]
comments_title_unique = set(comments_title_tokens)
len(comments_title_unique)
len(comments_title_tokens)/len(comments_title_unique)
sorted(comments_title_unique)[:30]
comments_title_single = [w for w in comments_title_unique if len(w) == 1 ]
len(comments_title_single)
comments_title_single

# frequently used words
fd = nltk.FreqDist(comments_title_tokens)
fd.most_common(50)
fd.plot(50)

# word length
fd_wlen = nltk.FreqDist([len(w) for w in comments_title_unique])
fd_wlen

# remove punctuation
print(string.punctuation)
comments_title_tokens_nop = [t for t in comments_title_tokens if t not in string.punctuation]
print(comments_title_tokens[:50])
print(comments_title_tokens_nop[:50])
len(comments_title_tokens)
len(comments_title_tokens_nop)
len(set(comments_title_tokens_nop))

# convert all characters to lower case
comments_title_tokens_lower = [t.lower() for t in comments_title_tokens_nop]
print(comments_title_tokens_lower[:50])
len(set(comments_title_tokens_lower))

# Create a stopword list from the standard list of stopwords available in nltk
stop = stopwords.words('english')
print(stop)

# Remove all these stopwords from the text
comments_title_tokens_nostop = [t for t in comments_title_tokens_lower if t not in stop]
print(comments_title_tokens_nostop[:50])
len(comments_title_tokens_lower)
len(comments_title_tokens_nostop)
FreqDist(comments_title_tokens_nostop).most_common(50)

# Use snowball stemmer
snowball = nltk.SnowballStemmer('english')
comments_title_tokens_snow = [snowball.stem(t) for t in comments_title_tokens_nostop]
print(comments_title_tokens_snow[:50])
len(set(comments_title_tokens_snow))

# Lemmatize words
wnl = nltk.WordNetLemmatizer()
comments_title_tokens_lem = [ wnl.lemmatize(t) for t in comments_title_tokens_nostop ]
print(comments_title_tokens_lem[:50])
len(set(comments_title_tokens_lem))

# Further cleaning: filter off anything with less than 3 characters
nltk.FreqDist(tokens_snow).most_common(100)
tokens_clean = [ t for t in tokens_snow if len(t) >= 3 ]
len(tokens_snow)
len(tokens_clean)
nltk.FreqDist(tokens_clean).most_common(50)
fd_clean = nltk.FreqDist(tokens_clean)