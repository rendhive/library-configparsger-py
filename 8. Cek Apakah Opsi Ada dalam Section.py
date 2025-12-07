import configparser

config = configparser.ConfigParser()
config.read('config.ini')

if 'ServerPort' in config['DEFAULT']:
    print("Opsi 'ServerPort' ada dalam section 'DEFAULT'.")
else:
    print("Opsi 'ServerPort' tidak ada.")
# Fungsi: Memeriksa apakah opsi tertentu ada dalam section.
# Kondisi: Ketika Anda perlu memastikan keberadaan opsi sebelum mengakses nilainya.
