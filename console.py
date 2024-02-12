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

    def do_quit(self, data):
        """Quit command to exit the program"""
        return True

    def do_create(self, data):
        """ create new instance of basemodel """
        if data:
            if data in self.model_name:
                current_class = eval(data)()
                current_class.save()
                print(current_class.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, data):
        """ show data of input class """
        if data:
            class_data = data.split(' ')
            if class_data[0] in self.model_name:
                if len(class_data) > 2:
                    class_k = f"{class_data[0]}.{class_data[1]}"
                    if class_k in models.storage.all():
                        print("** no instance found **")
                    else:
                        print(storage.all()[class_k])
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_EOF(self, data):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
