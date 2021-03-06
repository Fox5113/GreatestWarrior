class Warrior(object):


    maxlevel = 100
    startlevel = 1
    ranks = ['Pushover', 'Novice', 'Fighter', 'Warrior', 'Veteran', 'Sage', 'Elite', 'Conqueror', 'Champion', 'Master', 'Greatest']
    index_start_rank = 0
    experience_to_up = 100
    start_experience = 100
    max_experience = 10000


    def __init__(self):
        self.level = self.startlevel
        self.rank = self.ranks[self.index_start_rank]
        self.experience = self.start_experience
        self.achievements = []
        self.index_rank = self.index_start_rank


    def battle(self, enemy_level):
        if enemy_level <= 0 or enemy_level > 100:
            return "Invalid level"
        diff = enemy_level - self.level
        if 1 >   self.level > 100:
            return "Invalid level"
        if diff  == 0:
            self.add_experience(experience=10)
            return "A good fight"
        elif diff  == -1:
            self.add_experience(experience=5)
            return "A good fight"
        elif   diff  <= -2:
            #self.add_experience(experience=0)
            return "Easy fight"
        elif  5 > diff  > 0 or  enemy_level // 10 <= self.level // 10 :
            self.add_experience(experience= (20 * diff * diff))
            return "An intense fight"
        else:
            return "You've been defeated"

    def training(self, arr):
        name, count_experence, recomend_level = arr
        if recomend_level <= 0:
            return "Invalid level"
        if self.level >= recomend_level:

            self.achievements.append(name)
            self.add_experience(count_experence)
            return name
        else:
            return "Not strong enough"

    def add_experience(self, experience):
        current_exp  = self.experience + experience
        if current_exp >= self.max_experience:
            self.experience = self.max_experience
            self.level = 100
            self.rank = self.ranks[10]
        if current_exp > self.max_experience:
            current_exp = self.max_experience
            return "Invalid level"

        self.experience = current_exp
        self.level = current_exp // 100
        self.rank = self.ranks[current_exp // 1000]



