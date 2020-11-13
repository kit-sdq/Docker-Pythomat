import shutil
import subprocess
import sys

task = sys.argv[1]
targetFile = sys.argv[2]

subprocess.check_call(['python3', 'test_sample_solution.py'], cwd='praktomat/' + task)
shutil.move('praktomat/' + task + '/pythomat.zip', 'target/' + targetFile)
