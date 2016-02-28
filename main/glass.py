__author__ = 'Albert'


class Glass:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def set_glass_name(self, glass_name):
        self.name = glass_name

    def set_time(self, time):
        self.time = time

    def __str__(self):
        return "Glass: " + str(self.name) + "\nTime: " + str(self.time)
