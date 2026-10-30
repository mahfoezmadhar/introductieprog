aantal = int(input("Hoe hoog moet de piramide zijn?: "))
for rij in range(aantal + 1):
    kolom = aantal + 1
    
    while kolom >= rij:
        print('', end='')
        kolom += 1
    print()


    
    
    