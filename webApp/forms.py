from flask_wtf import FlaskForm
from wtforms import StringField
import requests
from webApp import main_functions

lang_list = main_functions.read_from_file("webApp/JSON_Files/lang_list.json")


class myForm(FlaskForm):
    text_area = StringField("Sentence")


def detectLanguageUserSent(sent):
    api_key = main_functions.read_from_file("webApp/JSON_Files/api_key.json")
    my_key = api_key["my_key"]

    url = "https://ws.detectlanguage.com/0.2/detect?q=" + sent + "&key=" + my_key

    response = requests.get(url).json()
    print(response)
    min_conf = 10000
    for i in response["data"]["detections"]: 
        if i["confidence"] < min_conf:
            min_conf, lang = i["confidence"], i["language"]
        
    for i in lang_list:
        if i["code"] == lang:
            lang = i["name"].title()

    return lang, min_conf
    #return response