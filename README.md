

* This is a prompt chat based on server client architecture 
* [Note] - This project is only been tested on kali linux and havent been tested on microsoft windows 
* There are 2 python scripts (client & server scripts)
     you can execute client & server script by simply running the below commands
     python chat_server.py #for server 
     python chat_client.py #for client
     But before that do execute the shell scripts. 
* There are 3 shell files inside Prompt_chat folder 
-->usage of shell files
   >>The shell files are created to install all the necessary libraries in your linux machine
   >>To execute shell files you need to provde executable permissions to these shell files 
        you can simply provide exe permission by using below command
             chmod +x <__Filename__>
* To know the ip address simply run the ipaddr.sh script or you can use (ip a) command.
* Remember first run the server script and add the ip address of your machine and then add the port 8080 and after that 
  perform the same process in the client script.
* The AES encryption makes the chat more secure as it is a symmetric key cryptography
* Thats it      


# clone the repo
git clone https://github.com/priyanxshu999/Prompt_chat.git
# install dependencies 
./install.sh
./implibs.sh
# find the ip of your machine  
./ipaddr.sh

# run the server script
python chat_server.py
# enter ip of your machine
# enter port number i.e 8080
# enter name 

# open new terminal 
# run the client script
python chat_client.py
# enter the ip enter by the server 
# enter port entered by server i.e 8080
# enter name 

# now the connection is established 



# dont forget to generate the aes keys and paste it in both client and server script (dont use the existing keys)

