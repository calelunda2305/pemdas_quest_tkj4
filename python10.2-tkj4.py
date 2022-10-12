# Membuat Tipe Data Koleksi

koleksi_data_str = ["Pisang", "Mangga", "Jambu", "Semangka"]

koleksi_data_int = [200, 300, 400, 500]

koleksi_data_mix = ["Rizky billar", 100, True, "Reza Arap"]

print("Koleksi data String:", koleksi_data_str)

print("Koleksi data Integer:", koleksi_data_int)

print("Koleksi data Campuran", koleksi_data_mix)

# Buatlah 3 Kumpulan data: Nama Hewan, Nilai UTS, Nama Teman sebangku kalian

nama_hewan= ["Kucing", "Kelinci", "Kangguru", "Burung", "Semut"]

nilai_UTS = [100, 90, 100]

nama_ts = ["Nazla", "Dewi", "Rizky Billar", "Reza Arap", "Owican",]

print("Nama Hewan:", nama_hewan)

print("Nilai UTS:", nilai_UTS)

print("Nama ts:", nama_ts)

# Tampilkan data koleksi dengan indeks 

# Data ke 2 Nama Hewan

print("Nama Hewan Data ke-2:", nama_hewan[1])

# Data pertama Nilai UTS 

print("Nilai UTS Data ke-1:", nilai_UTS[0])

# Data terakhir nama teman sebangku

print("Nama ts data ke-3:", nama_ts[2])

print(nama_ts[1:4])

print(nama_ts)

nama_ts[4] = "Jeno"

print(nama_ts) 

nama_ts.append("Jaehyun")

print(nama_ts)

# Tambahkan 1 data disetiap Data Koleksi

nama_hewan.append("Ikan")

nilai_UTS.append("90")

nama_ts.append("Megacan")

print(nama_hewan, nilai_UTS, nama_ts)

# Ubahlah data Terakhir Nilai UTS 

nilai_UTS[-1] = 80

# Ubahlah data ke-3 Nama Hewan 

nama_hewan[2] = "Monyet"

print(nilai_UTS, nama_hewan)
