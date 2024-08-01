import os
with open(os.path.dirname('Main.py') + '\\Settings.json', 'r') as settings:
    settings = settings
    with open(os.path.dirname(__file__) + f'\\{settings.read('Theme')}', 'r') as theme:
        theme = theme.read
        ...