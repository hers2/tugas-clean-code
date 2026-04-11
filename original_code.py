def t(a,b,c):
    x=a*b
    y=x-(x*c)
    print("hasil:",y)

harga = int(input("harga: "))
jumlah = int(input("jumlah: "))
diskon = float(input("diskon: "))

t(harga,jumlah,diskon)