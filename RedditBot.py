import praw 
import logging

class RedditBot:

    def __init__(self, bot_name, subreddit_name):
        # Construct bot_name and subreddit_name
        self.bot_name = bot_name
        self.subreddit_name = subreddit_name
        
        # Construct reddit and subreddit
        self.reddit = None
        self.subreddit = None

        # Call logging function
        self.logging()

    def logging(self):
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        for logger_name in ("praw", "prawcore"):
            logger = logging.getLogger(logger_name)
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)

    def connect(self):
        self.reddit = praw.Reddit(self.bot_name)
        self.subreddit = self.reddit.subreddit(self.subreddit_name)

    def fetch_submissions(self, limit=10, score_threshold=25):
        title = []
        url = []
        score = []

        if not self.reddit or not self.subreddit:
            print("Bot not connected to Reddit. Call connect() first.")
            return

        for submission in self.subreddit.hot(limit=limit):
            if submission.score > score_threshold:
                title.append(submission.title)
                url.append(submission.url)
                score.append(submission.score)

        return title, url, score