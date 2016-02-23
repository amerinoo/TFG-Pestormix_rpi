__author__ = 'Albert'


class Cocktail:
    def __init__(self):
        self.glass = ""
        self.drinks_alcohol = []
        self.drinks_no_alcohol = []

    def setglass(self, glass):
        self.glass = glass

    def setdrink(self, valve, alcohol):
        if alcohol:
            self.drinks_alcohol.append(valve)
        else:
            self.drinks_no_alcohol.append(valve)

    def serve(self):
        print self

    def __str__(self):
        return "Glass: " + str(self.glass) + "\nNo alcohol: " + str(self.drinks_no_alcohol) + "\nAlcohol: " \
               + str(self.drinks_alcohol)
