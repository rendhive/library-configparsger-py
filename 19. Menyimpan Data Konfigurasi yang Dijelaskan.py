import configparser

config = configparser.ConfigParser()

config['DOCUMENTATION'] = {
    'Title': 'My Application',
    'Version': '1.0',
    'Author': 'John Doe'
}

with open('doc_config.ini', 'w') as configfile:
    config.write(configfile)

print("File konfigurasi dokumentasi berhasil disimpan.")
# Fungsi: Menyimpan deskripsi metadata mengenai aplikasi.
# Kondisi: Ketika Anda perlu menyimpan informasi dokumentasi dalam pengaturan aplikasi.
