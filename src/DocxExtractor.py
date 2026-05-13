import os
from docx import Document

class DocxExtractor:
    def __init__(self):
        pass
    
    def extract(self,file_path:str) -> str:
        doc = Document(file_path)
        text = []

        for para in doc.paragraphs:
            text.append(para.text)

        return "\n".join(text).strip()