# year_in_day
## How it works:
### Start service:

- #### Склонируйте проект:

  `git clone https://github.com/danila-kuryakin/year_in_day.git`

- #### Перейдите в директорию проекта:

  `cd year_in_day`

- #### Соберите docker image:

  `sudo ./gradlew startService`

- #### Запустите docker: 

  `sudo docker run --rm -p 80:80 dakur/year_in_date`

### Отправьте запрос:

    curl http://localhost?year=2017