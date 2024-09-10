
inisial_warna = input("Masukan inisial warna yang muncul pada silinder (O,B,Y,G): ").strip().upper()

if inisial_warna == "O":
    content_warna = "Ammonia"
elif inisial_warna == "B":
    content_warna = "Carbon Monoxide"
elif inisial_warna == "Y":
    content_warna = "Hydrogen"
elif inisial_warna == "G":
    content_warna = "Oxygen"

print(f"Warna yang muncul adalah {content_warna}")