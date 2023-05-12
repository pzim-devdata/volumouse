#!/usr/bin/python3
# volumouse.py by @pzim-devdata
# MIT Licence
# Inspired by script from mehmet nural altintas <mehmet.nrl@hotmail.com>
# This script is inspired from  "record_demo.py -- demonstrate record extension" that can be found here: http://python-xlib.svn.sourceforge.net/viewvc/python-xlib/trunk/examples/

"""
This is the main module
"""

import subprocess
import os
import argparse
import sys
from Xlib import X, display
from Xlib.ext import record
from Xlib.protocol import rq
import time

file_temp =  os.path.dirname(os.path.abspath(__file__))+'/temp'
file_Top_right_card = os.path.dirname(os.path.abspath(__file__))+'/temp/top_right_card.txt'
file_Bottom_right_card = os.path.dirname(os.path.abspath(__file__))+'/temp/bottom_right_card.txt'
file_Top_left_card = os.path.dirname(os.path.abspath(__file__))+'/temp/top_left_card.txt'
file_Bottom_left_card = os.path.dirname(os.path.abspath(__file__))+'/temp/bottom_left_card.txt'

file_Screen_resolution = os.path.dirname(os.path.abspath(__file__))+'/temp/screen_resolution.txt'

file_Corner_area = os.path.dirname(os.path.abspath(__file__))+'/temp/corner_area_size.txt'

file_max_volume_top_right = os.path.dirname(os.path.abspath(__file__))+'/temp/max_top_right_volume.txt'
file_max_volume_bottom_right = os.path.dirname(os.path.abspath(__file__))+'/temp/max_bottom_right_volume.txt'
file_max_volume_top_left = os.path.dirname(os.path.abspath(__file__))+'/temp/max_top_left_volume.txt'
file_max_volume_bottom_left = os.path.dirname(os.path.abspath(__file__))+'/temp/max_bottom_left_volume.txt'

def main():
    import __version__
    version ='volumouse - Version '+ str(__version__.__version__)+' - by @pzim-devdata'
