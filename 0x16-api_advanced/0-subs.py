#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit. If an
invalid subreddit is given, the function should return 0.
"""


def number_of_subscribers(subreddit):
    """ does what is stated above """
    import requests

    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    # url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    request = requests.get(url,
                           headers={'User-Agent': 'Byn'},
                           allow_redirects=False)
    # print(request)
    if request.status_code == 404:
        return 0
    request = request.json()
    # print(request)
    if 'data' in request:
        print(request.get('data'))
        return request.get('data').get('subscribers')
    return 0
