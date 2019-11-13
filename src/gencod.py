import sys
from tool_checks import check_app_file
from tool_writers import write_project_folder

ACTIONS = ['init', 'build']

if len(sys.argv) != 3:
    print('Expecting exactly two arguments')
    print('Usage: gencod.py [init|build] <folder>')
    print('Exiting')
    sys.exit(1)
else:
    dir = sys.argv[2]

app_settings = check_app_file(dir)

if not app_settings:
    print('Exiting')
    sys.exit(1)
else:
    print('App file is here and contains expected entries')


if sys.argv[1] == 'init':
    write_project_folder(app_settings['rootFolder'], app_settings['project'])
elif sys.argv[1] == 'build':
    print('Builing source files')
else:
    print(f'Actions should be one of the following: {ACTIONS}')
    print('Exiting')
    sys.exit(1)