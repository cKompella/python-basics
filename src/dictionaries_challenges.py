#Challenge1: returns sum of dictionary values
def sum_values(my_dictionary):
  sum = 0
  for value in my_dictionary.values():
    sum+=value
  return sum
#Challenge2: returns sum of values of even keys in my_dict
def sum_even_keys(my_dict):
  sum=0
  for key,value in my_dict.items():
    if(key%2==0):
      sum+=value
  return sum
#Challenge3: adds 10 to every value in my_dict
def add_ten(my_dict):
  for key,value in my_dict.items():
    my_dict[key] = value+10
  return my_dict
#Challenge4: returns a list of all values that are keys
def values_that_are_keys(my_dict):
  list = []
  for value in my_dict.values():
    if(value in my_dict.keys()):
      list.append(value)
  return list
#Challenge5: returns the key with largest value in my_dict
def max_key(my_dict):
  max = list(my_dict.keys())[0]
  for key, value in my_dict.items():
    if(my_dict[key]>my_dict[max]):
      max = key
  return max
#Challenge6: returns a dictionary with keys as word from words and values as word length
def word_length_dictionary(words):
  return {word: len(word) for word in words}
#Challenge7: returns dictionary with frequency of word in words
def frequency_dictionary(words):
  return {word: words.count(word) for word in words}
#Challenge8: returns number of unique values in dict
def unique_values(dict):
  existing=[]
  for value in dict.values():
    if(value not in existing):
      existing.append(value)
  return len(existing)
#Challenge9: Return dictionary with key as initial and value as number of first names with that initial
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters


