import math
import time


def main():
    x = 0.01
    while True:
        a = math.cos(x)
        x = x + 0.01
        print(f"sin({x:.2f}) == {a:.2f}")
        time.sleep(0.05)


main()


