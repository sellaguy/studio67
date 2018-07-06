import requests
import random
import json
import urllib
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/search/duckduckgo/<word>', methods=['GET'])
def index(word):
	
	output = {}
	
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
	return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)