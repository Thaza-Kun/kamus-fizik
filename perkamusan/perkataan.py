import json
import os

file_dir = os.path.realpath('.')
base_dir = os.path.join('kamus_db', 'entri_ms')

class kata:
    """
    A class to contain words

    :init : Will search for the entri in the file and return the answer
    """

    def __init__(self, perkataan):
        self.entri = perkataan
        self.konsep = list(dict())
        print("Data: {}".format(self.data()))

    def makna(self, makna, bidang2):
        self.konsep.append(dict(
            konteks=bidang2,
            makna=makna
        ))

    def to_dict(self):
        return dict(
            kata=self.entri,
            konsep=self.konsep
        )

    def data(self):
        """A method to retrieve existing data on the word

        :return: dict or None"""
        try:
            with open(base_dir + self.entri + '/data.json', 'r') as f:
                data = json.load(f)
                data['kata'] = self.entri
        except FileNotFoundError:
            data = None
        return data

class masuk:
# TODO cari cara untuk masukkan kata
# TODO wujudkan conditional untuk bezakan bila nak guna masuk.baharu atau masuk.tambah
    @staticmethod
    def baharu(entri, data):                        # Untuk masukkan kata yang baharu
        data = data.pop('kata')                     # Kita tidak perlukan data kata dalam fail json
        PATH = os.path.join(file_dir, base_dir, entri)
        print(PATH)
        os.mkdir(PATH)                              # Untuk wujudkan folder 'kata' dalam 'kamus_db/entri_ms/'
        with open(PATH + '/data.json', 'w') as f:   # Untuk wujudkan fail JSON 'data.json' dalam folder 'kamus_db/entri_ms_<nama_kamus>/<kata>/'
            json.dump(data, f, indent=4)

    @staticmethod
    def tambah(self):
        # Untuk tambah makna
        # TODO Tambah makna untuk kata yang sudah wujud
        pass

string = input("Masukkan kata yang ingin dicari: ")
entri = kata(string)
print(file_dir + '\\' + base_dir + string)
makna = input( "Apakah maknanya?: ")
bidang2 = input("Dalam bidang apa? (dipisahkan koma): ")
bidang = bidang2.split(",")
entri.makna(makna, bidang)
print("Hello World!")
masuk.baharu(string, entri.to_dict())
print(entri.to_dict())