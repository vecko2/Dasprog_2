titik_X = float(input("masukkan koordinat titik x: "))
titik_Y = float(input("masukkan koordinat titik y: "))

if titik_X < 0 and titik_Y > 0:
    print (f"koordinat {titik_X, titik_Y} terletak di kuadran 2")

elif titik_X < 0 and titik_Y < 0:
    print (f"koordinat {titik_X, titik_Y} terletak di kuadran 3")

elif titik_X > 0 and titik_Y > 0:
    print (f"koordinat {titik_X, titik_Y} terletak di kuadran 1")

elif titik_X > 0 and titik_Y < 0:
    print (f"koordinat {titik_X, titik_Y} terletak di kuadran 4")

elif titik_X == 0:
    print (f"koordinat {titik_X, titik_Y} terletak di Y-axis")

elif titik_Y == 0:
    print (f"koordinat {titik_X, titik_Y} terletak di X-axis")
