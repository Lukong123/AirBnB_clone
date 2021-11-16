#!/usr/bin/python3
"""Command line"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Simple HBNBCommand"""
    prompt = '(hbnb)'

    def do_EOF(self,arg):
        """End of file"""
        return True

    def emptyline(self):
        """empyty line"""
        return False

    def do_quit(self,arg):
        """do quit"""
        return True

    def do_help(self, arg: str):
        """do help"""
        print("helping you get along")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
