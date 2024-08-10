meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "SHEESH": "Sedikit ketidaksetujuan",
            "CREEPY": "Menakutkan, tidak menyenangkan",
            "AGGRO": "Untuk menjadi agresif/marah"
            }

print("Selamat datang di Memectionary!")

for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!) :")

    if word == "END":
        print("Terimakasih telah menggunakan Memectionary!")
        break
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Maaf! Kata tidak ditemukan! Cobalah periksa kesalahan kata atau cari kata lain . . .")
