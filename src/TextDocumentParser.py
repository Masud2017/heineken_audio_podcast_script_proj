
'''
<h1>TextDocumentParser</h1>
This class uses multiple model to extract text data from these following types of documents: pdf, ppt, image, docs/docx

The constructor receives both website url or file path that exists in the local system.

@author Md Masud karim
'''
class TextDocumentParser:
    '''
    @params file_path - This can be either website url to an image or absolute file path for image stored in a local system.
    '''
    def __init__(self,file_path:str):
        self.doc_ext = ["pdf", "ppt", "jpg", "png","docx", "docs"]
        
    def extract_text(self)->str:
        pass