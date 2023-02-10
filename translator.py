import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['_OBZyB28gwASdAr-0ttdyJ-ywnzvhDuOZ8vnpVL71jL2']
url = os.environ['https://api.us-east.language-translator.watson.cloud.ibm.com/instances/2148bef1-7213-43ed-b49e-56be883fdb90']


authenticator = IAMAuthenticator('api')
language_translator = LanguageTranslatorV3( version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url('url')
# pylint: disable=missing-function-docstring
def english_to_french(english_text):
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text # r\n

def french_to_english(french_text):
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text # r\n
    # pylint: disable=C0304