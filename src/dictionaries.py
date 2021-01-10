letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


#Part1: Building a Point Dictionary
letter_to_points = {key:value for key, value in zip(letters, points)}
print(letter_to_points)
letter_to_points[" "] = 0

#Part2: Score a Word
def score_word(word):
  point_total=0
  for key, value in letter_to_points.items():
    if(key in word):
      point_total+=value
  return point_total

#Part3: Score a Game
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reading":[]} 
player_to_points = {}
for key,value in player_to_words.items():
  points=0
  for word in value:
    points+=score_word(word)
  player_to_points[key] = points
print("Player to points: ")
print(player_to_words)