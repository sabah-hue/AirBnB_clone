#!/usr/bin/python3
""" console module """
import cmd
from models.base_model import BaseModel
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
                if len(class_data) == 1:
                    print("** instance id missing **")
                else:
                    class_k = f"{class_data[0]}.{class_data[1]}"
                    if class_k in models.storage.all():
                        print(models.storage.all()[class_k])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, data):
        if data:
            my_data = data.split()
            if my_data[0] in self.model_name:
                if len(my_data) == 1:
                    print("** instance id missing **")
                else:
                    class_k = f"{my_data[0]}.{my_data[1]}"
                    if class_k in models.storage.all():
                        del models.storage.all()[class_k]
                        models.storage.save
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, data):
        """ Prints all string representation based on class name """
        if data:
            my_data = data.split()
            if my_data[0] not in self.model_name:
                print("** class doesn't exist **")
            else:
                my_class =  models.storage.all()
                my_list = []
                for value in my_class.values():
                    if value.__class__.__name__ == data:
                        my_list.append(str(value))
                print(my_list)
        else:
            all_class = models.storage.all()
            my_list = []
            for value in all_class.values():
                my_list.append(str(value))
            print(my_list)

    def do_update(self, data):
        """ Updates an instance based on the class name and id """
        if data:
            my_data = data.split()
            if my_data[0] not in self.model_name:
                print("** class doesn't exist **")
                return
            if len(my_data) == 1:
                print("** instance id missing **")
                return
            class_k = f"{my_data[0]}.{my_data[1]}"
            if class_k not in models.storage.all():
                print("** no instance found **")
                return
            else:
                if len(my_data) == 2:
                    print("** attribute name missing **")
                    return
                else:
                    if len(data.split('"')) == 1:
                        print("** value missing **")
                        return
                    my_attr = my_data[2]
                    x = models.storage.all()
                    new = data.split('"')
                    my_attr_value = getattr(x[class_k], my_attr)
                    setattr(x[class_k], my_attr, new[1])
                    storage.save()
        else:
            print("** class name missing **")

    def do_EOF(self, data):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
