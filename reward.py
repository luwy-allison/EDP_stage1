#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on 十二月 06, 2020, at 00:55
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
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
import random

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'EDP_stage1_reward'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\user\\Desktop\\EDP_stage1\\EDP_stage1_new.py',
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
    monitor='testMonitor', color='lightgray', colorSpace='rgb',
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

G = 500
l = -75
g = 75

text_L_list = [-500,None,None,None,None]
text_x1pos_list = [250,None,None,None,None]
text_x1neg_list = [None,None,None,None,None]
text_L2_list = [None,None,None,None,None]
text_x2pos_list = [None,None,None,None,None]
text_x3pos_list = [None,None,None,None,None]
text_x4pos_list = [None,None,None,None,None]
text_x5pos_list = [None,None,None,None,None]
text_x6pos_list = [None,None,None,None,None]
text_x7pos_list = [None,None,None,None,None]
text_x8pos_list = [None,None,None,None,None]
text_G2_list = [None,None,None,None,None]
text_x2neg_list = [None,None,None,None,None]
text_x3neg_list = [None,None,None,None,None]
text_x4neg_list = [None,None,None,None,None]
text_x5neg_list = [None,None,None,None,None]
text_x6neg_list = [None,None,None,None,None]
text_x7neg_list = [None,None,None,None,None]
text_x8neg_list = [None,None,None,None,None]

L = -500
x1pos = 123
x1neg = -66
L2 = -580
x2pos = 523
x3pos = 1180
x4pos = 1388
x5pos = 1471
x6pos = 2266
x7pos = 2742
x8pos = 4090
G2 = 310
x2neg = -451
x3neg = -763
x4neg = -1200
x5neg = -1413
x6neg = -1596
x7neg = -2432
x8neg = -2863
all_point_data_list=[text_L_list,text_x1pos_list,text_x1neg_list,text_L2_list,text_x2pos_list,text_x3pos_list,text_x4pos_list,text_x5pos_list,text_x6pos_list,text_x7pos_list,text_x8pos_list,text_G2_list,text_x2neg_list,text_x3neg_list,text_x4neg_list,text_x5neg_list,text_x6neg_list,text_x7neg_list,text_x8neg_list]

# Initialize components for Routine "random_2"
random_2Clock = core.Clock()

