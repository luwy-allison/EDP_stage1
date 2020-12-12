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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'EDP_stage1_new'  # from the Builder filename that created this script
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
L = text_L_list[-1]
x1pos = text_x1pos_list[-1]
x1neg = text_x1neg_list[-1]
L2 = text_L2_list[-1]
x2pos = text_x2pos_list[-1]
x3pos = text_x3pos_list[-1]
x4pos = text_x4pos_list[-1]
x5pos = text_x5pos_list[-1]
x6pos = text_x6pos_list[-1]
x7pos = text_x7pos_list[-1]
x8pos = text_x8pos_list[-1]
G2 = text_G2_list[-1]
x2neg = text_x2neg_list[-1]
x3neg = text_x3neg_list[-1]
x4neg = text_x4neg_list[-1]
x5neg = text_x5neg_list[-1]
x6neg = text_x6neg_list[-1]
x7neg = text_x7neg_list[-1]
x8neg = text_x8neg_list[-1]
all_point_data_list=[text_L_list,text_x1pos_list,text_x1neg_list,text_L2_list,text_x2pos_list,text_x3pos_list,text_x4pos_list,text_x5pos_list,text_x6pos_list,text_x7pos_list,text_x8pos_list,text_G2_list,text_x2neg_list,text_x3neg_list,text_x4neg_list,text_x5neg_list,text_x6neg_list,text_x7neg_list,text_x8neg_list]

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
interface_list = ['./interface/L.png', './interface/x1pos.png','./interface/x1neg.png', './interface/L2.png', './interface/xipos.png', './interface/G2.png', './interface/xineg.png']

