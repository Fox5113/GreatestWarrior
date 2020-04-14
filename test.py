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


bruce_leeV2 = Warrior()
print(bruce_leeV2.level)         # => 1
print(bruce_leeV2.experience)   # => 100
print(bruce_leeV2.rank)       # => "Pushover"
print(bruce_leeV2.achievements)  # => []
print(bruce_leeV2.training(["Defeated Chuck Norris", 500, 1]))
print(bruce_leeV2.level) 
print(bruce_leeV2.battle(16))
print(bruce_leeV2.experience)


bruce_leeV2 = Warrior()
print(bruce_leeV2.battle(1))
print(bruce_leeV2.experience)

bruce_leeV2 = Warrior()
print(bruce_leeV2.training(["Defeated Chuck Norris", 400, 1]))
print(bruce_leeV2.battle(4))
print(bruce_leeV2.experience)

bruce_leeV2 = Warrior()
print(bruce_leeV2.training(["Defeated Chuck Norris", 200, 1]))
print(bruce_leeV2.battle(9))
print(bruce_leeV2.experience)

bruce_leeV2 = Warrior()
print(bruce_leeV2.training(["Defeated Chuck Norris", 700, 1]))
print(bruce_leeV2.battle(13))
print(bruce_leeV2.experience)



bruce_leeV2 = Warrior()
print(bruce_leeV2.training(["Defeated Chuck Norris", 500, 1]))
print(bruce_leeV2.battle(2))
print(bruce_leeV2.experience)