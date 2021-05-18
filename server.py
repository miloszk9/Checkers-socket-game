import _pickle as pickle
from _thread import *
from socket import *


def threaded_client(connection, client_id, lobby_id): 
    global players, connections, lobbies
    
    id = client_id
    players.append(id)

    connection.send(pickle.dumps(lobbies[lobby_id]))

    while True:

        try:
            data = connection.recv(2048 * 12)
            update = pickle.loads(data)

            lobbies[lobby_id].append(update)

            send_data = pickle.dumps(lobbies[lobby_id])
            connection.send(send_data)

        except Exception as e:
            print(e)
            break

    # player disconneted
    try:
        print(f"Connection {id} Close")
        connections -= 1
        connection.close()

    except Exception as e:
        print(e)

if __name__ == '__main__':
    hostIp = "192.168.0.11"  # Change to your local IP address
    port = 8999

    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    try:
        s.bind((hostIp, port))
    except error as e:
        print(str(e))
    try:
        s.listen(2)  # max 2 users in queue
    except error as e:
        print(str(e))
    print("Waiting for a connection")

    # Game global variables
    players = list()
    lobbies = list()
    connections = 0
    player_queue = None
    id = 0

    while True:  # continuously looking for new connection
        client, addr = s.accept()
        print(f"Connection from {addr} has been established. ID = {id}.")
        connections += 1
        id += 1  # Next client will recive incremented id value

        if player_queue is not None:
            lobbies.append([])
            start_new_thread(threaded_client, (client, id, len(lobbies)-1))
            start_new_thread(threaded_client, (*player_queue, len(lobbies)-1))
            player_queue = None
        else:
            player_queue = (client, id)
    