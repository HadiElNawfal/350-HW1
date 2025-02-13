# Client-ProxyServer


This README provides instructions on how to run the Client and Proxy Server codes.

## Table of Contents

 [Client-Proxy Server](#Client-ProxyServer)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
  - [Running the Codes](#running-the-codes)
    - [Server](#Server)
    - [Client](#Client)

## Installation

### Prerequisites

Before installing Scapy, make sure you have the following prerequisites:

1. **Python**: Scapy requires Python 3.x. Make sure you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

2. **Pip**: Pip is the package manager for Python. It's usually included with Python, so you should have it available. You can check if Pip is installed by running `pip --version` in your terminal/command prompt.

### Installation Steps

1. Through your terminal or command prompt, install Scapy using pip by running the following command: `pip install scapy`. This will download and install Scapy and its dependencies.


2. You can clone both codes, once the installation is complete, using the command: git clone https://github.com/HadiElNawfal/Client-ProxyServer


## Running the Codes

1. Run the Server code by typing ```python Server.py``` in a terminal in the file's directory.

3. Run the Client code by typing ```python Client.py``` in a terminal in the file's directory.

### Server:
The script:
* Listens on a port that is specified to receive incoming connections.
* Analyzes the incoming request to extract the destination server's IP address.
* Generates a message detailing the request, including the IP address and the exact time it was made.
* Forwards the client's request to the destination server.
* Records the exact time when the actual request was made and prints a corresponding message.
* Receives the response from the destination server.
* Displays a message indicating the successful reception of the response along with the exact time.
* Sends the response back to the client.
* Prints a message confirming the response has been sent, including the exact time.
* If any errors occur either on the client's or server's end, the proxy server notifies the user and returns an error message to the client.

### Client:
The script:
* Accepts input for the IP address of the website you want to access.
* Sends the request to the proxy server.
* Prints a message displaying the request details and the exact time it was sent.
* Receives the reply from the proxy server and present it to the user, indicating the exact time it was received.
* Calculates and shows the total round-trip time.
* Displays the user's physical MAC address (not the one from the virtual machine).

</details>

When you push this to GitHub and view your README on GitHub.com, you’ll see:

1. The code block rendered with syntax highlighting (if you specified a language).
2. A small “copy” button at the top-right corner of the code block.

---

## 2. Verify on GitHub

After committing and pushing your README file (or any `.md` file) to your repository, navigate to your repo on GitHub and open the file. You should see the “copy” icon on the right side of the code block’s header. Clicking it will copy all the contents of that code block to your clipboard.

---

## 3. Important Notes

1. **No Extra Setup Required**: The “copy” button is built into GitHub’s Markdown rendering engine. You don’t need extra plugins or scripts.

2. **Language Syntax**: If you add a language identifier (e.g., `bash`, `js`, `python`) after the opening backticks, you’ll get syntax highlighting.  
   - Examples:  
     - \`\`\`js  
       console.log("Hello JS");  
       \`\`\`  
     - \`\`\`python  
       print("Hello Python")  
       \`\`\`

3. **Where It Works**: This feature appears when browsing code on GitHub’s website (GitHub.com). If you view the same Markdown locally (e.g., in a text editor), the button won’t be present. It’s purely a GitHub.com feature.

4. **Don’t Use Indented Code Blocks**: The copy button only appears for **fenced** code blocks (the triple backtick style). If you indent code for a code block instead (4 spaces), GitHub won’t show the copy button.

---

## 4. Example in a README

Here’s a sample README snippet that includes a code block:

<details>
<summary>Sample README.md content</summary>

```markdown
# My Project

This project demonstrates how to add a copy button to code blocks on GitHub.

## Usage

```bash
# Clone the repo
git clone https://github.com/username/my-project.git

# Change directory
cd my-project

# Run the script
./run.sh

