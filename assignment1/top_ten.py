import sys
import json
import collections


def main():
	tweet_data = {}
	entities = []
	hashtags_text = collections.OrderedDict()
	i = 0

	tweet_file = open(sys.argv[1])
	for line in tweet_file:
		tweet_data['%d'%i] = json.loads(line)
		i = i + 1
	# print type(tweet_data)
	# print tweet_data['1000'].keys()

#Extract the entities variable from the tweet file.
	for i in range(0,len(tweet_data)):
		if 'entities' in tweet_data['%d'%i]:
			entities.append(tweet_data['%d'%i]['entities'])

#Extract the hashtags text
	for i in range(0, len(entities)):
		for j in range(0,len(entities[i]['hashtags'])):
			text = entities[i]['hashtags'][j]['text']
			if text in hashtags_text:
				hashtags_text[text] = hashtags_text[text] + 1
			else:
				hashtags_text[text] = float(1)

#Sorting the hashtags according to the their frequencies.
	hashtags_text = sorted(hashtags_text.items(), key=lambda t: t[1],reverse=True)

#Printing the top ten hashtags that appear in the tweet file.
	for i in range(0,10):
		print hashtags_text[i][0], hashtags_text[i][1]
	# print dir(hashtags_text)
	


if __name__ == '__main__':
	main()