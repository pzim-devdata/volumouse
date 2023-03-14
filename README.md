# volumouse
A Python 3 program that allows you to change the volume with the mouse wheel using it at the four corners of the screen

![volumouse](https://www.evinco-software.com/eng/techImage/volumouse-mouse-volume-control.jpg)


[![GitHub license](https://img.shields.io/github/license/pzim-devdata/volumouse?style=plastic)](https://github.com/pzim-devdata/volumouse/blob/main/LICENSE)    ![](https://img.shields.io/badge/Works%20with-Python%203-red?style=plastic)    ![GitHub issues](https://img.shields.io/github/issues/pzim-devdata/volumouse?style=plastic)    [](https://github.com/pzim-devdata/volumouse/issues)    ![GitHub repo size](https://img.shields.io/github/repo-size/pzim-devdata/volumouse?style=plastic)    [![Visits Badge](https://badges.strrl.dev/visits/pzim-devdata/volumouse)](https://badges.strrl.dev)    ![GitHub release (latest by date)](https://img.shields.io/github/v/release/pzim-devdata/volumouse?style=plastic)    [![GitHub commits](https://img.shields.io/github/commits-since/pzim-devdata/volumouse/v2.2.0.svg?style=plastic)](https://GitHub.com/pzim-devata/tahoma/commit/)    
[![Downloads](https://static.pepy.tech/personalized-badge/volumouse?period=total&units=international_system&left_color=grey&right_color=blue&left_text=PyPI%20downloads)](https://pepy.tech/project/volumouse)




THIS IS THE PORTABLE VERSION FOR DIRECT DOWNLOADING. IT'S NOT AN INSTALLED PACKAGE. TO RUN THE APP JUST EXECUTE, IN YOUR IMPORTED FOLDER, `python3 volumouse.py -c`to configure and `python3 volumouse.py` to run the app . IF YOU WANT TO INSTALL THE PACKAGE USING PyPI (pip version) go there : [How to install volumouse with pip ?](https://github.com/pzim-devdata/volumouse#install-the-main-package-) or go directly to the [PyPI Project Website](https://pypi.org/project/volumouse/#description) It's easier.

# Download the folder and extract it :

https://github.com/pzim-devdata/volumouse/archive/refs/heads/main.zip

# Install dependancies :

You need x11-utils :
Debian, Ubuntu, Kali Linux, Raspbian :`apt-get install x11-utils`
Arch Linux :`pacman -S xorg-xdpyinfo`
CentOS : `yum install xorg-x11-utils`
Fedora : `dnf install xorg-x11-utils`

You also need pulseaudio-utils :
Debian, Ubuntu, Kali Linux, Raspbian : `apt-get install pulseaudio-utils`
Alpine : `apk add pulseaudio-utils`
Arch Linux : `pacman -S libpulse`
CentOS : `yum install pulseaudio-utils`
Fedora : `dnf install pulseaudio-utils`

# Start the app :

Run in your imported folder : 

- `python3 -m pip install -r requirements.txt` in order to install dependencies
and
- `python3 volumouse.py` for being sure that tahoma starts

# Configure :

It's very easy to configure, there are just a simple command to execute, once for all, the first time :

All is explained in volumouse --help and volumouse --info

Open a terminal and type :
- `volumouse --configure` or `volumouse -c`



# Usage : 


Just run the command `volumouse` at startup or in a terminal



# Create a PATH to volumouse :


You will need to create a PATH for starting volumouse with the `volumouse` command.

Indead, to be able to run volumouse directly in the terminal, without going to the source package, you should add the volumouse's folder to the PATH :

On Linux, it can be permanently done by executing : `sudo gedit ~/.bashrc` and adding, at the end of the document, this line :

`export PATH=$PATH:/place/of/the/folder/volumouse`



If you want to temporarily test it before, you can just execute this command in the terminal : 

`export PATH=$PATH:/place/of/the/folder/volumouse` 

It will be restored on the next reboot.



By doing this, instead of taping `python3 '/place/of/the/folder/volumouse/volumouse.py'`,
you will be able to directly tape in the terminal : `volumouse`.

Enjoy !

[@pzim-devdata GitHub Pages](https://github.com/pzim-devdata/volumouse/issues)












<p align="center" width="100%">
    <img width="33%" src="https://avatars.githubusercontent.com/u/52496172?v=4"> 
</p>

------------------------------------------------------------------

- [Licence](https://github.com/pzim-devdata/DATA-developer/raw/master/LICENSE)
MIT License Copyright (c) 2023 pzim-devdata

------------------------------------------------------------------

Created by @pzim-devdata - feel free to contact me!


