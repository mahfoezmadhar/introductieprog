def evaluate(x: int, y: str, z: int) -> float:
    """
    >>> evaluate(3, "*", 5)
    15.0
    >>>evaluate(4, "/", 8)
    0.5
    """
    x = int(x)
    z = int(z)
    if y == "+":
        return float(x + z)
    elif y == "*":
        return float(x * z)
    elif y == "-":
        return float(x - z)
    elif y == "/":
        return float(x / z)

if __name__ == '__main__':
    invoer = input()
    x, y, z = invoer.split()
    print(evaluate(x, y, z))