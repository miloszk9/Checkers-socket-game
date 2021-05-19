from network import Network


def main():
    global messages

    # connect to server and get data
    network = Network()
    messages = network.connect()
    
    input_data = ''

    while input_data != 'exit':
        input_data = str(input())
        messages = network.send(input_data)
        print(messages)

    network.disconnect()
    quit()

if __name__ == '__main__':
    # Global game variables
    messages = []

    main()
