import configparser

config = configparser.ConfigParser()
config.read('config.ini')

if 'DEFAULT' in config:
    print("Section 'DEFAULT' ada dalam file.")
else:
    print("Section 'DEFAULT' tidak ada.")
# Fungsi: Memeriksa apakah section tertentu ada dalam file konfigurasi.
# Kondisi: Ketika Anda perlu memastikan keberadaan section sebelum mengaksesnya.
