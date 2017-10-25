#!/usr/bin/python3

import praw
import pdb
import re
import os

#Reddit instance
reddit = praw.Reddit('bot1')

if not os.path.isfile("replied_to_posts.txt"):
    replied_to_posts = []
else:
    with open("replied_to_posts.txt", "r") as f:
        replied_to_posts = f.read()
        replied_to_posts = replied_to_posts.split("\n")
        replied_to_posts = list(filter(None, replied_to_posts))

subreddit = reddit.subreddit('davidemily')

for submission in subreddit.hot(limit=10):
    if submission.id not in replied_to_posts:
        if re.search("David", submission.title, re.IGNORECASE):
            submission.reply("Who the fuck is that?")
            print("Bot replying to : ", submission.title)
            replied_to_posts.append(submission.id)

with open("replied_to_posts.txt", "w") as f:
    for post_id in replied_to_posts:
        f.write(post_id + "\n")
