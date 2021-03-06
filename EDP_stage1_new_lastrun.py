﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on 十二月 06, 2020, at 00:54
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'EDP_stage1_new'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\user\\Desktop\\EDP_stage1\\EDP_stage1_new_lastrun.py',
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

# Initialize components for Routine "phase"
phaseClock = core.Clock()
interface_phase = visual.ImageStim(
    win=win,
    name='interface_phase', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
buttonOK_phase = visual.ImageStim(
    win=win,
    name='buttonOK_phase', 
    image='./interface/buttonOK.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
mouse_phase = event.Mouse(win=win)
x, y = [None, None]
mouse_phase.mouseClock = core.Clock()
interface_phase_list=['./interface/phase1.png', './interface/phase2.png', './interface/phase3.png']

# Initialize components for Routine "LE"
LEClock = core.Clock()
interface_LE = visual.ImageStim(
    win=win,
    name='interface_LE', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_LE = event.Mouse(win=win)
x, y = [None, None]
mouse_LE.mouseClock = core.Clock()
buttonA = visual.ImageStim(
    win=win,
    name='buttonA', 
    image='./interface/buttonA.png', mask=None,
    ori=0, pos=(-282.4,-189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
buttonB = visual.ImageStim(
    win=win,
    name='buttonB', 
    image='./interface/buttonB.png', mask=None,
    ori=0, pos=(263.5,-189.5), size=(128,72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
text_Aup_LE = visual.TextStim(win=win, name='text_Aup_LE',
    text=None,
    font='Arial',
    pos=(-150.6,75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_Adown_LE = visual.TextStim(win=win, name='text_Adown_LE',
    text=None,
    font='Arial',
    pos=(-150.6,-75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_Bmiddle_LE = visual.TextStim(win=win, name='text_Bmiddle_LE',
    text=None,
    font='Arial',
    pos=(376.5,0), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_Bup_LE = visual.TextStim(win=win, name='text_Bup_LE',
    text=None,
    font='Arial',
    pos=(395,75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_Bdown_LE = visual.TextStim(win=win, name='text_Bdown_LE',
    text=None,
    font='Arial',
    pos=(395,-75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "interval"
intervalClock = core.Clock()
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(30,30),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "CE"
CEClock = core.Clock()
interface_CE = visual.ImageStim(
    win=win,
    name='interface_CE', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_CE = event.Mouse(win=win)
x, y = [None, None]
mouse_CE.mouseClock = core.Clock()
buttonOK_CE = visual.ImageStim(
    win=win,
    name='buttonOK_CE', 
    image='./interface/buttonOK.png', mask=None,
    ori=0, pos=(0,-300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
slider = visual.Slider(win=win, name='slider',
    size=(400,50), pos=(263.5,-189.5), units=None,
    labels=(-2000,0), ticks=(-2000,0),
    granularity=0, style=['rating', 'whiteOnBlack'],
    color='black', font='HelveticaBold',
    flip=True)
down = visual.ShapeStim(
    win=win, name='down',
    vertices=[[-(50,50)[0]/2.0,-(50,50)[1]/2.0], [+(50,50)[0]/2.0,-(50,50)[1]/2.0], [0,(50,50)[1]/2.0]],
    ori=-90, pos=(10,-189.5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
up = visual.ShapeStim(
    win=win, name='up',
    vertices=[[-(50,50)[0]/2.0,-(50,50)[1]/2.0], [+(50,50)[0]/2.0,-(50,50)[1]/2.0], [0,(50,50)[1]/2.0]],
    ori=90, pos=(517,-189.5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text_Aup_CE = visual.TextStim(win=win, name='text_Aup_CE',
    text=None,
    font='Arial',
    pos=(-150.6,75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_Adown_CE = visual.TextStim(win=win, name='text_Adown_CE',
    text=None,
    font='Arial',
    pos=(-150.6,-75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_Bmiddle_CE = visual.TextStim(win=win, name='text_Bmiddle_CE',
    text=None,
    font='Arial',
    pos=(376.5,0), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
text_Bup_CE = visual.TextStim(win=win, name='text_Bup_CE',
    text=None,
    font='Arial',
    pos=(395,75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
text_Bdown_CE = visual.TextStim(win=win, name='text_Bdown_CE',
    text=None,
    font='Arial',
    pos=(395,-75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "phase"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_phase
mouse_phase.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
phaseComponents = [interface_phase, buttonOK_phase, mouse_phase]
for thisComponent in phaseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
phaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "phase"-------
while continueRoutine:
    # get current time
    t = phaseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=phaseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_phase* updates
    if interface_phase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_phase.frameNStart = frameN  # exact frame index
        interface_phase.tStart = t  # local t and not account for scr refresh
        interface_phase.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_phase, 'tStartRefresh')  # time at next scr refresh
        interface_phase.setAutoDraw(True)
    
    # *buttonOK_phase* updates
    if buttonOK_phase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonOK_phase.frameNStart = frameN  # exact frame index
        buttonOK_phase.tStart = t  # local t and not account for scr refresh
        buttonOK_phase.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonOK_phase, 'tStartRefresh')  # time at next scr refresh
        buttonOK_phase.setAutoDraw(True)
    # *mouse_phase* updates
    if mouse_phase.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_phase.frameNStart = frameN  # exact frame index
        mouse_phase.tStart = t  # local t and not account for scr refresh
        mouse_phase.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_phase, 'tStartRefresh')  # time at next scr refresh
        mouse_phase.status = STARTED
        mouse_phase.mouseClock.reset()
        prevButtonState = mouse_phase.getPressed()  # if button is down already this ISN'T a new click
    if mouse_phase.status == STARTED:  # only update if started and not finished!
        buttons = mouse_phase.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonOK_phase]:
                    if obj.contains(mouse_phase):
                        gotValidClick = True
                        mouse_phase.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phaseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "phase"-------
for thisComponent in phaseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('interface_phase.started', interface_phase.tStartRefresh)
thisExp.addData('interface_phase.stopped', interface_phase.tStopRefresh)
thisExp.addData('buttonOK_phase.started', buttonOK_phase.tStartRefresh)
thisExp.addData('buttonOK_phase.stopped', buttonOK_phase.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "phase" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "LE"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_LE
mouse_LE.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
LEComponents = [interface_LE, mouse_LE, buttonA, buttonB, text_Aup_LE, text_Adown_LE, text_Bmiddle_LE, text_Bup_LE, text_Bdown_LE]
for thisComponent in LEComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LEClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LE"-------
while continueRoutine:
    # get current time
    t = LEClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LEClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_LE* updates
    if interface_LE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_LE.frameNStart = frameN  # exact frame index
        interface_LE.tStart = t  # local t and not account for scr refresh
        interface_LE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_LE, 'tStartRefresh')  # time at next scr refresh
        interface_LE.setAutoDraw(True)
    # *mouse_LE* updates
    if mouse_LE.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_LE.frameNStart = frameN  # exact frame index
        mouse_LE.tStart = t  # local t and not account for scr refresh
        mouse_LE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_LE, 'tStartRefresh')  # time at next scr refresh
        mouse_LE.status = STARTED
        mouse_LE.mouseClock.reset()
        prevButtonState = mouse_LE.getPressed()  # if button is down already this ISN'T a new click
    if mouse_LE.status == STARTED:  # only update if started and not finished!
        buttons = mouse_LE.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonA,buttonB]:
                    if obj.contains(mouse_LE):
                        gotValidClick = True
                        mouse_LE.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *buttonA* updates
    if buttonA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonA.frameNStart = frameN  # exact frame index
        buttonA.tStart = t  # local t and not account for scr refresh
        buttonA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonA, 'tStartRefresh')  # time at next scr refresh
        buttonA.setAutoDraw(True)
    
    # *buttonB* updates
    if buttonB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonB.frameNStart = frameN  # exact frame index
        buttonB.tStart = t  # local t and not account for scr refresh
        buttonB.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonB, 'tStartRefresh')  # time at next scr refresh
        buttonB.setAutoDraw(True)
    
    # *text_Aup_LE* updates
    if text_Aup_LE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Aup_LE.frameNStart = frameN  # exact frame index
        text_Aup_LE.tStart = t  # local t and not account for scr refresh
        text_Aup_LE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Aup_LE, 'tStartRefresh')  # time at next scr refresh
        text_Aup_LE.setAutoDraw(True)
    
    # *text_Adown_LE* updates
    if text_Adown_LE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Adown_LE.frameNStart = frameN  # exact frame index
        text_Adown_LE.tStart = t  # local t and not account for scr refresh
        text_Adown_LE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Adown_LE, 'tStartRefresh')  # time at next scr refresh
        text_Adown_LE.setAutoDraw(True)
    
    # *text_Bmiddle_LE* updates
    if text_Bmiddle_LE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Bmiddle_LE.frameNStart = frameN  # exact frame index
        text_Bmiddle_LE.tStart = t  # local t and not account for scr refresh
        text_Bmiddle_LE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Bmiddle_LE, 'tStartRefresh')  # time at next scr refresh
        text_Bmiddle_LE.setAutoDraw(True)
    
    # *text_Bup_LE* updates
    if text_Bup_LE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Bup_LE.frameNStart = frameN  # exact frame index
        text_Bup_LE.tStart = t  # local t and not account for scr refresh
        text_Bup_LE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Bup_LE, 'tStartRefresh')  # time at next scr refresh
        text_Bup_LE.setAutoDraw(True)
    
    # *text_Bdown_LE* updates
    if text_Bdown_LE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Bdown_LE.frameNStart = frameN  # exact frame index
        text_Bdown_LE.tStart = t  # local t and not account for scr refresh
        text_Bdown_LE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Bdown_LE, 'tStartRefresh')  # time at next scr refresh
        text_Bdown_LE.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LEComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LE"-------
for thisComponent in LEComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_LE.started', mouse_LE.tStart)
thisExp.addData('mouse_LE.stopped', mouse_LE.tStop)
thisExp.nextEntry()
# the Routine "LE" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "interval"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
intervalComponents = [cross]
for thisComponent in intervalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "interval"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = intervalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intervalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cross* updates
    if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cross.frameNStart = frameN  # exact frame index
        cross.tStart = t  # local t and not account for scr refresh
        cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
        cross.setAutoDraw(True)
    if cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cross.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            cross.tStop = t  # not accounting for scr refresh
            cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
            cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intervalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "interval"-------
for thisComponent in intervalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "CE"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_CE
mouse_CE.clicked_name = []
gotValidClick = False  # until a click is received
slider.reset()
last = core.getTime()
# keep track of which components have finished
CEComponents = [interface_CE, mouse_CE, buttonOK_CE, slider, down, up, text_Aup_CE, text_Adown_CE, text_Bmiddle_CE, text_Bup_CE, text_Bdown_CE]
for thisComponent in CEComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CEClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "CE"-------
while continueRoutine:
    # get current time
    t = CEClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CEClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_CE* updates
    if interface_CE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_CE.frameNStart = frameN  # exact frame index
        interface_CE.tStart = t  # local t and not account for scr refresh
        interface_CE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_CE, 'tStartRefresh')  # time at next scr refresh
        interface_CE.setAutoDraw(True)
    # *mouse_CE* updates
    if mouse_CE.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_CE.frameNStart = frameN  # exact frame index
        mouse_CE.tStart = t  # local t and not account for scr refresh
        mouse_CE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_CE, 'tStartRefresh')  # time at next scr refresh
        mouse_CE.status = STARTED
        mouse_CE.mouseClock.reset()
        prevButtonState = mouse_CE.getPressed()  # if button is down already this ISN'T a new click
    if mouse_CE.status == STARTED:  # only update if started and not finished!
        buttons = mouse_CE.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [buttonOK_CE]:
                    if obj.contains(mouse_CE):
                        gotValidClick = True
                        mouse_CE.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *buttonOK_CE* updates
    if buttonOK_CE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttonOK_CE.frameNStart = frameN  # exact frame index
        buttonOK_CE.tStart = t  # local t and not account for scr refresh
        buttonOK_CE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonOK_CE, 'tStartRefresh')  # time at next scr refresh
        buttonOK_CE.setAutoDraw(True)
    
    # *slider* updates
    if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider.frameNStart = frameN  # exact frame index
        slider.tStart = t  # local t and not account for scr refresh
        slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
        slider.setAutoDraw(True)
    
    # *down* updates
    if down.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        down.frameNStart = frameN  # exact frame index
        down.tStart = t  # local t and not account for scr refresh
        down.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(down, 'tStartRefresh')  # time at next scr refresh
        down.setAutoDraw(True)
    
    # *up* updates
    if up.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        up.frameNStart = frameN  # exact frame index
        up.tStart = t  # local t and not account for scr refresh
        up.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(up, 'tStartRefresh')  # time at next scr refresh
        up.setAutoDraw(True)
    
    # *text_Aup_CE* updates
    if text_Aup_CE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Aup_CE.frameNStart = frameN  # exact frame index
        text_Aup_CE.tStart = t  # local t and not account for scr refresh
        text_Aup_CE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Aup_CE, 'tStartRefresh')  # time at next scr refresh
        text_Aup_CE.setAutoDraw(True)
    
    # *text_Adown_CE* updates
    if text_Adown_CE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Adown_CE.frameNStart = frameN  # exact frame index
        text_Adown_CE.tStart = t  # local t and not account for scr refresh
        text_Adown_CE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Adown_CE, 'tStartRefresh')  # time at next scr refresh
        text_Adown_CE.setAutoDraw(True)
    
    # *text_Bmiddle_CE* updates
    if text_Bmiddle_CE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Bmiddle_CE.frameNStart = frameN  # exact frame index
        text_Bmiddle_CE.tStart = t  # local t and not account for scr refresh
        text_Bmiddle_CE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Bmiddle_CE, 'tStartRefresh')  # time at next scr refresh
        text_Bmiddle_CE.setAutoDraw(True)
    
    # *text_Bup_CE* updates
    if text_Bup_CE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Bup_CE.frameNStart = frameN  # exact frame index
        text_Bup_CE.tStart = t  # local t and not account for scr refresh
        text_Bup_CE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Bup_CE, 'tStartRefresh')  # time at next scr refresh
        text_Bup_CE.setAutoDraw(True)
    
    # *text_Bdown_CE* updates
    if text_Bdown_CE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Bdown_CE.frameNStart = frameN  # exact frame index
        text_Bdown_CE.tStart = t  # local t and not account for scr refresh
        text_Bdown_CE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Bdown_CE, 'tStartRefresh')  # time at next scr refresh
        text_Bdown_CE.setAutoDraw(True)
    if slider.markerPos != None:
        #text.text = int(slider.markerPos)
        if mouse.isPressedIn(down):
            this = core.getTime()
            if this - last > 0.05:
                slider.markerPos-=5
            last = this
        if mouse.isPressedIn(up):
            this = core.getTime()
            if this -last > 0.05:
                slider.markerPos+=5
            last = this
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CEComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "CE"-------
for thisComponent in CEComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_CE.started', mouse_CE.tStart)
thisExp.addData('mouse_CE.stopped', mouse_CE.tStop)
thisExp.nextEntry()
thisExp.addData('slider.response', slider.getRating())
thisExp.addData('slider.rt', slider.getRT())
thisExp.addData('down.started', down.tStartRefresh)
thisExp.addData('down.stopped', down.tStopRefresh)
thisExp.addData('up.started', up.tStartRefresh)
thisExp.addData('up.stopped', up.tStopRefresh)
# the Routine "CE" was not non-slip safe, so reset the non-slip timer
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
