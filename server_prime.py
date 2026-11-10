#exercise 1:Prime checker server

import socket

HOST = 'localhost'
PORT = 8082
BUFF_SIZE = 1024

def _isPrime(number):
    #verifies wether the number is a prime number true/false
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
    return True

def parse_integer(message_str):
    #converts string to integer 
    try:
        return int(message_str)
    except ValueError:
        raise ValueError("This is not an integer")

def main():
    #create udp and connect to localhost
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    print(f"UDP Prime server listening on {HOST}:{PORT}")

    try: 
        while True:
            data, client_adress = sock.recvfrom(BUFF_SIZE)
            message = data.decode('utf-8')

            #verify that the message is an integer
            try:
                number = parse_integer(message)
            except ValueError as err:
                print(f"Error raised through '{message}': {err}")
                sock.sendto("This is not an integer".encode('utf-8'), client_adress)
                continue
            #verify the range 
            if number < 2 and number > 100:
                reply = "Error: Number is out of range"
            #check primarly
            elif _isPrime(number):
                reply = f"The number {number} is prime"
            else:
                reply = f"The number {number} is NOT prime"
            sock.sendto(reply.encode('utf-8'), client_adress)
    except KeyboardInterrupt:
        print("\nServer shutting down")
    finally:
        sock.close()
if __name__ == "__main__":
    main() 



        
