import SpeechToText
import pinecone
import constants
# import chatbot


from google.cloud import speech
from google.oauth2 import service_account

def main() -> None:
    
    # Congifuring Everything

    credentials = service_account.Credentials.from_service_account_file(
    'chatbot/Credentials.json',
    scopes=['https://www.googleapis.com/auth/cloud-platform']
    )

    language_code = "en-IN"  # a BCP-47 language tag

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz = SpeechToText.RATE,
        language_code=language_code,
    )

    print("config set")

    streaming_config = speech.StreamingRecognitionConfig(
        config=config,
        interim_results = True,
        single_utterance=True
    )

    print('streaming config set')

    pinecone.init(api_key= constants.PINECONE_API_KEY, environment= constants.PINECONE_ENVIRONMENT)

    print('pinecone initialized')

    # agent = chatbot.load_agent()

    print('done loading agent')



    with SpeechToText.MicrophoneStream(SpeechToText.RATE, SpeechToText.CHUNK) as stream:
        while True:  # Infinite loop
            audio_generator = stream.generator()
            requests = (
                speech.StreamingRecognizeRequest(audio_content=content)
                for content in audio_generator
            )

            print('start speaking')

            responses = client.streaming_recognize(streaming_config, requests)
            transcript = None

            for response in responses:
                transcript = SpeechToText.listen_print_loop([response])
                continue
                # agent(transcript)



if __name__ == "__main__":
    main()