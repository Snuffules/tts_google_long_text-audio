Google Cloud Text-to-Speech Long Audio Synthesis
This script uses Google Cloud's Text-to-Speech API to convert long text files into audio files. It's designed to handle large texts that exceed the standard API's 5000-byte limit.
Prerequisites
Python 3.7 or higher
Google Cloud account with billing enabled
Text-to-Speech API enabled in your Google Cloud project
Google Cloud Storage bucket for output
Google Cloud SDK installed and configured
Installation
Install the required library:
text
pip install google-cloud-texttospeech

Set up Google Cloud authentication:
text
gcloud auth application-default login

Script Explanation
python
from google.cloud import texttospeech_v1 as texttospeech

This line imports the Google Cloud Text-to-Speech library, specifically the v1 (stable) version.
python
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

This function reads the content of a text file and returns it as a string.
python
def synthesize_long_audio(text, output_gcs_uri):

This is the main function that handles the long audio synthesis process. It takes two parameters:
text: The input text to be converted to speech
output_gcs_uri: The Google Cloud Storage URI where the output audio file will be saved
python
client = texttospeech.TextToSpeechLongAudioSynthesizeClient()

This line creates a client for the Long Audio Synthesis API.
python
input_text = texttospeech.SynthesisInput(text=text)
voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Standard-A")
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16)

These lines set up the synthesis parameters:
input_text: The text to be synthesized
voice: The voice to be used (in this case, a standard US English voice)
audio_config: The audio configuration (using LINEAR16 encoding, which is uncompressed 16-bit signed little-endian samples)
python
request = texttospeech.SynthesizeLongAudioRequest(
    parent="projects/fifth-name-443410-d1/locations/global",
    input=input_text,
    voice=voice,
    audio_config=audio_config,
    output_gcs_uri=output_gcs_uri
)

This creates the request object for the long audio synthesis. The parent parameter should be replaced with your actual Google Cloud project ID.
python
operation = client.synthesize_long_audio(request=request)
print("Long audio synthesis in progress...")
result = operation.result()
print("Audio synthesized and saved to:", output_gcs_uri)

These lines send the request to the API, wait for the operation to complete, and print the result.
python
# Usage
text = read_text_file('DataPreprocessingTechniques.txt')
synthesize_long_audio(text, 'gs://long_audio_tts/DataPreprocessingTechniques.wav')

This is an example of how to use the script. It reads a text file and synthesizes it into an audio file stored in a Google Cloud Storage bucket.
Usage
Replace 'fifth-name-443410-d1' with your actual Google Cloud project ID.
Ensure your Google Cloud Storage bucket exists and you have write permissions.
Run the script:
text
python script_name.py

Note
This script is designed for long texts. For shorter texts (under 5000 bytes), consider using the standard Text-to-Speech API for faster processing.
