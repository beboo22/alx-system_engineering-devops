#!/usr/bin/python3
"""
1-main
"""
import requests


def top_ten(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0

    subreddit_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    geting_inf = requests.get(subreddit_url)
    data = geting_inf.json().get("data")
    
    print(data)
