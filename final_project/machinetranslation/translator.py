"""Required Modules for this program"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator('rNNe1tsh3f7x8WRZeJw0aUh0mnpXAkO3jptTu4QSnOAH')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/6e970e71-e943-4dba-b9bd-3b9b6287dd39')

def englishToFrench(englishText):
    """Translates English to French"""
    model_id='en-fr'
    fr_text = language_translator.translate(
    text=englishText,
    model_id=model_id).get_result()
    return(fr_text['translations'][0]['translation'])
    

def frenchToEnglish(frenchText):
    """Translates French to English"""
    model_id='fr-en'
    en_text = language_translator.translate(
    text=frenchText,
    model_id=model_id).get_result()
    return(en_text['translations'][0]['translation'])
    
