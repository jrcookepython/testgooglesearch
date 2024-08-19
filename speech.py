import speech_recognition

class SpeechRecording:
    def __init__(self):
        speech_rec = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as speech:
            print("Say Somthing as a test!")
            audio = speech_rec.listen(speech)
            self.audio_text = speech_rec.recognize_google(audio)
            print(self.audio_text)

            with open('speechtest.wav', 'wb') as f:
                f.write(audio.get_wav_data())
#
#
# speech_rec = speech_recognition.Recognizer()
#
# with speech_recognition.Microphone() as speech:
#     print("Say Somthing as a test!")
#     audio = speech_rec.listen(speech)
#     audio_text = speech_rec.recognize_google(audio)
#     print(audio_text)