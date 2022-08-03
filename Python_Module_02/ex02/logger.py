import time
from random import randint
import os

# ref: https://dojang.io/mod/page/view.php?id=2427
# ref: https://stickode.tistory.com/209


def log(func):
    # def wrapper(self, *args, **kwargs):
    def wrapper(self, *args, **kwargs):
        f = open("./log", "a")
        start_time = time.time()
        if (args):
            r = func(self, *args)
        else:
            r = func(self)
        exec_time = (time.time() - start_time) * 1000
        f.write("(" + os.getenv("USER", default="user_id") + ")" +
                "Running:" + func.__name__ +
                ": {0} {1}\n".format((exec_time / 1000 if exec_time > 1 else exec_time), 's' if exec_time > 1000 else 'ms'))
        f.close()
        return r
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
