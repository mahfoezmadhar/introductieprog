def print_collatz(n):
 print(n)
 
 
 while n > 1:
    if n % 2 == 0:
        n = n // 2
    elif n % 2 != 0:
        n = n * 3 + 1
    print(n)

def collats_length(n):
 lengte = 1
 while n > 1:
    if n % 2 == 0:
        n = n // 2
    elif n % 2 != 0:
        n = n * 3 + 1
    lengte += 1
    return lengte 
     