text_random_trial_1 = visual.TextStim(win=win, name='text_random_trial_1',
    text=None,
    font='Arial',
    pos=(-382, 38), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_random_trial_2 = visual.TextStim(win=win, name='text_random_trial_2',
    text=None,
    font='Arial',
    pos=(-226, 38), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_random_trial_3 = visual.TextStim(win=win, name='text_random_trial_3',
    text=None,
    font='Arial',
    pos=(-70, 38), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_random_trial_4 = visual.TextStim(win=win, name='text_random_trial_4',
    text=None,
    font='Arial',
    pos=(70, 38), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_random_trial_5 = visual.TextStim(win=win, name='text_random_trial_5',
    text=None,
    font='Arial',
    pos=(226, 38), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_random_trial_6 = visual.TextStim(win=win, name='text_random_trial_6',
    text=None,
    font='Arial',
    pos=(382, 38), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
buttonStop = visual.ImageStim(
    win=win,
    name='buttonStop', 
    image='./interface/buttonStop.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "outcome"
outcomeClock = core.Clock()
interface_outcome = visual.ImageStim(
    win=win,
    name='interface_outcome', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_G = visual.TextStim(win=win, name='text_G',
    text=G,
    font='Arial',
    pos=(-263.5, 303.2), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_L = visual.TextStim(win=win, name='text_L',
    text=L,
    font='Arial',
    pos=(-263.5, 151.6), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_x1pos = visual.TextStim(win=win, name='text_x1pos',
    text=x1pos,
    font='Arial',
    pos=(-320, 47.4), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_x1neg = visual.TextStim(win=win, name='text_x1neg',
    text=x1neg,
    font='Arial',
    pos=(-320, -37.1), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_x1pos_L2 = visual.TextStim(win=win, name='text_x1pos_L2',
    text=x1pos,
    font='Arial',
    pos=(-263.5, -151.6), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_L2 = visual.TextStim(win=win, name='text_L2',
    text=L2,
    font='Arial',
    pos=(-263.5, -303.2), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_x2pos = visual.TextStim(win=win, name='text_x2pos',
    text=x2pos,
    font='Arial',
    pos=(122.4, 303.2), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_L2_x2pos = visual.TextStim(win=win, name='text_L2_x2pos',
    text=L2,
    font='Arial',
    pos=(122.4, 151.6), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
text_x3pos = visual.TextStim(win=win, name='text_x3pos',
    text=x3pos,
    font='Arial',
    pos=(122.4, 75.8), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
text_L2_x3pos = visual.TextStim(win=win, name='text_L2_x3pos',
    text=L2,
    font='Arial',
    pos=(122.4, -75.8), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
text_x4pos = visual.TextStim(win=win, name='text_x4pos',
    text=x4pos,
    font='Arial',
    pos=(122.4, -151.6), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_L2_x4pos = visual.TextStim(win=win, name='text_L2_x4pos',
    text=L2,
    font='Arial',
    pos=(122.4, -303.2), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
text_x5pos = visual.TextStim(win=win, name='text_x5pos',
    text=x5pos,
    font='Arial',
    pos=(508.2, 303.2), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
text_L2_x5pos = visual.TextStim(win=win, name='text_L2_x5pos',
    text=L2,
    font='Arial',
    pos=(508.2, 151.6), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
text_x6pos = visual.TextStim(win=win, name='text_x6pos',
    text=x6pos,
    font='Arial',
    pos=(508.2, 75.8), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
text_L2_x6pos = visual.TextStim(win=win, name='text_L2_x6pos',
    text=L2,
    font='Arial',
    pos=(508.2, -75.8), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
text_x7pos = visual.TextStim(win=win, name='text_x7pos',
    text=x7pos,
    font='Arial',
    pos=(508.2, -151.6), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
text_L2_x7pos = visual.TextStim(win=win, name='text_L2_x7pos',
    text=L2,
    font='Arial',
    pos=(508.2, -303.2), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
buttonPlay = visual.ImageStim(
    win=win,
    name='buttonPlay', 
    image='./interface/buttonPlay.png', mask=None,
    ori=0, pos=(677.7, -397.9), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
text_G2 = visual.TextStim(win=win, name='text_x1neg_G2',
    text=None,
    font='Arial',
    pos=(-263.5, 75.8), height=35, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
text_x1neg_G2 = visual.TextStim(win=win, name='text_G2',
    text=None,
    font='Arial',
    pos=(-263.5, -75.8), height=35, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-21.0);
text_total = visual.TextStim(win=win, name='text_total',
    text='total:',
    font='Arial',
    pos=(0, -400), height=40, wrapWidth=1280, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-22.0);
text_reversed_trials = visual.TextStim(win=win, name='text_reversed_trials',
    text='反轉的回合：[]',
    font='Arial',
    pos=(0, 400), height=35, wrapWidth=1280, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-23.0);
mouse_outcome = event.Mouse(win=win)
x, y = [None, None]
mouse_outcome.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
 
# ------Prepare to start Routine "random_2"-------
continueRoutine = True
# update component parameters for each repeat
list = [i for i in range(1,20)]
reversed_trial = sorted(random.sample(list,6))
stopPressed = False
nextPressed = False
nowTime = 10000000000
# setup some python lists for storing info about the mouse
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
random_2Components = [text_random_trial_1, text_random_trial_2, text_random_trial_3, text_random_trial_4, text_random_trial_5, text_random_trial_6, buttonStop, mouse]
for thisComponent in random_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
random_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "random_2"-------
while continueRoutine:
    # get current time
    t = random_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=random_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    if frameN%3 == 0 and not stopPressed:
        reversed_trial = sorted(random.sample(list,6))
        text_random_trial_1.text = reversed_trial[0]
        text_random_trial_2.text = reversed_trial[1]
        text_random_trial_3.text = reversed_trial[2]
        text_random_trial_4.text = reversed_trial[3]
        text_random_trial_5.text = reversed_trial[4]
        text_random_trial_6.text = reversed_trial[5]
    
    # *text_random_trial_1* updates
    if text_random_trial_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_random_trial_1.frameNStart = frameN  # exact frame index
        text_random_trial_1.tStart = t  # local t and not account for scr refresh
        text_random_trial_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_random_trial_1, 'tStartRefresh')  # time at next scr refresh
        text_random_trial_1.setAutoDraw(True)
    
    # *text_random_trial_2* updates
    if text_random_trial_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_random_trial_2.frameNStart = frameN  # exact frame index
        text_random_trial_2.tStart = t  # local t and not account for scr refresh
        text_random_trial_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_random_trial_2, 'tStartRefresh')  # time at next scr refresh
        text_random_trial_2.setAutoDraw(True)
    
    # *text_random_trial_3* updates
    if text_random_trial_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_random_trial_3.frameNStart = frameN  # exact frame index
        text_random_trial_3.tStart = t  # local t and not account for scr refresh
        text_random_trial_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_random_trial_3, 'tStartRefresh')  # time at next scr refresh
        text_random_trial_3.setAutoDraw(True)
    
    # *text_random_trial_4* updates
    if text_random_trial_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_random_trial_4.frameNStart = frameN  # exact frame index
        text_random_trial_4.tStart = t  # local t and not account for scr refresh
        text_random_trial_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_random_trial_4, 'tStartRefresh')  # time at next scr refresh
        text_random_trial_4.setAutoDraw(True)
    
    # *text_random_trial_5* updates
    if text_random_trial_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_random_trial_5.frameNStart = frameN  # exact frame index
        text_random_trial_5.tStart = t  # local t and not account for scr refresh
        text_random_trial_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_random_trial_5, 'tStartRefresh')  # time at next scr refresh
        text_random_trial_5.setAutoDraw(True)
    
    # *text_random_trial_6* updates
    if text_random_trial_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_random_trial_6.frameNStart = frameN  # exact frame index
        text_random_trial_6.tStart = t  # local t and not account for scr refresh
        text_random_trial_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_random_trial_6, 'tStartRefresh')  # time at next scr refresh
        text_random_trial_6.setAutoDraw(True)
    
    # *buttonStop* updates
    if buttonStop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonStop.frameNStart = frameN  # exact frame index
        buttonStop.tStart = t  # local t and not account for scr refresh
        buttonStop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonStop, 'tStartRefresh')  # time at next scr refresh
        buttonStop.setAutoDraw(True)
    
    # mouse updates
    prevButtonState = [0,0,0]  # if button is down already this ISN'T a new click
    if not stopPressed and mouse.isPressedIn(buttonStop):  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                if buttonStop.contains(mouse):
                    stopPressed = True
                    reversed_trial = sorted(random.sample(list,6))
                    text_random_trial_1.text = reversed_trial[0]
                    text_random_trial_2.text = reversed_trial[1]
                    text_random_trial_3.text = reversed_trial[2]
                    text_random_trial_4.text = reversed_trial[3]
                    text_random_trial_5.text = reversed_trial[4]
                    text_random_trial_6.text = reversed_trial[5]
                    buttonStop.image = './interface/buttonNext.png'
                    nowTime = core.getTime()
    elif core.getTime()-nowTime > 1 and not nextPressed and mouse.isPressedIn(buttonStop):
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                if buttonStop.contains(mouse):
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in random_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "random_2"-------
for thisComponent in random_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "random_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "outcome"-------
continueRoutine = True
# update component parameters for each repeat
text_reversed_trials.text = "被反轉的回合："+str(reversed_trial[0])+", "+str(reversed_trial[1])+", "+str(reversed_trial[2])+", "+str(reversed_trial[3])+", "+str(reversed_trial[4])+", "+str(reversed_trial[5])
page = 1 # 1 for trials 1~10, 2 for trials 11~19
#outcome_pos = [G,x1pos,x1neg,x1pos,x2pos,x3pos,x4pos,x5pos,x6pos,x7pos,x8pos,G2,G2,G2,G2,G2,G2,G2,G2]
#outcome_neg = [L,x1pos,x1neg,L2,L2,L2,L2,L2,L2,L2,L2,x1neg,x2neg,x3neg,x4neg,x5neg,x6neg,x7neg,x8neg]
outcome_pos = [500, 425, -120, 425, 1140, 1800, 2805, 4090, 7380, 10505, 12040, 310, 310, 310, 310, 310, 310, 310, 310]
outcome_neg = [-500, 425, -120, -580, -580, -580, -580, -580, -580, -580, -580, -120, -400, -965, -1100, -1195, -2145, -2740, -2840]
pos_position = [text_G.pos, text_x1pos.pos,text_x1neg.pos,text_x1pos_L2.pos,text_x2pos.pos,text_x3pos.pos,text_x4pos.pos,text_x5pos.pos,text_x6pos.pos,text_x7pos.pos,text_G.pos,text_G2.pos,text_x1pos_L2.pos,text_x2pos.pos,text_x3pos.pos,text_x4pos.pos,text_x5pos.pos,text_x6pos.pos,text_x7pos.pos]
neg_position = [text_L.pos, text_x1pos.pos,text_x1neg.pos,text_L2.pos,text_L2_x2pos.pos,text_L2_x3pos.pos,text_L2_x4pos.pos,text_L2_x5pos.pos,text_L2_x6pos.pos,text_L2_x7pos.pos,text_L.pos,text_x1neg_G2.pos,text_L2.pos,text_L2_x2pos.pos,text_L2_x3pos.pos,text_L2_x4pos.pos,text_L2_x5pos.pos,text_L2_x6pos.pos,text_L2_x7pos.pos]
outcome_sign = []
outcome_value = []
total_reward = 0
nowTime = 1000000000
playPressed = False
endPressed = False
squareList = []

print(outcome_pos)
print(outcome_neg)

# setup some python lists for storing info about the mouse_outcome
mouse_outcome.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
outcomeComponents = [interface_outcome, text_G, text_L, text_x1pos, text_x1neg, text_x1pos_L2, text_L2, text_x2pos, text_L2_x2pos, text_x3pos, text_L2_x3pos, text_x4pos, text_L2_x4pos, text_x5pos, text_L2_x5pos, text_x6pos, text_L2_x6pos, text_x7pos, text_L2_x7pos, buttonPlay, text_x1neg_G2, text_G2, text_total, text_reversed_trials, mouse_outcome]
for thisComponent in outcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
outcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "outcome"-------
while continueRoutine:
    # get current time
    t = outcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=outcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_outcome* updates
    if interface_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_outcome.frameNStart = frameN  # exact frame index
        interface_outcome.tStart = t  # local t and not account for scr refresh
        interface_outcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_outcome, 'tStartRefresh')  # time at next scr refresh
        interface_outcome.setAutoDraw(True)
    
    # *text_G* updates
    if text_G.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_G.frameNStart = frameN  # exact frame index
        text_G.tStart = t  # local t and not account for scr refresh
        text_G.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_G, 'tStartRefresh')  # time at next scr refresh
        text_G.setAutoDraw(True)
    
    # *text_L* updates
    if text_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L.frameNStart = frameN  # exact frame index
        text_L.tStart = t  # local t and not account for scr refresh
        text_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L, 'tStartRefresh')  # time at next scr refresh
        text_L.setAutoDraw(True)
    
    # *text_x1pos* updates
    if text_x1pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x1pos.frameNStart = frameN  # exact frame index
        text_x1pos.tStart = t  # local t and not account for scr refresh
        text_x1pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x1pos, 'tStartRefresh')  # time at next scr refresh
        text_x1pos.setAutoDraw(True)
    
    # *text_x1neg* updates
    if text_x1neg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x1neg.frameNStart = frameN  # exact frame index
        text_x1neg.tStart = t  # local t and not account for scr refresh
        text_x1neg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x1neg, 'tStartRefresh')  # time at next scr refresh
        text_x1neg.setAutoDraw(True)
    
    # *text_x1pos_L2* updates
    if text_x1pos_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x1pos_L2.frameNStart = frameN  # exact frame index
        text_x1pos_L2.tStart = t  # local t and not account for scr refresh
        text_x1pos_L2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x1pos_L2, 'tStartRefresh')  # time at next scr refresh
        text_x1pos_L2.setAutoDraw(True)
    
    # *text_L2* updates
    if text_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L2.frameNStart = frameN  # exact frame index
        text_L2.tStart = t  # local t and not account for scr refresh
        text_L2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L2, 'tStartRefresh')  # time at next scr refresh
        text_L2.setAutoDraw(True)
    
    # *text_x2pos* updates
    if text_x2pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x2pos.frameNStart = frameN  # exact frame index
        text_x2pos.tStart = t  # local t and not account for scr refresh
        text_x2pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x2pos, 'tStartRefresh')  # time at next scr refresh
        text_x2pos.setAutoDraw(True)
    
    # *text_L2_x2pos* updates
    if text_L2_x2pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L2_x2pos.frameNStart = frameN  # exact frame index
        text_L2_x2pos.tStart = t  # local t and not account for scr refresh
        text_L2_x2pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L2_x2pos, 'tStartRefresh')  # time at next scr refresh
        text_L2_x2pos.setAutoDraw(True)
    
    # *text_x3pos* updates
    if text_x3pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x3pos.frameNStart = frameN  # exact frame index
        text_x3pos.tStart = t  # local t and not account for scr refresh
        text_x3pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x3pos, 'tStartRefresh')  # time at next scr refresh
        text_x3pos.setAutoDraw(True)
    
    # *text_L2_x3pos* updates
    if text_L2_x3pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L2_x3pos.frameNStart = frameN  # exact frame index
        text_L2_x3pos.tStart = t  # local t and not account for scr refresh
        text_L2_x3pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L2_x3pos, 'tStartRefresh')  # time at next scr refresh
        text_L2_x3pos.setAutoDraw(True)
    
    # *text_x4pos* updates
    if text_x4pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x4pos.frameNStart = frameN  # exact frame index
        text_x4pos.tStart = t  # local t and not account for scr refresh
        text_x4pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x4pos, 'tStartRefresh')  # time at next scr refresh
        text_x4pos.setAutoDraw(True)
    
    # *text_L2_x4pos* updates
    if text_L2_x4pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L2_x4pos.frameNStart = frameN  # exact frame index
        text_L2_x4pos.tStart = t  # local t and not account for scr refresh
        text_L2_x4pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L2_x4pos, 'tStartRefresh')  # time at next scr refresh
        text_L2_x4pos.setAutoDraw(True)
    
    # *text_x5pos* updates
    if text_x5pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x5pos.frameNStart = frameN  # exact frame index
        text_x5pos.tStart = t  # local t and not account for scr refresh
        text_x5pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x5pos, 'tStartRefresh')  # time at next scr refresh
        text_x5pos.setAutoDraw(True)
    
    # *text_L2_x5pos* updates
    if text_L2_x5pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L2_x5pos.frameNStart = frameN  # exact frame index
        text_L2_x5pos.tStart = t  # local t and not account for scr refresh
        text_L2_x5pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L2_x5pos, 'tStartRefresh')  # time at next scr refresh
        text_L2_x5pos.setAutoDraw(True)
    
    # *text_x6pos* updates
    if text_x6pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x6pos.frameNStart = frameN  # exact frame index
        text_x6pos.tStart = t  # local t and not account for scr refresh
        text_x6pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x6pos, 'tStartRefresh')  # time at next scr refresh
        text_x6pos.setAutoDraw(True)
    
    # *text_L2_x6pos* updates
    if text_L2_x6pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L2_x6pos.frameNStart = frameN  # exact frame index
        text_L2_x6pos.tStart = t  # local t and not account for scr refresh
        text_L2_x6pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L2_x6pos, 'tStartRefresh')  # time at next scr refresh
        text_L2_x6pos.setAutoDraw(True)
    
    # *text_x7pos* updates
    if text_x7pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x7pos.frameNStart = frameN  # exact frame index
        text_x7pos.tStart = t  # local t and not account for scr refresh
        text_x7pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x7pos, 'tStartRefresh')  # time at next scr refresh
        text_x7pos.setAutoDraw(True)
    
    # *text_L2_x7pos* updates
    if text_L2_x7pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L2_x7pos.frameNStart = frameN  # exact frame index
        text_L2_x7pos.tStart = t  # local t and not account for scr refresh
        text_L2_x7pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L2_x7pos, 'tStartRefresh')  # time at next scr refresh
        text_L2_x7pos.setAutoDraw(True)
    
    # *buttonPlay* updates
    if buttonPlay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonPlay.frameNStart = frameN  # exact frame index
        buttonPlay.tStart = t  # local t and not account for scr refresh
        buttonPlay.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonPlay, 'tStartRefresh')  # time at next scr refresh
        buttonPlay.setAutoDraw(True)
    
    # *text_x1neg_G2* updates
    if text_x1neg_G2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x1neg_G2.frameNStart = frameN  # exact frame index
        text_x1neg_G2.tStart = t  # local t and not account for scr refresh
        text_x1neg_G2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x1neg_G2, 'tStartRefresh')  # time at next scr refresh
        text_x1neg_G2.setAutoDraw(True)
    
    # *text_G2* updates
    if text_G2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_G2.frameNStart = frameN  # exact frame index
        text_G2.tStart = t  # local t and not account for scr refresh
        text_G2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_G2, 'tStartRefresh')  # time at next scr refresh
        text_G2.setAutoDraw(True)
    
    # *text_total* updates
    if text_total.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_total.frameNStart = frameN  # exact frame index
        text_total.tStart = t  # local t and not account for scr refresh
        text_total.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_total, 'tStartRefresh')  # time at next scr refresh
        text_total.setAutoDraw(True)
    
    # *text_reversed_trials* updates
    if text_reversed_trials.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_reversed_trials.frameNStart = frameN  # exact frame index
        text_reversed_trials.tStart = t  # local t and not account for scr refresh
        text_reversed_trials.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_reversed_trials, 'tStartRefresh')  # time at next scr refresh
        text_reversed_trials.setAutoDraw(True)
    if page == 1:
        text_G.text = G
        text_x1pos.text = x1pos
        text_x1neg.text = x1neg
        text_x1pos_L2.text = x1pos
        text_x2pos.text = x2pos
        text_x3pos.text = x3pos
        text_x4pos.text = x4pos
        text_x5pos.text = x5pos
        text_x6pos.text = x6pos
        text_x7pos.text = x7pos
        text_L.text = L2
        text_L2.text = L2
        text_L2_x2pos.text = L2
        text_L2_x3pos.text = L2
        text_L2_x4pos.text = L2
        text_L2_x5pos.text = L2
        text_L2_x6pos.text = L2
        text_L2_x7pos.text = L2
        interface_outcome.image = "./interface/outcome_1.png"
        if not playPressed and mouse_outcome.isPressedIn(buttonPlay):
            playPressed = True
