# chess-AI

## Prerequests

- `sudo apt-get install python3.7`

## Install guide

- `git clone https://github.com/Andy2903/chess-AI.git`
- `python3.7 -m pip install -r requirements.txt`

## Compiling the engine

- `cd ~/lichess-bot/engines/chess-AI`
- `pyinstaller --onefile uci.py`

## How to run

### Using [UCI](http://wbec-ridderkerk.nl/html/UCIProtocol.html)

- `python3.7 path/to/chess-AI/uci.py`

### Using [lichess-bot](https://github.com/ShailChoksi/lichess-bot)

- Requires the engine to be [compiled](##Compiling-the-engine)
- `git clone https://github.com/ShailChoksi/lichess-bot.git`
- `cp -r path/to/chess-AI path/to/lichess-bot/engines`
- Follow instructions in `README.md` from [lichess-bot](https://github.com/ShailChoksi/lichess-bot)
- Set `engine.name` in `path/to/lichess-bot/config.yml` to `chess-AI/dist/uci`
- `python3.7 path/to/lichess-bot/lichess-bot.py`
