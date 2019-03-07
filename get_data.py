from json import dumps
from collections import defaultdict
import praw, configparser

config = configparser.ConfigParser()
config.read('oauth.conf')
client_key = config['keys']['client_id']
secret_key = config['keys']['client_secret']
reddit = praw.Reddit(client_id=client_key, client_secret=secret_key, user_agent='python nlp project by /u/viraj25j')
data_file = open("data.json", "w")
text = defaultdict(list)
for post in reddit.subreddit('ucf').top(limit=200):
    post.comments.replace_more(limit=32, threshold=0)
    for comment in post.comments.list():
        text[post.title].append(comment.body)      
data_file.write(dumps(text))
data_file.close()
