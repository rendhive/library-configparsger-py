import configparser

config = configparser.ConfigParser()
config.read('multi_section_config.ini')

print("Host:", config['DEFAULT']['Host'])
print("Port:", config['DEFAULT']['Port'])
print("Database Name:", config['DATABASE']['DatabaseName'])
print("User:", config['DATABASE']['User'])
# Fungsi: Memuat dan membaca nilai dari beberapa sections.
# Kondisi: Ketika Anda ingin mengambil pengaturan dari berbagai sections yang ada.
