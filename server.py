import flask
import argparse
import city

app = flask.Flask('Greek civilization')
app.civ = city.Greek_civilization()


@app.route('/sign_up', methods=['GET'])
def sign_up():
    return app.civ.new_user(flask.request.args['login'], flask.request.args['password'])


@app.route('/sign_in', methods=['GET'])
def sign_in():
    return app.civ.try_login(flask.request.args['login'], flask.request.args['password'])


@app.route('/watch_building', methods=['GET'])
def watch_building():
    return app.civ.active[flask.request.args['login']].watch_building(flask.request.args['type'])


@app.route('/watch_all', methods=['GET'])
def watch():
    return app.civ.active[flask.request.args['login']].watch_all()


@app.route('/watch_info', methods=['GET'])
def watch_info():
    return app.civ.watch_info(flask.request.args['login'])

@app.route('/watch_city', methods=['GET'])
def watch_city():
    return app.civ.active[flask.request.args['login']].watch_info()

@app.route('/watch_army', methods=['GET'])
def watch_army():
    return app.civ.active[flask.request.args['login']].watch_army()

@app.route('/watch_players', methods=['GET'])   
def watch_players():
    return app.civ.watch_players()

@app.route('/watch_cities', methods=['GET'])
def watch_cities():
    return app.civ.watch_cities(flask.request.args['name'])

@app.route('/rename_city', methods=['GET'])
def rename_city():
    return app.civ.rename_city(flask.request.args['login'], flask.request.args['new_name'])


@app.route('/update_building', methods=['GET'])
def update_building():
    return app.civ.active[flask.request.args['login']].update_building(flask.request.args['type'])



@app.route('/create_unit', methods=['GET'])
def create_unit():
    return app.civ.active[flask.request.args['login']].create_unit(flask.request.args['type'],
                                                                   int(flask.request.args['count']))


@app.route('/view_messages', methods=['GET'])
def view_messages():
    return app.civ.view_messages(flask.request.args['login'])


@app.route('/send_message', methods=['GET'])
def send_message():
    return app.civ.send_message(flask.request.args['player'], flask.request.args['text'])


@app.route('/create_city', methods=['GET'])
def create_city():
    return app.civ.create_city(flask.request.args['login'], flask.request.args['name'])


@app.route('/change_city', methods=['GET'])
def change_city():
    return app.civ.change_city(flask.request.args['login'], flask.request.args['name'])


@app.route('/send_army', methods=['GET'])
def send_army():
    return app.civ.send_army(flask.request.args['login'], flask.request.args['player_name'],
                             flask.request.args['city_name'], flask.request.args['army'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost', type=str)
    parser.add_argument('--port', default=50000, type=int)

    args = parser.parse_args()

    app.run(args.host, args.port, debug=True, threaded=True)


if __name__ == '__main__':
    main()
