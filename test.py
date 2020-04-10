from greatest_warrior import *


bruce_lee = Warrior()
print(bruce_lee.level)         # => 1
print(bruce_lee.experience)   # => 100
print(bruce_lee.rank)       # => "Pushover"
print(bruce_lee.achievements)  # => []
print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1])) # => "Defeated Chuck Norris"
print(bruce_lee.experience)    # => 9100
print(bruce_lee.level)         # => 91
print(bruce_lee.rank)       # => "Master"
print(bruce_lee.battle(90))   # => "A good fight"
print(bruce_lee.experience)    # => 9105
print(bruce_lee.achievements)  # => ["Defeated Chuck Norris"]