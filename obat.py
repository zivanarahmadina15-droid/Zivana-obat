daftar_obat = [
    {"nama": "Paracetamol 500mg", "stok": 50, "harga": 10000},
    {"nama": "Amoxicillin 500mg", "stok": 8, "harga": 25000},
    {"nama": "Cetirizine 10mg", "stok": 0, "harga": 15000},
    {"nama": "Omeprazole 20mg", "stok": 15, "harga": 35000},
    {"nama": "Insulin Pen", "stok": 4, "harga": 250000},
    {"nama": "Salbutamol Inhaler", "stok": 10, "harga": 120000},
    {"nama": "Vitamin C 1000mg", "stok": 45, "harga": 45000},
    {"nama": "Antasida Doen", "stok": 20, "harga": 8000},
    {"nama": "Amlodipine 5mg", "stok": 0, "harga": 30000},
    {"nama": "Albumin Infus", "stok": 3, "harga": 450000}
]

print("=== LAPORAN MONITORING STOK & HARGA OBAT APOTEK ===\n")

for obat in daftar_obat:
    nama = obat["nama"]
    stok = obat["stok"]
    harga = obat["harga"]
    
    if stok == 0:
        status_stok = "HABIS (Tidak Tersedia)"
    elif stok <= 10:
        status_stok = "MENIPIS (Segera Restock)"
    else:
        status_stok = "AMAN"
        
    if harga >= 100000:
        kategori_harga = "Obat Mahal / Khusus"
    elif harga >= 25000:
        kategori_harga = "Obat Menengah"
    else:
        kategori_harga = "Obat Terjangkau"

    print(f"Nama Obat : {nama}")
    print(f"Sisa Stok : {stok} unit -> Status: {status_stok}")
    print(f"Harga     : Rp{harga:,} -> Kategori: {kategori_harga}")
    print("-" * 50)
