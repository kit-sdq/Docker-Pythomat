# Usage
Run `praktomat/test_sample_solution.sh` providing the configuration in `praktomat/config.json` the students submission in `solution/`.

# Docker
Build and run a docker image like this:
```
cd programmieren-metatutor/pythomat3
docker build -t pythomat:3 -f usage/Dockerfile .
docker run pythomat:3 >> out.html
<browser> out.html
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
