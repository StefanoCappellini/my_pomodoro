import time
import sys

desired = [25, 5, 4]
for i, el in enumerate(sys.argv[1:]):
    desired[i-1] = int(el)


def waiter(desired, text=""):
    print("\rStarting " + text)
    for elapsed in range(1, desired+1):
        time.sleep(60)
        print("\r{} / {} min".format(elapsed, desired), end="")
    print("\a" * 6)
    print(text + " ended", end="")

print("Starting {} minutes and {}-minutes breaks X {}".format(*desired))
for i in range(1, desired[2]):
    waiter(desired[0], "Focus {}".format(i))
    waiter(desired[1], "Relax")
