# Google's CLOUD TEXT-TO-SPEECH https://cloud.google.com/text-to-speech/

from google.cloud import texttospeech
import os

# auth setup https://cloud.google.com/docs/authentication/getting-started
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\speech\ttspeech-bfc6f17140d5.json'

# Instantiates client
client = texttospeech.TextToSpeechClient()

file = 'ssml_boilerplate.ssml'
with open(file, 'r') as f:
    text_ssml = f.read()
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(ssml=text_ssml) # pylint: disable=no-member

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(language_code='en-US', # pylint: disable=no-member
                                                name= 'en-US-Wavenet-I',
                                                ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3) # pylint: disable=no-member

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('file_output_speech.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)

