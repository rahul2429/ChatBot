
import requests, json
import nltk
from nltk.chat.util import Chat, reflections
import re
import random
import time
  
def remove(string):
    pattern = re.compile(r'\s+')
    return re.sub(pattern, '', string)


def weather_temp(city_name):
    city_name = city_name.groups()
    city_name = city_name[0]
    print(city_name)
    api_key = "b6b0d51a1f95f424ed11e35d3034cd03"


    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)

    x = response.json()
    
    if x["cod"] != "404":
        


        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]

        result=city_name+"Temperature (in kelvin unit) = " +str(current_temperature) +"\n atmospheric pressure (in hPa unit) = " +str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidity) +"\n description = " +str(weather_description)

    else:
        print(x)
        result=city_name+"City Not Found "
    print(result)
    return result


import requests, json
import nltk
from nltk.chat.util import Chat, reflections
import re
import time

class MyChat(Chat):

    def __init__(self, pairs, reflections={}):

        # add `z` because now items in pairs have three elements
        self._pairs = [(re.compile(x, re.IGNORECASE), y, z) for (x, y, z) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def respond(self, str):

        # add `callback` because now items in pairs have three elements
        for (pattern, response, callback) in self._pairs:
            match = pattern.match(str)

            if match:

                resp = random.choice(response)
                resp = self._wildcards(resp, match)

                if resp[-2:] == '?.':
                    resp = resp[:-2] + '.'
                if resp[-2:] == '??':
                    resp = resp[:-2] + '?'

                # run `callback` if exists  
                if callback: # eventually: if callable(callback):
                    callback(match)

                return resp



pairs = [
    ["Hi im (.*)", ["hello %1, What can I do for you?"],None],
    ["how is weather in (.*)?", ["Getting Weather Information ..."], weather_temp],
    ["my name is (.*)",["Hello %1, How are you today ?",],None],
    [
        "hi|hey|hello",
        ["Hello", "Hey there",],None
    ], 
    [
        "what is your name ?",
        ["I am a bot created by D17B Group 1. you can call me crazy!",],None
    ],
    [
        "how are you ?",
        ["I'm doing good 'n How about You ?",],None
    ],
    [
        "sorry (.*)",
        ["Its alright","Its OK, never mind",],None
    ],
    [
        "I am fine",
        ["Great to hear that, How can I help you?",],None
    ],
    [
        "i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",],None
    ],
    [
        "(.*) age?",
        ["I'm a computer program dude. Seriously you are asking me this?",],None
    ],
    [
        "what (.*) want ?",
        ["Make me an offer I can't refuse",],None
    ],
    [
        "(.*) created ?",
        ["Rahul created me using Python's NLTK library ","top secret ;)",],None
    ],
    [
        "(.*) (location|city) ?",
        ['Mumbai, Maharashtra',],None
    ],
    [
        "i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",],None
    ],
    [
        "(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"],None
    ],
    [
        "how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",],None
    ],
    [
        "(.*) (sports|game) ?",
        ["I'm a very big fan of Football",],None
    ],
    [
        "who (.*) player ?",
        ["Messy","Ronaldo","Roony"],None
    ],
    [
        "who (.*) (moviestar|actor)?",
        ["Brad Pitt"],None
    ],
    [
        "i am looking for online guides and courses to learn data science, can you suggest?",
        ["Crazy_Tech has many great articles with each step explanation along with code, you can explore"],None
    ],
    [
        "quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"],None
    ],
]

print("Greetings! My name is Chatbot-T1, What is yours?.")
Chatbot = MyChat(pairs, reflections)
Chatbot.converse()
