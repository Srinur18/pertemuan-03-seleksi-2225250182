# ==========================================================
# PROGRAM ANALISIS PERSAMAAN KUADRAT
# ==========================================================
# Program ini digunakan untuk menganalisis persamaan:
#
#                 ax^2 + bx + c = 0
#
# Program akan:
# 1. Meminta nilai a, b, dan c dari pengguna.
# 2. Memeriksa apakah a = 0 atau tidak.
# 3. Jika a = 0, persamaan bukan persamaan kuadrat.
# 4. Jika a != 0, program menghitung diskriminan.
# 5. Berdasarkan nilai diskriminan, program menentukan:
#       D > 0  -> dua akar real berbeda
#       D = 0  -> satu akar real kembar
#       D < 0  -> tidak memiliki akar real
# 6. Jika memiliki akar real, akar akan dihitung.
# 7. Hasil akar ditampilkan dengan 2 angka di belakang koma.
#
# Materi yang digunakan:
# - Input dan output
# - Konversi tipe data
# - Operator aritmatika
# - Percabangan if
# - Percabangan if-else
# - Nested if
# - Perhitungan diskriminan
# ==========================================================


# ----------------------------------------------------------
# BAGIAN 1: JUDUL PROGRAM
# ----------------------------------------------------------

print("==================================================")
print("       PROGRAM ANALISIS PERSAMAAN KUADRAT")
print("==================================================")
print()
print("Persamaan yang dianalisis:")
print("              ax^2 + bx + c = 0")
print()


# ----------------------------------------------------------
# BAGIAN 2: INPUT NILAI a, b, DAN c
# ----------------------------------------------------------

print("Masukkan nilai koefisien persamaan:")
print("------------------------------------------")

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

print()


# ----------------------------------------------------------
# BAGIAN 3: MENAMPILKAN PERSAMAAN
# ----------------------------------------------------------

print("Persamaan yang dimasukkan:")
print("------------------------------------------")
print(f"{a}x^2 + {b}x + {c} = 0")
print()


# ----------------------------------------------------------
# BAGIAN 4: MEMERIKSA NILAI a
# ----------------------------------------------------------
# Persamaan disebut persamaan kuadrat jika:
#
#               a != 0
#
# Jika a = 0, maka persamaan tersebut bukan persamaan
# kuadrat karena tidak memiliki suku x^2.
# ----------------------------------------------------------

if a == 0:

    print("Hasil analisis:")
    print("------------------------------------------")
    print("Nilai a = 0.")
    print("Persamaan tersebut bukan persamaan kuadrat.")
    print("Program tidak dapat menghitung akar persamaan kuadrat.")
    print("------------------------------------------")


# ----------------------------------------------------------
# BAGIAN 5: JIKA a TIDAK SAMA DENGAN 0
# ----------------------------------------------------------
# Jika a != 0, maka persamaan merupakan persamaan kuadrat.
# Selanjutnya program menghitung diskriminan.
#
# Rumus diskriminan:
#
#             D = b^2 - 4ac
# ----------------------------------------------------------

else:

    # Menghitung nilai diskriminan
    diskriminan = b ** 2 - 4 * a * c

    print("Hasil analisis:")
    print("------------------------------------------")

    # Menampilkan nilai diskriminan
    print(f"Nilai diskriminan (D) = {diskriminan:.2f}")
    print()


    # ------------------------------------------------------
    # BAGIAN 6: MEMERIKSA DISKRIMINAN
    # ------------------------------------------------------
    # Nested if digunakan untuk menentukan jenis akar.
    #
    # Jika D > 0:
    #       terdapat dua akar real berbeda.
    #
    # Jika D = 0:
    #       terdapat satu akar real kembar.
    #
    # Jika D < 0:
    #       tidak terdapat akar real.
    # ------------------------------------------------------

    if diskriminan > 0:

        # --------------------------------------------------
        # D > 0
        # Dua akar real berbeda
        # --------------------------------------------------

        print("Diskriminan lebih besar dari 0.")
        print("Persamaan memiliki dua akar real yang berbeda.")
        print()

        # Rumus akar pertama:
        #
        # x1 = (-b + sqrt(D)) / (2a)
        #
        # Rumus akar kedua:
        #
        # x2 = (-b - sqrt(D)) / (2a)
        #
        # Karena D > 0, akar dari diskriminan dapat dihitung.
        # --------------------------------------------------

        akar_positif = diskriminan ** 0.5
        x1 = (-b + akar_positif) / (2 * a)
        x2 = (-b - akar_positif) / (2 * a)

        print(f"Akar pertama (x1) = {x1:.2f}")
        print(f"Akar kedua   (x2) = {x2:.2f}")


    else:

        # --------------------------------------------------
        # Nested if berikut digunakan untuk membedakan
        # antara D = 0 dan D < 0.
        # --------------------------------------------------

        if diskriminan == 0:

            # ----------------------------------------------
            # D = 0
            # Satu akar real kembar
            # ----------------------------------------------

            print("Diskriminan sama dengan 0.")
            print("Persamaan memiliki satu akar real kembar.")
            print()

            # Rumus akar kembar:
            #
            # x = -b / (2a)
            # ----------------------------------------------

            x = -b / (2 * a)

            print(f"Akar kembar (x) = {x:.2f}")


        else:

            # ----------------------------------------------
            # D < 0
            # Tidak memiliki akar real
            # ----------------------------------------------

            print("Diskriminan kurang dari 0.")
            print("Persamaan tidak memiliki akar real.")


    # ------------------------------------------------------
    # Penutup hasil analisis
    # ------------------------------------------------------

    print("------------------------------------------")


# ----------------------------------------------------------
# BAGIAN 7: PROGRAM SELESAI
# ----------------------------------------------------------

print()
print("==================================================")
print("              PROGRAM SELESAI")
print("==================================================")