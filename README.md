Instructions for setting up project
=======


## What you will need 

Below is the hardware required inorder for the project to work.

  * Micro:bit sensor(s)
 
Below is the software required to be installed inorder for the project to work.

  * Mu editor
  * Python
  * MySQL
  * Visual Studio Code
  * Cygwin

Programming languages used:

  * Python
  * Javascript


## Quick quide
  
  Here you can find a quick guide to the more detailed steps below to setup the project.

  * Download all the necessary software
  * Make sure you have the required hardware
  * Download the .zip file
  * Flash scripts to the micro:bit sensors
  * Run the python script "microbit.py" for logging to the database
  * Start up server in Cygwin
  * Open browser to use web application

## Get started!

Start by downloading the node modules for Javascript and Nodejs, you do this by installing Node.js and npm from the official website
https://nodejs.org/en/download/. 
You can verify that it works by running the command `node --version` and  `npm --version`.

Now you can download all the necessary files for the project. This includes the folder named "kmom05", the six scripts for the micro:bit sensors ("reciever.py", "senderXXX.py") and the "microbit.py" file on GitHub.


Download the .zip file containing the following files/folders:

  * kmom05
  * all scripts for the sensors ("reciever.py" and "sensorXXX.py")
  * microbit.py




## Get data from Micro:bit sensor 

To get the data from the micro:bit sensor, the library "radio" is used for communication between the micro:bits. 
In the repository, there is two different kinds of scripts; "reciever" and "senderXXX". The Micro:bit which is recieving the data is the reciever and you shall therefore use this script in Mu editor and flash it to the head-micro:bit. 
The head micro:bit shall always be plugged in the computer via a USB-cable (even after you have flashed the program to it, this is because it is sending all the collected data through the USB port).
Run the script for the head sensor by clicking on the "REPL"-button.  

The script for the senders you shall flash to the sending micro:bit sensors. The only difference in their code is the harcoded ID. The senders shall be connected to battery packages and they connect with the head micro:bit using the "radio" library. 



## Run script to log data to database 

The data recieved is handled by a script written in regular Python. The data is logged to the database via this script and it is ran in cmd. 
The data is streamed through the USB-port and it is therefor essential to specify the right port, a guide for that follows below.

Get the correct USB-port:

  * Run cmd as admin
  * Type in the command `wmic path Win32_SerialPort` to check which port the USB is using (COMX).
  * In the beginning of the "microbit.py" file, the COM-port is specified in the code. Change the port to the one it is said is being used when you run above command if needed (COM5 and COM3 and COM7 is common).

To run script:

   * Run cmd as admin
   * Navigate in cmd to the folder where the "microbit.py" file is
   * Use the command `python microbit.py` to run script

Once you have done this, the script will log the data that is is recieving to the database and you will be able to view this on the web application. 


## Connect to localhost and use web application

Download files
run in cygwin
node modules, DOWNLOAD NODE! run commands etcetera ;)

To connect to localhost (local server on your computer) you will have to navigate to the path of the project folder on your computer. The file you want to run is "index.js".
You will be using the terminal Cygwin for this. 

Cygwin commands to navigate 

  * Navigates to the homepath:  `cd $HOMEPATH`
  
  * Navigate to folder name_Of_Folder:  `cd name_Of_Folder`
  
  * Navigate back one folder:  `cd ..`
  
  * Run Javascript file in Node.js:  `node filename.js`
  

Path to file "C:/Users/.../kmom05/eshop1/"


Instructions


  * Run Cygwin as administor
  * Navigate to the folder "C:/Users/.../kmom05/eshop1/"
  * Run command `node index.js` in above folder to start up the web server
  * Use a browser of your choice and type in "http://localhost:1337/eshop/index" in the search bar to get to the web application

You should now be connected and can now use the web application as you please.