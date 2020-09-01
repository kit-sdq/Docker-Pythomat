#!/usr/bin/env python3

import subprocess
import shutil

subprocess.check_call(['python3', 'test_sample_solution.py'], cwd='praktomat/TaskA/')
shutil.move('praktomat/TaskA/pythomat.zip', 'target/pythomat.zip')
