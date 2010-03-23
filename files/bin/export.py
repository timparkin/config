#!/usr/bin/python
import os
from optparse import OptionParser

def process(dirs, all):
    export = 'export PYTHONPATH=$PYTHONPATH'
    if all:
        dirs = [d for d in os.listdir('.')]
    for d in dirs:
        if os.path.exists('%s/.git'%d):
            #results = os.popen('cd %s && git %s && cd ..'%(d,command)).read()
            export += ':%s'%os.path.abspath(d)
    print export
            



if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-a", "--all",
                      action="store_true", dest="all", default=False,
                      help="process all dirs")

    (options, args) = parser.parse_args()
    process(args, options.all)




