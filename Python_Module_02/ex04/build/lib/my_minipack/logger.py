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
        to_write = "(" + os.getenv("USER", default="user_id") + ")" + \
                   "Running: " + \
                   f"{func.__name__.replace('_', ' ').title():18}"
        if exec_time > 1000:
            to_write += f" [exec-time = {exec_time / 1000: .3f} s]\n"
        else:
            to_write += f" [exec-time = {exec_time: .3f} ms]\n"
        f.write(to_write)
        f.close()
        return r
    return wrapper
