#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
sys.path.append("pythomat.zip")

from pythomat import analysers
from pythomat import ipo
from pythomat import interactive

tests = [
    {
        'name' : "Assignment sheet example",
        'description' : "Checks, if the program can simulate a container mover.",
        'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ft;100;20000kg;0
40ftHC;200;30000kg;0
40ft;300;22000kg;1
40ft;400;19000kg;1
40ft;500;20000kg;1
40ft;600;22000kg;2
40ftHC;700;28000kg;3
--
2;0
3;2"""
         },
         'stdout' :  """40ft;100;20000kg;0
             40ftHC;200;30000kg;0
             40ft;600;22000kg;0
             40ft;300;22000kg;1
             40ft;400;19000kg;1
             40ft;500;20000kg;1
             40ftHC;700;28000kg;2"""
    },
]

for test in tests:
    test['analysers'] = {
        'stdout' : analysers.ExceptionAnalyser(analysers.LineByLineAnalyser(test['stdout'])),
        'stderr' : analysers.ExceptionAnalyser()
}

success = ipo.run(sys.argv[1:], tests)
sys.exit(0 if success else 1)




