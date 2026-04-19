import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

class ElevenlabsTextToAudioPodcastConverter:
    def __init__(self):
        self.elevenlabs = ElevenLabs(api_key = os.getenv("eleven_labs_api"))
    
    def convert_to_podcast(self,text_doc:str):
        audio = self.elevenlabs.text_to_speech.convert(voice_id="NOpBlnGInO9m6vDvFkFC",
                                                       text = text_doc,
                                                       model_id = "eleven_v3",
                                                       language_code="en")
        
        print("Printing the type of audio ",type(audio))
        with open("output.mp3","wb") as file:
            for x in audio:
                file.write(x)
            
if __name__ == "__main__":
    ElevenlabsTextToAudioPodcastConverter().convert_to_podcast("Testing if changing the text passage can cause issues with the existing file.")