#1
evaluate_performance = input("Berapa nilainya?")
if float(evaluate_performance)>= 90:
    print ("then Excellent performance")
elif float(evaluate_performance) >= 80 :
    print ("then Very Good performance")
elif float(evaluate_performance) >= 70 :
    print ("then Good performance")
elif float(evaluate_performance) >= 60 :
    print ("then average performance")
else :
    print ("Needs Improvement")

#2
def terbesar_dari_tiga(a, b, c): #def = fungsi (void)
    if a >= b and a >= c: #Memeriksa apakah a adalah yang terbesar di antara a, b, dan c. Jika benar, fungsi mengembalikan nilai a.
        return a
    elif b >= a and b >= c:#jika kondisi pertama tidak terpenuhi, maka periksa apakah b adalah yang terbesar
        return b
    else:
        return c #jika kondisi keduanya tidak terpenuhi makan kembali ke c. 

# Penggunaan program:
a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))
c = float(input("Masukkan bilangan ketiga: "))
print(f"Bilangan terbesar adalah: {terbesar_dari_tiga(a, b, c)}")

#3
def fibonacci(n):
    # Inisialisasi dua angka pertama pada deret Fibonacci
    fib_series = [0, 1]
    
    # Menghitung angka Fibonacci berikutnya, menghitung dengan menjumlahkan dua angka terakhir yang ada di dalam list
    for i in range(2, n):
        next_fib = fib_series[-1] + fib_series[-2] #menjumlahkan elemen terakhir dgn elemen kedua terakhir
        fib_series.append(next_fib) #menambahkan angka ke akhir list
    
    # Mengembalikan deret Fibonacci sampai n
    return fib_series[:n]

# Penggunaan program:
n = int(input("Masukkan jumlah angka Fibonacci yang ingin dicetak: "))
print(f"Deret Fibonacci hingga {n} angka: {fibonacci(n)}")

#4
def cetak_bilangan_ganjil(n):
    for i in range(1, n + 1):
        if i % 2 != 0:  # Memeriksa apakah bilangan ganjil dengan membagi bilangan dengan 2
            print(i, end=" ")

# Penggunaan program:
n = int(input("Masukkan nilai n: "))
print(f"Bilangan ganjil hingga {n}:")
cetak_bilangan_ganjil(n)

#5
def cetak_pola(n):# Mendefinisikan fungsi bernama cetak_pola yang menerima parameter n.
    for i in range(1, n + 1): #perulangan berjalan dari 1 hingga n mengulangi setiap nilai i.
        print(f"{i} " * i)#mengulangi string tersebut sebanyak i kali

# Penggunaan program:
n = int(input("Masukkan nilai n: "))
cetak_pola(n)

    



