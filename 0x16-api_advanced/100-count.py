#!/usr/bin/python3
"""
2-main
"""
import requests


def count_words(subreddit, word_list):
    """
    count words
    """
    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers={"User-Agent": "My-User-Agent"}
    sub_info = requests.get(subreddit_url,headers)
    if sub_info.status_code != 200:
        return None
    lis = recurse(subreddit)
    if not lis:
        return None
    for title in lis:
        for word in word_list:
            for s in title:
                if s == word:
                    word_count[word] += 1
    if sub_info.json().get("data").get("after"):
        return count_words(subreddit, word_list, word_count)
    else:
        for k, v in word_count:
            print(k, ": ", v)
