# models.py
# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""Models module for Breakout

This module contains the model classes for the Breakout game. Anything that you
interact with on the screen is model: the paddle, the ball, and any of the bricks.

Just because something is a model does not mean there has to be a special class for
it.  Unless you need something special for your extra gameplay features, both paddle
and individual bricks can just be instances of GRectangle.  There is no need for a
new class in the case of these objects.

We only need a new class when we have to add extra features to our objects.  That
is why we have classes for Ball and BrickWall.  Ball is usually a subclass of GEllipse,
but it needs extra methods for movement and bouncing.  Similarly, BrickWall needs
methods for accessing and removing individual bricks.

You are free to add new models to this module.  You may wish to do this when you add
new features to your game.  If you are unsure about whether to make a new class or 
not, please ask on Piazza."""
import random # To randomly generate the ball velocity
from constants import *
from game2d import *


# PRIMARY RULE: Models are not allowed to access anything in any module other than
# constants.py.  If you need extra information from Gameplay, then it should be
# a parameter in your method, and Gameplay should pass it as a argument when it
# calls the method.


class BrickWall(object):
    """An instance represents the layer of bricks in the game.  When the wall is
    empty, the game is over and the player has won. This model class keeps track of
    all of the bricks in the game, allowing them to be added or removed.
    
    INSTANCE ATTRIBUTES:
        _bricks [list of GRectangle, can be empty]:
            This is the list of currently active bricks in the game.  When a brick
            is destroyed, it is removed from the list.
    
    As you can see, this attribute is hidden.  You may find that you want to access 
    a brick from class Gameplay. It is okay if you do that,  but you MAY NOT 
    ACCESS THE ATTRIBUTE DIRECTLY. You must use a getter and/or setter for any 
    attribute that you need to access in GameController.  Only add the getters and 
    setters that you need.
    
    We highly recommend a getter called getBrickAt(x,y).  This method returns the first
    brick it finds for which the point (x,y) is INSIDE the brick.  This is useful for
    collision detection (e.g. it is a helper for _getCollidingObject).
    
    You will probably want a draw method too.  Otherwise, you need getters in Gameplay
    to draw the individual bricks.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO LAYOUT BRICKS ON THE SCREEN
    
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    


class Ball(GEllipse):
    """Instance is a game ball.
    
    We extend GEllipse because a ball must have additional attributes for velocity.
    This class adds this attributes and manages them.
    
    INSTANCE ATTRIBUTES:
        _vx [int or float]: Velocity in x direction 
        _vy [int or float]: Velocity in y direction 
    
    The class Gameplay will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with no
    setters for the velocities.
    
    How? The only time the ball can change velocities is if it hits an obstacle
    (paddle or brick) or if it hits a wall.  Why not just write methods for these
    instead of using setters?  This cuts down on the amount of code in Gameplay.
    
    In addition you must add the following methods in this class: an __init__
    method to set the starting velocity and a method to "move" the ball.  The
    __init__ method will need to use the __init__ from GEllipse as a helper.
    The move method should adjust the ball position according to  the velocity.
    
    NOTE: The ball does not have to be a GEllipse. It could be an instance
    of GImage (why?). This change is allowed, but you must modify the class
    header up above.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO SET RANDOM VELOCITY
    
    # METHODS TO MOVE AND/OR BOUNCE THE BALL
    
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    


# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE