#!/usr/bin/python3
"""
0-main
"""
import requests


def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0

    subreddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    geting_inf = requests.get(subreddit_url)
    data = geting_inf.json()
    subscribe = data.get('data').get('subscribers')
    return subscribe