############################ARGUMENTS
    def info():
        print( "" )
        print( "      ***************************************************************      " )
        print( "------*         "+version+"          *-------" )
        print( "      ***************************************************************        " )
        print( "" )
        print( "                    https://github.com/pzim-devdata/volumouse" )
        print( "                             contact@pzim.fr" )
        print( "" )
        print( " HELP : python3 'volumouse.py' -h or python3 'volumouse.py' --help" )
        print( "        python3 'volumouse.py' -i or python3 'volumouse.py' --info" )
        print( "" )
        print( " CONFIGURE : python3 'volumouse.py' -c or python3 'volumouse.py' --configure ")
        print( "")
        print( " RUNNING THE APP : python3 'volumouse.py'")
        print( "" )
        print( " You should add volumouse to the starting apps to use it ")
        print( "" )
        print( " You need x11-utils :")
        print( " Debian, Ubuntu, Kali Linux, Raspbian :")
        print( " apt-get install x11-utils ")
        print( " Arch Linux :pacman -S xorg-xdpyinfo")
        print( " CentOS : yum install xorg-x11-utils")
        print( " Fedora : dnf install xorg-x11-utils" )
        print( "")
        print( " You also need pulseaudio-utils :")
        print( " Debian, Ubuntu, Kali Linux, Raspbian :")
        print( " apt-get install pulseaudio-utils")
        print( " Alpine : apk add pulseaudio-utils")
        print( " Arch Linux : pacman -S libpulse")
        print( " CentOS : yum install pulseaudio-utils")
        print( " Fedora : dnf install pulseaudio-utils")
        print( "")
        print("If you want to start volumouse at startup, enter this command as app's directory :")
        print("python3 '"+os.path.dirname(os.path.abspath(__file__))+"/volumouse.py'")

    for arg in sys.argv :
        if arg == '-h' or arg == '--help' :
            print("\n\npython3 'volumouse.py' -h, --help : "+version+"\n\nUsage:\n python3 'volumouse.py' \n\nHelp options :\n -h,   --help                      Show this help\n -i,   --info                      Show more info\n\nPlugin options :\n -v,   --version                   Show the version of the plugin\n -c,   --configure                 To configure volumouse in text files which are located there : \n                                   "+file_temp)
            print( "")
            print("If you want to start volumouse at startup, enter this command as app's directory :")
            print("python3 '"+os.path.dirname(os.path.abspath(__file__))+"/volumouse.py'")
            print("")
            exit()

        try :
            if arg == '-v' or arg == '--version' :
                print(version)
                exit()
        except IndexError: 
            info()
            exit()

        try :
            if arg == '-i' or arg == '--info' :
                info()
                exit()
        except IndexError: 
            info()
            exit()

        if arg == '-c' or arg == '--configure' or arg == '--config':
            try:
                screen_resolution = tuple(map(int, subprocess.check_output("xdpyinfo | awk '/dimensions/ {print $2}' | grep '[0-9]'", shell=True).decode().rstrip().replace('x',',').split(',')))
                print("Do you want to use the default screen resolution which is : "+str(screen_resolution)+" ? (Y/n)")
                answer = input()
                if answer.lower() == 'y'or answer.lower() == 'yes':
                    f = open(file_Screen_resolution, 'w')
                    f.write(str(screen_resolution))
                    f.close()
                    print( "Resolution stored in "+file_Screen_resolution ) 
                    time.sleep(2)
                elif answer.lower() == 'n'or answer.lower() == 'no':
                    print ("\nEnter the number in the list of your screen résolution :")
                    print("1- 800 x 600")
                    print("2- 823 x 624")
                    print("3- 1024 x 768") 
                    print("4- 1280 x 720")
                    print("5- 1152 x 864")
                    print("6- 1280 x 800")
                    print("7- 1440 x 900")
                    print("8- 1280 x 1024")
                    print("9- 1600 x 900")
                    print("10- 1680 x 1050")
                    print("11- 1920 x 1080")
                    print("12- 2560 x 1440")
                    print("13- 3840 x 2160")
                    print("14- 4096 x 2160")
                    print("15- CUSTOM Resolution")
                    answer = input()
                    if int(answer) == 1:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(800, 600)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    elif int(answer) == 2:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(823, 624)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    elif int(answer) == 3:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(1024, 768)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    elif int(answer) == 4:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(1280, 720)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    elif int(answer) == 5:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(1152, 864)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    elif int(answer) == 6:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(1280, 800)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    elif int(answer) == 7:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(1440, 900)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    elif int(answer) == 8:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(1280, 1024)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution )
                        time.sleep(2) 
                    elif int(answer) == 9:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(1600, 900)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    elif int(answer) == 10:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(1680, 1050)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    elif int(answer) == 11:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(1920, 1080)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution )
                        time.sleep(2) 
                    elif int(answer) == 12:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(2560, 1440)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    elif int(answer) == 13:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(3840, 2160)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    elif int(answer) == 14:
                        f = open(file_Screen_resolution, 'w')
                        f.write('(4096, 2160)')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    elif int(answer) == 15 or answer.lower() == custom :
                        f = open(file_Screen_resolution, 'w')
                        print("Please provide your custom resolution : '(x, y)'")
                        print("What is the value of x ?")
                        answer = input()
                        print("What is the value of y ?")
                        answer2 = input()
                        f.write('('+answer+', '+answer2+')')
                        f.close()
                        print( "Resolution stored in "+file_Screen_resolution ) 
                        time.sleep(2)
                    else :
                        print("You didn't provided a screen resolution ! Volumouse can't work without this info ...")
                        exit(1)
                else :
                    f = open(file_Screen_resolution, 'w')
                    f.write(str(screen_resolution))
                    f.close()
                    print("You didn't provided any answer, "+str(screen_resolution)+" will be used")
                    print( "Resolution stored in "+file_Screen_resolution ) 
                    time.sleep(5)
            except Exception as e:
                f = open(file_Screen_resolution, 'w')
                print("\nPlease provide your screen resolution :'(x, y)'\nFor instance (1920 x 1080) :")
                print("What is the value of x ?")
                answer = input()
                print("What is the value of y ?")
                answer2 = input()
                f.write('('+answer+', '+answer2+')')
                f.close()
                print( "Resolution stored in "+file_Screen_resolution ) 
                time.sleep(2)
                print( "\nAn error occured, please, look at the error bellow :\n")
                print(e)
                print("Press any key to continue ...")
                answer = input()
            #############################################
            try :
                corner_area = 30 
                print("\nPlease provide a size for the area's detection in the corners :")
                print("Default size is 30")
                answer3 = input()
                try:
                    if 1 <= int(answer3) and int(answer3) <= 200 :
                        f = open(file_Corner_area, 'w')
                        f.write(answer3)
                        f.close()
                        print("You have entered : "+answer3)
                        print( "Corner's size stored in "+file_Corner_area ) 
                        time.sleep(2)
                    else :
                        print("You have entered :"+answer3+" which is incorrect.")
                        print("The default value '"+str(corner_area)+"' will be used instead ...")
                        time.sleep (4)
                        f = open(file_Corner_area, 'w')
                        f.write(str(corner_area))
                        f.close()
                except :
                    print("You didn't provided any correct value, '"+str(corner_area)+"' will be used for the default size of the corner area")
                    f = open(file_Corner_area, 'w')
                    f.write(str(corner_area))
                    f.close()
                    time.sleep(2)
            except Exception as e:
                print( "\nAn error occured, please, try again the command 'volumouse -c'.\n")
                print(e)
                exit(1)
            #############################################
            try :
                list_cards = subprocess.check_output("pacmd list-sinks | grep 'name:' | cut -d '<' -f2 | cut -d '>' -f1", shell=True).decode().rstrip().replace('\n',',').split(",")
            except Exception as e:
                print( "\nAn error occured, look at the error message bellow :\n")
                print(e)
                exit(1)
            ####################
            try:
                print("\nPlease enter the number of the card you want to use for the 'Top Right' corner's side of the screen :")
                print("0- No Soundcard")
                print("1- Active soundcard")
                y=2
                for card in list_cards :
                    print (str(y)+'- '+card)
                    y=y+1
                print('')
                answer = input()
                top_right_card = list_cards[int(answer)-2]
                f = open(file_Top_right_card, 'w')
                if int(answer) == 0 :
                    print("\nYou don't have selected any card") 
                    f.write('')
                elif int(answer) == 1 :
                    print("\nYou have selected the default used card") 
                    f.write('@DEFAULT_SINK@')
                elif int(answer) >= 2 :
                    print("\nYou have selected : "+top_right_card) 
                    f.write(top_right_card)
                else:
                    print("\nYou didn't provided a card for the 'Top Right' corner's side of the screen.\nNo sound card will be assigned")
                    f.write('')
                f.close()
                time.sleep(2)

                print("\nWhat is the maximum volume you want for the 'Top Right' corner's side ? (Default is 150%).\nEnter a number without '%'...")
                print('')
                answer = input()
                f = open(file_max_volume_top_right, 'w')
                try :
                    f.write(str(int(answer)))
                except Exception as e:
                    print( "\nDid you provided a number without '%' ? Max volume will be defined to 150%")
                    f.write('150')
