class TextManager:
    def __init__(self, output_file="output.txt"):
        self.text = ""
        self.output_file = output_file

    def add_key(self, key):
        self.text += key
        self._save_to_file()

    def delete_last(self):
        self.text = self.text[:-1]
        self._save_to_file()

    def clear_text(self):
        self.text = ""
        self._save_to_file()

    def get_text(self):
        return self.text

    def _save_to_file(self):
        with open(self.output_file, "w", encoding="utf-8") as f:
            f.write(self.text)
