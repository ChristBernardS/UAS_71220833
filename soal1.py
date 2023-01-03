def poinpenilaian(a):
    poin = 0
    if a == 'prestasi':
        poin += 30
    elif a == 'organisasi':
        poin += 10
    elif a == 'kepanitiaan':
        poin += 5
    elif a == 'rekognisi':
        poin += 2
    else:
        print('error')
    print(f'JUMLAH POIN TOTAL POIN \t :{poin}')


def daftarkegiatanmahasiswa(a, b, c):
    a = list(kegiatan)
    b = list(tanggal)
    c = list(kategori)
    print(list(a, b, c))


while True:

    print('****** Kredit Keaktifan Mahasiswa ******')
    print('(Student Activities Credit)')
    listmenu = [
        '1. Menambahkan Kegiatan',
        '2. Menampilkan Jumlah Poin',
        '3. Keluar'
    ]
    for i in listmenu:
        print(i)

    print('-'*30)
    pilihanmenu = int(input('Silahkan masukan pilihan yang Anda: '))

    if pilihanmenu == 1:
        kegiatan = str(input('Nama kegiatan: '))
        tanggal = str(input('Tanggal kegiatan: '))
        print('Pilihan Kategori Kegiatan')

        listmenukegiatan = [
            '- Prestasi',
            '- Organisasi',
            '- Kepanitiaan',
            '- Rekognisi'
        ]
        for i in listmenukegiatan:
            print(i)

        kategori = str(input('Masukan Kategori Kegiatan: '))
        kategori = str.lower(kategori)

        daftarkegiatan = [kegiatan, tanggal, kategori]

        print('Kegiatan berhasil ditambahkan\n')

    elif pilihanmenu == 2:
        print('')
        print('-'*30)
        print('Nama Kegiatan \t Tanggal \t Kategori \t Poin')
        for i in list(daftarkegiatan):
            print(i, end='\t')
        print('')

        poinpenilaian(kategori)
        print('')

    elif pilihanmenu == 3:
        print('Sistem Berhenti...')
        break

    else:
        print('Pilihan Tidak Terdaftar Kedalam Menu')
