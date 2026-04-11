# fungsi untuk menghitung total harga setelah diskon
def hitung_total(harga, jumlah, diskon):
    total = harga * jumlah
    total_setelah_diskon = total - (total * diskon)
    return total_setelah_diskon

harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang: "))
diskon = float(input("Masukkan diskon (contoh 0.1 untuk 10%): "))

total_bayar = hitung_total(harga, jumlah, diskon)

print("Total yang harus dibayar:", total_bayar)