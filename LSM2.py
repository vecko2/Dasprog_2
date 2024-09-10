n, c = map(int, input("Masukan jumlah bola dan pemain pertama (1 untuk lala dan 2 untuk lili): ").split())
def last_man_standing(n, c):
    Menang = [False] * (n + 1)  

#Step 1
    for i in range (1, n + 1):
     if i >= 1 and not Menang [i - 1]:
        Menang[i] = True
     elif i >= 2 and not Menang [i - 2]:
        Menang[i] = True
     elif i >= 5 and not Menang[i - 5]:
        Menang[i] = True

#Step 2
    if c == 1:
        return "lala" if Menang [n] else "lili"
    else:
        return "lili" if Menang [n] else "lala"
    
print(last_man_standing(n, c))
