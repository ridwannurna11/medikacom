product = {
    "Beras": 18000,
    "Gula": 12500,
    "Telur": 35000,
    "Tepung": 18000,
    "Garam": 9000,
}

def belanja():
    print("Selamat Datang, Selamat Berbelanja")
    print("Berikut Adalah Daftar Barang Yang Tersedia:")
    for barang, harga in product.items():
        print(f"{barang}: Rp{harga} per kg")

    total belanja = 0
    while True:
        barang_dipilih = input("\nMasukan Nama Barang Yang Ingin Anda Beli)('Selesai' Untuk Selesai")
        if barang_dipilih.lower() == 'Selesai':
            break
        if barang_dipilih not in product:
            print('Maaf, Barang Tidak Tersedia')
            continue
        jumlah = float(input(f"Berapa kg (barang_dipilih) Yang Anda Inginkan"))
        total_belanja += product[barang_dipilih] * jumlah
    print(f"Total Belanja Anda Adalah: Rp{total_belanja}")

belanja()

