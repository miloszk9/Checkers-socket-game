from network import Network


def main():
    global messages

    # connect to server and get data
    network = Network()
    my_turn = network.connect()
    
    if my_turn:
        messages = network.recive()

    messages = []
    input_data = ''

    while input_data != 'exit':
        if my_turn == True:
            input_data = str(input('Enter message: '))
            network.send(input_data)
            my_turn = False
        else:
            print('Wait for response...')
            messages = network.recive()
            print(messages)
            my_turn = True

    network.disconnect()
    quit()

if __name__ == '__main__':
    # Global game variables
    messages = []

    main()
