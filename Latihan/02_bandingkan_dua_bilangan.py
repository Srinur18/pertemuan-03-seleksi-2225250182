# Program Membandingkan Dua Bilangan
# Pertemuan 03 - Algoritma dan Pemrograman

print("==========================================")
print("       PROGRAM MEMBANDINGKAN BILANGAN")
print("==========================================")

# Input dua bilangan
bilangan_pertama = float(input("Masukkan bilangan pertama: "))
bilangan_kedua = float(input("Masukkan bilangan kedua: "))

print()
print("Hasil perbandingan:")
print("------------------------------------------")

# Menggunakan nested if
if bilangan_pertama >= bilangan_kedua:

    # Memeriksa apakah kedua bilangan sama
    if bilangan_pertama == bilangan_kedua:
        print("Kedua bilangan sama.")

    else:
        print("Bilangan pertama lebih besar daripada bilangan kedua.")

else:
    print("Bilangan pertama lebih kecil daripada bilangan kedua.")

print("------------------------------------------")
print("Program selesai.")