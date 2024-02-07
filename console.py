#!/usr/bin/python3
""" console """


import cmd
from models.__init__ import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """our entry point to the command interpreter"""

    prompt = '(hbnb) '
    class_list = ['BaseModel']

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Overwriting the default one"""
        pass

    def do_create(self, arg):
        """Creates a new instance and stores it in JSON file"""
        args = arg.split()
        if not len(args):
            print("** class name missing **")
            return None
        try:
            new_instance = globals()[args[0]]()
        except KeyError:
            print("** class doesn't exist **")
            return None
        print("{}".format(new_instance.id))
        # instance to JSON file
        storage.new(new_instance)
        storage.save()

    def do_show(self, arg):
        """Print the string representation of an instance based on class\
and id"""
        args = arg.split()
        lenght = len(args)
        match lenght:
            case 0:
                print("** class name missing **")
                return None
            case 1:
                if args[0] not in HBNBCommand.class_list:
                    print("** class doesn't exist **")
                    return None
                print("** instance id missing **")
        key = '{}.{}'.format(args[0], args[1])
        if key not in storage.all().keys():
            print("** no instance found **")
            return None
        print(storage.all()[key])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
