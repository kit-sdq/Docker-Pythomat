# Dockermat

For a quick test run

```shell script
python3 run.py build
python3 run.py package /path/to/pythomat/ example/praktomat/ TaskA/
python3 run.py simulate --packaged pythomat.zip example/solution/
```

For testing run

```shell script
python3 run.py simulate \
  --pythomat /path/to/pythomat/ \
  --praktomat example/praktomat/ \
  --task TaskA/ \
  example/solution/
```

## Build

Build the container image.

The image will be tagged `pythomat:3`.

## Package

Package a praktomat instance.

`TARGET` will be created or overwritten.

In the process, the file `TaskX/pythomat.zip` will be deleted.

The praktomat instance has to be configured to only use `python3` and never `python`.

The key "pythomat" must be set to "../../pythomat" in `TaskX/config.json`.

`TaskX/test_sample_solution.py` must

- import `json` and not `simplejson` and
- call `fakeomat.run(command='package', ..)`.

For an example see `example/praktomat/`.

## Simulate

Simulate a packaged Praktomat instance.

Specify either `PACKAGED` or `PYTHOMAT`, `PRAKTOMAT` and `TASK` to package temporarily.

`TARGET` will be created or overwritten.

For an example solution see `example/solution/`.

## Various
### Java compiler encoding
Update `praktomat/config.json` with something like `compiler:UTF8` in the `checkers` block.

### Checkstyle jar
- defaults to `checkstyle-teaching-1.0.jar`.
- In order to change the path of the checkstyle jar update these files:
  - `praktomat/config.json`
  - `praktomat/javalyzer.py`: `['accept', '*checkstyle-teaching.jar*']`
  - `checkstyle/checkstyle-*.py`: `jars = ['checkstyle-teaching.jar']`
