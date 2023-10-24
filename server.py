import asyncio
import websockets
from google.cloud import speech


client = speech.SpeechClient()
language_code = "en-IN"
RATE = 16000

streaming_config = speech.StreamingRecognitionConfig(
        config= speech.RecognitionConfig(
                    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                    sample_rate_hertz=RATE,
                    language_code=language_code,
                ),
        # interim_results=True,
        #single_utterance=True
    )

async def handle_audio(websocket, path):
    while True:
        audio_data = await websocket.recv()
        # Process audio_data and transcribe it using Google Cloud Speech-to-Text

        response = client.streaming_recognize(streaming_config, audio_data)

        # response = client.recognize(
        #     config=streaming_config,
        #     audio={"content": audio_data},
        # )

        # Implement Google Cloud Speech-to-Text integration here
        for result in response.results:
            print("Transcription:", result.alternatives[0].transcript)

start_server = websockets.serve(handle_audio, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
