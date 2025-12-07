import configparser

config = configparser.ConfigParser(allow_no_value=True)

config['DEFAULT'] = {
    'ServerName': 'localhost',
    'ServerPort': '8080',
    'Debug': None  # Tanpa nilai
}

with open('config_no_value.ini', 'w') as configfile:
    config.write(configfile)

print("File konfigurasi dengan opsi tanpa nilai berhasil dibuat.")
# Fungsi: Menyimpan file konfigurasi dengan opsi tanpa nilai.
# Kondisi: Ketika Anda ingin menunjukan opsi yang ada tanpa nilai terkait.
