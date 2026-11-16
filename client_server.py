# primer checker client 
import socket 

SERVER_HOST = 'localhost'
SERVER_PORT = 8082
BUFF_SIZE = 1024

def main():
    server_adress = (SERVER_HOST, SERVER_PORT)
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            user_input = input("Enter an integer between 2,100 or 'exit' to quit").strip()
            if user_input.lower() == "exit":
                print("CLosing client socket")
                break
            #send input to UDP 
            client_sock.sendto(user_input.encode('utf-8'), server_adress)

            #wait for the server response
            response, _ = client_sock.recvfrom(BUFF_SIZE)
            print("Server response:", response.decode('utf-8'))

    except Exception as e:
        print(f"Communication error: {e}")
    finally:
        client_sock.close()

if __name__ == "__main__":
    main()


    