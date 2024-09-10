data_usage = float(input("data yang terpakai: "))

if data_usage < 0:
    print("bad data")
elif data_usage <= 1.0:
    print("biaya yang perlu kamu bayar= 250")
elif data_usage <= 2.0:
    print("biaya yang perlu kamu bayar= 500")
elif data_usage <=5.0:
    print("biaya yang perlu kamu bayar= 1000")
elif data_usage <= 10.0:
    print("biaya yang perlu kamu bayar= 1500")
elif data_usage > 10.0:
    print("biaya yang perlu kamu bayar= 2000")