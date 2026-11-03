def evaluate(x: int, y: str, z: int) -> float:
    """
    >>> 3 * 5
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