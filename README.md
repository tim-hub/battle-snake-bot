# Awesome Battle Snake Bot
[![CircleCI](https://circleci.com/gh/tim-hub/awesome-snake.svg?style=svg)](https://circleci.com/gh/tim-hub/awesome-snake)
[![CodeFactor](https://www.codefactor.io/repository/github/tim-hub/awesome-snake/badge?style=flat-square)](https://www.codefactor.io/repository/github/tim-hub/awesome-snake)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Ftim-hub%2Fawesome-snake.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Ftim-hub%2Fawesome-snake?ref=badge_shield)

![game 1](https://exporter.battlesnake.io/games/c2d1aa50-03c5-4b91-9664-f1ac97f334a3/gif) 
![game 2](https://exporter.battlesnake.io/games/36246bc1-75bf-4ff5-a225-5bf6551c3dd6/gif)

A simple [Battlesnake AI](http://battlesnake.io) bot written in Python. 

## How to
This AI client uses the Flask to serve requests and the [gunicorn web server](http://gunicorn.org/) for running bottle on Heroku. Dependencies are listed in [requirements.txt](requirements.txt).

0. set your `.env` (ref `.env.example`)
1. `export LC_ALL=en_US.utf-8;LANG=en_US.utf-8;APP_SETTINGS=config.DevelopmentConfig`
2. `flask run`
3. - or `gunicorn app:app` if you got gunicorn locally




## Differences
- bottle => flask
- no db => PostgreSQL db (to store turns and games data)

Visit https://github.com/battlesnakeio/community/blob/master/starter-snakes.md for API documentation and instructions for running your AI.


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Ftim-hub%2Fawesome-snake.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Ftim-hub%2Fawesome-snake?ref=badge_large)