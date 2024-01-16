#!/usr/bin/python3
"""Module"""

import requests


headers = {'User-Agent': 'MyCustomUserAgent/1.0'}


def top_ten(subreddit):
    """top ten"""
    url = f'https://www.reddit.com/r/{subreddit}/hot?limit=10.json'
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for i in data["data"]["children"]:
            print(i["data"]["title"])
    else:
        print("None")
