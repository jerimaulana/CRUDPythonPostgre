import psycopg2
import os

db = psycopg2.connect(
    host="localhost",
    port=5432,
    user="jeri",
    password="123",
    database="toko_komputer"
)


def insert_data(db):
    print("INPUT DATA BARANG TOKO KOMPUTER")
    nama_barang = input("Masukan Nama Barang: ")
    jumlah_stok = input("Masukan Jumlah Stok: ")
    harga_barang = input("Masukan Harga Barang: ")
    val = (nama_barang, jumlah_stok, harga_barang)
    cursor = db.cursor()
    sql = "INSERT INTO barang (nama_barang, jumlah_stok, harga_barang) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM barang"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)


def update_data(db):
    print("UBAH DATA BARANG TOKO KOMPUTER")
    cursor = db.cursor()
    show_data(db)
    id_barang = input("pilih id barang> ")
    nama_barang = input("Nama Barang baru: ")
    jumlah_stok = input("Jumlah Stok baru: ")
    harga_barang = input("Harga Barang baru: ")

    sql = "UPDATE barang SET nama_barang=%s, jumlah_stok=%s, harga_barang=%s WHERE id_barang=%s"
    val = (nama_barang, jumlah_stok, harga_barang, id_barang)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
    print("HAPUS DATA BARANG TOKO KOMPUTER")
    cursor = db.cursor()
    show_data(db)
    id_barang = input("pilih id barang> ")
    sql = "DELETE FROM barang WHERE id_barang=%s"
    val = (id_barang,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
    cursor = db.cursor()
    keyword = input("Cari Nama Barang: ")
    sql = "SELECT * FROM barang WHERE nama_barang ='" + keyword + "' "
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)


def show_menu(db):
    print("=== APLIKASI TOKO KOMPUTER JERI MAULANA ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    # clear screen
    os.system("cls")
    # os.clear_screen()

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while(True):
        show_menu(db)
