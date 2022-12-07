import string

# Adding an empty string at the start to start indexing letters at 1
priority = ' ' + string.ascii_lowercase + string.ascii_uppercase

def extract(file):
    with open(file, 'r') as f:
        return [l.strip() for l in f.readlines()]

"""given two strings, returns the only character present in both strings"""
def string_match(str1, str2):
       first_string = set(str1)
       second_string = set(str2)
       return list(first_string & second_string)[0]

"""given a string with even numbered length, split string in half"""
def string_split(str):
  list = []
  half = int(len(str)/2)
  first_chunk = slice(0, half)
  second_chunk = slice(half, len(str))
  list.append(str[first_chunk])
  list.append(str[second_chunk])
  return list

"""Find the priority of the item type that appears in two halves of a strings"""
def get_priority(str):
  l = string_split(str)
  return priority.index(string_match(l[0], l[1]))\

"""Given a list of valid strings, return the sum of their priorities"""
def priority_sum(list):
  return sum([get_priority(str) for str in list])

if __name__ == "__main__":
    print(priority_sum(extract('data/input.txt')))