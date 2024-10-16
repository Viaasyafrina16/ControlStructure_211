def temukan_terbesar(angka1, angka2, angka3):
    if angka1 >= angka2 and angka1 >= angka3:
        return angka1
    elif angka2 >= angka1 and angka2 >= angka3:
        return angka2
    else:
        return angka3

# Input tiga angka dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
angka3 = float(input("Masukkan angka ketiga: "))

# Menemukan dan mencetak bilangan terbesar
terbesar = temukan_terbesar(angka1, angka2, angka3)
print(f"Bilangan terbesar adalah: {terbesar}")