#                    print( "\nAn error occured, look at the error message bellow :\n")
#                    print(e)
                f.close()
                time.sleep(2)
            ####################
                print("\nPlease enter the number of the card you want to use for the 'Bottom Right' corner's side of the screen :")
                print("0- No Soundcard")
                print("1- Active soundcard")
                y=2
                for card in list_cards :
                    print (str(y)+'- '+card)
                    y=y+1
                print(' ')
                answer = input()
                bottom_right_card = list_cards[int(answer)-2]
                f = open(file_Bottom_right_card, 'w')
                if int(answer) == 0 :
                    print("\nYou don't have selected any card") 
                    f.write('')
                elif int(answer) == 1 :
                    print("\n\nYou have selected the default used card") 
                    f.write('@DEFAULT_SINK@')
                elif int(answer) >= 2 :
                    print("\nYou have selected : "+bottom_right_card) 
                    f.write(bottom_right_card)
                else:
                    print("\nYou didn't provided a card for the 'Bottom Right' corner's side of the screen.\nNo card will be assigned")
                    f.write('')
                f.close()
                time.sleep(2)

                print("\nWhat is the maximum volume you want for the 'Bottom Right' corner's side ? (Default is 150%).\nEnter a number without '%'...")
                print('')
                answer = input()
                f = open(file_max_volume_bottom_right, 'w')
                try :
                    f.write(str(int(answer)))
                except Exception as e:
                    print( "\nDid you provided a number without '%' ? Max volume will be defined to 150%")
                    f.write('150')
