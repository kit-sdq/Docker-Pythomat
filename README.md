# Containerized Pythomat
For a quick test run:
```shell script
python3 run.py build
python3 run.py package /path/to/pythomat/ example/praktomat/
python3 run.py simulate pythomat.zip example/solution/
```

Call `--help` on `run.py` or one of its subcommands for extended help.

You can make `run.py` executable to run it without `python3`.

## Various
### Java compiler encoding
Update `praktomat/config.json` with something like `compiler:UTF8` in the `checkers` block.

### Checkstyle jar
- defaults to `checkstyle-teaching-1.0.jar`.
- In order to change the path of the checkstyle jar update these files:
  - `praktomat/config.json`
  - `praktomat/javalyzer.py`: `['accept', '*checkstyle-teaching.jar*']`
  - `checkstyle/checkstyle-*.py`: `jars = ['checkstyle-teaching.jar']`
