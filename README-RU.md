Пеерйти в: [README-EN](./README.md)

# crontab-ui

crontab-ui - это пользовательская программа с графической оболочкой, предоставляющая возможность работы с инструментом cron для автоматизации задач.

# Установка

``` bash
git clone https://github.com/Stepan-Zhnets/crontab-ui.git
```

# Запуск

Чтобы запустить проект, вам необходимо запустить скрипт: `start.sh`

Этот скрипт запустит установку менеджера пакетов Python UV и запустит проект, установив необходимые зависимости.

``` bash
#!/bin/bash

# Установка UV
echo "Установка UV..."
curl -sSLf https://astral.sh/uv/install.sh | sh

# Checking for uv
if ! command -v uv &>/dev/null; then
    echo "Error! UV is not set."
    exit 1
fi

# Запуск программы main.py
echo "Запуск main.py..."
uv run main.py
```

