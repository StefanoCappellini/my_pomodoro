import time
import sys


def waiter(desired, text=""):
    print("\rStarting " + text)
    for elapsed in range(1, desired+1):
        time.sleep(60)
        print("\r{} / {} min".format(elapsed, desired), end="")
    print("\a" * 6)
    print(text + " ended", end="")

desired = [25, 5, 4]
for i, el in enumerate(sys.argv[1:]):
    desired[i] = int(el)

print("Starting {} minutes and {}-minutes breaks X {}".format(*desired))
for i in range(1, desired[2] + 1):
    waiter(desired[0], "Focus {}".format(i))
    waiter(desired[1], "Relax")
