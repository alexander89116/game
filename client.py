import requests
import argparse
import sys
from data_for_client import *


class PatchedHelpAction(argparse._HelpAction):
    def __call__(self, parser, namespace, values, option_string=None):
        parser.print_help()


class PatchedParserException(Exception):
    def __init__(self, parser, message):
        self.parser = parser
        self.message = message


class PatchedArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        assert 'add_help' not in kwargs, 'add_help option forbidden in {}'.format(self.__class__.__name__)

        super(PatchedArgumentParser, self).__init__(*args, **kwargs, add_help=False)

        self.register('action', 'help', PatchedHelpAction)

    def error(self, message):
        raise PatchedParserException(self, message)


def starting_parser(subs):
    start = subs.add_parser('start', description='Start session')
    start.set_defaults(method='start')
    start.add_argument('--host', default='localhost', type=str)
    start.add_argument('--port', default=50000, type=int)


def help_parser(subs):
    help = subs.add_parser('help', description='Help')
    help.set_defaults(method='help')


def exit_parser(subs):
    exit = subs.add_parser('exit', description='Exit')
    exit.set_defaults(method='exit')


def sign_in_parser(subs):
    sign_in = subs.add_parser('sign_in', description='Sign in')
    sign_in.set_defaults(method='sign_in')
    sign_in.add_argument('-l', '--login', required=True)
    sign_in.add_argument('-p', '--password', required=True)


def sign_up_parser(subs):
    sign_up = subs.add_parser('sign_up', description='Sign up')
    sign_up.set_defaults(method='sign_up')
    sign_up.add_argument('-l', '--login', required=True, help='Your login will be your name in the game')
    sign_up.add_argument('-p', '--password', required=True)


def watch_all_parser(subs, login):
    watch_all = subs.add_parser('watch_all', description='Watch everything about the city')
    watch_all.set_defaults(method='watch_all')
    watch_all.set_defaults(login=login)


def watch_building_parser(subs, login):
    watch_building = subs.add_parser('watch_building', description='Watch all building information')
    watch_building.set_defaults(method='watch_building')
    watch_building.set_defaults(login=login)
    watch_building.add_argument('-t', '--type', choices=BUILDINGS_NAME, required=True, type=str)


def watch_info_parser(subs, login):
    watch_info = subs.add_parser('watch_info', description='Watch basic information about the city')
    watch_info.set_defaults(method='watch_info')
    watch_info.set_defaults(login=login)


def watch_city_parser(subs, login):
    watch_city = subs.add_parser('watch_city', description='Watch basic information about the city')
    watch_city.set_defaults(method='watch_city')
    watch_city.set_defaults(login=login)


def watch_army_parser(subs, login):
    watch_army = subs.add_parser('watch_army', description='Watch your army composition')
    watch_army.set_defaults(method='watch_army')
    watch_army.set_defaults(login=login)


def rename_city_parser(subs, login):
    rename_city = subs.add_parser('rename_city', description='Rename your active city')
    rename_city.set_defaults(method='rename_city')
    rename_city.set_defaults(login=login)
    rename_city.add_argument('-nn', '--new_name', required=True)


def update_building_parser(subs, login):
    update_building = subs.add_parser('update_building', description='Update building')
    update_building.set_defaults(method='update_building')
    update_building.set_defaults(login=login)
    update_building.add_argument('-t', '--type', choices=BUILDINGS_NAME, required=True, type=str)


def units_info_parser(subs):
    units_info = subs.add_parser('units_info')
    units_info.set_defaults(method='units_info')


def create_unit_parser(subs, login):
    create_unit = subs.add_parser('create_unit', description='Create units')
    create_unit.set_defaults(method='create_unit')
    create_unit.set_defaults(login=login)
    create_unit.add_argument('-t', '--type', choices=UNITS_NAME, required=True, type=str)
    create_unit.add_argument('-c', '--count', default=1, type=int)


def create_city_parser(subs, login):
    create_city = subs.add_parser('create_city', description='Create new city')
    create_city.set_defaults(method='create_city')
    create_city.set_defaults(login=login)
    create_city.add_argument('-n', '--name', required=True, type=str)


