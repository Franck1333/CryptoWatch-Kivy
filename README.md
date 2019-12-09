

# CryptoWatch Kivy Version

This Software allow you to get financials informations about cryptocurrencies by using Python3 and the Kivy UI that will let you interact to the software with a modern graphic user interface.

*Tkinter Version here: [https://franck1333.github.io/CryptoWatch-Tkinter/](https://franck1333.github.io/CryptoWatch-Tkinter/)*

[![Image](https://alternative.me/crypto/fear-and-greed-index.png)](https://alternative.me/crypto/fear-and-greed-index.png)  

## Getting Started  
  
To get a copy of the project, you can go on the GitHub's webpage of the project and click on the green button to download as a .ZIP file. However, if you're using a prompt console on an Unix machine use this line :

```
git clone https://github.com/Franck1333/CryptoWatch-Kivy.git
```
  
### Prerequisites  
  
To use the project, you will need some Hardware :
  
```  
A Raspberry Pi (Last Version is better) or any Linux computer compatible,
An Internet Connection,
A Micro S.D card (8 Gb Minimum),
A Display (like the Pimoroni 4inch HyperPixel Display --> https://bit.ly/2FVOy5j).
```  
  And you will also need some libraries and softwares :

```
- Python version 3
- Kivy up to date
- An OS up to date
```

Be sure to be Up to date with your OS and Python3 environement with this command line:
```
- sudo apt-get update && sudo apt-get upgrade && sudo pip3 install --upgrade pip
```

Now especially for the *Pimoroni HyperPixel 4* in this case :
```
	- The Github page : https://github.com/pimoroni/hyperpixel4
	- The command line Setup (need to be install) : https://get.pimoroni.com/hyperpixel4 | bash 
```
  
### Downloading/Installing
To get and downloaded the files, use this line : 
```
git clone https://github.com/Franck1333/CryptoWatch-Kivy.git
```
- When the project is Downloaded, check your `pi` folder, and you will see the folder `CryptoWatch-Kivy`
When you did it, you will have to launch the file called `setup.py` to install the dependencies neccessary for the project with this command line : 

```
  sudo python3 setup.py install
```

- If some problem during the installation occured, please execute this command :
```
  sudo pip3 install cbpro cmc pandas numpy matplotlib pydub kivy
```

## Run
#### The Way to run the project :
To run the project; if you want to see the console activities, you can launch the file called `Interface_Kivy.py`  into the Command Line Prompt with `python3 Interface_CryptoView.py` in the main folder.

## Running the tests  
  
That's how to test features:

    python3 <file>.py

## The Folders and Files

In this project we've got some folders

#### Folders
```
Example 	: 	Any help or example that I used for the project
Services	:	Main features 
```
#### Files in "/CryptoWatch-Tkinter/Services/"

Main features of the program
```
- Graph.py : This feature allow the 'Historical_CMC.py' to draw a new graph with the data that has been received.

- Historical_CMC.py : This feature obtains the "Close" price of a choosen crypto by a given period.

- Info_Coins.py : This feature can get the Main data about a choosen crypto from 2 sources that are CoinbasePro and Cryptonator.
The data that you will receive are :  Price , Volume (24H) , diference of price (24H) , lowest price (24H) , highest price (24H) , Volume exchanged over 30 Days , Liquidity data [Bids,Asks] (Now). 

- Info_Hardware.py : This feature allow to the Main program to get informations about the status of processors(Usage,Temp),RAM(Usage). 

- Info_complementaires.py : This feature allow to the main program to get the real-time price of the Bitcoin in EURO; (Source: blockchain.info);
This feature allow also to the main program to download an Image on the website alternative.me/ that display an Index about the emotional status of the Investors on the BTC Market.

- Re_tailler_une_image.py : This feature allow to resize a picture.

- nettoyage_du_cache.py : Ancient program that allow all the program which using to delete all the Python2 Cache Files.
```

Folders inside
 ```
 - Sounds : Sound Pack use by the Main Program 
 - Téléchargements : This folder is use by the Main Program to download in this folder all the ressources which come from Internet 
 ```

## Authors

-   **Franck ROCHAT**  -  _Initial work_  -  [Franck ROCHAT](https://github.com/Franck1333)  Thank You !  :heart:

[![Image](https://i.goopics.net/51JA2.jpg)](https://goopics.net/i/51JA2)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAzNjM2MTA4NF19
-->
