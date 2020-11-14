#!/usr/bin/env python
import sys
import json

with open("config.json") as json_file:
    config = json.load(json_file)

sys.path.append(config["pythomat"])
import fakeomat # noqa

fakeomat.run(
    command="package",
    submission=str(config["sample_solution"]),
    checkers=config["checkers"]
)
