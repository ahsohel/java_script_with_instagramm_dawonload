from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def going_for_insta(request):
    import requests
    import os
    import json
    import shutil

    INSTA_URL = request.POST.get('link_get')

    header = {
        "User-Agent": "Mozilla/5.0"
    }

    # INSTA_URL = input("Enter the url")
    TAIL = "?__a=1"

    URL = INSTA_URL + TAIL
    response = requests.get(URL, headers=header).json()

    image_location = response["graphql"]["shortcode_media"]["display_resources"]
    image_location = image_location[2].get("src")

    print(image_location)

    hd_image_response = requests.get(image_location, stream=True)

    with open("C:\\Users\\sohel chowdhury\\Desktop\\Instagram Profile pictures\\hd_v.mp4", "wb") as out_file:
        shutil.copyfileobj(hd_image_response.raw, out_file)

    print('hello')


    return render(request, 'index.html')
