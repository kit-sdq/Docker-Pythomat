#!/usr/bin/env python

import json as simplejson
with open("config.json") as json_file:
  config = simplejson.load(json_file)

import sys
sys.path.append(config["pythomat"])

import fakeomat
fakeomat.run(
  command = "package",
    submission = str(config["sample_solution"]),
    checkers = config["checkers"]
)
