# using ElevenLabs for TTS
import sys
import constants
from  elevenlabs import set_api_key, generate, play
from langchain.callbacks.base import BaseCallbackHandler

set_api_key(constants.ELEVENLABS_API_KEY)

class TTSCallbackHandler(BaseCallbackHandler):
    def __init__(self) -> None:
        self.content: str = ""
        self.final_answer: bool = False

    def tts(text):
        play(generate(text=text, voice="Callum"))

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        if(token == "?" or token == "!" or token == ":"):
            self.content += token
            print(self.content)
            self.content = ""
        else :
            self.content += token
            # tts(token)


# Might come in handy but forgot what to use this for
    # def on_llm_new_token(self, token: str, **kwargs: any) -> None:
    #     self.content += token
    #     if "Final Answer" in self.content:
    #         # now we're in the final answer section, but don't print yet
    #         self.final_answer = True
    #         self.content = ""
    #     if self.final_answer:
    #         if '"action_input": "' in self.content:
    #             if token not in ["}"]:
    #                 sys.stdout.write(token)  # equal to `print(token, end="")`
    #                 sys.stdout.flush()



# To get a list of voices:

# import requests

# url = "https://api.elevenlabs.io/v1/voices"

# headers = {
#   "Accept": "application/json",
#   "xi-api-key": constants.ELEVENLABS_API_KEY
# }

# response = requests.get(url, headers=headers)

# print(response.text)