#!!!! BUAT KALKULATOR UNTUK MENGUKUR BMI !!!!

#step 1
Berat_badan = float(input("masukan berat badanmu: "))
if Berat_badan <= 18.5:
    print("Semangat!! jangan lupa makan, Karena BMI kamu termasuk UNDERWEIGHT")

elif Berat_badan <= 24.9:
    print("Amaann, BMI kamu NORMAL")

elif Berat_badan <= 29.9:
    print("Jaga makannya ya, BMI kamu udh masuk OVERWEIGHT")

elif Berat_badan >= 30.0:
    print("Waduh waduh kamu harus Diet sekarang juga!!!, kamu udah masuk OBESE")
