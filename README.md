# BuildAPCSales-Monitor

BuildAPCSales Monitor is a script that parses the r/BuildAPCSales subreddit using Reddit's API and the PRAW library to find the top posts of the day. The script will then email a list of the top posts or deals to the user. Deploying the script to a cloud service such as Heroku and using a scheduling app will allow the user to receive a list of deals emailed to their inbox every day at a set time.

## Dependencies

The program requires the PRAW library and python-dotenv. There may be other required libraries which are listed in `requirements.txt`.

`pip install praw`

`pip install python-dotenv`

## Usage

The user must set a SENDER_ADDRESS, SENDER_PASSWORD, and RECIPIENT_ADDRESS in .env. A separate email must be used for the sender. If using Gmail, an app password must be [generated](https://support.google.com/accounts/answer/185833?hl=en). Within the `praw.ini` file, the user must set the details for accessing [Reddit's API](https://www.reddit.com/wiki/api/). After these steps are completed, `python3 main.py` can be run.
