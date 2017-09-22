class Jedi:
    def __init__(self, age):
        self.age = age

    def getRank(self):
        # if self.age < 16:
        #     return "Padawan"
        #
        # if self.age < 30:
        #     return "Knight"
        #
        # return "Master"

        if self.age < 16:
            rank = "Padawan"
        elif self.age <= 29:
            rank = "Knight"
        else:
            rank = "Master"
        return rank


