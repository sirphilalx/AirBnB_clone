#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
"""
    HBNBCommand is a simple command-line interface (CLI) using the 'cmd' module.

    Attributes:
        prompt (str): The command prompt displayed to the user.

    Methods:
        do_EOF(self, line): Handles the EOF (End of File) command.

    Example Usage:
        >>> HBNBCommand().cmdloop()
    """


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

    def do_EOF(self, line):
        """
        Handles the EOF (End of File) command.

        Args:
            line (str): The input line passed to the method.

        Returns:
            bool: True to indicate that the program should exit.

        Example Usage:
            >>> do_EOF('exit')
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def default(self, line):
        print('default({})'.format(line))
        return cmd.Cmd.default(self, line)

    def emptyline(self):
        return cmd.Cmd.emptyline(self)

    def do_create(self, arg):
        """ Create a new instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        # new = None
        if arg:
            arg_list = arg.split()
            if len(arg_list) == 1:
                if arg in self.classes.keys():
                    new = self.classes[arg]()
                    new.save()
                    print(new.id)
                else:
                    print("** class doesn't exist **")
        # if len(arg) == 0:
        #     print("** class name missing **")
        #     return
        # elif arg not in self.classes:
        #     print("** class doesn't exist **")
        #     return
        # new = eval(arg)()
        # print(new.id)
        # new.save()

    def do_show(self, arg):
        """ Method to print instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                i = storage.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """ Method to delete instance with class and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """ Method to print all instances """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_update(self, arg):
        """ Method to update JSON file"""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')


if __name__ == "__main__":
    HBNBCommand().cmdloop()
