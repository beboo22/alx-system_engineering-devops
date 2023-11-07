#!/usr/bin/python3
"""
2-main
"""
import requests


def recurse(subreddit, hot_list=[], s=0):
    """
    subscribers
    """
    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    sub_info = requests.get(subreddit_url, headers)
    if sub_info.status_code < 300:
        if len(sub_info.json().get("data").get("children")) > s:
            hot_list.append(sub_info.json().get("data").get("children")[s]
                            .get("data").get("title"))
        if sub_info.json().get("data").get("after"):
            return recurse(subreddit, hot_list, s + 1)
        else:
            return hot_list
    else:
        return None
