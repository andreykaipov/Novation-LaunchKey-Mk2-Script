"""
lighting.py
This file contains functions and constants related to controlling lights on the controller.

"""


import time

import internal
import eventconsts
import eventprocessor

# LightMap is sent around to collect colours on UI redraws
class LightMap:
    def __init__(self):
        # 0 = off, 1-127 = colour
        self.reset()
    
    # Set all pads to off      
    def reset(self):
        self.PadMap = [
            [-1, -1],
            [-1, -1],
            [-1, -1],
            [-1, -1],
            [-1, -1],
            [-1, -1],
            [-1, -1],
            [-1, -1],
            [-1, -1]
            ]

    # Set the colour of a pad
    def setPadColour(self, x, y, colour, override = False):
        if self.PadMap[x][y] == -1 or override: # If pad available to map
            self.PadMap[x][y] = colour
            return True
        else: return False
    
    # Sets colours based on state of LightMap object
    def setFromMatrix(self, map):
        for x in range(len(self.PadMap)):
            for y in range(len(self.PadMap[x])):
                if self.PadMap[x][y] == -1:
                    self.setPadColour(x, y, map[x][y])
        return


    # Prevents pad from being overwritten
    def solidifyPad(self, x, y):
        if self.PadMap[x][y] == -1: # If pad available to map
            self.PadMap[x][y] = 0
    
    # Prevents row from being overwritten
    def solidifyRow(self, y):
        for x in range(len(self.PadMap)):
            if self.PadMap[x][y] == -1: self.PadMap[x][y] = 0
    
    # Prevents column from being overwritten
    def solidifyColumn(self, x):
        for y in range(len(self.PadMap)):
            if self.PadMap[x][y] == -1: self.PadMap[x][y] = 0

    # Prevents all pads from being overwritten
    def solidifyAll(self):
        for x in range(len(self.PadMap)):
            for y in range(len(self.PadMap[x])):
                self.solidifyPad(x, y)

    

# Lights manages state of pad lights
class Lights:
    def __init__(self):
        # 0 = off, 1-127 = colour
        self.PadMap = [
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0]
            ]

    # Set all pads to off      
    def reset(self):
        
        internal.sendMidiMessage(0xBF, 0x00, 0x00)
        self.__init__()

    # Set the colour of a pad
    def setPadColour(self, x, y, colour):
        if internal.extendedMode.query(eventconsts.INCONTROL_PADS): 
            internal.sendMidiMessage(0x9F, eventconsts.Pads[x][y], colour)
            
        else: 
            internal.sendMidiMessage(0x9F, eventprocessor.convertPadMapping(eventconsts.Pads[x][y]), colour)
        self.PadMap[x][y] = colour

    
    # Sets colours based on state of LightMap object
    def setFromMap(self, map):
        map.solidifyAll()
        for x in range(len(self.PadMap)):
            for y in range(len(self.PadMap[x])):
                if self.PadMap[x][y] != map.PadMap[x][y]:
                    self.setPadColour(x, y, map.PadMap[x][y])
        return
    
    def redraw(self):
        for x in range(len(self.PadMap)):
            for y in range(len(self.PadMap[x])):
                self.setPadColour(x, y, self.PadMap[x][y])

state = Lights()

