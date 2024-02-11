#!/usr/bin/python3
""" console module """
import cmd
from  models.base_model import BaseModel
import models
import sys


class HBNBCommand(cmd.Cmd):
    """ class to interact with application"""
    model_name = {'BaseModel': BaseModel}
    prompt = "(hbnb) "

    def emptyline(self):
        """an empty line + ENTER NOT execute anything"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """ create new instance of basemodel """
        if arg:
            if arg in self.model_name:
                current_class = eval(arg)()
                current_class.save()
                print(current_class.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
