import json

import requests
import gistats

config = json.load(open('config.json', 'r'))
gist = gistats.Gist(config['username'], config['token'], config['gist'], 'Chess Statistics')
response = requests.get(
    f'https://api.chess.com/pub/player/{config["chessname"]}/stats'
).json()

gist.update({
    'Bullets 🚅': response['chess_bullet']['last']['rating'],
    'Rapid ⏲': response['chess_rapid']['last']['rating']
})