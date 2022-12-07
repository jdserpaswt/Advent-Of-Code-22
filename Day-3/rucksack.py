import string

# Adding an empty string at the start to start indexing letters at 1
priority = ' ' + string.ascii_lowercase + string.ascii_uppercase

def extract(file):
  with open(file, 'r') as f:
    return [l.strip() for l in f.readlines()]

"""given two strings, returns the only character present in both strings"""
def string_match_double(str1, str2):
  first_string = set(str1)
  second_string = set(str2)
  return list(first_string & second_string)[0]

"""given three strings, returns the only character present in all strings"""
def string_match_triple(str1, str2, str3):
  first_string = set(str1)
  second_string = set(str2)
  third_string = set(str3)
  return list(first_string & second_string & third_string)[0]

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
def get_priority_half(str):
  l = string_split(str)
  return priority.index(string_match_double(l[0], l[1]))

"""Given a list of strings, sepperate the into a list with lists of three strings"""
# TODO
"""Find the priority of the item type that appears in three strings"""
def get_priority_three(str1, str2, str3):
  return priority.index(string_match_triple(str1, str2, str3))

"""Given a list of valid strings, return the sum of their priorities"""
def priority_sum(list, option):
  if(option == 'half'):
    return sum([get_priority_half(str) for str in list])
  elif(option == 'triple'):
    return sum()

if __name__ == "__main__":
    print(priority_sum(extract('data/input.txt'), 'half'))
    l = extract('data/test.txt')
    print(get_priority_three(l[0], l[1], l[2]))