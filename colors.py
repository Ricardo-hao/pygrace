#!/usr/bin/env python
"""
Amaral Group
Northwestern University
4/5/2006

This module holds the Color class and the dictionary of DEFAULT_COLORS that is
used in the grace.py module.  To include more default colors, just change the
default color dictionary.
"""

_DEFAULT_COLOR_DICTIONARY = {
#   "name":              [index, (R,   G,   B  )]
    "white":             [0,     (255, 255, 255)],
    "black":             [1,     (0  , 0  , 0  )],
    "red":               [2,     (255, 0  , 0  )],
    "green":             [3,     (0  , 255, 0  )],
    "blue":              [4,     (0  , 0  , 255)],
    "yellow":            [5,     (255, 255, 0  )],
    "brown":             [6,     (188, 143, 143)],
    "grey":              [7,     (220, 220, 220)],
    "violet":            [8,     (148, 0  , 211)],
    "cyan":              [9,     (0  , 255, 255)],
    "magenta":           [10,    (255, 0  , 255)],
    "orange":            [11,    (255, 165, 0  )],
    "indigo":            [12,    (114, 33 , 188)],
    "maroon":            [13,    (103, 7  , 72 )],
    "turquoise":         [14,    (64 , 224, 208)],
    "green4":            [15,    (0  , 139, 0  )],
#    "mjs_light_green":   [16,    (225, 235, 210)],
    "mjs_light_green":   [16,    (220, 255, 210)],
    "mjs_dark_blue":     [17,    (  0,   0, 110)],
    "mjs_dark_red":      [18,    (160,   5,   0)],
    "mjs_dark_grey":     [19,    (127, 127, 127)],
    "mjs_light_orange":  [20,    (255, 220, 120)],
    "mjs_color_2":       [21,    (190, 65, 65)],
    "mjs_color_1":       [22,    (65, 190, 65)],
    "mjs_color_0":       [23,    (65, 65, 190)],
    "mjs_color_3":       [24,    (0, 0, 0)],
    "mjs_dark_green":   [25,    (0, 110, 0)],
    }

# _DEFAULT_COLOR_DICTIONARY = {
# #   "name":              [index, (R,   G,   B  )]
#     "white":             [0,     (255, 255, 255)],
#     "black":             [1,     (0  , 0  , 0  )],
#     }

color_brewer = {
#   "name":              [index, (R,   G,   B  )]
    "white":             [0,  (255, 255, 255)],
    "black":             [1,  (  0,   0,   0)],
    "red":               [2,  (228,  26,  28)],
    "blue":              [3,  ( 55, 126, 184)],
    "green":             [4,  ( 77, 175,  74)],
    "violet":            [5,  (152,  78, 163)],
    "orange":            [6,  (255, 127,   0)],
    "yellow":            [7,  (255, 255,  51)],
    "brown":             [8,  (166,  86,  40)],
    "pink":              [9,  (247, 129, 191)],
    "grey":              [10, (153, 153, 153)],
    }

#map color 9 to (220, 255, 210), 
#map color 10 to (0, 85, 0), "mjs_dark_green"
#map color 11 to (230, 230, 255), "mjs_light_blue"
#map color 12 to (0, 0, 110), "mjs_dark_blue"
#map color 13 to (255, 220, 120), "mjs_light_orange"
#map color 14 to (160, 25, 0), "mjs_dark_red"
#map color 15 to (170, 170, 170), "mjs_mid_grey"
#map color 16 to (85, 85, 85), "mjs_dark_grey"

# ================================================================= Color class
class Color:
    """Color class

    Used to map colors to names in xmgrace.

    Example:

    >> print Color(42, 'smarmy', (180, 140, 120))
    @map color 42 to (180, 140, 120), \"smarmy\"

    Later, either 42 or \"smarmy\" can be used to set the color of an xmgrace
    object (eg. @timestamp color 42, or @timestamp color \"smarmy\")
    """
    def __init__(self,
                 index = 0,
                 name = '',
                 (red, green, blue) = (0, 0, 0)
                 ):
        self.index = index
        self.name = name
        self.red, self.green, self.blue = red, green, blue

    def __getitem__(self, name): return getattr(self, name)
    def __setitem__(self, name, value): setattr(self, name, value)

    def __repr__(self):
        return '@map color %i to (%i, %i, %i), "%s"'\
               % (self.index, self.red, self.green, self.blue, self.name)

# Build list of default Colors for dictionary
DEFAULT_COLORS = {}
for name in _DEFAULT_COLOR_DICTIONARY:
    index, (red, green, blue) = _DEFAULT_COLOR_DICTIONARY[name]
    DEFAULT_COLORS[name] = Color(index, name, (red, green, blue))

# =============================================================== Test function
if __name__ == '__main__':
    print Color(0, 'colorOne', (255,155,55))
    print Color(42, 'colorFortyTwo', (33,133,233))
    

