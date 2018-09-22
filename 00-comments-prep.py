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
                (type(input_dict[str(key)]).isinstance(type(None)))):
            to_delete.append(key)
    for key in to_delete:
        del input_dict[str(key)]


# remove_non_ascii takes a string and strips all non-ascii characters from it
# before returning a string
def remove_non_ascii(s):
    return "".join(i for i in s if ord(i) < 128)


# cleanup_dict takes a dictionary, removes all empty records, converts byte
# type to unicode, removes all non ascii characters, and remove html encoding
def cleanup_dict(input_dict):
    # delete empty records
    delete_empty(input_dict)
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
        if(type(input_dict[str(key)]) == bytes):
            input_dict[str(key)] = input_dict[str(key)].decode('utf-8')
        # remove non-ascii characters from strings
        input_dict[str(key)] = remove_non_ascii(input_dict[str(key)])
        # remove html encoding
        input_dict[str(key)] = html.unescape(input_dict[str(key)])


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


def main():
    FILEPATH = 'data/comments.json'
    KEY1 = 'title'
    KEY2 = 'text'
    comments_title = {}
    comments_title = min_extract_to_dict(FILEPATH, KEY1)
    comments_text = {}
    comments_text = min_extract_to_dict(FILEPATH, KEY2)
    # comments = extract_to_dict(FILEPATH)
    cleanup_dict(comments_title)
    cleanup_dict(comments_text)
    beautified_comments_title = {}
    beautified_comments_title = beautify_text(comments_title)
    beautified_comments_text = {}
    beautified_comments_text = beautify_text(comments_text)


if __name__ == '__main__':
    main()
