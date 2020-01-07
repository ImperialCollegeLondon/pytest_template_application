def recursive_fibonacci(n: int) -> int:
    """Return the nth number of the fibonacci sequence"""
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        print(recursive_fibonacci(int(sys.argv[1])))
