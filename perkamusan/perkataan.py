import json
base_dir = 'kamus_db/entri_ms/'

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
    def baharu(self):
        # Untuk masukkan kata yang baharu
        # TODO wujudkan folder 'kata' dalam 'kamus_db/entri_ms_<nama_kamus>'
        # TODO wujudkan fail JSON 'data.json' dalam folder 'kamus_db/entri_ms_<nama_kamus>/<kata>/'
        pass

    def tambah(self):
        # Untuk tambah makna
        pass


string = input("Masukkan kata yang ingin dicari: ")
entri = kata(string)
makna = input("Apakah maknanya?: ")
bidang2 = input("Dalam bidang apa? (dipisahkan koma): ")
bidang = bidang2.split(",")
entri.makna(makna, bidang)
print("Hello World!")
print(entri.to_dict())