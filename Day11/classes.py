# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 14:19:41 2014

@author: jvaccaro
"""

class User:
    pass

def print_user_info():
    a = "User's "
    print a + "Name: " + u.name
    print a + "Hometown: " + u.home_town
    print a + "Friends: "
    for friend in u.friends:
        print " " + friend.name
    
def make_friends(user_1, user_2):
    user_1.friends.append(user_2)
    user_2.friends.append(user_1)

if __name__ == '__main__':
    u = User()
    u.name = "Jenny Vaccaro"
    u.home_town = "Reading, MA"
    print u.name
    u2 = User()
    u2.name = "Sarah Walters"
    u2.home_town = "Boulder, CU"
    make_friends(u, u2)
    print 