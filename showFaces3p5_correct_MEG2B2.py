#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Fri 06 Jan 2023 15:10:57 GMT
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('3.1.5')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import parallel

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'showFaces3p5_correct'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001','Scanner':True}
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
    originPath='/groups/Projects/P1463/stim/Psychopy/showFaces3p5_correct.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation
# get scanner mode
if expInfo['Scanner'] == True:
    scannermode = 1 
else:
    scannermode = 0
    
    # set parallel port
if scannermode == 1:
    # select the correct port
    parport = parallel.Parallel('/dev/parport0')    
    # MUST set the read/write mode in linux, 0=read 1=write 
    parport.setDataDir(1)    
    # set the parallel port data pins (2-9) to zero before we start
    parport.setData(0)
else:
    print ('\nNo scanner - no parallel triggers')

# A routine to send a value to the scanner via the parallel port
def trigger(val):
    if scannermode == 1:
        parport.setData(val)
        print ('Trigger set to %s' %val)
    else:
        print ('No trigger but would have been set to %s' %val)
        

#Define some scanner codes:
texptStart = 100
texptStop = 199
tTrialStart=110
tTrialStop=120  
tImStart=130
tInvertedFlag=1 # When the image is inverted (0 for upright)

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Wait"
WaitClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Please Wait',
    font='Arial',
    pos=(0, 1), height=1.75, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rPadPic = visual.ImageStim(
    win=win,
    name='rPadPic', 
    image='responsePad.jpg', mask=None,
    ori=0, pos=[0,-5], size=[18,9],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "extractSession"
extractSessionClock = core.Clock()
fName=f"ExperimentList_{expInfo['session']}.csv"


# Initialize components for Routine "GetVarsReady_2"
GetVarsReady_2Clock = core.Clock()

# Initialize components for Routine "isi"
isiClock = core.Clock()
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2',
    vertices=[[-(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [+(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [0,(0.5, 0.5)[1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[.3,.3,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=0.0, interpolate=True)

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=(5,7.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-1.0, interpolate=True)

# Initialize components for Routine "Response"
ResponseClock = core.Clock()
polygon_5 = visual.ShapeStim(
    win=win, name='polygon_5', vertices='star7',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,.3,.3], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='Happy   Angry   Fear   Neutral',
    font='Arial',
    pos=[0,-3], height=1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Wait"-------
t = 0
WaitClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(180.000000)
# update component parameters for each repeat
key_resp_25 = keyboard.Keyboard()
# keep track of which components have finished
WaitComponents = [key_resp_25, text_2, rPadPic]
for thisComponent in WaitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Wait"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WaitClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_25* updates
    if t >= 0.0 and key_resp_25.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_25.tStart = t  # not accounting for scr refresh
        key_resp_25.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
        key_resp_25.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
        key_resp_25.clearEvents(eventType='keyboard')
    frameRemains = 0.0 + 180- win.monitorFramePeriod * 0.75  # most of one frame period left
    if key_resp_25.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        key_resp_25.tStop = t  # not accounting for scr refresh
        key_resp_25.frameNStop = frameN  # exact frame index
        win.timeOnFlip(key_resp_25, 'tStopRefresh')  # time at next scr refresh
        key_resp_25.status = FINISHED
    if key_resp_25.status == STARTED:
        theseKeys = key_resp_25.getKeys(keyList=['y', 'n', 'left', 'right', 'space', '5'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_25.keys = theseKeys.name  # just the last key pressed
            key_resp_25.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # not accounting for scr refresh
        text_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    frameRemains = 0.0 + 180- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_2.tStop = t  # not accounting for scr refresh
        text_2.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
        text_2.setAutoDraw(False)
    
    # *rPadPic* updates
    if t >= 0.0 and rPadPic.status == NOT_STARTED:
        # keep track of start time/frame for later
        rPadPic.tStart = t  # not accounting for scr refresh
        rPadPic.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rPadPic, 'tStartRefresh')  # time at next scr refresh
        rPadPic.setAutoDraw(True)
    frameRemains = 0.0 + 180- win.monitorFramePeriod * 0.75  # most of one frame period left
    if rPadPic.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        rPadPic.tStop = t  # not accounting for scr refresh
        rPadPic.frameNStop = frameN  # exact frame index
        win.timeOnFlip(rPadPic, 'tStopRefresh')  # time at next scr refresh
        rPadPic.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Wait"-------
for thisComponent in WaitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_25.keys in ['', [], None]:  # No response was made
    key_resp_25.keys = None
thisExp.addData('key_resp_25.keys',key_resp_25.keys)
if key_resp_25.keys != None:  # we had a response
    thisExp.addData('key_resp_25.rt', key_resp_25.rt)
thisExp.addData('key_resp_25.started', key_resp_25.tStartRefresh)
thisExp.addData('key_resp_25.stopped', key_resp_25.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('rPadPic.started', rPadPic.tStartRefresh)
thisExp.addData('rPadPic.stopped', rPadPic.tStopRefresh)

# ------Prepare to start Routine "extractSession"-------
t = 0
extractSessionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
extractSessionComponents = []
for thisComponent in extractSessionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "extractSession"-------
while continueRoutine:
    # get current time
    t = extractSessionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in extractSessionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "extractSession"-------
for thisComponent in extractSessionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "extractSession" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(fName),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "GetVarsReady_2"-------
    t = 0
    GetVarsReady_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    randISI=random()*.5+1 # MEG updated for shorter ISI
    
    # keep track of which components have finished
    GetVarsReady_2Components = []
    for thisComponent in GetVarsReady_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "GetVarsReady_2"-------
    #send a trigger saying we have entered the start of the loop (even though this bit should not take very long)
    trigger(tTrialStart)
    
    while continueRoutine:
        # get current time
        t = GetVarsReady_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GetVarsReady_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "GetVarsReady_2"-------
    for thisComponent in GetVarsReady_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "GetVarsReady_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "isi"-------
    t = 0
    isiClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isiComponents = [polygon_4]
    for thisComponent in isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "isi"-------
    while continueRoutine:
        # get current time
        t = isiClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if t >= 0.0 and polygon_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_4.tStart = t  # not accounting for scr refresh
            polygon_4.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        frameRemains = 0.0 + randISI- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon_4.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            polygon_4.tStop = t  # not accounting for scr refresh
            polygon_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "isi"-------
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_4.started', polygon_4.tStartRefresh)
    trials.addData('polygon_4.stopped', polygon_4.tStopRefresh)
    # the Routine "isi" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Ready"-------
    t = 0
    ReadyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ReadyComponents = [polygon_2]
    for thisComponent in ReadyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Ready"-------
    trigger(tImStart)

    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ReadyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_2* updates
        if t >= 0.0 and polygon_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_2.tStart = t  # not accounting for scr refresh
            polygon_2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        frameRemains = 0.0 + .2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon_2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            polygon_2.tStop = t  # not accounting for scr refresh
            polygon_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReadyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready"-------
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_2.started', polygon_2.tStartRefresh)
    trials.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    
    # ------Prepare to start Routine "trial_2"-------
    t = 0
    trial_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    image.setOri(180*InvertedFlag)
    image.setImage(FileName)
    # keep track of which components have finished
    trial_2Components = [image, polygon_3]
    for thisComponent in trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial_2"-------
 
    # There might be a reason for this later..
    tInvertedFlag=InvertedFlag
    trigger(InvertedFlag)
    trigger(EmotionType)
    trigger(0)
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # not accounting for scr refresh
            image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        frameRemains = 0.0 + .2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
        
        # *polygon_3* updates
        if t >= 0.0 and polygon_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_3.tStart = t  # not accounting for scr refresh
            polygon_3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        frameRemains = 0.0 + .2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon_3.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            polygon_3.tStop = t  # not accounting for scr refresh
            polygon_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_2"-------
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    trials.addData('polygon_3.started', polygon_3.tStartRefresh)
    trials.addData('polygon_3.stopped', polygon_3.tStopRefresh)
    
    # ------Prepare to start Routine "Response"-------
    t = 0
    ResponseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    key_resp = keyboard.Keyboard()
    # keep track of which components have finished
    ResponseComponents = [polygon_5, key_resp, text]
    for thisComponent in ResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Response"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ResponseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_5* updates
        if t >= 0.0 and polygon_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_5.tStart = t  # not accounting for scr refresh
            polygon_5.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon_5.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            polygon_5.tStop = t  # not accounting for scr refresh
            polygon_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_5, 'tStopRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(False)
        
        # *key_resp* updates
        if t >= 0.0 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp.tStart = t  # not accounting for scr refresh
            key_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            key_resp.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
            key_resp.status = FINISHED
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['1','num_1', '2','num_2', '3','num_3', '4','num_4','8','num_8'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # not accounting for scr refresh
            text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Response"-------
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_5.started', polygon_5.tStartRefresh)
    trials.addData('polygon_5.stopped', polygon_5.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


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