def change_city_parser(subs, login):
    change_city = subs.add_parser('change_city', description='Сhange city')
    change_city.set_defaults(method='change_city')
    change_city.set_defaults(login=login)
    change_city.add_argument('-n', '--name', required=True, type=str)


def send_army_parser(subs, login):
    send_army = subs.add_parser('send_army', description='send army')
    send_army.set_defaults(method='send_army')
    send_army.set_defaults(login=login)
    send_army.add_argument('-pn', '--player_name', required=True)
    send_army.add_argument('-cn', '--city_name', required=True)
    send_army.add_argument('-a', '--army', required=True)


def view_messages_parser(subs, login):
    view_messages = subs.add_parser('view_messages', description='View your messages')
    view_messages.set_defaults(method='view_messages')
    view_messages.set_defaults(login=login)


def send_message_parser(subs, login):
    send_message = subs.add_parser('send_message', description='send message to another player')
    send_message.set_defaults(method='send_message')
    send_message.set_defaults(login=login)
    send_message.add_argument('-p', '--player', required=True)
    send_message.add_argument('-t', '--text', required=True)


def watch_players_parser(subs):
    watch_players = subs.add_parser('watch_players')
    watch_players.set_defaults(method='watch_players')


def watch_cities_parser(subs):
    watch_cities = subs.add_parser('watch_cities')
    watch_cities.set_defaults(method='watch_cities')
    watch_cities.add_argument('-n', '--name', required=True)


def get_params(args):
    res = {}
    for p in args:
        if p[0] == 'method':
            continue
        res[p[0]] = p[1]
    return res


def main():
    start_parser = argparse.ArgumentParser(description='Greek civilization')
    start_subs = start_parser.add_subparsers()

    starting_parser(start_subs)

    args = start_parser.parse_args()

    host = args.host
    port = args.port

    print('Welcome to "Greek civilization". Sign in or sign up.\n')

    try_login_parser = PatchedArgumentParser(description='Try login')
    try_login_subs = try_login_parser.add_subparsers()
    sign_in_parser(try_login_subs)
    sign_up_parser(try_login_subs)
    help_parser(try_login_subs)
    exit_parser(try_login_subs)

    login = ''
    while True:
        input_data = input('> ').split()
        try:
            args = try_login_parser.parse_args(input_data)
        except PatchedParserException as exc:
            print(exc.message, file=sys.stdout)
            exc.parser.print_usage(sys.stdout)
        else:
            if args.method == 'help':
                try_login_parser.print_help()
            elif args.method == 'exit':
                print('Goodbye!')
                exit(0)
            else:
                r = requests.get('http://{}:{}/{}'.format(host, port, args.method),
                                 params=get_params(args._get_kwargs()))
                print(r.text)
                if r.text == 'OK':
                    login = args.login
                    break

    parser = PatchedArgumentParser(prog='')
    subs = parser.add_subparsers()

    watch_info_parser(subs, login)
    watch_all_parser(subs, login)
    watch_city_parser(subs, login)
    watch_building_parser(subs, login)
    watch_army_parser(subs, login)
    watch_players_parser(subs)
    watch_cities_parser(subs)
    rename_city_parser(subs, login)
    update_building_parser(subs, login)
    units_info_parser(subs)
    create_unit_parser(subs, login)
    send_army_parser(subs, login)
    create_city_parser(subs, login)
    change_city_parser(subs, login)
    view_messages_parser(subs, login)
    send_message_parser(subs, login)
    help_parser(subs)
    exit_parser(subs)

    while True:
        input_data = input('> ').split()
        try:
            args = parser.parse_args(input_data)
        except PatchedParserException as exc:
            print(exc.message, file=sys.stdout)
            exc.parser.print_usage(sys.stdout)
        else:
            if args.method == 'help':
                parser.print_help()
            elif args.method == 'exit':
                print('Goodbye!')
                exit(0)
            elif args.method == 'units_info':
                print(UNITS_INFO)
            else:
                r = requests.get('http://{}:{}/{}'.format(host, port, args.method),
                                 params=get_params(args._get_kwargs()))
                print(r.text)


if __name__ == '__main__':
    main()
