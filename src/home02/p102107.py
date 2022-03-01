import math
def minimalis():
    minimum = math.inf
    while True:
        n = input()
        if n != "":
            n = int(n)
            if n < minimum:
                minimum=n
        else:
            return minimum
if __name__ == "__main__":
    print(minimalis())