# Initialize components for Routine "TO"
TOClock = core.Clock()
interface_TO = visual.ImageStim(
    win=win,
    name='interface_TO', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(1280,720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_TO = event.Mouse(win=win)
x, y = [None, None]
mouse_TO.mouseClock = core.Clock()
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
text_Aup_TO = visual.TextStim(win=win, name='text_Aup_TO',
    text=None,
    font='Arial',
    pos=(-150.6,75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_Adown_TO = visual.TextStim(win=win, name='text_Adown_TO',
    text=None,
    font='Arial',
    pos=(-150.6,-75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_Bmiddle_TO = visual.TextStim(win=win, name='text_Bmiddle_TO',
    text=None,
    font='Arial',
    pos=(376.5,0), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_Bup_TO = visual.TextStim(win=win, name='text_Bup_TO',
    text=None,
    font='Arial',
    pos=(395,75.8), height=35, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_Bdown_TO = visual.TextStim(win=win, name='text_Bdown_TO',
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
figure_frame= visual.Rect(
    win=win, name='figure_frame',
    width=(102,57)[0], height=(102,57)[1],
    ori=0, pos=(-150.6,-75.8),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
slider = visual.Slider(win=win, name='slider',
    size=(400,40), pos=(0,-189.5), units=None,
    labels=None, ticks=(-2000,0),
    granularity=5, style=('rating', 'whiteOnBlack'),
    color='black', font='HelveticaBold',
    flip=True)
down = visual.ShapeStim(
    win=win, name='down',
    vertices=[[-(50,50)[0]/2.0,-(50,50)[1]/2.0], [+(50,50)[0]/2.0,-(50,50)[1]/2.0], [0,(50,50)[1]/2.0]],
    ori=-90, pos=(-253.5,-189.5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
up = visual.ShapeStim(
    win=win, name='up',
    vertices=[[-(50,50)[0]/2.0,-(50,50)[1]/2.0], [+(50,50)[0]/2.0,-(50,50)[1]/2.0], [0,(50,50)[1]/2.0]],
    ori=90, pos=(253.5,-189.5),
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
 
for i in range(0,19):
    text_Aup_CE.text = ''
    text_Adown_CE.text = ''
    text_Bmiddle_CE.text = ''
    text_Bup_CE.text = ''
    text_Bdown_CE.text = ''
    text_Aup_TO.text = ''
    text_Adown_TO.text = ''
    text_Bmiddle_TO.text = ''
    text_Bup_TO.text = ''
    text_Bdown_TO.text = ''

    if i == 0:
        # L
        interface_phase.image = interface_phase_list[0]
        interface_CE.image = interface_list[0]
        interface_TO.image = interface_list[0]
        text_Adown_CE.color = 'red'
        text_Adown_TO.color = 'red'
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

    elif i == 1:
        # x1pos
        interface_CE.image = interface_list[1]
        interface_TO.image = interface_list[1]
        text_Bmiddle_CE.color = 'blue'
        text_Bmiddle_TO.color = 'blue'
    elif i == 2:
        # x1neg
        interface_CE.image = interface_list[2]
        interface_TO.image = interface_list[2]
        text_Bmiddle_CE.color = 'red'
        text_Bmiddle_TO.color = 'red'
    elif i == 3:
        # L2
        interface_phase.image = interface_phase_list[1]
        interface_CE.image = interface_list[3]
        interface_TO.image = interface_list[3]
        text_Bup_CE.color = 'blue'
        text_Bup_TO.color = 'blue'
        text_Bdown_CE.color = 'red'
        text_Bdown_TO.color = 'red'
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

    elif i >= 4 and i < 11:
        # xipos
        interface_CE.image = interface_list[4]
        interface_TO.image = interface_list[4]
        text_Aup_CE.color = 'blue'
        text_Aup_TO.color = 'blue'
    elif i == 11:
        # G2
        interface_phase.image = interface_phase_list[2]
        interface_CE.image = interface_list[5]
        interface_TO.image = interface_list[5]
        
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

    else:
        # xineg
        interface_CE.image = interface_list[6]
        interface_TO.image = interface_list[6]

    target = all_point_data_list[i][0]
    step = target
    sliderMax = target
    slidermin = target
    for n in range(0,4):
        # ------Prepare to start Routine "TO"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_TO
        mouse_TO.clicked_name = []
        gotValidClick = False  # until a click is received
        
        if i == 0:
            text_Adown_TO.text = text_L_list[n]
        elif i == 1:
            text_Bmiddle_TO.text = text_x1pos_list[n]
        elif i == 2:
            text_Adown_TO.text = L
            text_Bmiddle_TO.text = text_x1neg_list[n]
        elif i == 3:
            text_Bup_TO.text = x1pos
            text_Bdown_TO.text = text_L2_list[n]
        elif i == 4:
            text_Aup_TO.text = x1pos
            text_Bup_TO.text = text_x2pos_list[n]
            text_Bdown_TO.text = L2
        elif i == 5:
            text_Aup_TO.text = x2pos
            text_Bup_TO.text = text_x3pos_list[n]
            text_Bdown_TO.text = L2
        elif i == 6:
            text_Aup_TO.text = x3pos
            text_Bup_TO.text = text_x4pos_list[n]
            text_Bdown_TO.text = L2
        elif i == 7:
            text_Aup_TO.text = x4pos
            text_Bup_TO.text = text_x5pos_list[n]
            text_Bdown_TO.text = L2
        elif i == 8:
            text_Aup_TO.text = x5pos
            text_Bup_TO.text = text_x6pos_list[n]
            text_Bdown_TO.text = L2
        elif i == 9:
            text_Aup_TO.text = x6pos
            text_Bup_TO.text = text_x7pos_list[n]
            text_Bdown_TO.text = L2
        elif i == 10:
            text_Aup_TO.text = x7pos
            text_Bup_TO.text = text_x8pos_list[n]
            text_Bdown_TO.text = L2
        elif i == 11:
            text_Bup_TO.text = text_G2_list[n]
            text_Bdown_TO.text = x1neg
        elif i == 12:
            text_Adown_TO.text = x1neg
            text_Bup_TO.text = G2
            text_Bdown_TO.text = text_x2neg_list[n]
        elif i == 13:
            text_Adown_TO.text = x2neg
            text_Bup_TO.text = G2
            text_Bdown_TO.text = text_x3neg_list[n]
        elif i == 14:
            text_Adown_TO.text = x3neg
            text_Bup_TO.text = G2
            text_Bdown_TO.text = text_x4neg_list[n]
        elif i == 15:
            text_Adown_TO.text = x4neg
            text_Bup_TO.text = G2
            text_Bdown_TO.text = text_x5neg_list[n]
        elif i == 16:
            text_Adown_TO.text = x5neg
            text_Bup_TO.text = G2
            text_Bdown_TO.text = text_x6neg_list[n]
        elif i == 17:
            text_Adown_TO.text = x6neg
            text_Bup_TO.text = G2
            text_Bdown_TO.text = text_x7neg_list[n]
        elif i == 18:
            text_Adown_TO.text = x7neg
            text_Bup_TO.text = G2
            text_Bdown_TO.text = text_x8neg_list[n]
        
        # keep track of which components have finished
        TOComponents = [interface_TO, mouse_TO, buttonA, buttonB, text_Aup_TO, text_Adown_TO, text_Bmiddle_TO, text_Bup_TO, text_Bdown_TO]
        for thisComponent in TOComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TOClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "TO"-------
        while continueRoutine:
            # get current time
            t = TOClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TOClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *interface_TO* updates
            if interface_TO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                interface_TO.frameNStart = frameN  # exact frame index
                interface_TO.tStart = t  # local t and not account for scr refresh
                interface_TO.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(interface_TO, 'tStartRefresh')  # time at next scr refresh
                interface_TO.setAutoDraw(True)
            # *mouse_TO* updates
            if mouse_TO.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_TO.frameNStart = frameN  # exact frame index
                mouse_TO.tStart = t  # local t and not account for scr refresh
                mouse_TO.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_TO, 'tStartRefresh')  # time at next scr refresh
                mouse_TO.status = STARTED
                mouse_TO.mouseClock.reset()
                prevButtonState = mouse_TO.getPressed()  # if button is down already this ISN'T a new click
            if mouse_TO.status == STARTED:  # only update if started and not finished!
                buttons = mouse_TO.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [buttonA,buttonB]:
                            if obj.contains(mouse_TO):
                                gotValidClick = True
                                mouse_TO.clicked_name.append(obj.name)
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
            
            # *text_Aup_TO* updates
            if text_Aup_TO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Aup_TO.frameNStart = frameN  # exact frame index
                text_Aup_TO.tStart = t  # local t and not account for scr refresh
                text_Aup_TO.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Aup_TO, 'tStartRefresh')  # time at next scr refresh
                text_Aup_TO.setAutoDraw(True)
            
            # *text_Adown_TO* updates
            if text_Adown_TO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Adown_TO.frameNStart = frameN  # exact frame index
                text_Adown_TO.tStart = t  # local t and not account for scr refresh
                text_Adown_TO.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Adown_TO, 'tStartRefresh')  # time at next scr refresh
                text_Adown_TO.setAutoDraw(True)
            
            # *text_Bmiddle_TO* updates
            if text_Bmiddle_TO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Bmiddle_TO.frameNStart = frameN  # exact frame index
                text_Bmiddle_TO.tStart = t  # local t and not account for scr refresh
                text_Bmiddle_TO.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Bmiddle_TO, 'tStartRefresh')  # time at next scr refresh
                text_Bmiddle_TO.setAutoDraw(True)
            
            # *text_Bup_TO* updates
            if text_Bup_TO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Bup_TO.frameNStart = frameN  # exact frame index
                text_Bup_TO.tStart = t  # local t and not account for scr refresh
                text_Bup_TO.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Bup_TO, 'tStartRefresh')  # time at next scr refresh
                text_Bup_TO.setAutoDraw(True)
            
            # *text_Bdown_TO* updates
            if text_Bdown_TO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Bdown_TO.frameNStart = frameN  # exact frame index
                text_Bdown_TO.tStart = t  # local t and not account for scr refresh
                text_Bdown_TO.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Bdown_TO, 'tStartRefresh')  # time at next scr refresh
                text_Bdown_TO.setAutoDraw(True)

            if mouse_TO.isPressedIn(buttonA):
                if i == 0:
                    sliderMax = int(target)
                    target = target-(1/(2**(n+1)))*abs(step)
                else:
                    slidermin = int(target)
                    target = target+(1/(2**(n+1)))*abs(step)
                
            elif mouse_TO.isPressedIn(buttonB):
                if i == 0 :
                    slidermin = int(target)
                    target = target+(1/(2**(n+1)))*abs(step)
                else:
                    sliderMax = int(target)
                    target = target-(1/(2**(n+1)))*abs(step)
                    
            if target%5 !=0 :
                target = (round(target/5))*5
            target = int(target)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TOComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "TO"-------
        for thisComponent in TOComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        if i == 0:
            text_L_list[n+1] = target
        elif i == 1:
            text_x1pos_list[n+1] = target
        elif i == 2:
            text_x1neg_list[n+1] = target
        elif i == 3:
            text_L2_list[n+1] = target
        elif i == 4:
            text_x2pos_list[n+1] = target
        elif i == 5:
            text_x3pos_list[n+1] = target
        elif i == 6:
            text_x4pos_list[n+1] = target
        elif i == 7:
            text_x5pos_list[n+1] = target
        elif i == 8:
            text_x6pos_list[n+1] = target
        elif i == 9:
            text_x7pos_list[n+1] = target
        elif i == 10:
            text_x8pos_list[n+1] = target
        elif i == 11:
            text_G2_list[n+1] = target
        elif i == 12:
            text_x2neg_list[n+1] = target
        elif i == 13:
            text_x3neg_list[n+1] = target
        elif i == 14:
            text_x4neg_list[n+1] = target
        elif i == 15:
            text_x5neg_list[n+1] = target
        elif i == 16:
            text_x6neg_list[n+1] = target
        elif i == 17:
            text_x7neg_list[n+1] = target
        elif i == 18:
            text_x8neg_list[n+1] = target
            
        # store data for thisExp (ExperimentHandler)
        thisExp.addData('mouse_TO.started', mouse_TO.tStart)
        thisExp.addData('mouse_TO.stopped', mouse_TO.tStop)
        thisExp.nextEntry()
        # the Routine "TO" was not non-slip safe, so reset the non-slip timer
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
    if i == 0:
#        text_Adown_CE.text = text_L_list[n]
        figure_frame.pos = text_Adown_CE.pos
    elif i == 1:
#        text_Bmiddle_CE.text = text_x1pos_list[n]
        figure_frame.pos = text_Bmiddle_CE.pos
    elif i == 2:
        text_Adown_CE.text = L
#        text_Bmiddle_CE.text = text_x1neg_list[n]
        figure_frame.pos = text_Bmiddle_CE.pos
    elif i == 3:
        text_Bup_CE.text = x1pos
#        text_Bdown_CE.text = text_L2_list[n]
        figure_frame.pos = text_Bdown_CE.pos
    elif i == 4:
        text_Aup_CE.text = x1pos
#        text_Bup_CE.text = text_x2pos_list[n]
        text_Bdown_CE.text = L2
        figure_frame.pos = text_Bup_CE.pos
    elif i == 5:
        text_Aup_CE.text = x2pos
#        text_Bup_CE.text = text_x3pos_list[n]
        text_Bdown_CE.text = L2
        figure_frame.pos = text_Bup_CE.pos
    elif i == 6:
        text_Aup_CE.text = x3pos
#        text_Bup_CE.text = text_x4pos_list[n]
        text_Bdown_CE.text = L2
        figure_frame.pos = text_Bup_CE.pos
    elif i == 7:
        text_Aup_CE.text = x4pos
#        text_Bup_CE.text = text_x5pos_list[n]
        text_Bdown_CE.text = L2
        figure_frame.pos = text_Bup_CE.pos
    elif i == 8:
        text_Aup_CE.text = x5pos
#        text_Bup_CE.text = text_x6pos_list[n]
        text_Bdown_CE.text = L2
        figure_frame.pos = text_Bup_CE.pos
    elif i == 9:
        text_Aup_CE.text = x6pos
#        text_Bup_CE.text = text_x7pos_list[n]
        text_Bdown_CE.text = L2
        figure_frame.pos = text_Bup_CE.pos
    elif i == 10:
        text_Aup_CE.text = x7pos
#        text_Bup_CE.text = text_x8pos_list[n]
        text_Bdown_CE.text = L2
        figure_frame.pos = text_Bup_CE.pos
    elif i == 11:
#        text_Bup_CE.text = text_G2_list[n]
        text_Bdown_CE.text = x1neg
        figure_frame.pos = text_Bup_CE.pos
    elif i == 12:
        text_Adown_CE.text = x1neg
        text_Bup_CE.text = G2
#        text_Bdown_CE.text = text_x2neg_list[n]
        figure_frame.pos = text_Bdown_CE.pos
    elif i == 13:
        text_Adown_CE.text = x2neg
        text_Bup_CE.text = G2
#        text_Bdown_CE.text = text_x3neg_list[n]
        figure_frame.pos = text_Bdown_CE.pos
    elif i == 14:
        text_Adown_CE.text = x3neg
        text_Bup_CE.text = G2
#        text_Bdown_CE.text = text_x4neg_list[n]
        figure_frame.pos = text_Bdown_CE.pos
    elif i == 15:
        text_Adown_CE.text = x4neg
        text_Bup_CE.text = G2
#        text_Bdown_CE.text = text_x5neg_list[n]
        figure_frame.pos = text_Bdown_CE.pos
    elif i == 16:
        text_Adown_CE.text = x5neg
        text_Bup_CE.text = G2
#        text_Bdown_CE.text = text_x6neg_list[n]
        figure_frame.pos = text_Bdown_CE.pos
    elif i == 17:
        text_Adown_CE.text = x6neg
        text_Bup_CE.text = G2
#        text_Bdown_CE.text = text_x7neg_list[n]
        figure_frame.pos = text_Bdown_CE.pos
    elif i == 18:
        text_Adown_CE.text = x7neg
        text_Bup_CE.text = G2
#        text_Bdown_CE.text = text_x8neg_list[n]
        figure_frame.pos = text_Bdown_CE.pos
    slider.reset()
    slider = visual.Slider(win=win, name='slider',
        size=(400,40), pos=(0,-189.5), units=None,
        labels=None, ticks=(slidermin,sliderMax),
        granularity=5, style=('rating', 'whiteOnBlack'),
        color='black', font='HelveticaBold',
        flip=True)
    slider.markerPos = (round((slidermin+sliderMax)/2/5))*5
    last = core.getTime()

    # keep track of which components have finished
    CEComponents = [interface_CE, mouse_CE, buttonOK_CE, figure_frame, slider, down, up, text_Aup_CE, text_Adown_CE, text_Bmiddle_CE, text_Bup_CE, text_Bdown_CE]
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
                    if slider.markerPos != None:
                        for obj in [buttonOK_CE]:
                            if obj.contains(mouse_CE):
                                gotValidClick = True
                                mouse_CE.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
        
        # *figure_frame* updates
        if figure_frame.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            figure_frame.frameNStart = frameN  # exact frame index
            figure_frame.tStart = t  # local t and not account for scr refresh
            figure_frame.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(figure_frame, 'tStartRefresh')  # time at next scr refresh
            figure_frame.setAutoDraw(True)
            
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
            if i == 0:
                text_Adown_CE.text = int(slider.markerPos)
            elif i <= 2:
                text_Bmiddle_CE.text = int(slider.markerPos)
            elif i == 3:
                text_Bdown_CE.text = int(slider.markerPos)
            elif i >= 4 and i <= 11:
                text_Bup_CE.text = int(slider.markerPos)
            else:
                text_Bdown_CE.text = int(slider.markerPos)
            
            if mouse_CE.isPressedIn(down):
                this = core.getTime()
                if this - last > 0.05:
                    slider.markerPos-=5
                last = this
            if mouse_CE.isPressedIn(up):
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
            
    if i == 0:
        text_L_list[-1] = int(slider.markerPos)
        L = text_L_list[-1]
    elif i == 1:
        text_x1pos_list[-1] = int(slider.markerPos)
        x1pos = text_x1pos_list[-1]
        text_x1neg_list[0] = (round(int((1/2)*L)/5))*5
    elif i == 2:
        text_x1neg_list[-1] = int(slider.markerPos)
        x1neg = text_x1neg_list[-1]
        text_L2_list[0] = int(l-x1pos)
    elif i == 3:
        text_L2_list[-1] = int(slider.markerPos)
        L2 = text_L2_list[-1]
        text_x2pos_list[0] = int(x1pos+l-L2)
    elif i == 4:
        text_x2pos_list[-1] = int(slider.markerPos)
        x2pos = text_x2pos_list[-1]
        text_x3pos_list[0] = int(x2pos+l-L2)
    elif i == 5:
        text_x3pos_list[-1] = int(slider.markerPos)
        x3pos = text_x3pos_list[-1]
        text_x4pos_list[0] = int(x3pos+l-L2)
    elif i == 6:
        text_x4pos_list[-1] = int(slider.markerPos)
        x4pos = text_x4pos_list[-1]
        text_x5pos_list[0] = int(x4pos+l-L2)
    elif i == 7:
        text_x5pos_list[-1] = int(slider.markerPos)
        x5pos = text_x5pos_list[-1]
        text_x6pos_list[0] = int(x5pos+l-L2)
    elif i == 8:
        text_x6pos_list[-1] = int(slider.markerPos)
        x6pos = text_x6pos_list[-1]
        text_x7pos_list[0] =int(x6pos+l-L2)
    elif i == 9:
        text_x7pos_list[-1] = int(slider.markerPos)
        x7pos = text_x7pos_list[-1]
        text_x8pos_list[0] = int(x7pos+l-L2)
    elif i == 10:
        text_x8pos_list[-1] = int(slider.markerPos)
        x8pos = text_x8pos_list[-1]
        text_G2_list[0] = int(g-x1neg)
    elif i == 11:
        text_G2_list[-1] = int(slider.markerPos)
        G2 = text_G2_list[-1]
        text_x2neg_list[0] = int(x1neg+g-G2)
    elif i == 12:
        text_x2neg_list[-1] = int(slider.markerPos)
        x2neg = text_x2neg_list[-1]
        text_x3neg_list[0] = int(x2neg+g-G2)
    elif i == 13:
        text_x3neg_list[-1] = int(slider.markerPos)
        x3neg = text_x3neg_list[-1]
        text_x4neg_list[0] = int(x3neg+g-G2)
    elif i == 14:
        text_x4neg_list[-1] = int(slider.markerPos)
        x4neg = text_x4neg_list[-1]
        text_x5neg_list[0] = int(x4neg+g-G2)
    elif i == 15:
        text_x5neg_list[-1] = int(slider.markerPos)
        x5neg = text_x5neg_list[-1]
        text_x6neg_list[0] = int(x5neg+g-G2)
    elif i == 16:
        text_x6neg_list[-1] = int(slider.markerPos)
        x6neg = text_x6neg_list[-1]
        text_x7neg_list[0] = int(x6neg+g-G2)
    elif i == 17:
        text_x7neg_list[-1] = int(slider.markerPos)
        x7neg = text_x7neg_list[-1]
        text_x8neg_list[0] = int(x7neg+g-G2)
    elif i == 18:
        text_x8neg_list[-1] = int(slider.markerPos)
        x8neg = text_x8neg_list[-1]
        
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    thisExp.addData('slider.response', slider.getRating())
    thisExp.addData('slider.rt', slider.getRT())
    thisExp.addData('down.started', down.tStartRefresh)
    thisExp.addData('down.stopped', down.tStopRefresh)
    thisExp.addData('up.started', up.tStartRefresh)
    thisExp.addData('up.stopped', up.tStopRefresh)
    # the Routine "CE" was not non-slip safe, so reset the non-slip timer
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
