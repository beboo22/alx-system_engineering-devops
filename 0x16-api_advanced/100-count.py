#!/usr/bin/python3
"""
2-main
"""
import requests
recurse = __import__('2-recurse').recurse


def count_words(subreddit, word_list, word_count=None):
    """
    count words
    """
    if word_count is None:
        word_count = {word: 0 for word in word_list}

    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    sub_info = requests.get(subreddit_url, headers=headers)

    if sub_info.status_code != 200:
        return None

    lis = recurse(subreddit)

    if not lis:
        return None

    for title in lis:
        for word in word_list:
            for s in title:
                if s.lower() == word.lower():
                    word_count[word] += 1

    if sub_info.json().get("data").get("after"):
        return count_words(subreddit, word_list, word_count)
    else:
        for k, v in word_count.items():
            print(k, ": ", v)
