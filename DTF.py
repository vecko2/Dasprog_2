#ubah waktu menjadi detik
def time_to_second (h, m, s):
    return h * 3600 + m * 60 + s

#ubah total detik menjadi jam, menit dan detik
def second_to_time (second):
    h = second // 3600
    second %= 3600
    m = second // 60
    s = second % 60
    return h, m, s

event_time_gmt2 = input().strip()
current_time_gmt7 = input().strip()

HH_event, MM_event, SS_event = map(int, event_time_gmt2.split(":"))
CH, CM, CS = map(int, current_time_gmt7.split(":"))

#ubah waktu acara menjadi GMT
event_time_in_gmt = time_to_second(HH_event - 2, MM_event, SS_event)

#ubah waktu sekarang menjadi GMT
current_time_in_gmt = time_to_second(CH - 7, CM, CS)

#kalkulasi perbedaan waktu
time_difference = (event_time_in_gmt - current_time_in_gmt)

if time_difference <= 0:
    print("See you on the next Pear Event!")
else:
    H, M, S = second_to_time(time_difference) 
    print(f"{H:02d}:{M:02d}:{S:02d}")

