import os

from PdfExtractor import PdfExtractor
from PPtExtractor import PPtExtractor
from DocxExtractor import DocxExtractor

pdf_extractor = PdfExtractor()
ppt_extractor = PPtExtractor()
docx_extractor = DocxExtractor()


def extract_file(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return pdf_extractor.extract(file_path)

    elif ext == ".docx":
        return docx_extractor.extract(file_path)

    elif ext == ".pptx":
        return ppt_extractor.extract(file_path)

    else:
        raise ValueError(f"Unsupported file type: {ext}")
    
print(extract_file("test_pdf.pdf"))