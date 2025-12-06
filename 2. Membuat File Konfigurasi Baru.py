import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'ServerName': 'localhost',
    'ServerPort': '8080'
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)

print("File konfigurasi berhasil dibuat sebagai 'config.ini'.")
# Fungsi: Membuat file konfigurasi baru dengan nilai default.
# Kondisi: Ketika Anda ingin memulai pengaturan dengan file konfigurasi baru.
