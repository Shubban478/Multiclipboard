# Python Multiclipboard

This is a python module that is run through the terminal or command prompt.

The clipboard contents will be saved in a json file in the same folder as the module is run from.

There is 4 different commands that can be passed as an argument:

- Save
- Load
- List
- Delete

Save stores the current contents of your clipboard.
Load will copy the selected clip to your clipboard.
List prints a list of clips available to load/delete.
Delete will delete the specified clip from the json file. 

# Instructions

Open a terminal or command prompt window.

Use the code below, followed by one of the commands.

Example: python Multiclipboard.py load

The clips will be saved with a key that you enter. Keys are used to load and delete items from the clipboard.

Notice that this module only takes 1 command at a time.

Enjoy!
