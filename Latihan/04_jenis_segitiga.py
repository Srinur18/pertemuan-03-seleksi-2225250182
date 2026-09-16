# Program Menentukan Jenis Segitiga
# Pertemuan 03 - Algoritma dan Pemrograman

print("==========================================")
print("          PROGRAM JENIS SEGITIGA")
print("==========================================")

# Input panjang ketiga sisi
a = float(input("Masukkan panjang sisi a: "))
b = float(input("Masukkan panjang sisi b: "))
c = float(input("Masukkan panjang sisi c: "))

print()
print("Hasil pemeriksaan:")
print("------------------------------------------")

# Memeriksa apakah ketiga sisi dapat membentuk segitiga.
#
# Syarat:
# a + b > c
# a + c > b
# b + c > a

if a + b > c and a + c > b and b + c > a:

    print("Ketiga sisi dapat membentuk segitiga.")

    # Nested if untuk menentukan jenis segitiga
    if a == b and b == c:

        print("Jenis segitiga: Segitiga sama sisi.")

    else:

        if a == b or a == c or b == c:

            print("Jenis segitiga: Segitiga sama kaki.")

        else:

            print("Jenis segitiga: Segitiga sembarang.")

else:

    print("Ketiga sisi tidak membentuk segitiga.")

print("------------------------------------------")
print("Program selesai.")