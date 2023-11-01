#soal no 2
print("===================================")
print("Program penghitung luas bangunan")
print('''
Pilih salah satu bangun datar:
1 = Luas Persegi
2 = Luas Lingkaran
3 = Luas Segitiga
''')


pilihan = int(input("Masukan pilihan: "))

match pilihan:
    case 1:
        sisi = int(input("Masukan sisi"))
        luas = sisi * sisi 
        print("luas persegi dengan sisi ","adalah", luas)
    case 2:
        jari = int(input("Masukan jari-jari: "))
        luas = 3.14 * jari ** 2
        print("Luas lingkaran dengan jari-jari ", "adalah", luas)
    case 3:
        alas = int(input("Masukan alas: "))
        tinggi = int(input("Masukan tinggi: "))
        luas = 1/2 * alas * tinggi
        print("Luas segitiga dengan atas ", alas, " dan tinggi ", tinggi, " adalah: ", luas)
    case _:
        print("pilihan salah,")