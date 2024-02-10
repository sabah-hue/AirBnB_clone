#!/usr/bin/python3
""" console module """
import cmd


class HBNBCommand(cmd.Cmd):
    """ class to interact with application"""
    prompt = "(hbnb) "

    def emptyline(self):
        """an empty line + ENTER NOT execute anything"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
