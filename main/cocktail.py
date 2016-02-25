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
        print self
        total_time = self.glass.time
        alcohol_time = 0
        if len(self.drinks_alcohol) != 0:
            alcohol_time = total_time * 0.2
        no_alcohol_time = total_time-alcohol_time
        print "Alcohol time =",alcohol_time
        print "No alcohol time =",no_alcohol_time

    def __str__(self):
        return "Glass: " + str(self.glass) + "\nNo alcohol: " + str(self.drinks_no_alcohol) + "\nAlcohol: " \
               + str(self.drinks_alcohol)
