#!/usr/bin/python
import os
from optparse import OptionParser

def process(dirs, command, all):
    verbs = {'status': 'Checking', 'pull': 'Pulling', 'push': 'Pushing'}
    verb = verbs[command]

    if all:
        dirs = [d for d in os.listdir('.')]
    for d in dirs:
        if os.path.exists('%s/.git'%d):
            print '%s %s\n%s\n'%(verb,d,'*'*(len(d)+len(verb)+1))
            results = os.popen('cd %s && git %s && cd ..'%(d,command)).read()
            print results


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-c", "--command", action='store', dest="command",
                                    help="action for git", default='status')
    parser.add_option("-a", "--all",
                      action="store_true", dest="all", default=False,
                      help="process all dirs")

    (options, args) = parser.parse_args()
    process(args, options.command, options.all)




