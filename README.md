Enter in: [README-RU](./README-RU.md)

# crontab-ui

crontab-ui is a user-defined program with a graphical shell that provides the ability to work with the cron tool to automate tasks.

![main_page](assets/crontabUI.png)

![termCrontab](assets/termCrontab.png)

# Python tools

**UI: [Flet](https://flet.dev/)**

<img src="assets/fletLogo.svg" width="50">

**Flet** — is a framework that enables you to easily build real-time web, mobile, and desktop apps in your favorite language and securely share them with your team. No frontend experience is required.

---

**Tools for working with Cron: [python-crontab](https://pypi.org/project/python-crontab/#description), [croniter](https://pypi.org/project/croniter/)**

<img src="assets/pythonCrontab.svg" width="50">

**python-crontab** - Crontab module for reading and writing crontab files and accessing the system cron automatically and simply using a direct API.

**Croniter** - croniter provides iteration for the datetime object with a cron like format.

---

# Installation

```bash
git clone https://github.com/Stepan-Zhnets/crontab-ui.git
```

# Launch

To run the project, you need to run the script: `start.sh `

``` bash
bash start.sh
```

This script will run the installation of the Python UV package manager and run the project, installing the necessary dependencies.

```bash
#!/bin/bash

# UV installation
echo "Installing UV..."
curl -sSLf https://astral.sh/uv/install.sh | sh

# Checking for uv
if ! command -v uv &>/dev/null; then
    echo "Error! UV is not set."
    exit 1
fi

# Program launch
main.py echo "Launch main.py ..."
uv run main.py
```

## Types of program launch
### Desktop

``` sh
uv run flet main.py
```

``` sh
flet run main.py
```

### Web

```sh
uv run flet --web main.py
```

``` sh
flet run --web main.py
```

# Working with the program

## Creating a job

![createNewJob](assets/createNewJob.png)

## The Actions panel

![actions](assets/actions.png)

### Editing a work

![editJob](assets/editJob.png)
