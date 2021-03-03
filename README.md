# chess-AI

Running instance playable at: [https://lichess.org/@/schach-KI](https://lichess.org/@/schach-KI)

## Prerequests

- `sudo apt-get install python3`

## Install guide

- `git clone https://github.com/Andy2903/chess-AI.git`
- `python3 -m pip install -r requirements.txt`

## Compiling the engine

- `cd path/to/lichess-bot/engines/chess-AI`
- `pyInstaller uci.py`

## How to run

### Using [UCI](http://wbec-ridderkerk.nl/html/UCIProtocol.html)

- `python3 path/to/chess-AI/uci.py`

### Using [lichess-bot](https://github.com/ShailChoksi/lichess-bot)

- Requires the engine to be [compiled](##Compiling-the-engine)
- `git clone https://github.com/ShailChoksi/lichess-bot.git`
- `cp -r path/to/chess-AI path/to/lichess-bot/engines`
- Follow instructions in `README.md` from [lichess-bot](https://github.com/ShailChoksi/lichess-bot)
- Set `engine.name` in `path/to/lichess-bot/config.yml` to `chess-AI/dist/uci`
- `python3 path/to/lichess-bot/lichess-bot.py`
