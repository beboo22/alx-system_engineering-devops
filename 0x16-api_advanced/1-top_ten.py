#!/usr/bin/python3
"""
1-main
"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""

    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    geting_inf = requests.get(subreddit_url, headers=headers, params=params)

    if geting_inf.status_code == 404:
        print("None")
        return

    data = geting_inf.json().get("data")

    for c in data.get("children"):
        print(c.get('data').get("title"))
