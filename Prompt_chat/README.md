# Prompt Chat
```
_______   _______    ______   __       __  _______   ________                                __                    __     
/       \ /       \  /      \ /  \     /  |/       \ /        |                              /  |                  /  |    
$$$$$$$  |$$$$$$$  |/$$$$$$  |$$  \   /$$ |$$$$$$$  |$$$$$$$$/                       _______ $$ |____    ______   _$$ |_   
$$ |__$$ |$$ |__$$ |$$ |  $$ |$$$  \ /$$$ |$$ |__$$ |   $$ |          ______        /       |$$      \  /      \ / $$   |  
$$    $$/ $$    $$< $$ |  $$ |$$$$  /$$$$ |$$    $$/    $$ |         /      |      /$$$$$$$/ $$$$$$$  | $$$$$$  |$$$$$$/   
$$$$$$$/  $$$$$$$  |$$ |  $$ |$$ $$ $$/$$ |$$$$$$$/     $$ |         $$$$$$/       $$ |      $$ |  $$ | /    $$ |  $$ | __ 
$$ |      $$ |  $$ |$$ \__$$ |$$ |$$$/ $$ |$$ |         $$ |                       $$ \_____ $$ |  $$ |/$$$$$$$ |  $$ |/  |
$$ |      $$ |  $$ |$$    $$/ $$ | $/  $$ |$$ |         $$ |                       $$       |$$ |  $$ |$$    $$ |  $$  $$/ 
$$/       $$/   $$/  $$$$$$/  $$/      $$/ $$/          $$/                         $$$$$$$/ $$/   $$/  $$$$$$$/    $$$$/  

```

Prompt Chat is a secure chat application based on a client-server architecture, utilizing AES encryption for secure communication. This project has been tested on Kali Linux but has not been tested on Microsoft Windows.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Generating AES Key](#generating-aes-key)
- [Running the Server](#running-the-server)
- [Running the Client](#running-the-client)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/priyanxshu999/Prompt_chat.git
    cd Prompt_chat
    ```

2. **Install dependencies:**
    ```sh
    chmod +x install.sh implibs.sh ipaddr.sh
    ./install.sh
    ./implibs.sh
    ```

3. **Find the IP address of your machine:**
    ```sh
    ./ipaddr.sh
    ```
   Or use the command:
    ```sh
    ip a
    ```

## Usage

### Generating AES Key

Generate an AES key for secure communication. Ensure to generate a new key and paste it into both `chat_server.py` and `chat_client.py` scripts.

### Running the Server

1. **Run the server script:**
    ```sh
    python chat_server.py
    ```

2. **Enter the following details:**
    - IP address of your machine
    - Port number (i.e, 8080)
    - Your name

### Running the Client

1. **Open a new terminal and run the client script:**
    ```sh
    python chat_client.py
    ```

2. **Enter the following details:**
    - IP address entered by the server
    - Port number entered by the server (i.e, 8080)
    - Your name

Once these steps are completed, the connection will be established and you can start chatting securely.

## Notes

- The shell scripts (`install.sh`, `implibs.sh`, `ipaddr.sh`) are created to install all necessary libraries and to find the IP address of your machine.
- Ensure to provide executable permissions to the shell scripts using:
    ```sh
    chmod +x <Filename>
    ```
- Always generate a new AES key for each session to enhance security. Do not use the existing keys provided in the scripts.

That's it! Enjoy secure chatting with Prompt Chat.
