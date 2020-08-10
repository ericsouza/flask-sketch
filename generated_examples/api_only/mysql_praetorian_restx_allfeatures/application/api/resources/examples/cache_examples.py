from application.ext.caching import cache
from random import randint
from time import sleep


@cache.cached(timeout=10)
def time_caching():
    """
    View route cached in time
    """

    rand_number = randint(1, 10000)
    return f"<h3> The number is: {rand_number}</h3>"


def external_func_caching():
    """
    View route that calls a function with caching
    """
    number = calculate()
    return f"<h3> The number is: {number}</h3>"


@cache.cached(timeout=10, key_prefix="calculate")
def calculate():
    return randint(50, 50000)


users_list = ["Eric", "Sarah", "Anthony", "Luke"]


@cache.memoize()
def get_names():
    sleep(3)  # sleeping for see caching in action

    ret = "<strong>Names:</strong> <br>"
    for name in users_list:
        ret += name + "<br>"

    return ret


# delete memoized when new user is added
def add_name(name):
    users_list.append(name)
    cache.delete_memoized(get_names)
    return f"{name} added to the list of name"
