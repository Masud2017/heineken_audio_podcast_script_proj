import fitz



class PdfExtractor:
    def __init__(self):
        pass
    def extract(self,file_path) -> str:
        doc = fitz.open(file_path)
        text = ""

        for page in doc:
            page_text = page.get_text()
            text += page_text + "\n"

        return text.strip()
