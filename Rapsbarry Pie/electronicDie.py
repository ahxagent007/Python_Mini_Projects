# Need to turn this into an object after its working!

from sense_hat import SenseHat
from time import sleep
import random


class Die():

    def __init__(self):

        self.sense = SenseHat()
        self.dice_value = 0
        self.sense.show_message("SHAKE ME!")
        r = (255, 0, 0)
        e = (0, 0, 0)

        self.one = [
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, r, r, e, e, e,
            e, e, e, r, r, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
        ]

        self.two = [
            e, e, e, e, e, e, e, e,
            e, r, r, e, e, e, e, e,
            e, r, r, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, r, r, e,
            e, e, e, e, e, r, r, e,
            e, e, e, e, e, e, e, e,
        ]

        self.three = [
            e, e, e, e, e, e, e, e,
            e, r, r, e, e, e, e, e,
            e, r, r, e, e, e, e, e,
            e, e, e, r, r, e, e, e,
            e, e, e, r, r, e, e, e,
            e, e, e, e, e, r, r, e,
            e, e, e, e, e, r, r, e,
            e, e, e, e, e, e, e, e,
        ]

        self.four = [
            e, e, e, e, e, e, e, e,
            e, r, r, e, e, r, r, e,
            e, r, r, e, e, r, r, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, r, r, e, e, r, r, e,
            e, r, r, e, e, r, r, e,
            e, e, e, e, e, e, e, e,
        ]

        self.five = [
            e, e, e, e, e, e, e, e,
            e, r, r, e, e, r, r, e,
            e, r, r, e, e, r, r, e,
            e, e, e, r, r, e, e, e,
            e, e, e, r, r, e, e, e,
            e, r, r, e, e, r, r, e,
            e, r, r, e, e, r, r, e,
            e, e, e, e, e, e, e, e,
        ]

        self.six = [
            r, r, e, r, r, e, r, r,
            r, r, e, r, r, e, r, r,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            r, r, e, r, r, e, r, r,
            r, r, e, r, r, e, r, r,
        ]

        self.wait = [
            r, e, r, e, r, e, r, e,
            e, r, e, r, e, r, e, r,
            r, e, r, e, r, e, r, e,
            e, r, e, r, e, r, e, r,
            r, e, r, e, r, e, r, e,
            e, r, e, r, e, r, e, r,
            r, e, r, e, r, e, r, e,
            e, r, e, r, e, r, e, r,
        ]

    def roll(self):

        global dice_value
        sleep(0.5)
        self.sense.set_pixels(self.one)
        sleep(0.5)
        self.sense.set_pixels(self.two)
        sleep(0.5)
        self.sense.set_pixels(self.three)
        sleep(0.5)
        self.sense.set_pixels(self.four)
        sleep(0.5)
        self.sense.set_pixels(self.five)
        sleep(0.5)
        self.sense.set_pixels(self.six)
        sleep(0.5)
        self.sense.set_pixels(self.wait)
        sleep(0.5)
        dice_value = random.randint(1, 6)

    def displayNumber(self):

        if dice_value == 1:
            self.sense.set_pixels(self.one)
        elif dice_value == 2:
            self.sense.set_pixels(self.two)
        elif dice_value == 3:
            self.sense.set_pixels(self.three)
        elif dice_value == 4:
            self.sense.set_pixels(self.four)
        elif dice_value == 5:
            self.sense.set_pixels(self.five)
        elif dice_value == 6:
            self.sense.set_pixels(self.six)

        sleep(5)
        self.sense.clear()

    def returnNumber(self):
        return dice_value

    def runDice(self):

        Rolled = False
        while not Rolled:

            acceleration = self.sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            x = abs(x)
            y = abs(y)
            z = abs(z)

            self.sense.set_pixels(self.one)

            if x > 1.5 or y > 1.5 or z > 1.5:
                self.sense.clear()
                self.roll()
                Rolled = True