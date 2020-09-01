#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
sys.path.append("pythomat.zip")

from pythomat import analysers
from pythomat import ipo
from pythomat import interactive

tests = [
         {
         'name' : "Moving more than one container - 40 ftHC",
         'description' : "Stacking containers on the top of other stacks. All of the containers are 40 ft.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ft;13;1000kg;0
40ft;31;11000kg;0
40ft;41;3000kg;1
40ft;4;29000kg;1
40ft;55;2700kg;2
40ft;63;2100kg;2
--
1;2
0;1"""
         },
         'stdout' :  """40ft;13;1000kg;0
40ft;41;3000kg;1
40ft;31;11000kg;1
40ft;55;2700kg;2
40ft;63;2100kg;2
40ft;4;29000kg;2"""
         },
         {
         'name' : "Moving the same container - 40 ft",
         'description' : "Moving a container on the top of other stacks and back again. All of the containers are 40 ft.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ft;13;1000kg;0
40ft;31;11000kg;0
40ft;41;3000kg;1
40ft;4;29000kg;1
40ft;55;2700kg;2
40ft;63;2100kg;2
--
1;0
0;1"""
         },
         'stdout' :  """40ft;13;1000kg;0
40ft;31;11000kg;0
40ft;41;3000kg;1
40ft;4;29000kg;1
40ft;55;2700kg;2
40ft;63;2100kg;2"""
         },
         {
         'name' : "Moving more than one container - 40 ftHC",
         'description' : "Stacking containers on the top of other stacks. All of the containers are 40 ftHC.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ftHC;13;1000kg;0
40ftHC;31;11000kg;0
40ftHC;41;3000kg;1
40ftHC;4;29000kg;1
40ftHC;55;2700kg;2
40ftHC;63;2100kg;2
--
1;2
0;1"""
         },
         'stdout' :  """40ftHC;13;1000kg;0
40ftHC;41;3000kg;1
40ftHC;31;11000kg;1
40ftHC;55;2700kg;2
40ftHC;63;2100kg;2
40ftHC;4;29000kg;2"""
         },
         {
         'name' : "Moving the same container - 40 ftHC",
         'description' : "Moving a container on the top of other stacks and back again. All of the containers are 40 ftHC.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ftHC;13;1000kg;0
40ftHC;31;11000kg;0
40ftHC;41;3000kg;1
40ftHC;4;29000kg;1
40ftHC;55;2700kg;2
40ftHC;63;2100kg;2
--
1;0
0;1"""
         },
         'stdout' :  """40ftHC;13;1000kg;0
40ftHC;31;11000kg;0
40ftHC;41;3000kg;1
40ftHC;4;29000kg;1
40ftHC;55;2700kg;2
40ftHC;63;2100kg;2"""
         },
         {
         'name' : "Moving containers - 40 ft and 40 ftHC",
         'description' : "Moving containers. The containers are 40 ft and 40 ftHC.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ftHC;13;1000kg;0
40ft;31;11000kg;0
40ftHC;41;3000kg;1
40ftHC;4;29000kg;1
40ft;55;2700kg;2
40ftHC;63;2100kg;2
--
1;2
0;1"""
         },
         'stdout' :  """40ftHC;13;1000kg;0
             40ftHC;41;3000kg;1
             40ft;31;11000kg;1
             40ft;55;2700kg;2
             40ftHC;63;2100kg;2
             40ftHC;4;29000kg;2"""
         }
]

for test in tests:
    test['analysers'] = {
        'stdout' : analysers.ExceptionAnalyser(analysers.LineByLineAnalyser(test['stdout'])),
        'stderr' : analysers.ExceptionAnalyser()
}

success = ipo.run(sys.argv[1:], tests, description="Tests the basic functionality.")
sys.exit(0 if success else 1)




