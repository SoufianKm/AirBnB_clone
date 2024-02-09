#!/usr/bin/python3
""" console """


import cmd
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """our entry point to the command interpreter"""

    prompt = '(hbnb) '
    class_list = ['Base\
Model', 'User', 'City', 'Amenity', 'Place', 'State', 'Review']

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
                return None
        key = '{}.{}'.format(args[0], args[1])
        if key not in storage.all().keys():
            print("** no instance found **")
            return None
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance given a class and an id"""
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
                return None
        key = '{}.{}'.format(args[0], args[1])
        if key not in storage.all().keys():
            print("** no instance found **")
            return None
        storage.delete(key)
        storage.save()

    def do_all(self, arg):
        """prints all the instances that belong to a certain class or all\
84 the classes"""
        args = arg.split()
        lenght = len(args)
        dic = storage.all()
        start = 0
        if lenght == 0:
            print("[", end='')
            for v in dic.values():
                if start != 0:
                    print(", ", end='')
                print("\"{}\"".format(v), end='')
                start = 1
            print("]")
            return None
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return None
        print("[", end='')
        for v in dic.values():
            if start != 0:
                print(", ", end='')
            if args[0] != v.__class__:
                print("\"{}\"".format(v), end='')
            start = 1
        print("]")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        Usage: update <class name> <id> <attribute name> \"<attribute value>\"
        """
        dic = storage.all()
        args = arg.split()
        lenght = len(args)
        if lenght == 0:
            print("** class name missing **")
            return None
        if lenght >= 1:
            if args[0] not in self.class_list:
                print("** class doesn't exist **")
                return None
            if lenght == 1:
                print("** instance id missing **")
                return None
        if lenght >= 2:
            if "{}.{}".format(args[0], args[1]) not in dic.keys():
                print("** no instance found **")
                return None
            if lenght == 2:
                print("** attribute name missing **")
                return None
        if lenght == 3:
            print("** value missing **")
            return None
        instance = dic["{}.{}".format(args[0], args[1])]
        # leave id, created_at and updated_at untouched
        if args[2] in ('id', 'created_at', 'updated_at'):
            return None
        if args[2] not in instance.__dict__.keys():
            instance.__dict__[args[2]] = args[3]
        else:
            instance.__dict__[args[2]] = type(instance.__dict__[args[2]])(args[3])
        # leave storage untouched if type fails or we try to change main attrs
        if instance is None:
            return None
        storage.delete("{}.{}".format(args[0], args[1]))
        storage.new(instance)
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
