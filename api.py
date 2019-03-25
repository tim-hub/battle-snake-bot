from functools import reduce
import pprint
from flask import request, Response
from app import app, db, logger
from models import Game, Turn, GameSchema, TurnSchema

pp = pprint.PrettyPrinter(indent=2)

@app.route('/', methods=['POST', 'GET'])
def index():
    return '''
    Snake bot is OK, can got to fight now. This is the dev version.
    '''

@app.route('/ping', methods=['POST', 'GET'])
def ping():
    return {'message': 'Server is running.'}

@app.route('/start', methods=['POST', 'GET'])
def start():
    logger.info('start a game')
    if request.method == 'POST':
        data = request.data
        game_id = data.get("game").get("id", -1)
        game_info = {
            'you': data.get('you', None),
            'board': data.get('board', None)
        }

        game = Game(game_uuid=game_id, game_info=game_info)
        db.session.add(game)
        db.session.commit()
    return {
        "color": "#ffffff",
        "headType": "bendr",
        "tailType": "pixel",
        'message': 'Starting the game.'
    }


@app.route('/move', methods=['POST', 'GET'])
def move():
    logger.info('start a move')
    if request.method =='POST':
        # get all data
        data = request.data
        game_uuid = data.get("game").get("id", -1)
        game = Game.query.filter_by(game_uuid=game_uuid).first()
        turn_id = data.get("turn", -1)
        you = data.get('you', None)
        board = data.get('board', None)
        turn_info = {
            'you': you,
            'board': board
        }
        # store to db
        turn = Turn(turn=turn_id, turn_info=turn_info, game=game)
        db.session.add(turn)
        db.session.commit()
        # pp.pprint(data)

        # analyze the map and bot
        height = board.get('height', 0)
        width = board.get('width', 0)

        snakes = board.get('snakes', [])
        all_body_list = [b.get('body', []) for b in snakes]
        all_bodies = list(reduce(lambda x, y: x+y, all_body_list))
        food = board.get('food', [])

        you_body = you.get('body', [])
        you_head = you_body[0]


        # pp.pprint(all_bodies)
        # pp.pprint(food)
        the_map = []
        for i in range(width):
            the_row = []
            for j in range(height):
                flag = ' '
                tmp_pos = {
                    'x': i+1,
                    'y': j+1
                }
                if tmp_pos in all_bodies:
                    flag = 'b'
                elif tmp_pos in food:
                    flag = 'f'
                the_row.append(flag)
            the_map.append(the_row)
        pp.pprint(the_map)

    return  { "move": "left" }





@app.route('/end', methods=['POST', 'GET'])
def end():
    return {'message':'Ending the game.'}


@app.route('/admin')
def admin():
    # query results
    games = Game.query.all()
    turns = Turn.query.all()
    return {
        'message': 'all data for admin only',
        'data': {
            'games': GameSchema(many=True).dump(games)[0],
            'scans': TurnSchema(many=True).dump(turns)[0]
        }
    }