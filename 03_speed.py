import numpy as np

def slow_max(x):
    return max(x)

def fast_max(x):
    return np.max(x)


if __name__ == '__main__':
    x = np.random.random(10_000_000)
    print(slow_max(x))
    print(fast_max(x))
