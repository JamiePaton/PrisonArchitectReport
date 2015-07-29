# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 19:27:44 2015

@author: Jamie
"""
TITLE = 'Prison Architect Savegame Parser'
VERSION = '0.0.1'
AUTHOR = 'Jamie E Paton'
TEST = 0

import sys
import logging
import logging.config
import unittest
import hypothesis as hs
import os
import json
import pyparsing


def setup_logging(default_path='logs/loggingconfig.json', default_level=logging.INFO,
                  env_key='LOG_CFG'):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def imports():
    import types
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            yield val.__name__

def read_file(savegame):
    with open(savegame) as prison:
        data = prison.read()
    return data

class SaveGame(object):
    """
        Represents a Prison Architect savegame
        d = {key: value for (key, value) in iterable}
    """
    def __init__(self, filename):
        self.data = SaveGame.read_file(filename).split('\n')
#        self.settings = [" ".join(line.split()).split() for line in self.data[1:22]]
        self.settings = {entry[0]: entry[1] for entry in
                        [" ".join(line.split()).split() for line in self.data[1:22]]}

    @staticmethod
    def read_file(filename):
        with open(filename) as prison:
            data = prison.read()
        return data

def main(args):
#    prison_data = read_file('testing1.prison').split('\n')
#    body = '\n'.join(prison_data[22:])
#    bodylist = pyparsing.nestedExpr('BEGIN', 'END').parseString(body).asList()
#    print 'done'
    import pprint
#    
#    pprint.pprint(bodylist)

    s = SaveGame('testing1.prison')
    pprint.pprint(s.settings)

class Testing(unittest.TestCase):
    """
    
    Methods
    -------
    
    
    Notes
    -----
    @given(parameter=hs.strategies.integers())
    
    def test_something(parameter):
        assert type(parameter) == int
    """


if __name__ == '__main__':
    setup_logging(default_level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info(''.join([TITLE, ' v', VERSION, ' ', AUTHOR]))
    logger.debug('Imported modules:\n\n\t' + '\n\t'.join(list(imports())))
    sys.exit(main(sys.argv))

