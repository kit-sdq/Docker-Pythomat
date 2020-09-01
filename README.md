# Pythomat 3
For a quick test run:
```shell script
cd /pythomat3/usage/
./run.py build
./run.py package example/praktomat/
./run.py simulate pythomat.zip example/solution/
```

## Build
```shell script
./run.py build
```

### Effects
Builds a Docker image `pythomat:3`.

## Package
```shell script
./run.py package PRAKTOMAT [TARGET]
```
- `PRAKTOMAT` - path of a praktomat directory (see `example/praktomat/` based on `WS1920/Blatt 4/TaskA/` for an example).
- `TARGET` - path of a target directory. Defaults to current directory.

### Requirements
The praktomat directory must
- contain a directory `TaskA/` (TODO) and
- be configured to only use `python3` and never `python`.

The key `"pythomat"` must be set to `"../../pythomat"` in `TaskA/config.json`.

`TaskA/test_sample_solution.py` must
- import `json` and not `simplejson`
- set the argument `command = 'package'` in `fakeomat.run(..).`

### Effects
The file `TARGET/pythomat.zip` will be created or overridden.
In the process, the file `TaskA/pythomat.zip` will be deleted.

## Simulate
```shell script
./run.py simulate PYTHOMAT SOLUTION [TARGET]
```
- `PYTHOMAT` - path of `pythomat.zip`.
- `SOLUTION` - path of a solution directory (see `example/solution/` for an example).
- `TARGET` - path of a target directory. Defaults to current directory.

### Effects
The file `TARGET/out.html` will be created or overridden.

## Various
### Java compiler encoding
Update `praktomat/config.json` with something like `compiler:UTF8` in the `checkers` block.

### Checkstyle jar
- defaults to `checkstyle-teaching-1.0.jar`.
- In order to change the path of the checkstyle jar update these files:
  - `praktomat/config.json`
  - `praktomat/javalyzer.py`: `['accept', '*checkstyle-teaching.jar*']`
  - `checkstyle/checkstyle-*.py`: `jars = ['checkstyle-teaching.jar']`
