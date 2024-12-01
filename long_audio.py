from google.cloud import texttospeech_v1 as texttospeech

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def synthesize_long_audio(text, output_gcs_uri):
    client = texttospeech.TextToSpeechLongAudioSynthesizeClient()
    
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Standard-A")
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16)

    request = texttospeech.SynthesizeLongAudioRequest(
        parent="projects/fifth-name-443410-d1/locations/global",
        input=input_text,
        voice=voice,
        audio_config=audio_config,
        output_gcs_uri=output_gcs_uri
    )

    operation = client.synthesize_long_audio(request=request)
    print("Long audio synthesis in progress...")
    result = operation.result()
    print("Audio synthesized and saved to:", output_gcs_uri)

# Usage
text = read_text_file('your_text_file.txt')
synthesize_long_audio(text, 'gs://long_audio_tts/output.wav')
