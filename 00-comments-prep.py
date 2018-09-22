#!/usr/bin/python3 -tt


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


# remove_non_ascii takes a string and strips all non-ascii characters from it
# before returning a string
def remove_non_ascii(s):
    return "".join(i for i in s if ord(i) < 128)


# checkUrl takes a string and checks if it is a properly formed URL address
def checkUrl(s):
    from urllib.parse import urlparse
    parse_result = urlparse(str(s))
    if parse_result.netloc == '':
        return False
    else:
        return True


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


def generate_wordcloud(input_dict, output_file_path):
    import nltk
    import string
    from nltk import word_tokenize, FreqDist
    from nltk.corpus import stopwords
    # convert dictionary into token list
    tokens = []
    for key in input_dict:
        tokens.extend(word_tokenize(input_dict[str(key)]))
    # remove punctuation
    tokens_nop = [t for t in tokens if t not in string.punctuation]
    # convert all characters to lower case
    tokens_lower = [t.lower() for t in tokens_nop]
    # Create a stopword list from the standard list of stopwords available in 
    # nltk
    stop = stopwords.words('english')
    # Remove all these stopwords from the text
    tokens_nostop = [t for t in tokens_lower if t not in stop]
    # Use snowball stemmer
    snowball = nltk.SnowballStemmer('english')
    tokens_snow = [snowball.stem(t) for t in tokens_nostop]
    # Lemmatize words
    wnl = nltk.WordNetLemmatizer()
    tokens_lem = [wnl.lemmatize(t) for t in tokens_nostop]
    # Further cleaning: filter off anything with less than 3 characters
    tokens_clean = [t for t in tokens_snow if len(t) >= 3]
    fd_clean = nltk.FreqDist(tokens_clean)
    text_clean = " ".join(tokens_clean)
    # Generate simple wordcloud
    import wordcloud
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    wc = WordCloud(background_color="white").generate(text_clean)
    # plt.imshow(wc, interpolation='bilinear')
    # plt.axis("off")
    # plt.show()
    # Save wordcloud to file
    wc.to_file(output_file_path)


FILEPATH = 'data/comments.json'
KEY1 = 'title'
KEY2 = 'text'
comments_title = {}
comments_title = min_extract_to_dict(FILEPATH, KEY1)
comments_text = {}
comments_text = min_extract_to_dict(FILEPATH, KEY2)
comments_title_sanitized = {}
comments_title_sanitized = sanitize_dict(comments_title)
comments_text_sanitized = {}
comments_text_sanitized = sanitize_dict(comments_text)
generate_wordcloud(comments_title_sanitized, 'results/comments_title.png')
generate_wordcloud(comments_text_sanitized, 'results/comments_text.png')
