# Usage
Run `praktomat/run.sh` (simulate) or `praktomat/package.sh` (package) providing the configuration in `praktomat/config.json` the students submission in `solution/`.

# Docker
## Build
```
docker build -t pythomat:3 .
```

## Run
Run with pythomat.zip and write result to /target/solution.html

```
./docker.sh /path/to/pythomat.zip /solution/ /target/
```

## Compose
```
docker-compose run pythomat
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
