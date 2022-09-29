"""
Алфавит
"""


class Alphabet:
    def __init__(self, lang, letters_row):
        self.lang = lang
        self.letters_row = letters_row

    def print_all(self):
        print(f"{self.lang}, {self.letters_row}")

    def letters_num(self):
        n = len(self.letters_row)
        print(f"Кол-во символов: {n}")


a = Alphabet("en", "abcdefghijklmnopqrstuvwxyz")
a.print_all()
a.letters_num()
