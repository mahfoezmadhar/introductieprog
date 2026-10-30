aantal = int(input("Hoe hoog moet de piramide zijn?: "))
for rij in range(aantal + 1):
    kolom = aantal + 1
    
    while kolom >= 2:
        print('#', end='')
        kolom += 1
    print()


    
    
    