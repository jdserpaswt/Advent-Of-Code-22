def extract(file):
    with open(file, 'r') as f:
        return [l.strip() for l in f.readlines()]

"""given two strings, returns the only character present in both strings"""
def string_match(str1, str2):
       first_string = set(str1)
       second_string = set(str2)
       return list(first_string & second_string)[0]

"""given a string with even numbered length, split string in half"""
# TODO

if __name__ == "__main__":
    l = extract('data/test.txt')