#            squareList = []
            for i in range(0,10):
                # draw loterry (0 = pos, 1 = neg)
                thisOutcome = random.sample([0,1],1)
                outcome_sign.append(thisOutcome[0])
                if thisOutcome[0] == 0:
                    outcome_value.append(outcome_pos[i])
                    temp = visual.Rect(
                        win=win, width=(97.9,60.6)[0], height=(97.9,60.6)[1],
                        ori=0, pos= pos_position[i],
                        lineWidth=3, lineColor='yellow', lineColorSpace='rgb',
                        fillColor=None, fillColorSpace='rgb',
                        opacity=1, depth=-26.0, interpolate=True)
                    squareList.append(temp)
                elif thisOutcome[0] == 1:
                    outcome_value.append(outcome_neg[i])
                    temp = visual.Rect(
                        win=win, width=(97.9,60.6)[0], height=(97.9,60.6)[1],
                        ori=0, pos= neg_position[i],
                        lineWidth=3, lineColor='yellow', lineColorSpace='rgb',
                        fillColor=None, fillColorSpace='rgb',
                        opacity=1, depth=-26.0, interpolate=True)
                    squareList.append(temp)
            for i in range(0,10):
                squareList[i].setAutoDraw(True)
                # calculate reward (0 = pos, 1 = neg)
                if i+1 in reversed_trial:
                    if outcome_sign[i] == 0:
                        total_reward -= outcome_value[i]
                    elif outcome_sign[i] == 1:
                        total_reward += outcome_value[i]
                else :
                    if outcome_sign[i] == 0:
                        total_reward += outcome_value[i]
                    elif outcome_sign[i] == 1:
                        total_reward -= outcome_value[i]
            text_total.text = "total: "+str(total_reward)
            buttonPlay.image = "./interface/buttonNext.png"
            nowTime = core.getTime()
        if core.getTime() - nowTime > 2 and mouse_outcome.isPressedIn(buttonPlay):
            page = 2
            for i in range(0,10):
                squareList[i].setAutoDraw(False)
                text_x1neg.setAutoDraw(False)
                text_x1pos.setAutoDraw(False)
            buttonPlay.image = "./interface/buttonPlay.png"
            interface_outcome.image = "./interface/outcome_2.png"
            playPressed = False
            win.flip()
            
    if page == 2:
