import shutil
import subprocess
import sys

targetFile = sys.argv[1]

subprocess.check_call(['python3', 'test_sample_solution.py'], cwd='praktomat/TaskA/')
shutil.move('praktomat/TaskA/pythomat.zip', 'target/' + targetFile)
