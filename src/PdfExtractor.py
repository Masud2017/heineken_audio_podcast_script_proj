import fitz
import os




class PdfExtractor:
    def __init__(self):
        pass
    def extract(self,file_path) -> str:
        pa = os.path.dirname(__file__)
        file_path = os.path.join(pa,file_path)
        print(file_path)
        
        doc = fitz.open(file_path)
        text = ""

        for page in doc:
            page_text = page.get_text()
            text += page_text + "\n"

        return text.strip()
