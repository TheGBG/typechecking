import src.non_typed as non_typed
import src.typed as typed

# How can we now if this code is correct without touching it? F12...
users = non_typed.get_users_data()  # what is this thing returing? A table?

# Is this going to work? What are users? How many users? all equal?
max_age = non_typed.get_max_age(users)


# Ok so users is some sort of collections of user. And each user has stuff
# in it, right?

type(users)  # cool, is a list

type(users[0])  # ok, the first elem is a dict.
                # what keys does it have?
                # are all items in this collection dicts?
                # do they have the same types?
                # what about cv? What the hell is that?
                # do all of them have that? And their nested keys?
                # what about the values of this keys?

# Ok, lets keep moving
assert all([isinstance(user, dict) for user in users])

# What keys do we have? And nested keys?
for user in users:
    print(user.keys())

    for value in user.values():
        if isinstance(value, dict):
            print(value.keys())
            print(value.values())

# ... we could keep going forever. and this is only for a dumb example

# We dont need to go see the implementation of the method and read it
users = typed.get_users_data()
max_age = typed.get_max_age(users)


# Mypy will catch this
typed.get_max_age(users=["user_a", "user_b"])
