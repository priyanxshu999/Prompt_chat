#By Priyanshu
#CONTRIBUTE
#server script


from termcolor import colored
from Crypto.Cipher import AES
import socket
import sys
import os

banner = '''

 _______   _______    ______   __       __  _______   ________                                __                    __     
/       \ /       \  /      \ /  \     /  |/       \ /        |                              /  |                  /  |    
$$$$$$$  |$$$$$$$  |/$$$$$$  |$$  \   /$$ |$$$$$$$  |$$$$$$$$/                       _______ $$ |____    ______   _$$ |_   
$$ |__$$ |$$ |__$$ |$$ |  $$ |$$$  \ /$$$ |$$ |__$$ |   $$ |          ______        /       |$$      \  /      \ / $$   |  
$$    $$/ $$    $$< $$ |  $$ |$$$$  /$$$$ |$$    $$/    $$ |         /      |      /$$$$$$$/ $$$$$$$  | $$$$$$  |$$$$$$/   
$$$$$$$/  $$$$$$$  |$$ |  $$ |$$ $$ $$/$$ |$$$$$$$/     $$ |         $$$$$$/       $$ |      $$ |  $$ | /    $$ |  $$ | __ 
$$ |      $$ |  $$ |$$ \__$$ |$$ |$$$/ $$ |$$ |         $$ |                       $$ \_____ $$ |  $$ |/$$$$$$$ |  $$ |/  |
$$ |      $$ |  $$ |$$    $$/ $$ | $/  $$ |$$ |         $$ |                       $$       |$$ |  $$ |$$    $$ |  $$  $$/ 
$$/       $$/   $$/  $$$$$$/  $$/      $$/ $$/          $$/                         $$$$$$$/ $$/   $$/  $$$$$$$/    $$$$/  
                                                                    *created by-Priyanshu                                  
                                                                                                                            
                                                                                                                           

'''
print(banner)

#Receiving The Value Of IP and PORT From the User

LISN_IP = input(colored("Enter The Local IP of your Machine: ", "green"))
LISN_PORT = int(input(colored("Enter The port no. to bind: ", "green")))

USER_NAME = input(colored("Please Choose a Username for Chat: "))

# Clears the terminal screen
os.system('clear')

print(colored("<1>ONLINE...", "green", attrs=['reverse', 'blink']))

name = USER_NAME + ">> "
encoded_name = name.encode()    #encodes the name to send it over the network

# this chat function starts the server

def chat():
    s = socket.socket()              #creates a new obj
    #binding the socket address and port
    s.bind((LISN_IP, LISN_PORT))
    s.listen(1)   # listen for inc connections
    conn , addr = s.accept()    #Accept inc conn
    print(colored(f"[+] {addr} Connected", "green"))      

#infinite loop to recieve messages from the user till the server runs

    while True:              #infinite loops for the message
        msg = input(colored("\nSEND-> ", "red", attrs=['bold']))
        #condition statement to close the chat incase server_user enters 'bye'
        if msg == 'bye':
            conn.send('bye'.encode())
            os.system('clear')
            print(colored("<0>OFFLINE", "red", attrs=['bold']))
            conn.close()
            sys.exit()
            break

        else:
         #adding AES encryption
            key = b'EBC3D4C51C46801A7267AAB59A63551B'       #key (generate a new key)
            iv = b'This is an IV456'    #initialization vector
            data = encoded_name + msg.encode()      #prep data for enc
            magic = AES.new(key, AES.MODE_CFB, iv)     #creates aes cypher object
            data_send = magic.encrypt(data)            #enc data
            conn.send(data_send)         #send data to client
            #reciving encrypted message
            In_messg = conn.recv(8192)
            #decrypting the incoming AES encrypted data
            decrypt_magic = AES.new(key, AES.MODE_CFB, iv)
            recv_data_enc = decrypt_magic.decrypt(In_messg)
            recv_data_unenc = recv_data_enc.decode()                #decode encrypted msg byte fmt
            print("\n" + recv_data_unenc) # print dec msg

#Final Main function to run the Chat Program! 

def main():
    chat()
main()    #start the chat prog
