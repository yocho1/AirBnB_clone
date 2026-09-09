#!/usr/bin/python3
"""Command interpreter for AirBnB clone"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB objects"""

    prompt = "(hbnb) "
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_help(self, arg):
        """Show available commands"""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        new_obj = self.__classes[class_name]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Show an instance by class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """Delete an instance by class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, arg):
        """Show all instances, or all of a specific class"""
        all_objs = storage.all()
        if not arg:
            print([str(obj) for obj in all_objs.values()])
            return
        class_name = arg.split()[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        filtered = [str(obj) for obj in all_objs.values()
                    if obj.__class__.__name__ == class_name]
        print(filtered)

    def do_update(self, arg):
        """Update an attribute of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = " ".join(args[3:])
        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]
        elif attr_value.startswith("'") and attr_value.endswith("'"):
            attr_value = attr_value[1:-1]
        try:
            if '.' in attr_value:
                attr_value = float(attr_value)
            else:
                attr_value = int(attr_value)
        except ValueError:
            pass
        obj = all_objs[key]
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
