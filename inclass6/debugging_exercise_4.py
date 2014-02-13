# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:52:54 2014

@author: pruvolo
"""
def get_multiple_of_list(L,n):
    K = []    
    for i in range(len(L)):  
        K.append(L[i]*n)
        print K
    return K
    
def get_doubles_then_triples(J):
    """ Returns a new list containing the original list with each element
    	multiplied by 2 concatenated with the original list with each element
	multiplied by 3 """
    
    return get_multiple_of_list(J,2) + get_multiple_of_list(J,3)


if __name__ == '__main__':
    print get_doubles_then_triples([1, 4, 8])
