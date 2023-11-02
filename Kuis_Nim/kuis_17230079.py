print('===================================================')
print('                     Hotel')
print('===================================================')
print('KODE HOTEL     NAMA HOTEL')
print('     1         Hotel Maju Mundur')
print('     2         Hotel Tanpa Nama')
print('===================================================')
print('KODE KAMAR   JENIS KAMAR     HARGA')
print('     1           VP          500.000')
print('     2           VIP         750.000')
print('     3           VVIP        1.500.000')
print('===================================================')

# handle harga dan jenis kamar


def handle_data(kode_hotel, kode_kamar):
    if kode_hotel == "1":
        nama_hotel = "Hotel maju mundur"
        if kode_kamar == "1":
            jenis_kamar = "vp"
            harga = 500000
        elif kode_kamar == "2":
            jenis_kamar = "vip"
            harga = 750000
        elif kode_kamar == "3":
            jenis_kamar = "vvip"
            harga = 2500000
        else:
            jenis_kamar = "salah memasukan kode kamar"
            harga = 0
    elif kode_hotel == "2":
        nama_hotel = "Hotel tanpa nama"
        if kode_kamar == "1":
            jenis_kamar = "vp"
            harga = 500000
        elif kode_kamar == "2":
            jenis_kamar = "vip"
            harga = 750000
        elif kode_kamar == "3":
            jenis_kamar = "vvip"
            harga = 2500000
        else:
            jenis_kamar = "salah memasukan kode kamar"
            harga = 0
    else:
        nama_hotel = "salah memasukan kode hotel"
        jenis_kamar = "salah memasukan kode hotel"
        harga = 0

    return {"nama_hotel": nama_hotel, "jenis_kamar": jenis_kamar, "harga": harga}


# penampung semua data
data_all_pesanan = []
again = True

while True:
    banyak = int(input('masukan banyak jenis kamar:'))
    for i in range(banyak):
        print(f"pesanan ke- {i+1}")
        kode_hotel = input('masukan kode hotel[1|2]:')
        kode_kamar = input('masukan kode kamar[1|2|3]:')

        data = handle_data(kode_hotel, kode_kamar)
        jml_psn = int(input('ingin pesan berapa kamar: '))
        lama_nginap = int(input("lama nginnap : "))
        total_harga = jml_psn * data.get('harga') * lama_nginap

        # asign data pesanan ke data semua data
        data_pesanan = [data.get(
            "nama_hotel"), data.get("jenis_kamar"), total_harga, jml_psn, lama_nginap]

        data_all_pesanan.append(data_pesanan)

        print('-------------------------')
        print(f"harga satuan kamar  :{data.get('harga'):,}")
        print(f"jumlah pesan kamar  :{jml_psn:,}")
        print(f"lama nginep         :{lama_nginap:,}")
        print(f"total harga         :{total_harga:,}")
        print('-------------------------')

    total_all_harga = 0
    for i in range(len(data_all_pesanan)):
        total_all_harga += data_all_pesanan[i][2]

    if lama_nginap > 7:
        discount = 0.07
    elif lama_nginap > 5:
        discount = 0.05
    elif lama_nginap > 0.03:
        discount = 0.03
    else:
        discount = 0

    pajak = total_all_harga * 0.15
    getdiscount = total_all_harga * discount
    total_bayar = total_all_harga - getdiscount + pajak

    print('===========================================')
    print(f"total harga         :{total_all_harga:,}")
    print(f"discount anda       :{discount:.0%}")
    print(f"potongan discount   :{getdiscount:,}")
    print(f"bayar pajak         :{pajak:,}")
    print(f"total bayar         :{total_bayar:,}")
    # mencari uang kembalian
    uang_bayar = int(input('masukan uang bayar  :'))
    uang_kembalian = uang_bayar - total_bayar
    print(f"uang kembali        :{uang_kembalian:,}")
    print('===========================================')

    ulangi = input(('apakah anda ingin mengulangi lagi ? [ya/tidak]'))
    if ulangi != "ya":
        break
