# Checkers socket game

Python implementation of checkers game using python sockets.
## Prerequirements
* Python 3.8
* Python package: Pygame, Numpy

## Packages installation
```sh
$ pip install pygame==2.0.1 numpy==1.20.3
```

## Example usage
Local game (on one PC) - getting the ip address automatically
```sh
$ python server.py
$ python client.py
$ python client.py
```
Game via LAN
```sh
$ python server.py <server_ipv4>
$ python client.py <server_ipv4>
$ python client.py <server_ipv4>
```
Example
```sh
$ python server.py 192.168.0.1
$ python client.py 192.168.0.1
$ python client.py 192.168.0.1
```

## Example screenshots
![screen1](https://github.com/miloszk9/Checkers-socket-game/blob/main/example_screenshots/checkers1.png?raw=true)
![screen2](https://github.com/miloszk9/Checkers-socket-game/blob/main/example_screenshots/checkers2.png?raw=true)
![screen3](https://github.com/miloszk9/Checkers-socket-game/blob/main/example_screenshots/checkers3.png?raw=true)
