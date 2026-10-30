aantal = int(input("Hoe hoog moet de piramide zijn? ")) -> int

for rij in range(1, aantal + 1):
    for spatie in range(aantal - rij):
        print(' ', end='')

    for hekje in range(rij + 1):
        print('#', end='')

    print()


    
    
    