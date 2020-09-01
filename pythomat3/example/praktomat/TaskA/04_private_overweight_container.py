#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
sys.path.append("pythomat.zip")

from pythomat import analysers
from pythomat import ipo
from pythomat import interactive

tests = [
         {
         'name' : "Overweight Container - 40 ft",
         'description' : "One of the containers is overweight. Moving the overweight container on the top of second stack. All of the containers are 40 ft.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ft;13;1000kg;0
40ft;41;3000kg;1
40ft;4;35000kg;1
40ft;55;2700kg;2
40ft;63;2100kg;2
--
1;2"""
         },
         'stdout' :  """40ft;13;1000kg;0
40ft;41;3000kg;1
40ft;4;35000kg;1
40ft;55;2700kg;2
40ft;63;2100kg;2"""
         },
         {
         'name' : "Overweight Container - 40 ft",
         'description' : "One of the containers is overweight. Moving the overweight container on the top of second stack. All of the containers are 40 ft.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ft;13;1000kg;0
40ft;41;3000kg;1
40ft;4;35000kg;1
40ft;55;2700kg;2
40ft;63;2100kg;2
--
1;2
2;0"""
         },
         'stdout' :  """40ft;13;1000kg;0
             40ft;63;2100kg;0
             40ft;41;3000kg;1
             40ft;4;35000kg;1
             40ft;55;2700kg;2"""
         },
         {
         'name' : "Overweight Container - 40 ftHC",
         'description' : "The second container 55 is overweight. Moving the overweight container on the top of second stack. All of the containers are 40 ftHC.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ftHC;13;1000kg;0
40ftHC;41;3000kg;1
40ftHC;4;35000kg;1
40ftHC;55;2700kg;2
40ftHC;63;2100kg;2
--
1;2"""
         },
         'stdout' :  """40ftHC;13;1000kg;0
             40ftHC;41;3000kg;1
             40ftHC;4;35000kg;1
             40ftHC;55;2700kg;2
             40ftHC;63;2100kg;2"""
         },
         {
         'name' : "Overweight Container - 40 ftHC",
         'description' : "The second container 55 is overweight. Moving the overweight container on the top of second stack. All of the containers are 40 ftHC.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ftHC;13;1000kg;0
40ftHC;41;3000kg;1
40ftHC;4;35000kg;1
40ftHC;55;2700kg;2
40ftHC;63;2100kg;2
--
1;2
2;0"""
         },
         'stdout' :  """40ftHC;13;1000kg;0
             40ftHC;63;2100kg;0
             40ftHC;41;3000kg;1
             40ftHC;4;35000kg;1
             40ftHC;55;2700kg;2"""
         }
]

for test in tests:
    test['analysers'] = {
        'stdout' : analysers.ExceptionAnalyser(analysers.LineByLineAnalyser(test['stdout'])),
        'stderr' : analysers.ExceptionAnalyser()
}

success = ipo.run(sys.argv[1:], tests, description="Tests the basic functionality if one of the container is overweight.")
sys.exit(0 if success else 1)




