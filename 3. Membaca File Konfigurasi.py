import configparser

config = configparser.ConfigParser()
config.read('config.ini')

print("Server Name:", config['DEFAULT']['ServerName'])
print("Server Port:", config['DEFAULT']['ServerPort'])
# Fungsi: Membaca file konfigurasi yang sudah ada.
# Kondisi: Ketika Anda perlu mengambil nilai dari file konfigurasi.
