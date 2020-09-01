#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
sys.path.append("pythomat.zip")

from pythomat import analysers
from pythomat import ipo
from pythomat import interactive

tests = [
    {
        'name' : "Empty stack - 40 ft",
        'description' : "The first stack become empty. All of the containers are 40 ft.",
        'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ft;13;1000kg;0
40ft;4;3000kg;1
40ft;55;2700kg;2
--
0;1"""
         },
         'stdout' :  """40ft;4;3000kg;1
40ft;13;1000kg;1
40ft;55;2700kg;2"""
    },
         {
         'name' : "Empty stack - 40 ft",
         'description' : "The second stack become empty. All of the containers are 40 ft.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ft;13;1000kg;0
40ft;4;3000kg;1
40ft;55;2700kg;2
--
1;2"""
         },
         'stdout' :  """40ft;13;1000kg;0
40ft;55;2700kg;2
40ft;4;3000kg;2"""
         },
         {
         'name' : "Empty stack - 40 ft",
         'description' : "The last stack become empty. All of the containers are 40 ft.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ft;13;1000kg;0
40ft;4;3000kg;1
40ft;55;2700kg;2
--
2;1"""
         },
         'stdout' :  """40ft;13;1000kg;0
40ft;4;3000kg;1
40ft;55;2700kg;1"""
         },
         {
         'name' : "Empty stack - 40 ftHC",
         'description' : "The first stack become empty. All of the containers are 40 ftHC.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ftHC;13;1000kg;0
40ftHC;4;3000kg;1
40ftHC;55;2700kg;2
--
0;1"""
         },
         'stdout' :  """40ftHC;4;3000kg;1
40ftHC;13;1000kg;1
40ftHC;55;2700kg;2"""
         },
         {
         'name' : "Empty stack - 40 ftHC",
         'description' : "The second stack become empty. All of the containers are 40 ftHC.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ftHC;13;1000kg;0
40ftHC;4;3000kg;1
40ftHC;55;2700kg;2
--
1;2"""
         },
         'stdout' :  """40ftHC;13;1000kg;0
40ftHC;55;2700kg;2
40ftHC;4;3000kg;2"""
         },
         {
         'name' : "Empty stack - 40 ftHC",
         'description' : "The last stack become empty. All of the containers are 40 ftHC.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ftHC;13;1000kg;0
40ftHC;4;3000kg;1
40ftHC;55;2700kg;2
--
2;1"""
         },
         'stdout' :  """40ftHC;13;1000kg;0
40ftHC;4;3000kg;1
40ftHC;55;2700kg;1"""
         }
]

for test in tests:
    test['analysers'] = {
        'stdout' : analysers.ExceptionAnalyser(analysers.LineByLineAnalyser(test['stdout'])),
        'stderr' : analysers.ExceptionAnalyser()
}

success = ipo.run(sys.argv[1:], tests, description="Tests the basic functionality if one of the stacks become empty.")
sys.exit(0 if success else 1)




