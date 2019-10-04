#!/usr/bin/python3

'''
Written by Bianca Power for CSB2019

A flask server for presenting pokemon color, species and names from the pokemon api

Demonstration of the Pokemon API using Flask.
Purpose: Get list of pokemon by colour
'''

from flask import Flask
import requests
APP = Flask(__name__)

POKEMON_API_URL = "https://pokeapi.co/api/v2/"
COLOUR_URL = POKEMON_API_URL + 'pokemon-color'

@APP.route('/<colour>')
def get_by_colour(colour):
    '''
    Sends a get request to the pokemon api a gets pokemon species by color
    '''
    colour_json = requests.get(f'{COLOUR_URL}/{colour}').json()
    pokemon_species_list = colour_json["pokemon_species"]

    html = ''

    for species in pokemon_species_list:
        html += f'<p>{species["name"]}</p>'
        # print(species["name"])

    # colour_json["pokemon_species"][0]["name"]
    return html

@APP.route('/')
def index():
    '''
    Serves html pages for pokemon
    '''
    colours_json = requests.get(COLOUR_URL).json()
    colours_list = colours_json['results']

    html = ''
    for colour in colours_list:
        url = '/' + colour["name"]
        html += f'<a href="{url}">{colour["name"]}</a><br>'

    return html
