from gtts import gTTS

def generate_speech(text):
    tts = gTTS(text, lang="en")
    file_name = 'file.mp3'
    file_path = f'audio/tmp/{file_name}'
    tts.save(file_path)
    return file_name