import requests
import random
import json
import urllib

results = []
response = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
input = response.text.split()
count = 0

for line in input:
	if(random.randint(1,1000)==1 and line[0].islower() and line.isalpha() and count < 100):
		results.append(line.replace('\n',','))
		count = count + 1

output = {}

for word in results:
	index = 0
	temp = []
	params = urllib.parse.urlencode({'q': word, 'format': 'json', 'pretty': '1'})
	url = 'http://api.duckduckgo.com/?' + params
	ddgresponse = requests.get(url)
	json_data = json.loads(ddgresponse.text)
	for subword in json_data['RelatedTopics']:
		if (index < 3):
			temp.append(subword['Text'])
			index += 1
	output[word] = temp


