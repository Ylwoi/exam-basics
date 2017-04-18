# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination


import sys


class Copy(object):
    def __init__(self):
        self.args = sys.argv
        if len(self.args) == 1:
            print("Enter after the file name: copy [source] [destination]")
        else:
            self.command = sys.argv[1:]
            if len(self.command) < 2:
                print('No destination provided')


copy = Copy()