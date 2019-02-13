#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""


def recurse(subreddit=None, hot_list=[], after=None):
    """ does what is stated above """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)
    request = requests.get(url, headers={'User-Agent': 'Byn'})
    if request.status_code != 200:
        print(None)
        return None
    request = request.json()
    threads = request.get('data').get('children')
    for thread in threads:
        hot_list.append(thread.get('data').get('title'))
    if request.get('data').get('after'):
        return recurse(subreddit, hot_list=hot_list,
                       after=request.get('data').get('after'))
    return hot_list
