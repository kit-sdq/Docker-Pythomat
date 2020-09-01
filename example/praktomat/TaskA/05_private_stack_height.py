#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
sys.path.append("pythomat.zip")

from pythomat import analysers
from pythomat import ipo
from pythomat import interactive

tests = [
         {
         'name' : "Stack's Height",
         'description' : "The stack's height must not exceed 160 ft.",
         'arguments' : 'input.txt',
         'files' : { 'input.txt' : """40ftHC;1;1000kg;0
40ft;2;3000kg;0
40ftHC;3;2100kg;0
40ft;4;35000kg;1
40ftHC;5;2700kg;1
40ft;6;2100kg;1
40ftHC;7;35000kg;1
40ftHC;8;2700kg;1
40ft;9;2100kg;1
40ft;10;35000kg;1
40ft;11;2700kg;1
40ftHC;12;2100kg;1
40ft;13;35000kg;1
40ftHC;14;2700kg;1
40ft;15;2100kg;1
40ftHC;16;35000kg;1
40ftHC;17;2700kg;1
40ft;18;2100kg;1
40ft;19;35000kg;1
40ft;20;2700kg;1
--
0;1"""
         },
         'stdout' :  """40ftHC;1;1000kg;0
40ft;2;3000kg;0
40ftHC;3;2100kg;0
40ft;4;35000kg;1
40ftHC;5;2700kg;1
40ft;6;2100kg;1
40ftHC;7;35000kg;1
40ftHC;8;2700kg;1
40ft;9;2100kg;1
40ft;10;35000kg;1
40ft;11;2700kg;1
40ftHC;12;2100kg;1
40ft;13;35000kg;1
40ftHC;14;2700kg;1
40ft;15;2100kg;1
40ftHC;16;35000kg;1
40ftHC;17;2700kg;1
40ft;18;2100kg;1
40ft;19;35000kg;1
40ft;20;2700kg;1"""
         }
]

for test in tests:
    test['analysers'] = {
        'stdout' : analysers.ExceptionAnalyser(analysers.LineByLineAnalyser(test['stdout'])),
        'stderr' : analysers.ExceptionAnalyser()
}

success = ipo.run(sys.argv[1:], tests, description="Tests the basic functionality if the stack's height exceeds 160 ft.")
sys.exit(0 if success else 1)




