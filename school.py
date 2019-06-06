class School:
    def __init__(self, name=None, roster={}):
        self.name = name
        self.roster = roster

    def add_student(self, stdnt_name, grade):
        student_name = []
        self.roster[grade] = student_name.append(stdnt_name)

             

    def grade(self, grd):
        for keys, values in self.roster.items():
            return keys
