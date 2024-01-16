#!/usr/bin/python3
"""Module"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """docs"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        hot_list.extend([post['data']['title']
                        for post in data['data']['children']])
        if data['data']['after']:
            recurse(subreddit, hot_list, after=data['data']['after'])
        else:
            return hot_list
    else:
        return None
