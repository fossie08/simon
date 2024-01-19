import time
import os
import random
import curses

guesses = []
key = []
colours = ["Red","Green","Blue","Yellow"]

class col:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    grey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

def clear():
    os.system('cls||clear')

def Red():
    print(f'{col.red}Red')
    time.sleep(0.5)
    clear()

def Blue():
    print(f'{col.blue}Blue')
    time.sleep(0.5)
    clear()

def Green():
    print(f'{col.green}Green')
    time.sleep(0.5)
    clear()

def Yellow():
    print(f'{col.yellow}Yellow')
    time.sleep(0.5)
    clear()

# define the menu function
def menu(title, classes, color='white'):
  # define the curses wrapper
  def character(stdscr,):
    attributes = {}
    # stuff i copied from the internet that i'll put in the right format later
    icol = {
      1:'red',
      2:'green',
      3:'yellow',
      4:'blue',
      5:'magenta',
      6:'cyan',
      7:'white'
    }
    # put the stuff in the right format
    col = {v: k for k, v in icol.items()}

    # declare the background color

    bc = curses.COLOR_BLACK

    # make the 'normal' format
    curses.init_pair(1, 7, bc)
    attributes['normal'] = curses.color_pair(1)


    # make the 'highlighted' format
    curses.init_pair(2, col[color], bc)
    attributes['highlighted'] = curses.color_pair(2)


    # handle the menu
    c = 0
    option = 0
    while c != 10:

        stdscr.erase() # clear the screen (you can erase this if you want)

        # add the title
        stdscr.addstr(f"{title}\n", curses.color_pair(1))

        # add the options
        for i in range(len(classes)):
            # handle the colors
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            
            # actually add the options

            stdscr.addstr(f'> ', attr)
            stdscr.addstr(f'{classes[i]}' + '\n', attr)
        c = stdscr.getch()

        # handle the arrow keys
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(classes) - 1:
            option += 1
    return option
  return curses.wrapper(character)
clear()
print('READY')
time.sleep(3)
clear()
count = 0
while count >= 0:
    key.append(random.choice(colours))
    count = 1
    for colour in key:
        print(f'{col.reset}{count}')
        if colour == "Red":
            Red()
        elif colour == "Green":
            Green()
        elif colour == "Blue":
            Blue()
        elif colour == "Yellow":
            Yellow()
        time.sleep(0.01)
        count += 1
    count = 0
    for colour in key:
        option = menu(f'SIMON - {count+ 1}', ['Red','Green','Blue','Yellow'], 'blue')
        option_colour = colours[int(option)]
        if option_colour == key[count]:
            count += 1
        else:
            count = -1
            break