# before using tqdm it needs to be installed
from tqdm import tqdm

from time import sleep


# ref: https://stackoverflow.com/questions/68211844/python-change-tqdm-bar-style
#      https://stackoverflow.com/questions/54362541/how-to-change-tqdms-bar-size
#      https://stackoverflow.com/questions/57473107/how-to-set-the-r-bar-part-of-tqdm


def ft_progress(listy):
    return tqdm(listy,
                bar_format="ETA: {remaining_s:.2f}s " +
                           "[{desc}: {percentage:.0f}%] " +
                           "[{bar: 20}] " +
                           "{n_fmt}/{total_fmt} | " +
                           "elapsed time: {elapsed_s:.2f}s",
                ascii=' >=')


# 1
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)

# 2
# listy = range(3333)
# ret = 0
# for elem in ft_progress(listy):
#     ret += elem
# sleep(0.005)
# print()
# print(ret)

