#!/usr/bin/env python3

import argparse
import os
import subprocess
from os.path import abspath
from types import SimpleNamespace

parser = argparse.ArgumentParser()

parser.add_argument(
    '--docker', type=str, default='docker',
    help='use other command instead of `docker`'
)

parser.add_argument(
    '--podman', action='store_const', dest='docker', const='podman',
    help='use `podman` instead of `docker`'
)

subparsers = parser.add_subparsers()


def build(args):
    if not os.path.exists('Dockerfile'):
        raise Exception('Missing `Dockerfile`')

    subprocess.check_call([args.docker, 'build', '-t', 'pythomat:3', '.'])


build_parser = subparsers.add_parser(
    'build',
    description='Build the container image.\n\n'
                'The image will be tagged `pythomat:3`.',
    formatter_class=argparse.RawTextHelpFormatter
)

build_parser.set_defaults(command=build)


def read_delete_write(path):
    with open(path, 'rb') as file:
        content = file.read()

    os.remove(path)

    with open(path, 'wb') as file:
        file.write(content)


def package(args):
    if not os.path.exists('package.py'):
        raise Exception('Missing `package.py`')

    pythomat = abspath(args.pythomat)
    praktomat = abspath(args.praktomat)
    task = args.task
    target = abspath(args.target)

    target_dir, target_file = os.path.split(target)

    if not target_file.endswith('.zip'):
        raise Exception('Target file must have extension `.zip`.')

    subprocess.check_call([
        args.docker, 'run', '-it',
        '-v', abspath('package.py') + ':/prod/package.py',
        '-v', pythomat + ':/prod/pythomat/',
        '-v', praktomat + ':/prod/praktomat/',
        '-v', target_dir + ':/prod/target/',
        'pythomat:3',
        'python3', 'package.py', task, target_file
    ])

    read_delete_write(target)


package_parser = subparsers.add_parser(
    'package',
    description='Package a praktomat instance.\n\n'
                'TARGET will be created or overwritten.\n'
                'In the process, the file `TaskA/pythomat.zip` will be deleted.\n\n'
                'The praktomat instance has to\n'
                '- contain a task `TaskA/` (TODO) and\n'
                '- be configured to only use `python3` and never `python`.\n\n'
                'The key "pythomat" must be set to "../../pythomat" in `TaskA/config.json`.\n\n'
                '`TaskA/test_sample_solution.py` must\n'
                '- import `json` and not `simplejson` and\n'
                '- call `fakeomat.run(command=\'package\', ..)`.\n\n'
                'For an example see `example/praktomat/`.',
    formatter_class=argparse.RawTextHelpFormatter
)

package_parser.add_argument(
    'pythomat', type=str,
    help='Pythomat path'
)

package_parser.add_argument(
    'praktomat', type=str,
    help='Praktomat instance path'
)

package_parser.add_argument(
    'task', type=str,
    help='Praktomat task'
)

package_parser.add_argument(
    '--target', type=str, default='pythomat.zip',
    help='use other target file than pythomat.zip'
)

package_parser.set_defaults(command=package)


def simulate(args):
    if not os.path.exists('simulate.py'):
        raise Exception('Missing `simulate.py`.')

    if args.pythomat and args.praktomat and args.task:
        package_target = abspath('pythomat.temp.zip')
        package_args = SimpleNamespace()
        package_args.docker = args.docker
        package_args.pythomat = args.pythomat
        package_args.praktomat = args.praktomat
        package_args.task = args.task
        package_args.target = package_target
        package(package_args)
        packaged = package_target
    elif args.packaged:
        package_target = None
        packaged = abspath(args.packaged)
    else:
        raise Exception('Specify either PACKAGED or PYTHOMAT, PRAKTOMAT and TASK.')

    solution = abspath(args.solution)
    target = abspath(args.target)

    target_dir, target_file = os.path.split(target)

    if not target_file.endswith('.html'):
        raise Exception('Target file must have extension `.html`.')

    subprocess.check_call([
        args.docker, 'run', '-it',
        '-v', abspath('simulate.py') + ':/prod/simulate.py',
        '-v', packaged + ':/prod/pythomat.zip',
        '-v', solution + ':/prod/solution/',
        '-v', target_dir + ':/prod/target/',
        'pythomat:3',
        'python3', 'simulate.py', target_file
    ])

    if package_target:
        os.remove(package_target)

    read_delete_write(target)


simulate_parser = subparsers.add_parser(
    'simulate',
    description='Simulate a packaged Praktomat instance.\n\n'
                'Specify either PACKAGED or PYTHOMAT, PRAKTOMAT and TASK to package temporarily.\n\n'
                'TARGET will be created or overwritten.\n\n'
                'For an example solution see `example/solution/`.',
    formatter_class=argparse.RawTextHelpFormatter
)

simulate_parser.add_argument(
    '--packaged', type=str, default=None,
    help='Packaged Pythomat (`pythomat.zip`) path'
)

simulate_parser.add_argument(
    '--pythomat', type=str, default=None,
    help='Pythomat path'
)

simulate_parser.add_argument(
    '--praktomat', type=str, default=None,
    help='Praktomat instance path'
)

simulate_parser.add_argument(
    '--task', type=str, default=None,
    help='Praktomat task'
)

simulate_parser.add_argument(
    'solution', type=str,
    help='Solution path'
)

simulate_parser.add_argument(
    '--target', type=str, default='out.html',
    help='use other target file than `out.html`'
)

simulate_parser.set_defaults(command=simulate)


def main():
    args = parser.parse_args()
    args.command(args)


if __name__ == '__main__':
    main()
