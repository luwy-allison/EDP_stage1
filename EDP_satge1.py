#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on 十二月 04, 2020, at 23:03
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'EDP_stage1'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\user\\Desktop\\EDP_stage1\\EDP_satge1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='EDP', color='lightgray', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()

# Initialize components for Routine "phase1"
phase1Clock = core.Clock()
interface_phase1 = visual.ImageStim(
    win=win,
    name='interface_phase1', 
    image='./interface/phase1.png', mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_phase1 = event.Mouse(win=win)
x, y = [None, None]
mouse_phase1.mouseClock = core.Clock()
buttonOK_phase1 = visual.ImageStim(
    win=win,
    name='buttonOK_phase1', 
    image='./interface/buttonOK.png', mask=None,
    ori=0, pos=(0, -300), size=(160,90),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "L"
LClock = core.Clock()
interface_L = visual.ImageStim(
    win=win,
    name='interface_L', 
    image='./interface/L.png', mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_L = event.Mouse(win=win)
x, y = [None, None]
mouse_L.mouseClock = core.Clock()
text_L = visual.TextStim(win=win, name='text_L',
    text='-500',
    font='Arial',
    pos=(-150.6, -75.8), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
slider_L = visual.Slider(win=win, name='slider_L',
    size=(400, 50), pos=(263.5, -189.5), units='pix',
    labels=(-2000,0), ticks=(-2000,0),
    granularity=5, style=('rating', 'whiteOnBlack'),
    color='black', font='HelveticaBold',
    flip=True)
buttonA_L = visual.ImageStim(
    win=win,
    name='buttonA_L', 
    image='./interface/buttonA.png', mask=None,
    ori=0, pos=(-282.4, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
buttonB_L = visual.ImageStim(
    win=win,
    name='buttonB_L', 
    image='./interface/buttonB.png', mask=None,
    ori=0, pos=(263.5, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
down_L = visual.ShapeStim(
    win=win, name='down_L',
    vertices=[[-(50,50)[0]/2.0,-(50,50)[1]/2.0], [+(50,50)[0]/2.0,-(50,50)[1]/2.0], [0,(50,50)[1]/2.0]],
    ori=-90, pos=(10,-180),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
up_L = visual.ShapeStim(
    win=win, name='up_L',
    vertices=[[-(50,50)[0]/2.0,-(50,50)[1]/2.0], [+(50,50)[0]/2.0,-(50,50)[1]/2.0], [0,(50,50)[1]/2.0]],
    ori=90, pos=(517,-180),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "x1pos"
x1posClock = core.Clock()
interface_x1pos = visual.ImageStim(
    win=win,
    name='interface_x1pos', 
    image='./interface/x1pos.png', mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_x1pos = event.Mouse(win=win)
x, y = [None, None]
mouse_x1pos.mouseClock = core.Clock()
text_x1pos = visual.TextStim(win=win, name='text_x1pos',
    text='250',
    font='Arial',
    pos=(376.5, 0), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
buttonA_x1pos = visual.ImageStim(
    win=win,
    name='buttonA_x1pos', 
    image='./interface/buttonA.png', mask=None,
    ori=0, pos=(-282.4, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
buttonB_x1pos = visual.ImageStim(
    win=win,
    name='buttonB_x1pos', 
    image='./interface/buttonB.png', mask=None,
    ori=0, pos=(263.5, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "x1neg"
x1negClock = core.Clock()
interface_x1neg = visual.ImageStim(
    win=win,
    name='interface_x1neg', 
    image='./interface/x1neg.png', mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_x1neg = event.Mouse(win=win)
x, y = [None, None]
mouse_x1neg.mouseClock = core.Clock()
text_L_x1neg = visual.TextStim(win=win, name='text_L_x1neg',
    text='test',
    font='Arial',
    pos=(-150.6, -75.8), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_x1neg = visual.TextStim(win=win, name='text_x1neg',
    text='-250',
    font='Arial',
    pos=(376.5, 0), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
buttonA_x1neg = visual.ImageStim(
    win=win,
    name='buttonA_x1neg', 
    image='./interface/buttonA.png', mask=None,
    ori=0, pos=(-282.4, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
buttonB_x1neg = visual.ImageStim(
    win=win,
    name='buttonB_x1neg', 
    image='./interface/buttonB.png', mask=None,
    ori=0, pos=(263.5, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "phase2"
phase2Clock = core.Clock()
interface_phase2 = visual.ImageStim(
    win=win,
    name='interface_phase2', 
    image='./interface/phase2.png', mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_phase2 = event.Mouse(win=win)
x, y = [None, None]
mouse_phase2.mouseClock = core.Clock()
buttonOK_phase2 = visual.ImageStim(
    win=win,
    name='buttonOK_phase2', 
    image='./interface/buttonOK.png', mask=None,
    ori=0, pos=(0, -300), size=(160,90),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "L2"
L2Clock = core.Clock()
interface_L2 = visual.ImageStim(
    win=win,
    name='interface_L2', 
    image='./interface/L2.png', mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_L2 = event.Mouse(win=win)
x, y = [None, None]
mouse_L2.mouseClock = core.Clock()
text_L2 = visual.TextStim(win=win, name='text_L2',
    text='-500',
    font='Arial',
    pos=(395, -75.8), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_x1pos_L2 = visual.TextStim(win=win, name='text_x1pos_L2',
    text='250',
    font='Arial',
    pos=(395, 75.8), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
buttonA_L2 = visual.ImageStim(
    win=win,
    name='buttonA_L2', 
    image='./interface/buttonA.png', mask=None,
    ori=0, pos=(-282.4, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
buttonB_L2 = visual.ImageStim(
    win=win,
    name='buttonB_L2', 
    image='./interface/buttonB.png', mask=None,
    ori=0, pos=(263.5, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "xipos"
xiposClock = core.Clock()
interface_xipos = visual.ImageStim(
    win=win,
    name='interface_xipos', 
    image='./interface/xipos.png', mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_xipos = event.Mouse(win=win)
x, y = [None, None]
mouse_xipos.mouseClock = core.Clock()
text_xiprepos_xipos = visual.TextStim(win=win, name='text_xiprepos_xipos',
    text='-500',
    font='Arial',
    pos=(-150.6, 75.8), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_L2_xipos = visual.TextStim(win=win, name='text_L2_xipos',
    text='-500',
    font='Arial',
    pos=(395, -75.8), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_xipos = visual.TextStim(win=win, name='text_xipos',
    text='250',
    font='Arial',
    pos=(395, 75.8), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
buttonA_xipos = visual.ImageStim(
    win=win,
    name='buttonA_xipos', 
    image='./interface/buttonA.png', mask=None,
    ori=0, pos=(-282.4, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
buttonB_xipos = visual.ImageStim(
    win=win,
    name='buttonB_xipos', 
    image='./interface/buttonB.png', mask=None,
    ori=0, pos=(263.5, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "phase3"
phase3Clock = core.Clock()
interface_phase3 = visual.ImageStim(
    win=win,
    name='interface_phase3', 
    image='./interface/phase3.png', mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
buttonOK_phase3 = visual.ImageStim(
    win=win,
    name='buttonOK_phase3', 
    image='./interface/buttonOK.png', mask=None,
    ori=0, pos=(0, -300), size=(160,90),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "G2"
G2Clock = core.Clock()
interface_G2 = visual.ImageStim(
    win=win,
    name='interface_G2', 
    image='./interface/G2.png', mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_G2 = event.Mouse(win=win)
x, y = [None, None]
mouse_G2.mouseClock = core.Clock()
text_G2 = visual.TextStim(win=win, name='text_G2',
    text='-500',
    font='Arial',
    pos=(395, 75.8), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_x1neg_G2 = visual.TextStim(win=win, name='text_x1neg_G2',
    text='250',
    font='Arial',
    pos=(395, -75.8), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
buttonA_G2 = visual.ImageStim(
    win=win,
    name='buttonA_G2', 
    image='./interface/buttonA.png', mask=None,
    ori=0, pos=(-282.4, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
buttonB_G2 = visual.ImageStim(
    win=win,
    name='buttonB_G2', 
    image='./interface/buttonB.png', mask=None,
    ori=0, pos=(263.5, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "xineg"
xinegClock = core.Clock()
interface_xineg = visual.ImageStim(
    win=win,
    name='interface_xineg', 
    image='./interface/xineg.png', mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_xineg = event.Mouse(win=win)
x, y = [None, None]
mouse_xineg.mouseClock = core.Clock()
text_xipreneg_xineg = visual.TextStim(win=win, name='text_xipreneg_xineg',
    text='-500',
    font='Arial',
    pos=(-150.6, -75.8), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_G2_xineg = visual.TextStim(win=win, name='text_G2_xineg',
    text='-500',
    font='Arial',
    pos=(395, 75.8), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_xineg = visual.TextStim(win=win, name='text_xineg',
    text='250',
    font='Arial',
    pos=(395, -75.8), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
buttonA_xineg = visual.ImageStim(
    win=win,
    name='buttonA_xineg', 
    image='./interface/buttonA.png', mask=None,
    ori=0, pos=(-282.4, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
buttonB_xineg = visual.ImageStim(
    win=win,
    name='buttonB_xineg', 
    image='./interface/buttonB.png', mask=None,
    ori=0, pos=(263.5, -189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "end"
endClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
welcomeComponents = []
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "phase1"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_phase1
mouse_phase1.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
phase1Components = [interface_phase1, mouse_phase1, buttonOK_phase1]
for thisComponent in phase1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
phase1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "phase1"-------
while continueRoutine:
    # get current time
    t = phase1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=phase1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_phase1* updates
    if interface_phase1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_phase1.frameNStart = frameN  # exact frame index
        interface_phase1.tStart = t  # local t and not account for scr refresh
        interface_phase1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_phase1, 'tStartRefresh')  # time at next scr refresh
        interface_phase1.setAutoDraw(True)
    # *mouse_phase1* updates
    if mouse_phase1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_phase1.frameNStart = frameN  # exact frame index
        mouse_phase1.tStart = t  # local t and not account for scr refresh
        mouse_phase1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_phase1, 'tStartRefresh')  # time at next scr refresh
        mouse_phase1.status = STARTED
        mouse_phase1.mouseClock.reset()
        prevButtonState = mouse_phase1.getPressed()  # if button is down already this ISN'T a new click
    if mouse_phase1.status == STARTED:  # only update if started and not finished!
        buttons = mouse_phase1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonOK_phase1]:
                    if obj.contains(mouse_phase1):
                        gotValidClick = True
                        mouse_phase1.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *buttonOK_phase1* updates
    if buttonOK_phase1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonOK_phase1.frameNStart = frameN  # exact frame index
        buttonOK_phase1.tStart = t  # local t and not account for scr refresh
        buttonOK_phase1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonOK_phase1, 'tStartRefresh')  # time at next scr refresh
        buttonOK_phase1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "phase1"-------
for thisComponent in phase1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('interface_phase1.started', interface_phase1.tStartRefresh)
thisExp.addData('interface_phase1.stopped', interface_phase1.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_phase1.started', mouse_phase1.tStart)
thisExp.addData('mouse_phase1.stopped', mouse_phase1.tStop)
thisExp.nextEntry()
thisExp.addData('buttonOK_phase1.started', buttonOK_phase1.tStartRefresh)
thisExp.addData('buttonOK_phase1.stopped', buttonOK_phase1.tStopRefresh)
# the Routine "phase1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

for n in range(1,6):
    # ------Prepare to start Routine "L"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_L
    mouse_L.clicked_name = []
    gotValidClick = False  # until a click is received
    slider_L.reset()
    last = core.getTime()
    # keep track of which components have finished
    LComponents = [interface_L, mouse_L, text_L, slider_L, buttonA_L, buttonB_L, down_L, up_L]
    for thisComponent in LComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "L"-------
    while continueRoutine:
        # get current time
        t = LClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=LClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *interface_L* updates
        if interface_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            interface_L.frameNStart = frameN  # exact frame index
            interface_L.tStart = t  # local t and not account for scr refresh
            interface_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(interface_L, 'tStartRefresh')  # time at next scr refresh
            interface_L.setAutoDraw(True)
        # *mouse_L* updates
        if mouse_L.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_L.frameNStart = frameN  # exact frame index
            mouse_L.tStart = t  # local t and not account for scr refresh
            mouse_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_L, 'tStartRefresh')  # time at next scr refresh
            mouse_L.status = STARTED
            mouse_L.mouseClock.reset()
            prevButtonState = mouse_L.getPressed()  # if button is down already this ISN'T a new click
        if mouse_L.status == STARTED:  # only update if started and not finished!
            buttons = mouse_L.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [buttonA_L,buttonB_L]:
                        if obj.contains(mouse_L):
                            gotValidClick = True
                            mouse_L.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *text_L* updates
        if text_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_L.frameNStart = frameN  # exact frame index
            text_L.tStart = t  # local t and not account for scr refresh
            text_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_L, 'tStartRefresh')  # time at next scr refresh
            text_L.setAutoDraw(True)
        
        # *slider_L* updates
        if slider_L.status == NOT_STARTED and n==5:
            # keep track of start time/frame for later
            slider_L.frameNStart = frameN  # exact frame index
            slider_L.tStart = t  # local t and not account for scr refresh
            slider_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_L, 'tStartRefresh')  # time at next scr refresh
            slider_L.setAutoDraw(True)
        
        # *buttonA_L* updates
        if buttonA_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttonA_L.frameNStart = frameN  # exact frame index
            buttonA_L.tStart = t  # local t and not account for scr refresh
            buttonA_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonA_L, 'tStartRefresh')  # time at next scr refresh
            buttonA_L.setAutoDraw(True)
        if buttonA_L.status == STARTED:
            if bool(n>4):
                # keep track of stop time/frame for later
                buttonA_L.tStop = t  # not accounting for scr refresh
                buttonA_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(buttonA_L, 'tStopRefresh')  # time at next scr refresh
                buttonA_L.setAutoDraw(False)
        
        # *buttonB_L* updates
        if buttonB_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttonB_L.frameNStart = frameN  # exact frame index
            buttonB_L.tStart = t  # local t and not account for scr refresh
            buttonB_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonB_L, 'tStartRefresh')  # time at next scr refresh
            buttonB_L.setAutoDraw(True)
        if buttonB_L.status == STARTED:
            if bool(n>4):
                # keep track of stop time/frame for later
                buttonB_L.tStop = t  # not accounting for scr refresh
                buttonB_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(buttonB_L, 'tStopRefresh')  # time at next scr refresh
                buttonB_L.setAutoDraw(False)
        
        # *down_L* updates
        if down_L.status == NOT_STARTED and n==5:
            # keep track of start time/frame for later
            down_L.frameNStart = frameN  # exact frame index
            down_L.tStart = t  # local t and not account for scr refresh
            down_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(down_L, 'tStartRefresh')  # time at next scr refresh
            down_L.setAutoDraw(True)
        
        # *up_L* updates
        if up_L.status == NOT_STARTED and n==5:
            # keep track of start time/frame for later
            up_L.frameNStart = frameN  # exact frame index
            up_L.tStart = t  # local t and not account for scr refresh
            up_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(up_L, 'tStartRefresh')  # time at next scr refresh
            up_L.setAutoDraw(True)
        if slider_L.markerPos != None:
            text_L.text = int(slider_L.markerPos)
            if mouse.isPressedIn(down_L):
                this = core.getTime()
                if this - last > 0.05:
                    slider_L.markerPos-=5
                last = this
            if mouse.isPressedIn(up_L):
                this = core.getTime()
                if this -last > 0.05:
                    slider_L.markerPos+=5
                last = this
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "L"-------
    for thisComponent in LComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for thisExp (ExperimentHandler)
    x, y = mouse_L.getPos()
    buttons = mouse_L.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [buttonA_L,buttonB_L]:
            if obj.contains(mouse_L):
                gotValidClick = True
                mouse_L.clicked_name.append(obj.name)
    thisExp.addData('mouse_L.x', x)
    thisExp.addData('mouse_L.y', y)
    thisExp.addData('mouse_L.leftButton', buttons[0])
    thisExp.addData('mouse_L.midButton', buttons[1])
    thisExp.addData('mouse_L.rightButton', buttons[2])
    if len(mouse_L.clicked_name):
        thisExp.addData('mouse_L.clicked_name', mouse_L.clicked_name[0])
    thisExp.nextEntry()
    thisExp.addData('slider_L.response', slider_L.getRating())
    thisExp.addData('slider_L.rt', slider_L.getRT())
    thisExp.addData('slider_L.history', slider_L.getHistory())
    thisExp.addData('slider_L.started', slider_L.tStartRefresh)
    thisExp.addData('slider_L.stopped', slider_L.tStopRefresh)
    #L = int(slider_L.markerPos)
    # the Routine "L" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

# ------Prepare to start Routine "x1pos"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_x1pos
mouse_x1pos.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
x1posComponents = [interface_x1pos, mouse_x1pos, text_x1pos, buttonA_x1pos, buttonB_x1pos]
for thisComponent in x1posComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
x1posClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "x1pos"-------
while continueRoutine:
    # get current time
    t = x1posClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=x1posClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_x1pos* updates
    if interface_x1pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_x1pos.frameNStart = frameN  # exact frame index
        interface_x1pos.tStart = t  # local t and not account for scr refresh
        interface_x1pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_x1pos, 'tStartRefresh')  # time at next scr refresh
        interface_x1pos.setAutoDraw(True)
    # *mouse_x1pos* updates
    if mouse_x1pos.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_x1pos.frameNStart = frameN  # exact frame index
        mouse_x1pos.tStart = t  # local t and not account for scr refresh
        mouse_x1pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_x1pos, 'tStartRefresh')  # time at next scr refresh
        mouse_x1pos.status = STARTED
        mouse_x1pos.mouseClock.reset()
        prevButtonState = mouse_x1pos.getPressed()  # if button is down already this ISN'T a new click
    if mouse_x1pos.status == STARTED:  # only update if started and not finished!
        buttons = mouse_x1pos.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonA_x1pos,buttonB_x1pos]:
                    if obj.contains(mouse_x1pos):
                        gotValidClick = True
                        mouse_x1pos.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *text_x1pos* updates
    if text_x1pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x1pos.frameNStart = frameN  # exact frame index
        text_x1pos.tStart = t  # local t and not account for scr refresh
        text_x1pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x1pos, 'tStartRefresh')  # time at next scr refresh
        text_x1pos.setAutoDraw(True)
    
    # *buttonA_x1pos* updates
    if buttonA_x1pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonA_x1pos.frameNStart = frameN  # exact frame index
        buttonA_x1pos.tStart = t  # local t and not account for scr refresh
        buttonA_x1pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonA_x1pos, 'tStartRefresh')  # time at next scr refresh
        buttonA_x1pos.setAutoDraw(True)
    
    # *buttonB_x1pos* updates
    if buttonB_x1pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonB_x1pos.frameNStart = frameN  # exact frame index
        buttonB_x1pos.tStart = t  # local t and not account for scr refresh
        buttonB_x1pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonB_x1pos, 'tStartRefresh')  # time at next scr refresh
        buttonB_x1pos.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in x1posComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "x1pos"-------
for thisComponent in x1posComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('interface_x1pos.started', interface_x1pos.tStartRefresh)
thisExp.addData('interface_x1pos.stopped', interface_x1pos.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_x1pos.getPos()
buttons = mouse_x1pos.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [buttonA_x1pos,buttonB_x1pos]:
        if obj.contains(mouse_x1pos):
            gotValidClick = True
            mouse_x1pos.clicked_name.append(obj.name)
thisExp.addData('mouse_x1pos.x', x)
thisExp.addData('mouse_x1pos.y', y)
thisExp.addData('mouse_x1pos.leftButton', buttons[0])
thisExp.addData('mouse_x1pos.midButton', buttons[1])
thisExp.addData('mouse_x1pos.rightButton', buttons[2])
if len(mouse_x1pos.clicked_name):
    thisExp.addData('mouse_x1pos.clicked_name', mouse_x1pos.clicked_name[0])
thisExp.addData('mouse_x1pos.started', mouse_x1pos.tStart)
thisExp.addData('mouse_x1pos.stopped', mouse_x1pos.tStop)
thisExp.nextEntry()
thisExp.addData('text_x1pos.started', text_x1pos.tStartRefresh)
thisExp.addData('text_x1pos.stopped', text_x1pos.tStopRefresh)
thisExp.addData('buttonA_x1pos.started', buttonA_x1pos.tStartRefresh)
thisExp.addData('buttonA_x1pos.stopped', buttonA_x1pos.tStopRefresh)
thisExp.addData('buttonB_x1pos.started', buttonB_x1pos.tStartRefresh)
thisExp.addData('buttonB_x1pos.stopped', buttonB_x1pos.tStopRefresh)
# the Routine "x1pos" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "x1neg"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_x1neg
mouse_x1neg.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
x1negComponents = [interface_x1neg, mouse_x1neg, text_L_x1neg, text_x1neg, buttonA_x1neg, buttonB_x1neg]
for thisComponent in x1negComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
x1negClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "x1neg"-------
while continueRoutine:
    # get current time
    t = x1negClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=x1negClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_x1neg* updates
    if interface_x1neg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_x1neg.frameNStart = frameN  # exact frame index
        interface_x1neg.tStart = t  # local t and not account for scr refresh
        interface_x1neg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_x1neg, 'tStartRefresh')  # time at next scr refresh
        interface_x1neg.setAutoDraw(True)
    # *mouse_x1neg* updates
    if mouse_x1neg.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_x1neg.frameNStart = frameN  # exact frame index
        mouse_x1neg.tStart = t  # local t and not account for scr refresh
        mouse_x1neg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_x1neg, 'tStartRefresh')  # time at next scr refresh
        mouse_x1neg.status = STARTED
        mouse_x1neg.mouseClock.reset()
        prevButtonState = mouse_x1neg.getPressed()  # if button is down already this ISN'T a new click
    if mouse_x1neg.status == STARTED:  # only update if started and not finished!
        buttons = mouse_x1neg.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonA_x1neg,buttonB_x1neg]:
                    if obj.contains(mouse_x1neg):
                        gotValidClick = True
                        mouse_x1neg.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *text_L_x1neg* updates
    if text_L_x1neg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L_x1neg.frameNStart = frameN  # exact frame index
        text_L_x1neg.tStart = t  # local t and not account for scr refresh
        text_L_x1neg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L_x1neg, 'tStartRefresh')  # time at next scr refresh
        text_L_x1neg.setAutoDraw(True)
    
    # *text_x1neg* updates
    if text_x1neg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x1neg.frameNStart = frameN  # exact frame index
        text_x1neg.tStart = t  # local t and not account for scr refresh
        text_x1neg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x1neg, 'tStartRefresh')  # time at next scr refresh
        text_x1neg.setAutoDraw(True)
    
    # *buttonA_x1neg* updates
    if buttonA_x1neg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonA_x1neg.frameNStart = frameN  # exact frame index
        buttonA_x1neg.tStart = t  # local t and not account for scr refresh
        buttonA_x1neg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonA_x1neg, 'tStartRefresh')  # time at next scr refresh
        buttonA_x1neg.setAutoDraw(True)
    
    # *buttonB_x1neg* updates
    if buttonB_x1neg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonB_x1neg.frameNStart = frameN  # exact frame index
        buttonB_x1neg.tStart = t  # local t and not account for scr refresh
        buttonB_x1neg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonB_x1neg, 'tStartRefresh')  # time at next scr refresh
        buttonB_x1neg.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in x1negComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "x1neg"-------
for thisComponent in x1negComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('interface_x1neg.started', interface_x1neg.tStartRefresh)
thisExp.addData('interface_x1neg.stopped', interface_x1neg.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_x1neg.getPos()
buttons = mouse_x1neg.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [buttonA_x1neg,buttonB_x1neg]:
        if obj.contains(mouse_x1neg):
            gotValidClick = True
            mouse_x1neg.clicked_name.append(obj.name)
thisExp.addData('mouse_x1neg.x', x)
thisExp.addData('mouse_x1neg.y', y)
thisExp.addData('mouse_x1neg.leftButton', buttons[0])
thisExp.addData('mouse_x1neg.midButton', buttons[1])
thisExp.addData('mouse_x1neg.rightButton', buttons[2])
if len(mouse_x1neg.clicked_name):
    thisExp.addData('mouse_x1neg.clicked_name', mouse_x1neg.clicked_name[0])
thisExp.addData('mouse_x1neg.started', mouse_x1neg.tStart)
thisExp.addData('mouse_x1neg.stopped', mouse_x1neg.tStop)
thisExp.nextEntry()
thisExp.addData('text_L_x1neg.started', text_L_x1neg.tStartRefresh)
thisExp.addData('text_L_x1neg.stopped', text_L_x1neg.tStopRefresh)
thisExp.addData('text_x1neg.started', text_x1neg.tStartRefresh)
thisExp.addData('text_x1neg.stopped', text_x1neg.tStopRefresh)
thisExp.addData('buttonA_x1neg.started', buttonA_x1neg.tStartRefresh)
thisExp.addData('buttonA_x1neg.stopped', buttonA_x1neg.tStopRefresh)
thisExp.addData('buttonB_x1neg.started', buttonB_x1neg.tStartRefresh)
thisExp.addData('buttonB_x1neg.stopped', buttonB_x1neg.tStopRefresh)
# the Routine "x1neg" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "phase2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_phase2
mouse_phase2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
phase2Components = [interface_phase2, mouse_phase2, buttonOK_phase2]
for thisComponent in phase2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
phase2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "phase2"-------
while continueRoutine:
    # get current time
    t = phase2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=phase2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_phase2* updates
    if interface_phase2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_phase2.frameNStart = frameN  # exact frame index
        interface_phase2.tStart = t  # local t and not account for scr refresh
        interface_phase2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_phase2, 'tStartRefresh')  # time at next scr refresh
        interface_phase2.setAutoDraw(True)
    # *mouse_phase2* updates
    if mouse_phase2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_phase2.frameNStart = frameN  # exact frame index
        mouse_phase2.tStart = t  # local t and not account for scr refresh
        mouse_phase2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_phase2, 'tStartRefresh')  # time at next scr refresh
        mouse_phase2.status = STARTED
        mouse_phase2.mouseClock.reset()
        prevButtonState = mouse_phase2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_phase2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_phase2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonOK_phase2]:
                    if obj.contains(mouse_phase2):
                        gotValidClick = True
                        mouse_phase2.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *buttonOK_phase2* updates
    if buttonOK_phase2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonOK_phase2.frameNStart = frameN  # exact frame index
        buttonOK_phase2.tStart = t  # local t and not account for scr refresh
        buttonOK_phase2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonOK_phase2, 'tStartRefresh')  # time at next scr refresh
        buttonOK_phase2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "phase2"-------
for thisComponent in phase2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('interface_phase2.started', interface_phase2.tStartRefresh)
thisExp.addData('interface_phase2.stopped', interface_phase2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_phase2.getPos()
buttons = mouse_phase2.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [buttonOK_phase2]:
        if obj.contains(mouse_phase2):
            gotValidClick = True
            mouse_phase2.clicked_name.append(obj.name)
thisExp.addData('mouse_phase2.x', x)
thisExp.addData('mouse_phase2.y', y)
thisExp.addData('mouse_phase2.leftButton', buttons[0])
thisExp.addData('mouse_phase2.midButton', buttons[1])
thisExp.addData('mouse_phase2.rightButton', buttons[2])
if len(mouse_phase2.clicked_name):
    thisExp.addData('mouse_phase2.clicked_name', mouse_phase2.clicked_name[0])
thisExp.addData('mouse_phase2.started', mouse_phase2.tStart)
thisExp.addData('mouse_phase2.stopped', mouse_phase2.tStop)
thisExp.nextEntry()
thisExp.addData('buttonOK_phase2.started', buttonOK_phase2.tStartRefresh)
thisExp.addData('buttonOK_phase2.stopped', buttonOK_phase2.tStopRefresh)
# the Routine "phase2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "L2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_L2
mouse_L2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
L2Components = [interface_L2, mouse_L2, text_L2, text_x1pos_L2, buttonA_L2, buttonB_L2]
for thisComponent in L2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
L2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "L2"-------
while continueRoutine:
    # get current time
    t = L2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=L2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_L2* updates
    if interface_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_L2.frameNStart = frameN  # exact frame index
        interface_L2.tStart = t  # local t and not account for scr refresh
        interface_L2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_L2, 'tStartRefresh')  # time at next scr refresh
        interface_L2.setAutoDraw(True)
    # *mouse_L2* updates
    if mouse_L2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_L2.frameNStart = frameN  # exact frame index
        mouse_L2.tStart = t  # local t and not account for scr refresh
        mouse_L2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_L2, 'tStartRefresh')  # time at next scr refresh
        mouse_L2.status = STARTED
        mouse_L2.mouseClock.reset()
        prevButtonState = mouse_L2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_L2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_L2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonA_L2,buttonB_L2]:
                    if obj.contains(mouse_L2):
                        gotValidClick = True
                        mouse_L2.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *text_L2* updates
    if text_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L2.frameNStart = frameN  # exact frame index
        text_L2.tStart = t  # local t and not account for scr refresh
        text_L2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L2, 'tStartRefresh')  # time at next scr refresh
        text_L2.setAutoDraw(True)
    
    # *text_x1pos_L2* updates
    if text_x1pos_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x1pos_L2.frameNStart = frameN  # exact frame index
        text_x1pos_L2.tStart = t  # local t and not account for scr refresh
        text_x1pos_L2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x1pos_L2, 'tStartRefresh')  # time at next scr refresh
        text_x1pos_L2.setAutoDraw(True)
    
    # *buttonA_L2* updates
    if buttonA_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonA_L2.frameNStart = frameN  # exact frame index
        buttonA_L2.tStart = t  # local t and not account for scr refresh
        buttonA_L2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonA_L2, 'tStartRefresh')  # time at next scr refresh
        buttonA_L2.setAutoDraw(True)
    
    # *buttonB_L2* updates
    if buttonB_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonB_L2.frameNStart = frameN  # exact frame index
        buttonB_L2.tStart = t  # local t and not account for scr refresh
        buttonB_L2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonB_L2, 'tStartRefresh')  # time at next scr refresh
        buttonB_L2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in L2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "L2"-------
for thisComponent in L2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('interface_L2.started', interface_L2.tStartRefresh)
thisExp.addData('interface_L2.stopped', interface_L2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_L2.getPos()
buttons = mouse_L2.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [buttonA_L2,buttonB_L2]:
        if obj.contains(mouse_L2):
            gotValidClick = True
            mouse_L2.clicked_name.append(obj.name)
thisExp.addData('mouse_L2.x', x)
thisExp.addData('mouse_L2.y', y)
thisExp.addData('mouse_L2.leftButton', buttons[0])
thisExp.addData('mouse_L2.midButton', buttons[1])
thisExp.addData('mouse_L2.rightButton', buttons[2])
if len(mouse_L2.clicked_name):
    thisExp.addData('mouse_L2.clicked_name', mouse_L2.clicked_name[0])
thisExp.addData('mouse_L2.started', mouse_L2.tStart)
thisExp.addData('mouse_L2.stopped', mouse_L2.tStop)
thisExp.nextEntry()
thisExp.addData('text_L2.started', text_L2.tStartRefresh)
thisExp.addData('text_L2.stopped', text_L2.tStopRefresh)
thisExp.addData('text_x1pos_L2.started', text_x1pos_L2.tStartRefresh)
thisExp.addData('text_x1pos_L2.stopped', text_x1pos_L2.tStopRefresh)
thisExp.addData('buttonA_L2.started', buttonA_L2.tStartRefresh)
thisExp.addData('buttonA_L2.stopped', buttonA_L2.tStopRefresh)
thisExp.addData('buttonB_L2.started', buttonB_L2.tStartRefresh)
thisExp.addData('buttonB_L2.stopped', buttonB_L2.tStopRefresh)
# the Routine "L2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "xipos"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_xipos
mouse_xipos.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
xiposComponents = [interface_xipos, mouse_xipos, text_xiprepos_xipos, text_L2_xipos, text_xipos, buttonA_xipos, buttonB_xipos]
for thisComponent in xiposComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xiposClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xipos"-------
while continueRoutine:
    # get current time
    t = xiposClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xiposClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_xipos* updates
    if interface_xipos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_xipos.frameNStart = frameN  # exact frame index
        interface_xipos.tStart = t  # local t and not account for scr refresh
        interface_xipos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_xipos, 'tStartRefresh')  # time at next scr refresh
        interface_xipos.setAutoDraw(True)
    # *mouse_xipos* updates
    if mouse_xipos.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_xipos.frameNStart = frameN  # exact frame index
        mouse_xipos.tStart = t  # local t and not account for scr refresh
        mouse_xipos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_xipos, 'tStartRefresh')  # time at next scr refresh
        mouse_xipos.status = STARTED
        mouse_xipos.mouseClock.reset()
        prevButtonState = mouse_xipos.getPressed()  # if button is down already this ISN'T a new click
    if mouse_xipos.status == STARTED:  # only update if started and not finished!
        buttons = mouse_xipos.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonA_xipos,buttonB_xipos]:
                    if obj.contains(mouse_xipos):
                        gotValidClick = True
                        mouse_xipos.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *text_xiprepos_xipos* updates
    if text_xiprepos_xipos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_xiprepos_xipos.frameNStart = frameN  # exact frame index
        text_xiprepos_xipos.tStart = t  # local t and not account for scr refresh
        text_xiprepos_xipos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_xiprepos_xipos, 'tStartRefresh')  # time at next scr refresh
        text_xiprepos_xipos.setAutoDraw(True)
    
    # *text_L2_xipos* updates
    if text_L2_xipos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L2_xipos.frameNStart = frameN  # exact frame index
        text_L2_xipos.tStart = t  # local t and not account for scr refresh
        text_L2_xipos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L2_xipos, 'tStartRefresh')  # time at next scr refresh
        text_L2_xipos.setAutoDraw(True)
    
    # *text_xipos* updates
    if text_xipos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_xipos.frameNStart = frameN  # exact frame index
        text_xipos.tStart = t  # local t and not account for scr refresh
        text_xipos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_xipos, 'tStartRefresh')  # time at next scr refresh
        text_xipos.setAutoDraw(True)
    
    # *buttonA_xipos* updates
    if buttonA_xipos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonA_xipos.frameNStart = frameN  # exact frame index
        buttonA_xipos.tStart = t  # local t and not account for scr refresh
        buttonA_xipos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonA_xipos, 'tStartRefresh')  # time at next scr refresh
        buttonA_xipos.setAutoDraw(True)
    
    # *buttonB_xipos* updates
    if buttonB_xipos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonB_xipos.frameNStart = frameN  # exact frame index
        buttonB_xipos.tStart = t  # local t and not account for scr refresh
        buttonB_xipos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonB_xipos, 'tStartRefresh')  # time at next scr refresh
        buttonB_xipos.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xiposComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xipos"-------
for thisComponent in xiposComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('interface_xipos.started', interface_xipos.tStartRefresh)
thisExp.addData('interface_xipos.stopped', interface_xipos.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_xipos.getPos()
buttons = mouse_xipos.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [buttonA_xipos,buttonB_xipos]:
        if obj.contains(mouse_xipos):
            gotValidClick = True
            mouse_xipos.clicked_name.append(obj.name)
thisExp.addData('mouse_xipos.x', x)
thisExp.addData('mouse_xipos.y', y)
thisExp.addData('mouse_xipos.leftButton', buttons[0])
thisExp.addData('mouse_xipos.midButton', buttons[1])
thisExp.addData('mouse_xipos.rightButton', buttons[2])
if len(mouse_xipos.clicked_name):
    thisExp.addData('mouse_xipos.clicked_name', mouse_xipos.clicked_name[0])
thisExp.addData('mouse_xipos.started', mouse_xipos.tStart)
thisExp.addData('mouse_xipos.stopped', mouse_xipos.tStop)
thisExp.nextEntry()
thisExp.addData('text_xiprepos_xipos.started', text_xiprepos_xipos.tStartRefresh)
thisExp.addData('text_xiprepos_xipos.stopped', text_xiprepos_xipos.tStopRefresh)
thisExp.addData('text_L2_xipos.started', text_L2_xipos.tStartRefresh)
thisExp.addData('text_L2_xipos.stopped', text_L2_xipos.tStopRefresh)
thisExp.addData('text_xipos.started', text_xipos.tStartRefresh)
thisExp.addData('text_xipos.stopped', text_xipos.tStopRefresh)
thisExp.addData('buttonA_xipos.started', buttonA_xipos.tStartRefresh)
thisExp.addData('buttonA_xipos.stopped', buttonA_xipos.tStopRefresh)
thisExp.addData('buttonB_xipos.started', buttonB_xipos.tStartRefresh)
thisExp.addData('buttonB_xipos.stopped', buttonB_xipos.tStopRefresh)
# the Routine "xipos" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "phase3"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
phase3Components = [interface_phase3, buttonOK_phase3, mouse]
for thisComponent in phase3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
phase3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "phase3"-------
while continueRoutine:
    # get current time
    t = phase3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=phase3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_phase3* updates
    if interface_phase3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_phase3.frameNStart = frameN  # exact frame index
        interface_phase3.tStart = t  # local t and not account for scr refresh
        interface_phase3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_phase3, 'tStartRefresh')  # time at next scr refresh
        interface_phase3.setAutoDraw(True)
    
    # *buttonOK_phase3* updates
    if buttonOK_phase3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonOK_phase3.frameNStart = frameN  # exact frame index
        buttonOK_phase3.tStart = t  # local t and not account for scr refresh
        buttonOK_phase3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonOK_phase3, 'tStartRefresh')  # time at next scr refresh
        buttonOK_phase3.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonOK_phase3]:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "phase3"-------
for thisComponent in phase3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('interface_phase3.started', interface_phase3.tStartRefresh)
thisExp.addData('interface_phase3.stopped', interface_phase3.tStopRefresh)
thisExp.addData('buttonOK_phase3.started', buttonOK_phase3.tStartRefresh)
thisExp.addData('buttonOK_phase3.stopped', buttonOK_phase3.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [buttonOK_phase3]:
        if obj.contains(mouse):
            gotValidClick = True
            mouse.clicked_name.append(obj.name)
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
if len(mouse.clicked_name):
    thisExp.addData('mouse.clicked_name', mouse.clicked_name[0])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "phase3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "G2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_G2
mouse_G2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
G2Components = [interface_G2, mouse_G2, text_G2, text_x1neg_G2, buttonA_G2, buttonB_G2]
for thisComponent in G2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
G2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "G2"-------
while continueRoutine:
    # get current time
    t = G2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=G2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_G2* updates
    if interface_G2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_G2.frameNStart = frameN  # exact frame index
        interface_G2.tStart = t  # local t and not account for scr refresh
        interface_G2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_G2, 'tStartRefresh')  # time at next scr refresh
        interface_G2.setAutoDraw(True)
    # *mouse_G2* updates
    if mouse_G2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_G2.frameNStart = frameN  # exact frame index
        mouse_G2.tStart = t  # local t and not account for scr refresh
        mouse_G2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_G2, 'tStartRefresh')  # time at next scr refresh
        mouse_G2.status = STARTED
        mouse_G2.mouseClock.reset()
        prevButtonState = mouse_G2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_G2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_G2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonA_G2,buttonB_G2]:
                    if obj.contains(mouse_G2):
                        gotValidClick = True
                        mouse_G2.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *text_G2* updates
    if text_G2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_G2.frameNStart = frameN  # exact frame index
        text_G2.tStart = t  # local t and not account for scr refresh
        text_G2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_G2, 'tStartRefresh')  # time at next scr refresh
        text_G2.setAutoDraw(True)
    
    # *text_x1neg_G2* updates
    if text_x1neg_G2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x1neg_G2.frameNStart = frameN  # exact frame index
        text_x1neg_G2.tStart = t  # local t and not account for scr refresh
        text_x1neg_G2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x1neg_G2, 'tStartRefresh')  # time at next scr refresh
        text_x1neg_G2.setAutoDraw(True)
    
    # *buttonA_G2* updates
    if buttonA_G2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonA_G2.frameNStart = frameN  # exact frame index
        buttonA_G2.tStart = t  # local t and not account for scr refresh
        buttonA_G2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonA_G2, 'tStartRefresh')  # time at next scr refresh
        buttonA_G2.setAutoDraw(True)
    
    # *buttonB_G2* updates
    if buttonB_G2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonB_G2.frameNStart = frameN  # exact frame index
        buttonB_G2.tStart = t  # local t and not account for scr refresh
        buttonB_G2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonB_G2, 'tStartRefresh')  # time at next scr refresh
        buttonB_G2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in G2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "G2"-------
for thisComponent in G2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('interface_G2.started', interface_G2.tStartRefresh)
thisExp.addData('interface_G2.stopped', interface_G2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_G2.getPos()
buttons = mouse_G2.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [buttonA_G2,buttonB_G2]:
        if obj.contains(mouse_G2):
            gotValidClick = True
            mouse_G2.clicked_name.append(obj.name)
thisExp.addData('mouse_G2.x', x)
thisExp.addData('mouse_G2.y', y)
thisExp.addData('mouse_G2.leftButton', buttons[0])
thisExp.addData('mouse_G2.midButton', buttons[1])
thisExp.addData('mouse_G2.rightButton', buttons[2])
if len(mouse_G2.clicked_name):
    thisExp.addData('mouse_G2.clicked_name', mouse_G2.clicked_name[0])
thisExp.addData('mouse_G2.started', mouse_G2.tStart)
thisExp.addData('mouse_G2.stopped', mouse_G2.tStop)
thisExp.nextEntry()
thisExp.addData('text_G2.started', text_G2.tStartRefresh)
thisExp.addData('text_G2.stopped', text_G2.tStopRefresh)
thisExp.addData('text_x1neg_G2.started', text_x1neg_G2.tStartRefresh)
thisExp.addData('text_x1neg_G2.stopped', text_x1neg_G2.tStopRefresh)
thisExp.addData('buttonA_G2.started', buttonA_G2.tStartRefresh)
thisExp.addData('buttonA_G2.stopped', buttonA_G2.tStopRefresh)
thisExp.addData('buttonB_G2.started', buttonB_G2.tStartRefresh)
thisExp.addData('buttonB_G2.stopped', buttonB_G2.tStopRefresh)
# the Routine "G2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "xineg"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_xineg
mouse_xineg.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
xinegComponents = [interface_xineg, mouse_xineg, text_xipreneg_xineg, text_G2_xineg, text_xineg, buttonA_xineg, buttonB_xineg]
for thisComponent in xinegComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xinegClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xineg"-------
while continueRoutine:
    # get current time
    t = xinegClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xinegClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_xineg* updates
    if interface_xineg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_xineg.frameNStart = frameN  # exact frame index
        interface_xineg.tStart = t  # local t and not account for scr refresh
        interface_xineg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_xineg, 'tStartRefresh')  # time at next scr refresh
        interface_xineg.setAutoDraw(True)
    # *mouse_xineg* updates
    if mouse_xineg.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_xineg.frameNStart = frameN  # exact frame index
        mouse_xineg.tStart = t  # local t and not account for scr refresh
        mouse_xineg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_xineg, 'tStartRefresh')  # time at next scr refresh
        mouse_xineg.status = STARTED
        mouse_xineg.mouseClock.reset()
        prevButtonState = mouse_xineg.getPressed()  # if button is down already this ISN'T a new click
    if mouse_xineg.status == STARTED:  # only update if started and not finished!
        buttons = mouse_xineg.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonA_xineg,buttonB_xineg]:
                    if obj.contains(mouse_xineg):
                        gotValidClick = True
                        mouse_xineg.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *text_xipreneg_xineg* updates
    if text_xipreneg_xineg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_xipreneg_xineg.frameNStart = frameN  # exact frame index
        text_xipreneg_xineg.tStart = t  # local t and not account for scr refresh
        text_xipreneg_xineg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_xipreneg_xineg, 'tStartRefresh')  # time at next scr refresh
        text_xipreneg_xineg.setAutoDraw(True)
    
    # *text_G2_xineg* updates
    if text_G2_xineg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_G2_xineg.frameNStart = frameN  # exact frame index
        text_G2_xineg.tStart = t  # local t and not account for scr refresh
        text_G2_xineg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_G2_xineg, 'tStartRefresh')  # time at next scr refresh
        text_G2_xineg.setAutoDraw(True)
    
    # *text_xineg* updates
    if text_xineg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_xineg.frameNStart = frameN  # exact frame index
        text_xineg.tStart = t  # local t and not account for scr refresh
        text_xineg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_xineg, 'tStartRefresh')  # time at next scr refresh
        text_xineg.setAutoDraw(True)
    
    # *buttonA_xineg* updates
    if buttonA_xineg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonA_xineg.frameNStart = frameN  # exact frame index
        buttonA_xineg.tStart = t  # local t and not account for scr refresh
        buttonA_xineg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonA_xineg, 'tStartRefresh')  # time at next scr refresh
        buttonA_xineg.setAutoDraw(True)
    
    # *buttonB_xineg* updates
    if buttonB_xineg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonB_xineg.frameNStart = frameN  # exact frame index
        buttonB_xineg.tStart = t  # local t and not account for scr refresh
        buttonB_xineg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonB_xineg, 'tStartRefresh')  # time at next scr refresh
        buttonB_xineg.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xinegComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xineg"-------
for thisComponent in xinegComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('interface_xineg.started', interface_xineg.tStartRefresh)
thisExp.addData('interface_xineg.stopped', interface_xineg.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_xineg.getPos()
buttons = mouse_xineg.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [buttonA_xineg,buttonB_xineg]:
        if obj.contains(mouse_xineg):
            gotValidClick = True
            mouse_xineg.clicked_name.append(obj.name)
thisExp.addData('mouse_xineg.x', x)
thisExp.addData('mouse_xineg.y', y)
thisExp.addData('mouse_xineg.leftButton', buttons[0])
thisExp.addData('mouse_xineg.midButton', buttons[1])
thisExp.addData('mouse_xineg.rightButton', buttons[2])
if len(mouse_xineg.clicked_name):
    thisExp.addData('mouse_xineg.clicked_name', mouse_xineg.clicked_name[0])
thisExp.addData('mouse_xineg.started', mouse_xineg.tStart)
thisExp.addData('mouse_xineg.stopped', mouse_xineg.tStop)
thisExp.nextEntry()
thisExp.addData('text_xipreneg_xineg.started', text_xipreneg_xineg.tStartRefresh)
thisExp.addData('text_xipreneg_xineg.stopped', text_xipreneg_xineg.tStopRefresh)
thisExp.addData('text_G2_xineg.started', text_G2_xineg.tStartRefresh)
thisExp.addData('text_G2_xineg.stopped', text_G2_xineg.tStopRefresh)
thisExp.addData('text_xineg.started', text_xineg.tStartRefresh)
thisExp.addData('text_xineg.stopped', text_xineg.tStopRefresh)
thisExp.addData('buttonA_xineg.started', buttonA_xineg.tStartRefresh)
thisExp.addData('buttonA_xineg.stopped', buttonA_xineg.tStopRefresh)
thisExp.addData('buttonB_xineg.started', buttonB_xineg.tStartRefresh)
thisExp.addData('buttonB_xineg.stopped', buttonB_xineg.tStopRefresh)
# the Routine "xineg" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
