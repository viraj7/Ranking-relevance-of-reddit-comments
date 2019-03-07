from json import dumps
from collections import defaultdict
import praw
reddit = praw.Reddit(client_id='zneTpAmTMY7CoQ', client_secret='McixCrruKKChhHw3SElyvVleb5w', user_agent='python nlp project by /u/viraj25j')
data_file = open("data.json", "w")
text = defaultdict(list)
for post in reddit.subreddit('ucf').top(limit=200):
    post.comments.replace_more(limit=32, threshold=0)
    for comment in post.comments.list():
        text[post.title].append(comment.body)
print(len(text))        
data_file.write(dumps(text))
data_file.close()
