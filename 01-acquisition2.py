# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=The Meg'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print out the info
print(r.text)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()
print(type(json_data))
print(json_data)
print(json_data['Title'])
print(json_data.keys())

# for m in [1,2,3,5,6]:
#     print(m+1)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ':', json_data[k])