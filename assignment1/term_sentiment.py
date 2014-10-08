import json
import sys

def lines(fp):
	print str(len(fp.readlines()))


def main():
#Reads the data from the sentiment file and the tweet file.
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
#Declares the various data structures needed in the program. scores is a dictionary which stores the scores for each word. tweet_data stores the tweeted data.
#tweets is a list which extracts only tweets from the twitter data. sentiment_score calculates the final score for each tweet.
	scores = {}
	tweet_data = {}
	non_sentiment_words = {}
	# non_sentiment_words_score = []
	tweets = []
	sentiment_score = []
	i = 0

#Storing values in scores dictionary
	for line in sent_file:
		term,score = line.split("\t")
		scores[term] = int(score)
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
		sentiments = 0
		for j in range(0,len(tweet)):
			if tweet[j] in scores:
				sentiments = sentiments + scores[tweet[j]]
			elif tweet[j] in non_sentiment_words:
				continue
			else:
				non_sentiment_words[tweet[j]] = 0

		sentiment_score.append(sentiments)
	# print non_sentiment_words.keys()
	# print len(non_sentiment_words)

#This block of code produces sentiment score for the words which are not assigned a sentiment score beforehand.
	for i in range(0,len(tweets)):
		tweet = tweets[i].rsplit(" ")
		for j in range(0,len(tweet)):
			if tweet[j] in non_sentiment_words:
				if sentiment_score[i] > 0:
					non_sentiment_words[tweet[j]] = float(non_sentiment_words[tweet[j]]) + float(2*int(sentiment_score[i]))	
				if j>0 and tweet[j-1] in scores:
					non_sentiment_words[tweet[j]] = float(non_sentiment_words[tweet[j]]) + float(10*int(scores[tweet[j-1]]))
				if j<(len(tweet)-1) and tweet[j+1] in scores:
					non_sentiment_words[tweet[j]] = float(non_sentiment_words[tweet[j]]) + float(10*int(scores[tweet[j+1]]))
	
	new_scores = non_sentiment_words.values()
	new_words = non_sentiment_words.keys()
	for i in range(0,len(new_words)):
		print new_words[i], new_scores[i]


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