#                    print( "\nAn error occured, look at the error message bellow :\n")
#                    print(e)
                f.close()
                time.sleep(2)
            ####################
                print("\nPlease enter the number of the card you want to use for the 'Top Left' corner's side of the screen :")
                print("0- No Soundcard")
                print("1- Active soundcard")
                y=2
                for card in list_cards :
                    print (str(y)+'- '+card)
                    y=y+1
                print('')
                answer = input()
                top_left_card = list_cards[int(answer)-2]
                f = open(file_Top_left_card, 'w')
                if int(answer) == 0 :
                    print("\nYou don't have selected any card") 
                    f.write('')
                elif int(answer) == 1 :
                    print("\nYou have selected the default used card") 
                    f.write('@DEFAULT_SINK@')
                elif int(answer) >= 2 :
                    print("\n\nYou have selected : "+top_left_card) 
                    f.write(top_left_card)
                else:
                    print("\nYou didn't provided a card for the 'Top Left' corner's side of the screen.\nNo card will be assigned")
                    f.write('')
                f.close()
                time.sleep(2)

                print("\nWhat is the maximum volume you want for the 'Top Left' corner's side ? (Default is 150%).\nEnter a number without '%'...")
                print('')
                answer = input()
                f = open(file_max_volume_top_left, 'w')
                try :
                    f.write(str(int(answer)))
                except Exception as e:
                    print( "\nDid you provided a number without '%' ? Max volume will be defined to 150%")
                    f.write('150')
#                    print( "\nAn error occured, look at the error message bellow :\n")
#                    print(e)
                f.close()
                time.sleep(2)
            ####################
                print("\nPlease enter the number of the card you want to use for the 'Bottom Left' corner's side of the screen :")
                print("0- No Soundcard")
                print("1- Active soundcard")
                y=2
                for card in list_cards :
                    print (str(y)+'- '+card)
                    y=y+1
                print('')
                answer = input()
                bottom_left_card = list_cards[int(answer)-2]
                f = open(file_Bottom_left_card, 'w')
                if int(answer) == 0 :
                    print("\nYou don't have selected any card") 
                    f.write('')
                elif int(answer) == 1 :
                    print("\nYou have selected the default used card") 
                    f.write('@DEFAULT_SINK@')
                elif int(answer) >= 2 :
                    print("\n\nYou have selected : "+bottom_left_card) 
                    f.write(bottom_left_card)
                else:
                    print("\nYou didn't provided a card for the 'Bottom Left' corner's side of the screen.\nNo card will be assigned")
                    f.write('')
                f.close()
                time.sleep(2)

                print("\nWhat is the maximum volume you want for the 'Bottom Left' corner's side ? (Default is 150%).\nEnter a number without '%'...")
                print('')
                answer = input()
                f = open(file_max_volume_bottom_left, 'w')
                try :
                    f.write(str(int(answer)))
                except Exception as e:
                    print( "\nDid you provided a number without '%' ? Max volume will be defined to 150%")
                    f.write('150')
#                    print( "\nAn error occured, look at the error message bellow :\n")
#                    print(e)
                f.close()
                time.sleep(2)

            except Exception as e:
                print( "\nAn error occured, look at the error message bellow :\n")
                print(e)
                exit(1)
            #############################################
            try:
                print("\nDo you want to create an autostart entry for volumouse ? (Y/n)\n(Volumouse will automatically start when the computer start)\nIf not, volumouse autostart entry will be removed ...")
                answer = input()
                if answer.lower() == 'yes' or answer.lower() == 'y' :
                    f = open(os.path.expanduser('~')+"/.config/autostart/volumouse.desktop", "w")
                    f.write("[Desktop Entry]\nName=Volumouse\nGenericName=Controle the volume with the mouse wheel\nComment=Control the volume with the mouse wheel\nExec=python3 '"+__file__+"'\nIcon="+os.path.dirname(os.path.abspath(__file__))+"/icons/volumouse.png\nNoDisplay=false\nHidden=false\nTerminal=false\nType=Application\nVersion="+ str(__version__.__version__)+"\nCategories==AudioVideo;Audio;Utility\nX-GNOME-Autostart-enabled=true\nX-GNOME-Autostart-Delay=7")
                    f.close()
                    print("An autostart entry has been created, reboot the computer and volumouse will start automatically ;-)\n")
                    time.sleep(3)
                else :
                    print("\n\nNo autostart entry will be add for volumouse !")
                    print("\nIf an autostart entry was previously created, it will be deleted ...")
                    os.system("rm "+os.path.expanduser('~')+"/.config/autostart/volumouse.desktop")
                    print("\nIf you want to start volumouse at startup, enter this command as app's directory :")
                    print("python3 '"+os.path.dirname(os.path.abspath(__file__))+"/volumouse.py'")
                    time.sleep(5)
            except Exception as e:
                print( "\nAn error occured, please, look at the error message bellow :\n")
                print(e)
                time.sleep(3)
                print("\nIf you want to start volumouse at startup, enter this command as app's directory :")
                print("python3 '"+os.path.dirname(os.path.abspath(__file__))+"/volumouse.py'")
                time.sleep(5)
            #############################################
            print("\nConfiguration completed, you can now run the command : python3 'volumouse.py'")
            print("Press any key to quit")
            answer = input()
            exit(0)

