#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""

def top_ten(subreddit):
    """ does what is stated above """
    import requests

    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    request = requests.get(url, headers={'User-Agent': 'Byn'})
    if request.status_code != 200:
        print(None)
        return None
    request = request.json()
    if 'data' in request:
        for thread in request.get('data').get('children'):
            print(thread.get('data').get('title'))
    else:
        print(None)
        return None
