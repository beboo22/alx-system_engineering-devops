#!/usr/bin/python3
"""
1-main
"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""

    subreddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    geting_inf = requests.get(subreddit_url, headers=headers)

    if geting_inf.status_code == 404:
        return 0

    data = geting_inf.json().get("data")
    for c in data.get("children"):
        print(c.get('data').get("title"))
