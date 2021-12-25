from enum import Enum
from fastapi import FastAPI
from random import randrange

app = FastAPI()

class arms(str, Enum):
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'
    lizard = 'lizard'
    spock = 'spock'

@app.get('/')
async def root():
    return {'message': 'Connected'}

@app.get('/shoot')
async def shoot(arm: arms):
    game_key = {
        ('rock', 'rock'): "It's a tie.",
        ('rock', 'paper'): "You lost.",
        ('rock', 'scissors'): "You won!",
        ('rock', 'lizard'): "You won!",
        ('rock', 'spock'): "You lost.",
        ('paper', 'rock'): "You won!",
        ('paper', 'paper'): "It's a tie.",
        ('paper', 'scissors'): "You lost.",
        ('paper', 'lizard'): "You lost.",
        ('paper', 'spock'): "You won!", 
        ('scissors', 'rock'): "You lost.",
        ('scissors', 'paper'): "You won!",
        ('scissors', 'scissors'): "It's a tie.",
        ('scissors', 'lizard'): "You won!",
        ('scissors', 'spock'): "You lost.",
        ('lizard', 'rock'): "You lost.",
        ('lizard', 'paper'): "You won!",
        ('lizard', 'scissors'): "You lost.",
        ('lizard', 'lizard'): "It's a tie.",
        ('lizard', 'spock'): "You won!",
        ('spock', 'rock'): "You won!",
        ('spock', 'paper'): "You lost.",
        ('spock', 'scissors'): "You won!",
        ('spock', 'lizard'): "You lost.",
        ('spock', 'spock'): "It's a tie.", 
    }
    weapons = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    opponent_weapon = weapons[randrange(0, 5)]
    response = game_key[(arm, opponent_weapon)]
    result = {'your_weapon': arm, 'opponent_weapon': opponent_weapon, 'response': response}
    return result