# OoooOooOOOooO PREETTTTTYYYY!!!!!!
def lightShow():
    sleepTime = 0.05
    x = 0
    while True:
        # Group 1
        if (x >= 0) and (x < len(rainbowColours)):
            state.setPadColour(0, 1, rainbowColours[x])
        
         # Group 2
        if (x >= 1) and (x < len(rainbowColours) + 1):
            state.setPadColour(1, 1, rainbowColours[x - 1])
            state.setPadColour(0, 0, rainbowColours[x - 1])
        
        # Group 3
        if (x >= 2) and (x < len(rainbowColours) + 2):
            state.setPadColour(2, 1, rainbowColours[x - 2])
            state.setPadColour(1, 0, rainbowColours[x - 2])
        
        # Group 4
        if (x >= 3) and (x < len(rainbowColours) + 3):
            state.setPadColour(3, 1, rainbowColours[x - 3])
            state.setPadColour(2, 0, rainbowColours[x - 3])
        
        # Group 5
        if (x >= 4) and (x < len(rainbowColours) + 4):
            state.setPadColour(4, 1, rainbowColours[x - 4])
            state.setPadColour(3, 0, rainbowColours[x - 4])
        
    
        # Group 6
        if (x >= 5) and (x < len(rainbowColours) + 5):
            state.setPadColour(5, 1, rainbowColours[x - 5])
            state.setPadColour(4, 0, rainbowColours[x - 5])
        
        # Group 7
        if (x >= 6) and (x < len(rainbowColours) + 6):
            state.setPadColour(6, 1, rainbowColours[x - 6])
            state.setPadColour(5, 0, rainbowColours[x - 6])
        
        # Group 8
        if (x >= 7) and (x < len(rainbowColours) + 7):
            state.setPadColour(7, 1, rainbowColours[x - 7])
            state.setPadColour(6, 0, rainbowColours[x - 7])
        
        # Group 9
        if (x >= 8) and (x < len(rainbowColours) + 8):
            state.setPadColour(7, 0, rainbowColours[x - 8])
        
        x += 1
        time.sleep(sleepTime)
        
        if x > len(rainbowColours) + 8: break

    state.reset()



# Define colour codes
COLOUR_TRANSPARENT = -1
COLOUR_OFF = 0
COLOUR_WHITE = 3
COLOUR_RED = 5
COLOUR_GREEN = 25
COLOUR_PINK = 53
COLOUR_BLUE = 46
COLOUR_YELLOW = 13
COLOUR_PURPLE = 49
COLOUR_LILAC = 116
COLOUR_ORANGE = 84

COLOUR_LIGHT_YELLOW = 109
COLOUR_LIGHT_BLUE = 37

rainbowColours = [COLOUR_RED, COLOUR_PINK, COLOUR_PURPLE, COLOUR_BLUE, COLOUR_LIGHT_BLUE, COLOUR_GREEN, COLOUR_YELLOW, COLOUR_ORANGE, COLOUR_OFF]

# Define UI colours
UI_NAV_VERTICAL = COLOUR_LIGHT_BLUE
UI_NAV_HORIZONTAL = COLOUR_PURPLE
UI_ZOOM = COLOUR_BLUE
UI_ACCEPT = COLOUR_GREEN
UI_REJECT = COLOUR_RED
UI_CHOOSE = COLOUR_PURPLE

# Define tool colours
TOOL_PENCIL = COLOUR_ORANGE
TOOL_BRUSH = COLOUR_LIGHT_BLUE
TOOL_DELETE = COLOUR_RED
TOOL_MUTE = COLOUR_PINK
TOOL_SLIP = COLOUR_ORANGE
TOOL_SLICE = COLOUR_LIGHT_BLUE
TOOL_SELECT = COLOUR_YELLOW
TOOL_ZOOM = COLOUR_BLUE
TOOL_PLAYBACK = COLOUR_GREEN

# Define Window Colours
WINDOW_PLAYLIST = COLOUR_GREEN
WINDOW_CHANNEL_RACK = COLOUR_RED
WINDOW_PIANO_ROLL = COLOUR_PINK
WINDOW_MIXER = COLOUR_LIGHT_BLUE
WINDOW_BROWSER = COLOUR_ORANGE

# Define Beat Indicator Colours
BEAT_PAT_BAR = COLOUR_RED
BEAT_PAT_BEAT = COLOUR_ORANGE
BEAT_SONG_BAR = COLOUR_LIGHT_BLUE
BEAT_SONG_BEAT = COLOUR_GREEN


