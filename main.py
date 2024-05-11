import random
import time
print('Selamat Datang di permainan tes keberuntungan')
print('Peringatan:\n-Permainan ini akan berjalan secara otomatis\n-Permainan ini akan berhenti jika player telah mencapai angka yang ditentukan\n')
while True:
    pilihan = int(input('Apakah anda ingin bermain? (1 = iya, 2 = tidak)\nJawab: '))
    if pilihan == 1:
        print('\nSelamat bermain')
        break
    elif pilihan == 2:
        print('Sampai jumpa')
        break
    elif pilihan < 1 or pilihan > 2:
        print('Nomor tidak valid. Masukkan nomor lagi\n')

if pilihan == 1:
    print('Permainan akan dimulai dalam...')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1\n')
    time.sleep(1)

    while True:
        angka = int(input('Masukkan angka yang ingin dijadikan patokan (1-100) = '))
        if angka < 1:
            print('Angka terlalu kecil. Silahkan coba lagi\n')
        elif angka > 100:
            print('Angka terlalu besar. Silahkan coba lagi\n')
        else:
            print('Angka yang anda masukkan:', angka)
            print('')
            break

    pengulangan = 0

    while True:
        kocokan = random.randint(1,100)
        pengulangan += 1
        if kocokan == angka:
            print('Anda mendapat angka', kocokan)
            print('Permainan selesai, anda berhasil mendapatkan angka pilihan')
            print('Total jumlah pengulangan sebanyak', pengulangan, 'kali\n')
            break
        else:
            print('Anda mendapat angka', kocokan, 'coba lagi')
            time.sleep(1)