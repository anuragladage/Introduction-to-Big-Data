import json
import sys
import math

# def lines(fp):
# 	print str(len(fp.readlines()))


def main():
#Reads the data from the sentiment file and the tweet file.
	tweet_file = open(sys.argv[1])
#Declares the various data structures needed in the program. scores is a dictionary which stores the scores for each word. tweet_data stores the tweeted data.
#tweets is a list which extracts only tweets from the twitter data. sentiment_score calculates the final score for each tweet.
	tweet_data = {}
	tweets = []
	words = {}
	frequency = {}
	i=0

#Storing value in the tweet_data dictionary.
	for line in tweet_file:
		tweet_data['%d'%i] = json.loads(line)
		i = i + 1
#Extracting tweets from the tweet_data dictionary.
	for i in range(0,len(tweet_data)):
		if 'text' in tweet_data['%d'%i]:
			tweets.append(tweet_data['%d'%i]['text'])

# The below block of code splits the sentence into words and stores it in a list called tweet. Then the sentiment score is calculated. 
	for i in range(0,len(tweets)):
		tweet = tweets[i].rsplit(" ")
		for j in range(0,len(tweet)):
			if tweet[j] in words:
				words[tweet[j]] = words[tweet[j]] + 1
			else:
				words[tweet[j].strip()] = 1

	words_sum = sum(words.values())
	for i in words.keys():
		frequency[i] = float(words[i])/float(words_sum)

	words = words.keys()
	frequency = frequency.values()

	for i in range(1,len(frequency)):
		print words[i], frequency[i]






#A test code to verify whether the sentiment score calculated is correct by analysing a single tweet. In this case the tweet number 18 is analysed.
	# tweet = tweets[18].rsplit(" ")
	# sentiments = 0
	# for i in range(0,len(tweet)):
	# 	if tweet[i] in scores:
	# 		sentiments = sentiments + scores[tweet[i]]
	# 		print tweet[i]
	# print sentiments

if __name__ == '__main__':
	main()


