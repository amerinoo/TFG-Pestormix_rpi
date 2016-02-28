import threading

# import RPi.GPIO as GPIO
import time

__author__ = "Albert"


class Proto:
    def __init__(self):
        self.valves = {}
        self.init()

    def init(self):
        self.valves["v0"] = 21
        self.valves["v1"] = 20
        self.valves["v2"] = 16
        self.valves["v3"] = 26

    def serve(self, cocktail):
        # print cocktail
        total_time = cocktail.glass.time
        alcohol_time = 0
        print total_time
        if len(cocktail.drinks_alcohol) != 0:
            alcohol_time = total_time * 0.2
            for item in cocktail.drinks_alcohol:
                self.create_worker(self.valves[item], alcohol_time / len(cocktail.drinks_alcohol))
        no_alcohol_time = total_time - alcohol_time
        for item in cocktail.drinks_no_alcohol:
            self.create_worker(self.valves[item], no_alcohol_time / len(cocktail.drinks_no_alcohol))

    def worker(self, pin, total_time):
        print "Start", pin, total_time, "seconds"  # GPIO.output(pin, 1)
        time.sleep(total_time)
        print "Exit", pin  # GPIO.output(pin, 0)

    def create_worker(self, pin, total_time):
        threading.Thread(target=self.worker, args=(pin, total_time)).start()
