data = list(map(int, input("masukan data: ").split()))

n = data[0]
jarak = data[1:]

if all(j <= n for j in jarak):
    print("YES HE CAN")
else:
    print("NO HE CAN'T")