from main.proto import Proto

__author__ = 'Albert'


class Cocktail:
    def __init__(self):
        self.glass = None
        self.drinks_alcohol = []
        self.drinks_no_alcohol = []

    def set_glass(self, glass):
        self.glass = glass

    def setdrink(self, valve, alcohol):
        if alcohol:
            self.drinks_alcohol.append(valve)
        else:
            self.drinks_no_alcohol.append(valve)

    def serve(self):
        Proto().serve(self)

    def __str__(self):
        return "Glass: " + str(self.glass) + "\nNo alcohol: " + str(self.drinks_no_alcohol) + "\nAlcohol: " \
               + str(self.drinks_alcohol)
