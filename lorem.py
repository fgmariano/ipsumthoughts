import tweepy
from random import randint

# Feed this next four vars with your tokens of access
CONSUMER_KEY = "-------------------"
CONSUMER_SECRET = "----------------------------------"
ACCESS_KEY = "----------------------------------"
ACCESS_SECRET = "-----------------------------------"

# postTweet receives the "tweet" string and send the status update via tweepy
def postTweet(tweet):
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	api.update_status(tweet)

# Gets the latin words from a .txt file to a list
def fileToArray():
	with open("resources/lorem.txt", "r") as file:
		myList = []
		for line in file:
			myList.append(line)
		stripped = [s.rstrip() for s in myList]
	return stripped

# Gets the previous list and generate a "tweet" string by sorting up to 18 words
def generateIpsum(myList):
	tweet = myList[randint(0, 502)].capitalize()
	for i in range(0, 18):
		tweet += " " + myList[randint(0, 502)]
	return tweet

# getTweet runs the previous function to get a sorted string, checks if has less than 141 characters and send it to the postTweet function
def getTweet(lorem):
	passed = True
	tweet = ""
	while passed:
		tweet = generateIpsum(lorem)
		if len(tweet) <= 140:
			passed = False
	postTweet(tweet)

# Creates a instance of the txt wordlist
lorem = fileToArray()

# Runs the getTweet function to generate and post a new tweet
getTweet(lorem)