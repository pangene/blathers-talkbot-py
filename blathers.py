import sqlite3, re, sys

ENABLE_VERSION_SELECTION = True

def connect_to_database(database):
    '''Connects to the dialogue.db database.'''
    conn = sqlite3.connect(database)
    return conn


def table_to_dict(conn, table):
    '''Converts a two-column SQL table into a dictionary.'''
    result_dict = {}
    c = conn.cursor()
    for col1, col2 in c.execute(f'SELECT * FROM "{table}"'):
        result_dict[col1] = col2
    return result_dict


def get_version_creature_SQL_table(version, creature, connection):
    '''Returns the appropriate version-creature SQL table as a dictionary.'''
    table_name = f'{version}_{creature}s'
    if creature == 'fish':
        table_name = table_name[:-1]
    try:
        dialogues = table_to_dict(connection, table_name)
    except sqlite3.OperationalError:
        raise NotImplementedError
    return dialogues

def separate_to_single_sentences(string):
    '''Returns a list of individual sentences within string.'''
    return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!|\")\s',
        string.replace('\n',' '))


def print_single_sentence(string):
    '''Prints a single sentence in a string, requests user input to proceed.'''
    for sentence in separate_to_single_sentences(string):
        input(sentence)


def convert_to_options(list):
    '''Enumerates list and adds cancel option'''
    list = [f'{index + 1}. {element}' for index, element in enumerate(list)]
    list.append(f'{len(list) + 1}. Never mind.')
    return list


def print_options(options_list):
    '''Prints out a list of options for the user to select with user select.'''
    for option in options_list:
        print(option)

def user_select(origin_func):
    '''Returns user choice among given dialogue options.'''
    try:
        return int(input('Pick a number to proceed.\n'))
    except ValueError:
        print('Please pick a number.')
        origin_func()


class Blathers:
    '''Blathers is a class that changes depending on game version.'''

    versions = [
        'animal_crossing',
        'wild_world',
        'city_folk',
        'new_leaf',
        'new_horizons'
    ]

    creatures = ['bug', 'fish', 'deep-sea_creature', 'end']

    root_player_options = [
        '1. Tell me more about a bug.',
        '2. Tell me more about a fish.',
        '3. Tell me more about a sea creature.',
        '4. Never mind.'
    ]

    def __init__(self, version='new_horizons', database='dialogue.db'):
        self.version = version
        if self.version not in ('new_horizons', 'new_leaf'):
            Blathers.root_player_options.pop()
            Blathers.root_player_options[2] = '3. Never mind.'
        self.connection = connect_to_database(database)
        self.first_conversation = True
        input("Hootie hoo! Hello! I'm Blathers! Nice to meet you.")


    def root_dialogue(self):
        '''Requests user for dialogue option to learn more.'''
        if self.first_conversation:
            self.first_conversation = False
            root_dialogues = table_to_dict(self.connection, 'root_dialogues')
            print(root_dialogues[self.version])
        else:
            print('Is there anything else I can help you with?')
        print_options(Blathers.root_player_options)
        choice = user_select(self.root_dialogue)
        if self.version not in ('new_horizons', 'new_leaf') and choice == 3:
            choice = 4
        try:
            creature = Blathers.creatures[choice - 1]
        except IndexError:
            print('Invalid choice.')
            self.root_dialogue()
        if creature == 'end':
            self.bye()
            sys.exit()
        else:
            self.creature_dialogue(creature)

    def creature_dialogue(self, creature):
        '''Explains a requested creature and returns to root.'''
        if creature == 'bug':
            print('Oh... you would like to learn about a bug. Alright then...')
        else:
            print(f'Oh wonderful! You would like to learn about a {creature}. \
                They are marvellous things!')
        print(f'Which {creature} would you like to know about?')
        dialogues = get_version_creature_SQL_table(self.version,
            creature, self.connection)
        options = convert_to_options(dialogues.keys())
        print_options(options)
        choice = user_select(lambda: self.creature_dialogue(creature))
        if choice != len(options):
            try:
                description = list(dialogues.values())[choice - 1]
            except IndexError:
                print('Invalid option!')
                self.creature_dialogue(creature)
            print_single_sentence(description)
        self.root_dialogue()


    def bye(self):
        print('Goodbye then. Thank you for talking to me!')


def version_select():
    '''Returns user-selected version number.'''
    for version_num, version in enumerate(Blathers.versions):
        print(str(version_num + 1) + '. ' + version)
    version_num = int(input('Which Blathers would you like to speak to?\n'))
    try:
        version = Blathers.versions[version_num-1]
    except IndexError:
        print('Invalid version number or version is unavailable. \
            Restarting...\n')
        main()
    return version

def main():
    print('Hello, and welcome to the Blathers talkbot.')
    if ENABLE_VERSION_SELECTION:
        version = version_select()
        blathers = Blathers(version)
    else:
        blathers = Blathers()
    blathers.root_dialogue()


if __name__ == "__main__":
    main()