#        interface_outcome.image = "./interface/outcome_2.png"
        text_G.text = x8pos
        text_G2.text = G2
        text_x1pos_L2.text = G2
        text_x2pos.text = G2
        text_x3pos.text = G2
        text_x4pos.text = G2
        text_x5pos.text = G2
        text_x6pos.text = G2
        text_x7pos.text = G2
        text_L.text = L2
        text_x1neg_G2.text = x1neg
        text_L2.text = x2neg
        text_L2_x2pos.text = x3neg
        text_L2_x3pos.text = x4neg
        text_L2_x4pos.text = x5neg
        text_L2_x5pos.text = x6neg
        text_L2_x6pos.text = x7neg
        text_L2_x7pos.text = x8neg
        if not playPressed and mouse_outcome.isPressedIn(buttonPlay):
            playPressed = True
            for i in range(0,9):
                # draw loterry (0 = pos, 1 = neg)
                thisOutcome = random.sample([0,1],1)
                outcome_sign.append(thisOutcome[0])
                if thisOutcome[0] == 0:
                    outcome_value.append(outcome_pos[i+10])
                    temp = visual.Rect(
                        win=win, width=(97.9,60.6)[0], height=(97.9,60.6)[1],
                        ori=0, pos= pos_position[i+10],
                        lineWidth=3, lineColor='yellow', lineColorSpace='rgb',
                        fillColor=None, fillColorSpace='rgb',
                        opacity=1, depth=-26.0, interpolate=True)
                    squareList.append(temp)
                elif thisOutcome[0] == 1:
                    outcome_value.append(outcome_neg[i+10])
                    temp = visual.Rect(
                        win=win, width=(97.9,60.6)[0], height=(97.9,60.6)[1],
                        ori=0, pos= neg_position[i+10],
                        lineWidth=3, lineColor='yellow', lineColorSpace='rgb',
                        fillColor=None, fillColorSpace='rgb',
                        opacity=1, depth=-26.0, interpolate=True)
                    squareList.append(temp)
            for i in range(0,9):
                squareList[i+10].setAutoDraw(True)
                # calculate reward (0 = pos, 1 = neg)
                if i+1+10 in reversed_trial:
                    if outcome_sign[i+10] == 0:
                        total_reward -= outcome_value[i+10]
                    elif outcome_sign[i+10] == 1:
                        total_reward += outcome_value[i+10]
                else :
                    if outcome_sign[i+10] == 0:
                        total_reward += outcome_value[i+10]
                    elif outcome_sign[i+10] == 1:
                        total_reward -= outcome_value[i+10]
            final_reward = total_reward / 50
            text_total.text = "total: "+str(total_reward)+' / 50 = '+str(final_reward)
            buttonPlay.image = "./interface/buttonEnd.png"
            nowTime = core.getTime()
            
        if playPressed and not endPressed and core.getTime() - nowTime > 2 and mouse_outcome.isPressedIn(buttonPlay):
            continueRoutine = False
                

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in outcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
print(outcome_value)
# -------Ending Routine "outcome"-------
for thisComponent in outcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)

if len(mouse_outcome.clicked_name):
    thisExp.addData('mouse_outcome.clicked_name', mouse_outcome.clicked_name[0])
thisExp.nextEntry()
# the Routine "outcome" was not non-slip safe, so reset the non-slip timer
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
