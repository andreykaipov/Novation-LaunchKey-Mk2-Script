"""
internalconstants.py
This file contains constants used by the script to allow it to function properly.
It is not recommended that the user modify these constants, as they may break the script.

"""

import midi

#---------------------------------
# Script Info - Change this if you're forking the project
#---------------------------------

SCRIPT_NAME = "Novation LaunchKey Mk2 Controller Script"
SCRIPT_AUTHOR = "Miguel Guthridge"
SCRIPT_VERSION_MAJOR = 1
SCRIPT_VERSION_MINOR = 2
SCRIPT_VERSION_REVISION = 2
MIN_FL_SCRIPT_VERSION = 4
SCRIPT_URL = "https://github.com/MiguelGuthridge/Novation-LaunchKey-Mk2-Script"
UPDATE_JSON_URL = "https://api.github.com/repos/MiguelGuthridge/Novation-LaunchKey-Mk2-Script/tags"

#---------------------------------
# Device constants
#---------------------------------

DEVICE_UNRECOGNISED = -1
DEVICE_NOT_SET = 0
DEVICE_KEYS_25 = 25
DEVICE_KEYS_49 = 49
DEVICE_KEYS_61 = 61

#---------------------------------

DEVICE_ENQUIRY_MESSAGE = bytes([0xF0, 0x7E, 0x7F, 0x06, 0x01, 0xF7])

#---------------------------------
# Initialisation states
#---------------------------------
INIT_INCOMPLETE = -1
INIT_OK = 0
INIT_UPDATE_AVAILABLE = 1
INIT_API_OUTDATED = 2
INIT_PORT_MISMATCH = 3

#---------------------------------
# Window constants
#---------------------------------

WINDOW_PLAYLIST = midi.widPlaylist
WINDOW_PIANO_ROLL = midi.widPianoRoll
WINDOW_CHANNEL_RACK = midi.widChannelRack
WINDOW_MIXER = midi.widMixer
WINDOW_BROWSER = midi.widBrowser

WINDOW_SCRIPT_OUTPUT = "Script output"
WINDOW_COLOUR_PICKER = "Color selector"
#---------------------------------
# Snapping constants
#---------------------------------

# Mixer snap values
MIXER_VOLUME_SNAP_TO = 0.8 # Snap mixer track volumes to 100%
MIXER_PAN_SNAP_TO = 0.0 # Snap mixer track pannings to Centred
MIXER_STEREO_SEP_SNAP_TO = 0.0 # Snap mixer track stereo separation to Original

# Channel rack snap values
CHANNEL_VOLUME_SNAP_TO = 0.78125 # Snap channel volumes to ~= 78% (FL Default)
CHANNEL_PAN_SNAP_TO = 0.0 # Snap channel pans to Centred

#---------------------------------
# Debug level constants
#---------------------------------

DEBUG_ERROR = "Errors"
DEBUG_PROCESSOR_PERFORMANCE = "Processor performance"
DEBUG_LIGHTING_RESET = "Lighting reset"
DEBUG_LIGHTING_MESSAGE = "Lighting message"
DEBUG_DISPATCH_EVENT = "Dispatch event"
DEBUG_IDLE_PERFORMANCE = "Idle Performance"
