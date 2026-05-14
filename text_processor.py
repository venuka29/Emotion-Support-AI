import re

class TextProcessor:
    def clean(self, text):
        return re.sub(r'\s+', ' ', text.lower().strip())

    def tokenize(self, text):
        return self.clean(text).split()