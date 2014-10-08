import sys
import json
import math
import collections

def main():
#Reads the data from the sentiment file and the tweet file.
        states = {
                'AK': 'Alaska',
                'AL': 'Alabama',
                'AR': 'Arkansas',
                'AS': 'American Samoa',
                'AZ': 'Arizona',
                'CA': 'California',
                'CO': 'Colorado',
                'CT': 'Connecticut',
                'DC': 'District of Columbia',
                'DE': 'Delaware',
                'FL': 'Florida',
                'GA': 'Georgia',
                'GU': 'Guam',
                'HI': 'Hawaii',
                'IA': 'Iowa',
                'ID': 'Idaho',
                'IL': 'Illinois',
                'IN': 'Indiana',
                'KS': 'Kansas',
                'KY': 'Kentucky',
                'LA': 'Louisiana',
                'MA': 'Massachusetts',
                'MD': 'Maryland',
                'ME': 'Maine',
                'MI': 'Michigan',
                'MN': 'Minnesota',
                'MO': 'Missouri',
                'MP': 'Northern Mariana Islands',
                'MS': 'Mississippi',
                'MT': 'Montana',
                'NA': 'National',
                'NC': 'North Carolina',
                'ND': 'North Dakota',
                'NE': 'Nebraska',
                'NH': 'New Hampshire',
                'NJ': 'New Jersey',
                'NM': 'New Mexico',
                'NV': 'Nevada',
                'NY': 'New York',
                'OH': 'Ohio',
                'OK': 'Oklahoma',
                'OR': 'Oregon',
                'PA': 'Pennsylvania',
                'PR': 'Puerto Rico',
                'RI': 'Rhode Island',
                'SC': 'South Carolina',
                'SD': 'South Dakota',
                'TN': 'Tennessee',
                'TX': 'Texas',
                'UT': 'Utah',
                'VA': 'Virginia',
                'VI': 'Virgin Islands',
                'VT': 'Vermont',
                'WA': 'Washington',
                'WI': 'Wisconsin',
                'WV': 'West Virginia',
                'WY': 'Wyoming'
        }
        sent_file = open(sys.argv[1])
        tweet_file = open(sys.argv[2])
#Declares the various data structures needed in the program. scores is a dictionary which stores the scores for each word. tweet_data stores the tweeted data.
#tweets is a list which extracts only tweets from the twitter data. sentiment_score calculates the final score for each tweet.
        scores = {}
        tweet_data = {}
        tweet_location = {}
        happy_states = collections.OrderedDict()
        tweets = []
        users = []
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

#Extracting user list from the tweet_data dictionary.
        for i in range(0,len(tweet_data)):
                if 'user' in tweet_data['%d'%i]:
                        users.append(tweet_data['%d'%i]['user'])

#Extracting tweets from the tweet_data dictionary.
        for i in range(0,len(tweet_data)):
                if 'text' in tweet_data['%d'%i]:
                        tweets.append(tweet_data['%d'%i]['text'])

# The below block of code splits the sentence into words and stores it in a list called tweet. Then the sentiment score is calculated. 
        for i in range(0,len(tweets)):
                tweet = tweets[i].rsplit(" ")
                sentiments = 0
                for i in range(0,len(tweet)):
                        if tweet[i] in scores:
                                sentiments = sentiments + scores[tweet[i]]
                sentiment_score.append(sentiments)
# #Printing the sentiment score        
#         for i in range(0,len(sentiment_score)):
#                 print sentiment_score[i]

#Making a tweet_location dictionary which renames anything other than US states as 'Others'.
        for i in range(0,len(users)):
                location = users[i]['location'].rsplit()
                count = 0
                for j in range(0,len(location)):
                        if location[j].capitalize() in states.values():
                                count = count + 1
                                tweet_location['%d'%i] = location[j].capitalize()
                if count == 0:
                        tweet_location['%d'%i] = 'Others'

        for i in range(0,len(tweet_location)):
                if sentiment_score[i]>0:
                        if tweet_location['%d'%i] == 'Others':
                                happy_states['Others'] = 0
                        elif tweet_location['%d'%i] in happy_states:
                                happy_states[tweet_location['%d'%i]] = happy_states[tweet_location['%d'%i]]+ sentiment_score[i]
                        else:
                                happy_states[tweet_location['%d'%i]] = sentiment_score[i]

        happy_states = sorted(happy_states.items(), key=lambda t: t[1],reverse=True)

#Converting the state name to its corresponding abbreviated form.
        for i in states:
                if happy_states[0][0] == states[i]:
                        return i


# #Printing out only the states in US
#         for i in range(0,len(tweet_location)):
#                 if tweet_location['%d'%i] != 'Others':
#                         print tweet_location['%d'%i]



if __name__ == '__main__':
        print main()

