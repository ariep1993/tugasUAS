from views import view_nilai
from tabulate import tabulate

dataMahasiswa = {
    'NO': [],
    'Nim': [],
    'Nama': [],
    'Tugas': [],
    'Uts': [],
    'Uas': [],
    'Nilai Akhir': []
}

# fungsi mengembalikan dataMahasiswa


def index():
    return dataMahasiswa

# fungsi dataMahasiswa


def tambah_data(no, nim, nama, tugas, uas, uts):
    nilai_akhir = tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100
    # menambahnan data
    dataMahasiswa['No'].append(no)
    dataMahasiswa['Nim'].append(nim)
    dataMahasiswa['Nama'].append(nama)
    dataMahasiswa['Tugas'].append(tugas)
    dataMahasiswa['Uts'].append(uts)
    dataMahasiswa['Uas'].append(uas)
    dataMahasiswa['Nilai Akhir'].append(nilai_akhir)
    print('Data berhasil ditambahkan.')

# fungsi untuk mengedit data


def ubah_data():
    # print data untuk referensi nim pada data yang mau dihapus
    print(tabulate(dataMahasiswa, headers=[
        'No', 'NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tabulate="fancy_grid"))

    # cek jika ada nama  tersebut di dataMahasiswa
    nim = int(input('Masukan NIM yang mau diedit  :'))

    if nim in dataMahasiswa['Nim']:
        # cari posisi indexnya lalu disimpan di nimIndex
        nimIndex = dataMahasiswa['Nim'].index(nim)
        print("Pilih Data yang mau diedit")
        # perulangan mengedit data dalam bentuk pilihan
        while True:
            editApa = int(input(
                "(1) Nim, |  (2) Nama, | (3) Nilai Tugas, | (4) Nilai Uts, | (5) Nilai Uas, | (0) Save Perubahan & exit  : \n"))
            print("")

            if editApa == 1:
                # jika memilih opsi 1 merubah nim
                newNim = int(input("Masukan Nim :"))
                dataMahasiswa['Nim'][nimIndex] = newNim
            elif editApa == 2:
                # jika memilih opsi 2 merubah nama
                newNama = input("Masukan Nama :")
                dataMahasiswa['Nama'][nimIndex] = newNama
            elif editApa == 3:
                # jika memilih opsi 3 merubah nilai tugas & nilai akhir
                newTugas = int(input("Masukan Nilai Tugas :"))
                # memperbarui nilai akhir
                nilai_akhir = (newTugas * 30 / 100) + (dataMahasiswa['Uts'][nimIndex] * 35 / 100) + (
                    dataMahasiswa['Uas'][nimIndex] * 35 / 100)
                dataMahasiswa['Tugas'][nimIndex] = newTugas
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 4:
                # jika memilih opsi 4 merubah nilai uts & nilai akhir
                newUts = int(input("Masukan Nilai Uts :"))
                # memperbarui nilai akhir
                nilai_akhir = (dataMahasiswa['Tugas'][nimIndex] * 30 / 100) + (newUts * 35 / 100) + (
                    dataMahasiswa['Uas'][nimIndex] * 35 / 100)
                dataMahasiswa['Uts'][nimIndex] = newUts
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 5:
                # jika memilih opsi 5 merubah nilai uas & nilai akhir
                newUas = int(input("Masukan Nilai Uas :"))
                # memperbarui nilai akhir
                nilai_akhir = (dataMahasiswa['Tugas'][nimIndex] * 30 / 100) + (dataMahasiswa['Uts'][nimIndex] * 35 / 100) + (
                    newUas * 35 / 100)
                dataMahasiswa['Uas'][nimIndex] = newUas
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 0:
                # jika memilih opsi 0 menyimpan perubahan dan keluar dari edit data
                print('Perubahan Data berhasil disimpan,')
                break

    else:
        print("data tidak ditemukan")

    
    # fungsi untuk mengedit data


def ubah_data():
    # print data untuk referensi nim pada data yang mau dihapus
    print(tabulate(dataMahasiswa, headers=[
        'No', 'NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tabulate="fancy_grid"))

    # cek jika ada nama  tersebut di dataMahasiswa
    nim = int(input('Masukan NIM yang mau diedit  :'))

    if nim in dataMahasiswa['Nim']:
        # cari posisi indexnya lalu disimpan di nimIndex
        nimIndex = dataMahasiswa['Nim'].index(nim)
        print("Pilih Data yang mau diedit")
        # perulangan mengedit data dalam bentuk pilihan
        while True:
            editApa = int(input(
                "(1) Nim, |  (2) Nama, | (3) Nilai Tugas, | (4) Nilai Uts, | (5) Nilai Uas, | (0) Save Perubahan & exit  : \n"))
            print("")

            if editApa == 1:
                # jika memilih opsi 1 merubah nim
                newNim = int(input("Masukan Nim :"))
                dataMahasiswa['Nim'][nimIndex] = newNim
            elif editApa == 2:
                # jika memilih opsi 2 merubah nama
                newNama = input("Masukan Nama :")
                dataMahasiswa['Nama'][nimIndex] = newNama
            elif editApa == 3:
                # jika memilih opsi 3 merubah nilai tugas & nilai akhir
                newTugas = int(input("Masukan Nilai Tugas :"))
                # memperbarui nilai akhir
                nilai_akhir = (newTugas * 30 / 100) + (dataMahasiswa['Uts'][nimIndex] * 35 / 100) + (
                    dataMahasiswa['Uas'][nimIndex] * 35 / 100)
                dataMahasiswa['Tugas'][nimIndex] = newTugas
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 4:
                # jika memilih opsi 4 merubah nilai uts & nilai akhir
                newUts = int(input("Masukan Nilai Uts :"))
                # memperbarui nilai akhir
                nilai_akhir = (dataMahasiswa['Tugas'][nimIndex] * 30 / 100) + (newUts * 35 / 100) + (
                    dataMahasiswa['Uas'][nimIndex] * 35 / 100)
                dataMahasiswa['Uts'][nimIndex] = newUts
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 5:
                # jika memilih opsi 5 merubah nilai uas & nilai akhir
                newUas = int(input("Masukan Nilai Uas :"))
                # memperbarui nilai akhir
                nilai_akhir = (dataMahasiswa['Tugas'][nimIndex] * 30 / 100) + (dataMahasiswa['Uts'][nimIndex] * 35 / 100) + (
                    newUas * 35 / 100)
                dataMahasiswa['Uas'][nimIndex] = newUas
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 0:
                # jika memilih opsi 0 menyimpan perubahan dan keluar dari edit data
                print('Perubahan Data berhasil disimpan,')
                break

    else:
        print("data tidak ditemukan")