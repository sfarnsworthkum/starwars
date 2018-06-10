import requests
from django.http import HttpResponse
from django.shortcuts import render
import random


def index(request):
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    return render(request, 'index.html')


def about_me(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'name': 'Ash Ketchum',
        'pokemon': 'Pikachu',
    }
    return render(request, 'about_me.html', context)

def character_api(request):
    num = random.randint(1, 87)
    response = requests.get(f'https://swapi.co/api/people/{num}/')
    data = response.json()
    print('Name:',data['name'], '\n'
    'Height:', data['height'], '\n'
    'Mass:' ,data['mass'], '\n'
    'Hair Color:', data['hair_color'], '\n'
    'Skin Color:', data['skin_color'], '\n'
    'Eye Color:', data['eye_color'], '\n'
    'Birth Year:', data['birth_year'], '\n'
    'Gender:', data['gender'])
    context = {
        'data': data,
    }
    return render(request, 'character.html', context)


def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)
