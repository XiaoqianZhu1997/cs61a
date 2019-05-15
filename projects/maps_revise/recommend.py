"""A Yelp-powered Restaurant Recommendation Program"""

from abstractions import *
from data import ALL_RESTAURANTS, CATEGORIES, USER_FILES, load_user_file
from ucb import main, trace, interact
from utils import distance, mean, zip, enumerate, sample
from visualize import draw_map

##################################
# Phase 2: Unsupervised Learning #
##################################


def find_closest(location, centroids):
    """ Return the centroid in centroids that is closest to location.
        If multiple centroids are equally close, return the first one."""
    ### first find the minimum value
    min_value = min([distance(p, location) for p in centroids])
    for p in centroids:
        if distance(p, location) == min_value:
            return p


def group_by_first(pairs):
    """ Return a list of pairs that relates each unique key in the [key, value]
        pairs to a list of all values that appear paired with that key.

        Arguments:
        pairs -- a sequence of pairs
        """
    keys = []
    for key, _ in pairs:
        if key not in keys:  # get all the unique keys
            keys.append(key)  # append new element
    return [[y for x, y in pairs if x == key] for key in keys]


def group_by_centroid(restaurants, centroids):
    """ Return a list of clusters, where each cluster contains all restaurants
        nearest to a corresponding centroid in centroids. Each item in
        restaurants should appear once in the result, along with the other
        restaurants closest to the same centroid.
        """
    clusters = [[find_closest(restaurant_location(restaurant), centroids), restaurant] for restaurant in restaurants]

    return group_by_first(clusters)
    ### find the nearest centroid one by one in the restaurants, and return a list
    ### each element in that returned list are paris like [centroid, restaurant]


def find_centroid(cluster):
    """Return the centroid of the locations of the restaurants in cluster."""
    loc = [restaurant_location(restaurant) for restaurant in cluster]
    lat, lot = [x for x, y in loc], [y for x, y in loc]
    return [mean(lat), mean(lot)]


def k_means(restaurants, k, max_updates=100):
    """Use k-means to group restaurants by location into k clusters."""
    assert len(restaurants) >= k, 'Not enough restaurants to cluster'
    old_centroids, n = [], 0
    # Select initial centroids randomly by choosing k different restaurants
    centroids = [restaurant_location(r) for r in sample(restaurants, k)]

    while old_centroids != centroids and n < max_updates:   # 不停迭代
        old_centroids = centroids
        # BEGIN Question 6
        "*** YOUR CODE HERE ***"
        clusters = group_by_centroid(restaurants, old_centroids)
        centroids = [find_centroid(lists) for lists in clusters]
        # END Question 6
        n += 1
    return centroids


################################
# Phase 3: Supervised Learning #
################################


def find_predictor(user, restaurants, feature_fn):
    """Return a rating predictor (a function from restaurants to ratings),
    for a user by performing least-squares linear regression using feature_fn
    on the items in restaurants. Also, return the R^2 value of this model.

    Arguments:
    user -- A user
    restaurants -- A sequence of restaurants
    feature_fn -- A function that takes a restaurant and returns a number
    """
    reviews_by_user = {review_restaurant_name(review): review_rating(review)
                       for review in user_reviews(user).values()}

    xs = [feature_fn(r) for r in restaurants]
    ys = [reviews_by_user[restaurant_name(r)] for r in restaurants]


    S_xx, S_yy = sum([(i - mean(xs))**2 for i in xs]), sum([(j - mean(ys))**2 for j in ys])
    S_xy = sum([(i - mean(xs)) * (j - mean(ys)) for i, j in zip(xs, ys)])
    b = S_xy / S_xx
    a = mean(ys) - b * mean(xs)
    r_squared = S_xy ** 2 / (S_xx * S_yy)


    def predictor(restaurant):
        return b * feature_fn(restaurant) + a

    return predictor, r_squared



def best_predictor(user, restaurants, feature_fns):
    """Find the feature within feature_fns that gives the highest R^2 value
    for predicting ratings by the user; return a predictor using that feature.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of functions that each takes a restaurant
    """
    reviewed = user_reviewed_restaurants(user, restaurants)

    func = max(feature_fns, key=lambda x: find_predictor(user, reviewed, x)[1])
    return find_predictor(user, reviewed, func)[0]


def rate_all(user, restaurants, feature_fns):
    """Return the predicted ratings of restaurants by user using the best
    predictor based on a function from feature_fns.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of feature functions

    """
    predictor = best_predictor(user, ALL_RESTAURANTS, feature_fns)
    reviewed = user_reviewed_restaurants(user, restaurants)

    all_restaurant = {}

    for restaurant in restaurants:
        name = restaurant_name(restaurant)
        if restaurant in reviewed:
            all_restaurant[name] = user_rating(user, name)   # 给dict的key赋值
        else:
            all_restaurant[name] = predictor(restaurant)
    return all_restaurant


def search(query, restaurants):
    """Return each restaurant in restaurants that has query as a category.

    Arguments:
    query -- A string
    restaurants -- A sequence of restaurants
    """
    return [r for r in restaurants if query in restaurant_categories(r)]


def feature_set():
    """Return a sequence of feature functions."""
    return [lambda r: mean(restaurant_ratings(r)),
            restaurant_price,
            lambda r: len(restaurant_ratings(r)),
            lambda r: restaurant_location(r)[0],
            lambda r: restaurant_location(r)[1]]


@main
def main(*args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Run Recommendations',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-u', '--user', type=str, choices=USER_FILES,
                        default='test_user',
                        metavar='USER',
                        help='user file, e.g.\n' +
                        '{{{}}}'.format(','.join(sample(USER_FILES, 3))))
    parser.add_argument('-k', '--k', type=int, help='for k-means')
    parser.add_argument('-q', '--query', choices=CATEGORIES,
                        metavar='QUERY',
                        help='search for restaurants by category e.g.\n'
                        '{{{}}}'.format(','.join(sample(CATEGORIES, 3))))
    parser.add_argument('-p', '--predict', action='store_true',
                        help='predict ratings for all restaurants')
    parser.add_argument('-r', '--restaurants', action='store_true',
                        help='outputs a list of restaurant names')
    args = parser.parse_args()

    # Output a list of restaurant names
    if args.restaurants:
        print('Restaurant names:')
        for restaurant in sorted(ALL_RESTAURANTS, key=restaurant_name):
            print(repr(restaurant_name(restaurant)))
        exit(0)

    # Select restaurants using a category query
    if args.query:
        restaurants = search(args.query, ALL_RESTAURANTS)
    else:
        restaurants = ALL_RESTAURANTS

    # Load a user
    assert args.user, 'A --user is required to draw a map'
    user = load_user_file('{}.dat'.format(args.user))

    # Collect ratings
    if args.predict:
        ratings = rate_all(user, restaurants, feature_set())
    else:
        restaurants = user_reviewed_restaurants(user, restaurants)
        names = [restaurant_name(r) for r in restaurants]
        ratings = {name: user_rating(user, name) for name in names}

    # Draw the visualization
    if args.k:
        centroids = k_means(restaurants, min(args.k, len(restaurants)))
    else:
        centroids = [restaurant_location(r) for r in restaurants]
    draw_map(centroids, restaurants, ratings)