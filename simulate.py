import subprocess
import sys

targetFile = sys.argv[1]

subprocess.check_call(['python3', 'pythomat.zip', 'solution/', '-o', 'target/' + targetFile])
