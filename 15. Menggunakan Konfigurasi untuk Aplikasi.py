import configparser

config = configparser.ConfigParser()
config.read('multi_section_config.ini')

def print_config():
    print("Configuration:")
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config[section].items():
            print(f"{key}: {value}")

print_config()
# Fungsi: Menampilkan konfigurasi aplikasi.
# Kondisi: Ketika Anda ingin memeriksa semua pengaturan aplikasi yang ada.
