import configparser

config = configparser.ConfigParser()

config['SETTINGS'] = {
    'Volume': '75',
    'Brightness': '85'
}

with open('settings.ini', 'w') as configfile:
    config.write(configfile)

print("File konfigurasi untuk pengaturan berhasil dibuat.")
# Fungsi: Menyimpan pengaturan dengan berbagai tipe data dalam file konfigurasi.
# Kondisi: Ketika Anda memiliki pengaturan berbasis angka yang perlu disimpan sebagai string.