############################FUNCTION
    print(version)
    info()
    try :
        f = open(file_Top_right_card, 'r')
        Top_right_card = f.read()
        f.close()
    except : pass

    try :
        f = open(file_Bottom_right_card, 'r')
        Bottom_right_card = f.read()
        f.close()
    except : pass

    try :
        f = open(file_Top_left_card, 'r')
        Top_left_card = f.read()
        f.close()
    except : pass

    try :
        f = open(file_Bottom_left_card, 'r')
        Bottom_left_card = f.read()
        f.close()
    except : pass

    try :
        f = open(file_Corner_area, 'r')
        Corner_area = int(f.read())
        f.close()
    except :
        Corner_area = 30

    try :
        f = open(file_Screen_resolution, 'r')
        str_resolution=f.read().replace('(','').replace(')','')
        Screen_resolution = tuple(map(int, str_resolution.split(',')))
        f.close()
    except :
        Screen_resolution = (1920,1080)
        print(Screen_resolution)

    try :
        f = open(file_max_volume_top_right, 'r')
        max_volume_top_right=int(f.read())
        f.close()
    except :
        max_volume_top_right=int(150)
    try :
        f = open(file_max_volume_bottom_right, 'r')
        max_volume_bottom_right=int(f.read())
        f.close()
    except :
        max_volume_bottom_right=int(150)
    try :
        f = open(file_max_volume_top_left, 'r')
        max_volume_top_left=int(f.read())
        f.close()
    except :
        max_volume_top_left=int(150)
    try :
        f = open(file_max_volume_bottom_left, 'r')
        max_volume_bottom_left=int(f.read())
        f.close()
    except :
        max_volume_bottom_left=int(150)

    def volume_up_top_right():
        subprocess.run("pactl set-sink-volume "+Top_right_card+" +5% & pid=$!",shell=True)
        #######"IT COULD ALSO BE FOR EXEMPLE:
        #subprocess.run("pactl set-sink-volume alsa_output.pci-0000_01_00.1.hdmi-stereo-extra3 +5% & pid=$!",shell=True)
        #subprocess.run("pactl set-sink-volume @DEFAULT_SINK@ +5% & pid=$!",shell=True)
        #subprocess.run("amixer set Master 5%+ & pid=$!",shell=True)
        #subprocess.run("pactl set-sink-volume 4 +5% & pid=$!",shell=True)
        #subprocess.run("pacmd set-sink-volume 1 10 & pid=$!",shell=True)
        #subprocess.run("amixer -q sset Master 3%+ & pid=$!",shell=True)

        # use "& pid=$!" end of your command to prevent freezing python script if your command takes long time to process.
    def volume_down_top_right():
        subprocess.run("pactl set-sink-volume "+Top_right_card+" -5% & pid=$!",shell=True)

    def volume_up_bottom_right():
        subprocess.run("pactl set-sink-volume "+Bottom_right_card+" +5% & pid=$!",shell=True)
    def volume_down_bottom_right():
        subprocess.run("pactl set-sink-volume "+Bottom_right_card+" -5% & pid=$!",shell=True)

    def volume_up_top_left():
        subprocess.run("pactl set-sink-volume "+Top_left_card+" +5% & pid=$!",shell=True)    
    def volume_down_top_left():
        subprocess.run("pactl set-sink-volume "+Top_left_card+" -5% & pid=$!",shell=True)

    def volume_up_bottom_left():
        subprocess.run("pactl set-sink-volume "+Bottom_left_card+" +5% & pid=$!",shell=True)    
    def volume_down_bottom_left():
        subprocess.run("pactl set-sink-volume "+Bottom_left_card+" -5% & pid=$!",shell=True)

    try :
        record_dpy = display.Display()

        ctx = record_dpy.record_create_context(
                0,
                [record.AllClients],
                [{
                        'core_requests': (0, 0),
                        'core_replies': (0, 0),
                        'ext_requests': (0, 0, 0, 0),
                        'ext_replies': (0, 0, 0, 0),
                        'delivered_events': (0, 0),
                        'device_events': (X.KeyPress, X.MotionNotify),
                        'errors': (0, 0),
                        'client_started': False,
                        'client_died': False,
                }])

        def record_callback(reply):

            data = reply.data
            while len(data):
                event, data = rq.EventField(None).parse_binary_value(data, record_dpy.display, None, None)
                
                if event.type == X.ButtonPress:
                    print (event.detail, event.root_x, event.root_y)

                    # Let's set up right up corner 

                    if all( [event.root_x > Screen_resolution [0] - Corner_area, event.root_y < Corner_area] ):

                       print ("right up corner detected") 

                       # event.detail 4 means wheel up event

                       if event.detail == 4 : 
                          print ("volume up!")
                          volume_up_top_right() 
                          if int(str(subprocess.check_output("pactl get-sink-volume "+Top_right_card+" | grep % | cut -d '/' -f2 | cut -d'%' -f1", shell=True).rstrip()).replace("b' ","").replace("'","")) > max_volume_top_right :
                            print("Volume exceeded the maximum value : "+str(max_volume_top_right)+"% !")
                            subprocess.run("pactl set-sink-volume "+Top_right_card+" "+str(max_volume_top_right)+"% & pid=$!",shell=True)

                       # event.detail 5 means wheel down event

                       if event.detail == 5 :
                          print ("volume down!")
                          volume_down_top_right()

                    # Let's set up left up corner

                    if all( [event.root_x < Corner_area , event.root_y < Corner_area] ):

                       print ("left up corner detected")

                       if event.detail == 4 :
                          print ("volume up!")
                          volume_up_top_left()
                          if int(str(subprocess.check_output("pactl get-sink-volume "+Top_left_card+" | grep % | cut -d '/' -f2 | cut -d'%' -f1", shell=True).rstrip()).replace("b' ","").replace("'","")) > 100 :
                            print("Volume exceeded the maximum value : "+str(max_volume_top_left)+"% !")
                            subprocess.run("pactl set-sink-volume "+Top_left_card+" "+str(max_volume_top_left)+"% & pid=$!",shell=True)

                       if event.detail == 5 :
                          print ("volume down!")
                          volume_down_top_left() 
          
                    # Let's set up right down corner

                    if all( [event.root_x > Screen_resolution[0] - Corner_area, event.root_y > Screen_resolution[1] - Corner_area] ):

                       print ("right down corner detected")

                       if event.detail == 4 :
                          print ("volume up!")
                          volume_up_bottom_right() 
                          if int(str(subprocess.check_output("pactl get-sink-volume "+Bottom_right_card+" | grep % | cut -d '/' -f2 | cut -d'%' -f1", shell=True).rstrip()).replace("b' ","").replace("'","")) > 100 :
                            print("Volume exceeded the maximum value : "+str(max_volume_bottom_right)+"% !")
                            subprocess.run("pactl set-sink-volume "+Bottom_right_card+" "+str(max_volume_bottom_right)+"% & pid=$!",shell=True)

                       if event.detail == 5 :
                          print ("volume down!")
                          volume_down_bottom_right() 

                    # Let's set up left down corner 

                    if all( [event.root_x < Corner_area , event.root_y > Screen_resolution[1] - Corner_area] ):

                       print ("left down corner detected")

                       if event.detail == 4 :
                          print ("volume up!") 
                          volume_up_bottom_left()
                          if int(str(subprocess.check_output("pactl get-sink-volume "+Bottom_left_card+" | grep % | cut -d '/' -f2 | cut -d'%' -f1", shell=True).rstrip()).replace("b' ","").replace("'","")) > 100 :
                            print("Volume exceeded the maximum value : "+str(max_volume_bottom_left)+"% !")
                            subprocess.run("pactl set-sink-volume "+Bottom_left_card+" "+str(max_volume_bottom_left)+"% & pid=$!",shell=True) 

                       if event.detail == 5 :
                          print ("volume down!") 
                          volume_down_bottom_left() 
                                           
                    
                elif event.type == X.ButtonRelease:

                    print  (event.detail, event.root_x, event.root_y)
                    
                elif event.type == X.MotionNotify:

                    print (event.root_x, event.root_y)
                    

        record_dpy.record_enable_context(ctx, record_callback)
    except Exception as error:
        print( "An error occured. Here is the error message bellow :\n" )
        print(error)
        print( "\nDid you configure volumouse ?")
        print( "Execute : python3 '"+os.path.dirname(os.path.abspath(__file__))+"/volumouse.py' -c")
        exit(1)



if __name__ == "__main__":
    # Catch all untrapped exceptions
    try:
        main()
    except Exception as error:
        print(error)
        exit(1)

