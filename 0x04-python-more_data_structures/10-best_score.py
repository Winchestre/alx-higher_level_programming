#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    keys = list(a_dictionary)
    val_big = a_dictionary[keys[0]]
    key_big = keys[0]
    for key in keys:
        if a_dictionary[key] > val_big:
            val_big = a_dictionary[key]
            key_big = key
    return key_big
