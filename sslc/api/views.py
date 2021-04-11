from django.http import JsonResponse
from django.shortcuts import render
import speech_recognition as sr
import requests
import json
from django.views.generic import View
from time import time
from django.http import JsonResponse

def get_gif_ID(speech):
    url = 'http://api.giphy.com/v1/gifs/search'
    q = "@signwithrobert "+speech
    data = {
        "q": q,
        "api_key": "FlIXrnEA6ge1L7mmEE1FtkHbvnueTO85",
        "limit": "5"
    }
    res = requests.get(url, data)
    content = res.json()
    gif_id = content['data'][0]['id']
    print("Fetching gif ID => ",gif_id)
    print(type(gif_id))
    return gif_id

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Say something')
        try:
            audio = r.listen(source)
            speech = r.recognize_google(audio)
        except Exception as e:
            print("Your voice is not audiable")
            speech="try again"

    return speech

class AjaxHandlerView(View):

    def get(self, request):

        if request.is_ajax():
            try:
                speech = listen()
                if speech == 'try again':
                    gif_url = ''
                    speech = 'Your voice is not audiable. Could you please Try again'
                    print("Your voice is not audiable Try again")

                else:
                    print("you said " + speech.lower())
                    gif_id = get_gif_ID(speech)
                    gif_url = f"https://i.giphy.com/media/{gif_id}/giphy.webp"
                    print("Gif URL => ", gif_url)
            except Exception as e:
                print("Exception at get function!")
                speech = "Something went wrong.. Please Try again!"
                gif_url = ''
            # gif_url = "https://i.giphy.com/media/26FLchGgqamznV64E/giphy.webp"
            # speech = "Good morning"
            return JsonResponse({'gif_url': gif_url, 'speech': speech})

        return render(request,'api/index.html')




        # https: // www.youtube.com / watch?v = d1VoThpQno4
        #

# def index(request):
#     return render(request, 'api/index.html')
#
#
#
#
# def record(request):
#
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#         print('Say something')
#         audio = r.listen(source)
#
#         # recognize speech using Sphinx
#         try:
#             speech = r.recognize_google(audio)
#             # speech = "Good morning"
#             print("you said " + speech.lower())
#             if len(speech)>0:
#                 gif_id = get_gif_ID(speech)
#                 gif_url = f"https://i.giphy.com/media/{gif_id}/giphy.webp"
#                 print("Gif URL ",gif_url)
#             else:
#
#                 speech="Sorry! I am not sure i understand. Could you please Try again!"
#                 return JsonResponse({'speech': speech})
#         except Exception as e:
#             print("Could not listen Try again!")
#             speech = "Something went wrong.. Please Try again!"
#             return JsonResponse({'speech': speech})
#
#     return JsonResponse({'gif_url':gif_url, 'speech':speech})