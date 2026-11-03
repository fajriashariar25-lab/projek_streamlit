# =================================
# PROGRAM PROFIL DIRI
# =================================

print("=" * 40)
print("         PROFIL DIRI SAYA")
print("=" * 40)

# Input data
nama = input("Masukkan nama lengkap: ")
panggilan = input("Masukkan nama panggilan: ")
jenis_kelamin = input("Masukkan jenis kelamin: ")
status = input("Masukkan status (Mahasiswa/Pelajar/Bekerja): ")
cita_cita = input("Masukkan cita-cita: ")

print("\nPilih hobi:")
print("1. Coding")
print("2. Gaming")
print("3. Membaca")
print("4. Musik")
print("5. Olahraga")
print("6. Traveling")

pilihan = input("Masukkan nomor hobi: ")

# Menentukan hobi
if pilihan == "1":
    hobi = "Coding"
elif pilihan == "2":
    hobi = "Gaming"
elif pilihan == "3":
    hobi = "Membaca"
elif pilihan == "4":
    hobi = "Musik"
elif pilihan == "5":
    hobi = "Olahraga"
elif pilihan == "6":
    hobi = "Traveling"
else:
    hobi = "Tidak diketahui"

# Output profil
print("\n" + "=" * 40)
print("           HASIL PROFIL")
print("=" * 40)

print("Nama Lengkap  :", nama)
print("Nama Panggilan:", panggilan)
print("Jenis Kelamin :", jenis_kelamin)
print("Status        :", status)
print("Cita-cita     :", cita_cita)
print("Hobi          :", hobi)

print("=" * 40)
print("Terima kasih sudah mengisi profil!")