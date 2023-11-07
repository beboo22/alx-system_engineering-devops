#!/usr/bin/python3
"""
2-main
"""
import requests


def recurse(subreddit, hot_list=[], s=0):
    """
    subscribers
    """
    req = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers={"User-Agent": "User-Agent"})
    if req.status_code < 300:
        if len(req.json().get("data").get("children")) > s:
            hot_list.append(req.json().get("data").get("children")[s]
                               .get("data").get("title"))
        if req.json().get("data").get("after"):
            return recurse(subreddit, hot_list, s + 1)
        else:
            return hot_list
    else:
        return None 
