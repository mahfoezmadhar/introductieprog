def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    """
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
    print({evaluate(x, y, z)})