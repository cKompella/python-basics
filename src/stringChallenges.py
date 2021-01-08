#Challenge1: returns number of unique letters in word
def unique_english_letters(word):
  temp = ""
  for letter in word:
    if(not letter in temp):
      temp+=letter
  return len(temp)

#Challenge2: returns number of times x appears in word
def count_char_x(word, x):
  count = 0
  index = word.find(x)
  while(not index==-1):
    count+=1
    word = word[index+1:]
    index = word.find(x)
  return count

#Challenge3: returns substring of word between start and end letters
def substring_between_letters(word, start, end):
  indexStart = word.find(start)+1
  indexEnd = word.find(end)
  if(indexStart==-1 or indexEnd==-1):
    return word
  return word[indexStart:indexEnd]

#Challenge4: returns True if every word in sentence has length>=x
def x_length_words(sentence, x):
  list = sentence.split(" ")
  for word in list: 
    if(not len(word)>=x):
      return False
  return True

#Challenge5: returns True if name appears in sentence
def check_for_name(sentence, name):
  sentence = sentence.lower()
  name = name.lower()
  if (name in sentence):
    return True
  return False

#Challenge6: returns a string with every other letter in word 
def every_other_letter(word):
  temp = [word[i] for i in range(len(word)) if i%2==0]
  return "".join(temp)

#Challenge7: returns word in reverse
def reverse_string(word):
  temp = ""
  for i in range(len(word)):
    temp+=word[len(word)-i-1]
  return temp
  
#Challenge8: returns string with first letters of word1 and word2 switched
def make_spoonerism(word1, word2):
  first_word1 = word1[0]
  first_word2 = word2[0]
  word1 = first_word2+word1[1:]
  word2 = first_word1+word2[1:]
  return word1+" "+word2

#Challenge9: adds exclamation points to word until it is 20 characters long
def add_exclamation(word):
  if(len(word)<20):
    while(len(word)<20):
      word = word+"!"
  return word

