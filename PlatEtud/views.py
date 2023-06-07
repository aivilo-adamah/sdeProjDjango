import requests
from isodate import parse_duration
from django.conf import settings 
from django.shortcuts import render
from django.views import View
# from . models import Cour()
# Create your views here.
def LoginView(request):
    return render(request, 'login.html', {})

def AcceuilView(request):
    return render(request, 'Acceuil.html', {})

def RegistrationView(request):
    return render(request, 'registration.html', {})

def CoursView(request):
    return render(request, 'cours.html', {})

def ContactView(request):
    return render(request, 'cours.html', {})


def SearchView(request):
    videos=[]
    if request.method=='POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'
        search_params= {
            'part' : 'snippet',
            'q' : request.POST['search'],
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 9,
            'type' : 'video'

        }
        video_ids =[]
        r= requests.get(search_url,params=search_params)
        results = r.json().get('items', [])
        # results = r.json()['items']
        for result in results :
            video_ids.append(result['id']['videoId'])
        


        video_params={
            'key' :  settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),


        }    
        r= requests.get(video_url,params=video_params)
        # result = r.json()['items']
        results = r.json().get('items', [])


        # videos = []
        for result in results:
            print(result['snippet']['title'])
            print(result['id'])
            duration = result.get('contentDetails', {}).get('duration', 'PT1H30M')
            print(parse_duration(duration))
        
                # traiter l'erreur, par exemple en affichant un message d'erreur
            # print(parse_duration(result['contentDetails']['duration']))
            print(result['snippet']['thumbnails']['high']['url'])
            duration = result.get('contentDetails', {}).get('duration', 'PT1H30M')
            
            video_data = {

                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration' : parse_duration(duration),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']

            }
            videos.append(video_data)
            print(videos) 

    context = {
         'videos' : videos
     }
    
    return render(request,'search.html',context)
# --------------------------------------------------------------------------------
# pour python

# ''' def Search_pythonView(request):
#     # videos=[]
#     # if request.method=='POST':
#     search_url = 'https://www.googleapis.com/youtube/v3/search'
#     video_url = 'https://www.googleapis.com/youtube/v3/videos'
#     search_params= {
#         'part' : 'snippet',
#         'q' : 'learn python',
#         'key' : settings.YOUTUBE_DATA_API_KEY,
#         'maxResults' : 9,
#         'type' : 'video'

#     }
#     video_ids =[]
#     r= requests.get(search_url,params=search_params)
#     results = r.json().get('items', [])
#         # results = r.json()['items']
#     for result in results :
#         video_ids.append(result['id']['videoId'])
        


#         video_params={
#             'key' :  settings.YOUTUBE_DATA_API_KEY,
#             'part' : 'snippet,contentDetails',
#             'id' : ','.join(video_ids),


#         }    
#         r= requests.get(video_url,params=video_params)
#         # result = r.json()['items']
#         results = r.json().get('items', [])


#         videos = []
#     for result in results:
#         print(result['snippet']['title'])
#         print(result['id'])
#         duration = result.get('contentDetails', {}).get('duration', 'PT1H30M')
#         print(parse_duration(duration))
        
#                 # traiter l'erreur, par exemple en affichant un message d'erreur
#             # print(parse_duration(result['contentDetails']['duration']))
#         print(result['snippet']['thumbnails']['high']['url'])
#         duration = result.get('contentDetails', {}).get('duration', 'PT1H30M')
            
#         video_data = {

#             'title' : result['snippet']['title'],
#             'id' : result['id'],
#             'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
#             'duration' : parse_duration(duration),
#             'thumbnail' : result['snippet']['thumbnails']['high']['url']

#         }
#         videos.append(video_data)
#         print(videos) 

#     context = {
#          'videos' : videos
#      }
    
#     return render(request,'search.html',context) '''