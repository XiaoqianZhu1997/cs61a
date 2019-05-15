import collections
import os
from abstractions import *


"""A wrapper around Python's json module to parse newline-delimited json.

>>> all_reviews = load(open('reviews.json'))
>>> dump(all_reviews, open('reviews_copy.json', 'w'))
>>> all_reviews == load(open('reviews_copy.json'))
True
"""

from json import loads, dumps

def load(fp, **kw):
    return [loads(obj, **kw) for obj in fp]

def dump(objs, fp, **kw):
    for obj in objs:
        fp.write(dumps(obj, **kw))
        fp.write('\n')

DATA_DIRECTORY = 'data'
USER_DIRECTORY = 'users'

def load_data(user_dataset, review_dataset, restaurant_dataset):
    path = "/Users/zhuxiaoxi/Desktop/🇨🇭交换/Skills_Programming_Introduction_Level/report/data/"  # set the path
    user_path = path + user_dataset
    f1 = open(user_path)
    user_data = load(f1)

    review_path = path + review_dataset
    f2 = open(review_path)
    review_data = load(f2)

    restaurant__path = path + restaurant_dataset
    f3 = open(restaurant__path)
    restaurant_data = load(f3)

    # Load users.
    userid_to_user = {}
    for user in user_data:
        name = user['name']
        _user_id = user['user_id']
        user = make_user(name, []) # MISSING: reviews

        userid_to_user[_user_id] = user

    # Load restaurants.
    busid_to_restaurant = {}
    for restaurant in restaurant_data:
        name = restaurant['name']
        location = float(restaurant['latitude']), float(restaurant['longitude'])
        categories = restaurant['categories']
        price = restaurant['price']
        if price is not None:
            price = int(price)
        num_reviews = int(restaurant['review_count'])

        _business_id = restaurant['business_id']
        restaurant = make_restaurant(name, location, categories, price, []) # MISSING: reviews
        busid_to_restaurant[_business_id] = restaurant

    # Load reviews.
    reviews = []
    busid_to_reviews = collections.defaultdict(list)
    userid_to_reviews = collections.defaultdict(list)
    for review in review_data:
        _user_id = review['user_id']
        _business_id = review['business_id']

        restaurant = restaurant_name(busid_to_restaurant[_business_id])
        rating = float(review['stars'])

        review = make_review(restaurant, rating)
        reviews.append(review)
        busid_to_reviews[_business_id].append(review)
        userid_to_reviews[_user_id].append(review)
    # Reviews done.

    restaurants = {}
    for busid, restaurant in busid_to_restaurant.items():
        name = restaurant_name(restaurant)
        location = list(restaurant_location(restaurant))
        categories = restaurant_categories(restaurant)
        price = restaurant_price(restaurant)
        restaurant_reviews = busid_to_reviews[busid]

        restaurant = make_restaurant(name, location, categories, price, restaurant_reviews)
        restaurants[name] = restaurant
    # Restaurants done.

    users = []
    for userid, user in userid_to_user.items():
        name = user_name(user)
        user_reviews = userid_to_reviews[userid]

        user = make_user(name, user_reviews)
        users.append(user)
    # Users done.

    return users, reviews, list(restaurants.values())

USERS, REVIEWS, ALL_RESTAURANTS = load_data('users.json', 'reviews.json', 'restaurants.json')
CATEGORIES = {c for r in ALL_RESTAURANTS for c in restaurant_categories(r)}

def load_user_file(user_file):
    with open(os.path.join(USER_DIRECTORY, user_file)) as f:
        return eval(f.read())

import glob
USER_FILES = [f[6:-4] for f in glob.glob('users/*.dat')]
