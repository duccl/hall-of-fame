import requests
from django.http import JsonResponse
from django.conf import settings
import json
class Api:
    baseURL = 'https://www.googleapis.com/youtube/v3/'
    maxResults = '6'
    def buildURL(self,typeOfCall,part,options):
        self.url = f'{self.baseURL}{typeOfCall}?key={settings.YOUTUBE_API_KEY}&{part}&{options}'

    def callYoutbeAPI(self):
        return requests.get(self.url).json()

    def listVideos(self,search_form):
        if search_form.is_valid():
            search_term = search_form.cleaned_data.get('search_term')
            formated_options = f'q={search_term}&maxResults={self.maxResults}'
            self.buildURL('search','part=snippet,id',formated_options)
            response = self.callYoutbeAPI()
            return JsonResponse(response)
        return JsonResponse({'data':None})