#### Пишем пульт охраны банка

Данный проект создан в образовательных целях согласно Урока 1
модуля "Знакомство с Django: ORM " образовательного ресурса [Devman](www.dvmn.org)

##### Установка

Для использования вам необходимо:
- [python3](www.python.org)
- pip3 (для установки зависимостей из файла requirements.txt)
- интернет браузер (который есть уже везде)

Рекомендуется использовать [виртуальное окружение](https://pythoner.name/documentation/tutorial/venv)
python для разворачивания проекта.

##### Рекомендации при разворацивании в среде Linux

1. Скопируйте проект в локальную папку, например с помощью git:

`git clone https://github.com/Sam1808/django-orm-watching-storage.git`

2. Создайте виртуальное окружение:

`python3 -m venv <название_окружения>`

3. Активируйте виртуальное окружение:

`source <название_окружения>/bin/activate`

4. Опционально - обновите установщик пакетов pip

`pip install --upgrade pip`

После того, как все шаги выполнены, пожалуйста запустите pip3 для установки зависимостей:

`pip install -r requirements.txt`

##### Как запустить?

Для локальной работы сайта необходимо определить ряд переменных окружения.

В свою очередь, для определения данных переменных предусмотрена библиотека [python-dotenv](https://pypi.org/project/python-dotenv/)
и использование файла .env.

Создайте текстовый файл **.env** в папке **project** и заполните его следующим образом:

```
DB_HOST="hostname" # имя узла к которому будет обращаться settings.py
DB_PORT="5434" # соответствующий номер порта
DB_NAME="databasename" #  имя базы данных
DB_USER_NAME="username" # имя пользователя
DB_PASSWORD="userpassword" # пароль пользователя
SECRET_KEY='REPLACE_ME' # секретный ключ
DEBUG=1 # debug-статус, где значение 1 это True, а значение 0 это False
```

Скрипт запускается из консоли с помощью командной строки.

В активном виртуальном окружении запустите:

`python3 main.py`

Где:
- python3 - файл запуска python
- main.py - скрипт запуска

Тестовый сайт будет доступен локально по [ссылке](http://0.0.0.0:8000/)


Описание:

Скрипт запускает локальный учебный web-сервер, который должен соотвествовать заданию преподавателя.  


##### Важно
Для коррекной работы скрипта необходимы настройки, предоставляемые [Devman](www.dvmn.org)
