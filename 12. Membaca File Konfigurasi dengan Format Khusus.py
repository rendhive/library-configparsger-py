import configparser

config = configparser.ConfigParser(allow_no_value=True)
config.read('config_no_value.ini')

print("Debug option:", config['DEFAULT']['Debug'])
# Fungsi: Membaca file konfigurasi yang memungkinkan opsi tanpa nilai.
# Kondisi: Ketika Anda memiliki pengaturan yang menyatakan keberadaan tanpa memberikan nilai.
