#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """quit and EOF to exit the program
    help (this action is provided by default by
    cmd but you should keep it updated and documented
    as you work through tasks) a custom prompt: (hbnb)
    an empty line + ENTER shouldn’t execute anything"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        "Quit command to exit the program"
        return sys.exit()

    def do_create(self, class_name):
        """create new instances of BaseModel"""
        if not class_name:
            print("** class name missing **")
        elif class_name != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            storage.new(new_instance)
            storage.save
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                del(objects[key])
                storage.save

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name"""
        dict_all = []
        if line:
            class_name = line.strip()
            if class_name != "BaseModel":
                print("** class doesn't exist **")
                return
            else:
                objects = storage.all()
                for key, val in objects.items():
                    if key.startswith(f"{class_name}."):
                        dict_all.append(str(val))
        else:
            objects = storage.all()
            for val in objects.values():
                dict_all.append(str(val))
                dict_all.append(str(val))
                dict_all
        print(dict_all)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        if line:
            args = line.split()
            if not args:
                print("** class name missing **")
            elif args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) >= 2:
                key = "{}.{}".format(args[0], args[1])
                objects = storage.all()
                if key not in objects:
                    print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                objects = storage.all()
                objects[key][args[2]] = args[3]
                storage.save



if __name__ == '__main__':
    HBNBCommand().cmdloop()
