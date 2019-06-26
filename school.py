class School:
    def __init__(self, name, roster = {}):
        self.name = name
        self.roster = roster


    def add_student(self, name, grade_level):
        self.name = name
        self.grade_level = grade_level

        std_name = []
        if grade_level in self.roster:
            self.roster[grade_level].append(name)
        else:
            self.roster[grade_level] = std_name
            std_name.append(name)


    def grade(self, grade2):
        self.grade2 = grade2
        return self.roster[grade2]

    def sort_roster(self):
        new_dict = self.roster
        for key in new_dict:
            new_dict[key].sort()
        return new_dict
# I don't fully understand why, but one of the keys to completing
# this lesson was the fact that the "grade" that both 
# "add_student" and "grade" were supposed to take as arguments
# had to be named different things, even though they were
# referring to the same thing, and even though they were all
# tied up in the _init_ of "School's" "roster" dictionary