#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
sys.path.append("pythomat.zip")

from pythomat import javalyzer

filenames = [
    ["reject", "Terminal.java", "Please don't upload the Terminal class."],
    ['reject', "*.class", "Please don't upload compiled *.class-files. They are of no use for us. Do only submit readable Java source code (*.java)."],
    ['accept', "*.java"],
    ['accept', "*javalyzer.py"],
    ['accept', "*checkstyle-teaching-1.0.jar"],
    ['accept', "*checkstyle-optional.py"],
    ['accept', "*checkstyle-required.py"],
    ['reject', "*", "Please don't upload any file other than *.java."]
]

packages = [
    ['reject', "edu.kit.informatik._intern.*"],
    ['accept', '*']
]

imports = [
    ['reject', "edu.kit.informatik._intern.*"],
    ['accept', "java.lang.*"],
    ['accept', "java.util"],
    ['accept', "java.util.*"],
    ['accept', "java.util.regex"],
    ['accept', "java.util.regex.*"],
    ['accept', "java.util.function"],
    ['accept', "java.util.function.*"],
    ['reject', '*']
]

classes = [
    ['reject', "edu.kit.informatik.Terminal", "Please don't upload the Terminal class."],
    ['reject', "*Terminal", "Please don't upload the Terminal class and leave it in edu.kit.informatik."],
    ['accept', "*.*"],
    ['reject', "*", "Please do not use the default package."]
]

methods = [
    ['accept', '*']
]

success = javalyzer.run(
        sys.argv[1:],
        filenames=filenames,
        packages=packages,
        imports=imports,
        classes=classes,
        methods=methods
)

sys.exit(0 if success else 1)
