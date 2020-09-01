#!/usr/bin/env python3

import os
import subprocess
import sys
from os import path


def build(args):
    if not path.exists('Dockerfile'):
        print('Missing Dockerfile')
        exit(-1)

    if args:
        print('Usage: ./run.py build')
        exit(-1)

    subprocess.check_call(['docker', 'build', '-t', 'pythomat:3', '.'])


def recreate(_path):
    with open(_path, 'rb') as file:
        content = file.read()

    os.remove(_path)

    with open(_path, 'wb') as file:
        file.write(content)


def package(args):
    if not path.exists('package.py'):
        print('Missing package.py')
        exit(-1)

    if len(args) not in range(1, 3):
        print('Usage: ./run.py package PRAKTOMAT [TARGET]')
        exit(-1)

    praktomat = args[0]

    if len(args) == 2:
        target = args[1]
    else:
        target = os.getcwd()

    subprocess.check_call([
        'docker', 'run', '-it',
        '-v', path.abspath('package.py') + ':/prod/run.py',
        '-v', path.abspath('../../pythomat3') + ':/prod/pythomat/',
        '-v', path.abspath(praktomat) + ':/prod/praktomat/',
        '-v', path.abspath(target) + ':/prod/target/',
        'pythomat:3'
    ])

    recreate(path.join(target, 'pythomat.zip'))


def simulate(args):
    if not path.exists('simulate.py'):
        print('Missing simulate.py')
        exit(-1)

    if len(args) not in range(2, 4):
        print('Usage: ./run.py simulate PYTHOMAT SOLUTION [TARGET]')
        exit(-1)

    pythomat = args[0]
    solution = args[1]

    if len(args) == 3:
        target = args[2]
    else:
        target = os.getcwd()

    subprocess.check_call([
        'docker', 'run', '-it',
        '-v', path.abspath('simulate.py') + ':/prod/run.py',
        '-v', path.abspath(pythomat) + ':/prod/pythomat.zip',
        '-v', path.abspath(solution) + ':/prod/solution/',
        '-v', path.abspath(target) + ':/prod/target/',
        'pythomat:3'
    ])

    recreate(path.join(target, 'out.html'))


def main(args):
    if not args:
        print('Usage: ./run.py build | package | simulate')
        exit(-1)
    else:
        command = args[0]
        args = args[1:]

        if command == 'build':
            build(args)
        elif command == 'simulate':
            simulate(args)
        elif command == 'package':
            package(args)
        else:
            print('Unknown command:', command)
            exit(-1)


if __name__ == '__main__':
    main(sys.argv[1:])
