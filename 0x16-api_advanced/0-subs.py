#!/usr/bin/python3
"""0-subs Module"""

import requests

headers = {"User-Agent": "MyRedditBot/1.0"}


def number_of_subscribers(subreddit):
    """number of subs"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
