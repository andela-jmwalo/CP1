#!/usr/bin/env python
"""

Usage:
    amity create_room (livingspace | office) (<room_name>)...
    amity add_person <first_name> <last_name> (fellow | staff)
    amity reallocate_person <person_id> <room_name> (LivingSpace | Office)
    amity load_people <filename>
    amity print_allocations [--output=<filename>]
    amity print_unallocated [--output=<filename>]
    amity print_room <roomname>
    amity save_state [--db=<sqlite_database>]
    amity load_state <db_name>
    amity (-i | --interactive)
    amity (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import os
import cmd
from models.amity import Amity
from docopt import docopt, DocoptExit
import colorama
from termcolor import cprint, colored
from pyfiglet import figlet_format


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    cprint(figlet_format('AMITY', font='isometric1'),
           'magenta')
    cprint('*' * 60, 'white')
    cprint("    AMITY ROOM ALLOCATION SYSTEM.    ", 'magenta')
    cprint('*' * 60, 'white')
    cprint(" Below is a list of available commands.", 'magenta')
    cprint('*' * 60, 'white')
    cprint(__doc__, 'magenta')


class Allocator (cmd.Cmd):

    prompt = colored('Amity>>> ', 'magenta')
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room (livingspace | office) (<room_name>)..."""

        rooms = [x.upper() for x in args['<room_name>']]
        if args['livingspace']:
            room_type = 'LIVINGSPACE'
        else:
            room_type = 'OFFICE'

        Amity().create_room(room_type, rooms)

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <first_name> <last_name> (fellow| staff)"""
        person_name = args["<first_name>"].upper(
        ) + " " + args["<last_name>"].upper()
        job_type = 'FELLOW' if args['fellow'] else 'STAFF'
        if job_type == 'STAFF':
            wants_accomodation = 'NO'
        else:
            answer = input("Require accomodation?Y for Yes and N for No:")
            if answer.upper() == "Y":
                wants_accomodation = 'YES'
            else:
                wants_accomodation = 'NO'
        Amity().add_person(person_name, job_type, wants_accomodation)

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <id> <room_name> (Living | Office)"""
        person_id = args["<id>"]
        room_name = args["<room_name>"].upper()
        if args['Living']:
            room_type = "LIVINGSPACE"
        else:
            room_type = "OFFICE"
        cprint(Amity().reallocate_person(
            person_id, room_name, room_type), 'yellow')

    @docopt_cmd
    def do_load_people(self, args):
        """Usage: load_people <filename>"""
        filename = args['<filename>']
        cprint(Amity.load_people(filename), 'yellow')

    @docopt_cmd
    def do_print_allocations(self, args):
        """
        Usage: print_allocations [--output=<filename>]

        Options:
        -o, --output=<filename>  Output to file
        """
        if args['--output']:
            file_name = args['--output']
        else:
            file_name = None

        Amity.print_allocations(file_name)

    @docopt_cmd
    def do_print_unallocated(self, args):
        """
        Usage: print_unallocated [--output=<filename>]

        Options:
        -o, --output=<filename>  Output to file
        """
        if args['--output']:
            file_name = args['--output']
        else:
            file_name = None
        Amity().print_unallocated(file_name)

    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <roomname>"""
        room_name = args['<roomname>']

        Amity.print_room(room_name)

    @docopt_cmd
    def do_save_state(self, args):
        """
         Usage: save_state [--db=<db_name>]

         Options:
         -d, --dbname=<db_name>  Output to file
         """
        if args['--dbname']:
            db_name = args['--dbname']
        else:
            db_name = 'amity.db'

        cprint(Amity.save_state(db_name), 'yellow')

    @docopt_cmd
    def do_load_state(self, args):
        """Usage: load_state <db_name>"""
        db_name = args['<db_name>']
        cprint(Amity.load_state(db_name), 'yellow')

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])
if opt['--interactive']:
    os.system('clear')
    intro()
    Allocator().cmdloop()


print(opt)
