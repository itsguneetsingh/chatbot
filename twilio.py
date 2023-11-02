from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import elevenlabs

'''
Everything written here is assuming that you have:
    1. installed the required packages in requirements.txt
    2. set credentials for twilio and google cloud
'''

#Configuring Twilio
twilio_account_sid = "TWILIO_ACCOUNT_SID"
twilio_auth_token = "TWILIO_AUTH_TOKEN"
client = Client(twilio_account_sid, twilio_auth_token)

# Configuring Google Cloud
google_cloud_speech_client = speech.SpeechClient()

'''
If you need to listen to what the custoer says on the phone call using twilio, do the following things:
    put their phone number in the chat history
    use Google speech to text to transcribe what they say
'''

# Defining a callback function to handle audio data using Google Cloud
def process_audio(message):
    audio = message.media_stream.content
    if audio:
        audio_config = types.RecoginitionConfig(
            encoding = enums.regognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz = 16000,
        )
        audio_data = types.RecognitionAudio(content=audio)

        response = google_cloud_speech_client.recognize(config=audio_config, audio=audio_data)

        for result in response.results:
            print('Transcript: {}'.format(result.alternatives[0].transcript))


#Settin up a call with Media Streams using twilio
call = client.calls.create(
    url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient",
    to="TO_PHONE_NUMBER",
    from_="FROM_PHONE_NUMBER",
    meadia_stream_callback = process_audio,
)

# Just printing unique call id for the record
print(f"Call SID : {call.sid}")

'''
If you need to send elevenlabs audio to twilio, you need to do the following things:
    Take the text given by LLM
    Convert it into an audio file using elevenlabs api using the generate function from elevelabs
    Write it into a folder as an audio file
    Then, play the thing into the twilio call
'''

audio = elevenlabs.generate(text = "", voice = "Callum", model = "eleven_multilingual_v2", stream = True)

response = VoiceResponse()

response.play(audio)
response.record(timeout=3, action='/recording', finish_on_key='1', play_beep=True)