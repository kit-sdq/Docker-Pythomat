# Usage
Run `praktomat/run.sh` (simulate) or `praktomat/package.sh` (package) providing the configuration in `praktomat/config.json` the students submission in `solution/`.

# Docker
## Build
```
cd programmieren-metatutor/pythomat3
docker build -t pythomat:3 -f usage/Dockerfile .
```

## Run
```
cd programmieren-metatutor/pythomat3/usage
./docker.sh /path/to/solution /target/path
```

# Dependencies
- JDK 8 or later
- Python 3.x with `python3` in path

# Java compiler encoding
Update `praktomat/config.json` with something like `compiler:UTF8` in the `checkers` block.

# Checkstyle jar
- defaults to `checkstyle-teaching-1.0.jar`.
- In order to change the path of the checkstyle jar update these files:
  - `praktomat/config.json`
  - `praktomat/javalyzer.py`: `['accept', '*checkstyle-teaching.jar*']`
  - `checkstyle/checkstyle-*.py`: `jars = ['checkstyle-teaching.jar']`
