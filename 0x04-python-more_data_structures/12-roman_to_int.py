#!/usr/bin/python3
def roman_to_int(roman_string):
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    if type(roman_string) != str or roman_string is None:
        return result
    prev = None
    for ch in roman_string:
        n = nums[ch]

        if prev is None:
            result = n
            prev = n
            continue
        elif prev < n:
            result = result + n - prev * 2
        else:
            result += n

        prev = n

    return result
