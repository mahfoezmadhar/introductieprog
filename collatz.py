def print_collatz(n: int) -> None:
 print(n)
 
 
 while n > 1:
    if n % 2 == 0:
        n = n // 2
    elif n % 2 != 0:
        n = n * 3 + 1
    print(n)

def collatz_length(n: int) -> int:
 lengte = 1
 while n > 1:
    if n % 2 == 0:
        n = n // 2
    elif n % 2 != 0:
        n = n * 3 + 1
    lengte += 1
 return lengte 
 

     