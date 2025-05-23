Пеерйти в: [README-EN](./README.md)

<div align="center">
    <h1>crontab-ui</h1>
    <img   src="assets/LogoCrontabUI.png" width="100">
</div>

**Crontab-ui** - это пользовательская программа с графической оболочкой, предоставляющая возможность работы с инструментом `cron` для автоматизации задач.

**Cron** - Компьютерная программа (демон) использующийся для периодического выполнения заданий в определённое время. Регулярные действия описываются инструкциями, помещенными в файлы `crontab` и в специальные каталоги.

![CrontabUI_mainPage](assets/crontabUI.png)

![termCrontab](assets/termCrontab.png)

# Python инструменты

**Графическая оболочка: [Flet](https://flet.dev/)**

<img src="assets/fletLogo.svg" width="50">

**Flet** — это фреймворк, который позволяет вам легко создавать веб-приложения, мобильные и настольные приложения в реальном времени на вашем любимом языке и безопасно делиться ими с вашей командой. Опыт работы с frontend не требуется.

---

**Инструменты по работе с Cron: [python-crontab](https://pypi.org/project/python-crontab/#description), [croniter](https://pypi.org/project/croniter/)**

<img src="assets/pythonCrontab.svg" width="50">

**Python-crontab** - Модуль Crontab для чтения и записи файлов crontab и доступа к системному cron автоматически и просто с помощью прямого API.

**Croniter** - обеспечивает итерацию для объекта datetime в формате, подобном cron.

---

# Установка

``` bash
git clone https://github.com/Stepan-Zhnets/crontab-ui.git
```

# Запуск

Чтобы запустить проект, вам необходимо запустить скрипт `start.sh`, через команду:

``` bash
bash start.sh
```

Этот скрипт запустит установку менеджера пакетов Python UV и запустит проект, установив необходимые зависимости.

``` bash
#!/bin/bash

# Установка UV
echo "Установка UV..."
curl -sSLf https://astral.sh/uv/install.sh | sh

# Проверка на наличие UV
if ! command -v uv &>/dev/null; then
    echo "Error! UV is not set."
    exit 1
fi

# Запуск программы main.py
echo "Запуск main.py..."
uv run main.py
```

## Виды запуска программы
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

# Работа с программой

## Создание работы

![createNewJob](assets/createNewJob.png)

## Панель "действия"

![actions](assets/actions.png)

### Редактирование работы

![editJob](assets/editJob.png)

