#!!!! TENTUKAN TOTAL BELANJA SISWA & YANG BUKAN SISWA !!!!

#step 1
total_pembelian = float(input("masukan jumlah total pembelian: $"))
siswa = input("apakah kamu adalah siswa (iya/tidak): ").strip().lower()

#step 2
diskon_siswa = 0.20
besar_pajak = 0.05

#step 3
if siswa == "iya":
    harga_sudah_didiskon = total_pembelian - (total_pembelian * diskon_siswa)
    harga_setelah_pajak = harga_sudah_didiskon + (harga_sudah_didiskon * besar_pajak)
    total_yang_harus_dibayar = harga_setelah_pajak
    print (f"Total biaya yang harus kamu bayar = ${total_yang_harus_dibayar:.2f}")
    
elif siswa == "tidak":
    biaya_selain_siswa = total_pembelian + (total_pembelian * besar_pajak)
    print (f"Total biaya yang harus kamu bayar = ${biaya_selain_siswa:.2f}")





