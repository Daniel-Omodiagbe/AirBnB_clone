#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """quit and EOF to exit the program
    help (this action is provided by default by
    cmd but you should keep it updated and documented
    as you work through tasks) a custom prompt: (hbnb)
    an empty line + ENTER shouldn’t execute anything"""

    prompt = 'hbnb '

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        "Quit command to exit the program"
        return sys.exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
