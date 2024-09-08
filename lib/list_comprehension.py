#!/usr/bin/env python3

def return_evens(num_list):
    # Use 'num_list' instead of 'num'
    return [x for x in num_list if x % 2 == 0]

# Example usage
print(return_evens([0, 1, 3, 5, 7, 8, 9]))  # Output: [0, 8]

def make_exclamation(sentences_list):
    return [s + '!' for s in sentences_list]

# Example usage
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
# Output: ["Hello!", "I'm doing great!", "Python is fun!"]