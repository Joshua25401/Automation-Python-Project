import sys
import clipboard
import json

FILENAME = "CLIPBOARD.json"

# Function untuk menyimpan data kedalam file
# Format yang digunakan adalah .json (JavaScript Object Notation)
# format w digunakan untuk menulis kedalam file
# Sifat : Selalu melakukan overwrite data.


def save_data(lokasiFile, data):
    with open(lokasiFile, 'w') as file:
        json.dump(data, file)

# Function untuk membaca data dari file json
# Mengembalikan nilai empty dictionary jika terdapat error
# Pada saat membuka file


def read_data(lokasiFile):
    try:
        with open(lokasiFile, 'r') as file:
            data = json.load(file)
            return data
    except:
        return {}


# Check apakah ada command yang dimasukkan
# Melalui variabel sys.argv
# Pertama check apakah panjang dari sys.argv == 2
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = read_data(FILENAME)

    # Check perintah yang dimasukkan
    if command == "save":
        key = input("Masukkan kata kunci : ")
        data[key] = clipboard.paste()
        save_data(FILENAME, data)
        print("Data tersimpan")
    elif command == "load":
        key = input("Masukkan kata kunci : ")
        if key in data:
            clipboard.copy(data[key])
            print("Data telah di copy ke clipboard")
    elif command == "list":
        print(data)
    else:
        print("Perintah tidak tersedia!")

else:
    print("Tolong masukkan perintah !")
