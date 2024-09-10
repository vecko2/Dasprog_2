M,N,T = map(int, input().split())
waktu_rem = (T % 85)

if(waktu_rem > 25):
    rem_hijau = waktu_rem - 25
else:
    rem_hijau = 0
mobil_keluar = ( (T // 85) * 12 + rem_hijau // 5)
rem = (M + N + 1) - mobil_keluar

if(mobil_keluar >= M + 1):
    print(f"YES! {rem}")
else:
    print(f"NO! {rem}")