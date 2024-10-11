# Program untuk menghitung total bayar dengan diskon

# Inisialisasi diskon
diskon = 0.075

# Input data dari pengguna
nama_barang = input("Masukkan nama barang: ")
jumlah_barang = int(input("Masukkan jumlah barang: "))
harga = float(input("Masukkan harga per barang: "))

# Hitung total harga
total_harga = jumlah_barang * harga

# Hitung total diskon
total_diskon = total_harga * diskon

# Hitung total bayar
total_bayar = total_harga - total_diskon

# Tampilkan hasil
print(f"\nTotal harga sebelum diskon: Rp{total_harga:.2f}")
print(f"Diskon (7.5%): Rp{total_diskon:.2f}")
print(f"Total yang harus dibayar: Rp{total_bayar:.2f}")
print("\nSelesai")
