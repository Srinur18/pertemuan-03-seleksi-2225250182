# Program Menentukan Bilangan Genap atau Ganjil
# Pertemuan 03 - Algoritma dan Pemrograman

print("==========================================")
print("     PROGRAM BILANGAN GENAP ATAU GANJIL")
print("==========================================")

# Input bilangan dari pengguna
bilangan = int(input("Masukkan bilangan bulat: "))

# Memeriksa apakah bilangan habis dibagi 2
if bilangan % 2 == 0:
    print()
    print(f"{bilangan} adalah bilangan genap.")
else:
    print()
    print(f"{bilangan} adalah bilangan ganjil.")

print()
print("Program selesai.")