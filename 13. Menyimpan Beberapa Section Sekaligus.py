import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'Host': 'localhost',
    'Port': '8080'
}

config['DATABASE'] = {
    'DatabaseName': 'my_db',
    'User': 'root'
}

with open('multi_section_config.ini', 'w') as configfile:
    config.write(configfile)

print("File konfigurasi dengan beberapa sections berhasil dibuat.")
# Fungsi: Menyimpan beberapa section sekaligus dalam file konfigurasi.
# Kondisi: Ketika Anda perlu menyimpan beberapa pengaturan yang terpisah dengan jelas.
