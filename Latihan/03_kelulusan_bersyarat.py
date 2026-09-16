# Program Menentukan Kelulusan Bersyarat
# Pertemuan 03 - Algoritma dan Pemrograman

print("==========================================")
print("        PROGRAM KELULUSAN BERSYARAT")
print("==========================================")

# Input nilai akhir dan kehadiran
nilai = float(input("Masukkan nilai akhir: "))
kehadiran = float(input("Masukkan kehadiran (%): "))

print()
print("Hasil pemeriksaan:")
print("------------------------------------------")

# Mahasiswa harus memenuhi dua syarat:
# 1. Nilai minimal 60
# 2. Kehadiran minimal 80%
#
# Karena kedua syarat harus terpenuhi,
# digunakan operator logika AND.

if nilai >= 60 and kehadiran >= 80:
    print("Status: Lulus")
else:
    print("Status: Belum lulus")

print("------------------------------------------")
print("Program selesai.")