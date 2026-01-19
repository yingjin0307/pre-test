#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.2),
    on 一月 19, 2026, at 17:53
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.2'
expName = 'untitled'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1707, 1067]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\营烬\\Desktop\\实验_psychopy\\untitled.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_text') is None:
        # initialise key_text
        key_text = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_text',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_6') is None:
        # initialise key_resp_6
        key_resp_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_6',
        )
    if deviceManager.getDevice('key_prac_limited') is None:
        # initialise key_prac_limited
        key_prac_limited = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_prac_limited',
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('key_prac_limited_NL') is None:
        # initialise key_prac_limited_NL
        key_prac_limited_NL = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_prac_limited_NL',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    if deviceManager.getDevice('key_formal_limited') is None:
        # initialise key_formal_limited
        key_formal_limited = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_formal_limited',
        )
    if deviceManager.getDevice('key_resp_5') is None:
        # initialise key_resp_5
        key_resp_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_5',
        )
    if deviceManager.getDevice('key_formal_no_limited') is None:
        # initialise key_formal_no_limited
        key_formal_no_limited = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_formal_no_limited',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "start_word" ---
    start_text = visual.TextStim(win=win, name='start_text',
        text='欢迎参加本次心理学实验。\n> 在本实验中，您将面临一系列关于金钱分配的选择。在每次选择中，屏幕上会出现两个不同的分配方案（例如“方案 A”和“方案 B”）。每个方案都包含两部分金额：一部分是分给您自己的，另一部分是分给另一位匿名参与者的。\n> 您的任务是根据自己的偏好，在两个方案中选择一个。请注意，实验中没有正确或错误的答案，请完全按照您的真实想法进行选择。\n\n> 按 [空格键] 继续。',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_text = keyboard.Keyboard(deviceName='key_text')
    
    # --- Initialize components for Routine "practise_instruction" ---
    text = visual.TextStim(win=win, name='text',
        text='这是练习指导语 ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "练习_时间限制指导语" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='时间限制练习指导语：空格继续',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    
    # --- Initialize components for Routine "practise_time_limited" ---
    Title_L = visual.TextStim(win=win, name='Title_L',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Self_L = visual.TextStim(win=win, name='Self_L',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=0.04, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Others_L = visual.TextStim(win=win, name='Others_L',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    Title_R = visual.TextStim(win=win, name='Title_R',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    Self_R = visual.TextStim(win=win, name='Self_R',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    Others_R = visual.TextStim(win=win, name='Others_R',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    key_prac_limited = keyboard.Keyboard(deviceName='key_prac_limited')
    
    # --- Initialize components for Routine "worn_page_prac" ---
    worn_prac = visual.Rect(
        win=win, name='worn_prac',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "练习_非时间限制指导语" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='压力转变间歇指导语',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    
    # --- Initialize components for Routine "prac_time_none_limited" ---
    Title_Left_NL = visual.TextStim(win=win, name='Title_Left_NL',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Self_Left_NL = visual.TextStim(win=win, name='Self_Left_NL',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=0.04, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Others_Left_NL = visual.TextStim(win=win, name='Others_Left_NL',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    Title_Right_NL = visual.TextStim(win=win, name='Title_Right_NL',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    Self_Right_NL = visual.TextStim(win=win, name='Self_Right_NL',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    Others_Right_NL = visual.TextStim(win=win, name='Others_Right_NL',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    key_prac_limited_NL = keyboard.Keyboard(deviceName='key_prac_limited_NL')
    worn_NL = visual.Rect(
        win=win, name='worn_NL',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "实验_正式实验指导语" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='这是练习指导语 ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "实验_时间限制指导语" ---
    text_7 = visual.TextStim(win=win, name='text_7',
        text='开始实验指导语：按空格进入',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    
    # --- Initialize components for Routine "Trail_loop_limited" ---
    T_L = visual.TextStim(win=win, name='T_L',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    S_L = visual.TextStim(win=win, name='S_L',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=0.04, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    O_L = visual.TextStim(win=win, name='O_L',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    T_R = visual.TextStim(win=win, name='T_R',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    S_R = visual.TextStim(win=win, name='S_R',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    O_R = visual.TextStim(win=win, name='O_R',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    key_formal_limited = keyboard.Keyboard(deviceName='key_formal_limited')
    worn_formal = visual.Rect(
        win=win, name='worn_formal',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "worn_page" ---
    worn = visual.Rect(
        win=win, name='worn',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "间歇休息" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text='间歇30s',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "实验_非时间限制指导语" ---
    text_8 = visual.TextStim(win=win, name='text_8',
        text='转换实验指导语：按空格继续',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    
    # --- Initialize components for Routine "Trail_loop_no_limited" ---
    T_L_N = visual.TextStim(win=win, name='T_L_N',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    S_L_N = visual.TextStim(win=win, name='S_L_N',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=0.04, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    O_L_N = visual.TextStim(win=win, name='O_L_N',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    T_R_N = visual.TextStim(win=win, name='T_R_N',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    S_R_L = visual.TextStim(win=win, name='S_R_L',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    O_R_N = visual.TextStim(win=win, name='O_R_N',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=1.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    key_formal_no_limited = keyboard.Keyboard(deviceName='key_formal_no_limited')
    worn_Nl = visual.Rect(
        win=win, name='worn_Nl',
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "间歇休息" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text='间歇30s',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "end_word" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='jieshuyv',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "start_word" ---
    # create an object to store info about Routine start_word
    start_word = data.Routine(
        name='start_word',
        components=[start_text, key_text],
    )
    start_word.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_text
    key_text.keys = []
    key_text.rt = []
    _key_text_allKeys = []
    # store start times for start_word
    start_word.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    start_word.tStart = globalClock.getTime(format='float')
    start_word.status = STARTED
    thisExp.addData('start_word.started', start_word.tStart)
    start_word.maxDuration = None
    # keep track of which components have finished
    start_wordComponents = start_word.components
    for thisComponent in start_word.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "start_word" ---
    start_word.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *start_text* updates
        
        # if start_text is starting this frame...
        if start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_text.frameNStart = frameN  # exact frame index
            start_text.tStart = t  # local t and not account for scr refresh
            start_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'start_text.started')
            # update status
            start_text.status = STARTED
            start_text.setAutoDraw(True)
        
        # if start_text is active this frame...
        if start_text.status == STARTED:
            # update params
            pass
        
        # *key_text* updates
        waitOnFlip = False
        
        # if key_text is starting this frame...
        if key_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_text.frameNStart = frameN  # exact frame index
            key_text.tStart = t  # local t and not account for scr refresh
            key_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_text.started')
            # update status
            key_text.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_text.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_text.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_text.status == STARTED and not waitOnFlip:
            theseKeys = key_text.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_text_allKeys.extend(theseKeys)
            if len(_key_text_allKeys):
                key_text.keys = _key_text_allKeys[-1].name  # just the last key pressed
                key_text.rt = _key_text_allKeys[-1].rt
                key_text.duration = _key_text_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            start_word.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_word.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start_word" ---
    for thisComponent in start_word.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for start_word
    start_word.tStop = globalClock.getTime(format='float')
    start_word.tStopRefresh = tThisFlipGlobal
    thisExp.addData('start_word.stopped', start_word.tStop)
    # check responses
    if key_text.keys in ['', [], None]:  # No response was made
        key_text.keys = None
    thisExp.addData('key_text.keys',key_text.keys)
    if key_text.keys != None:  # we had a response
        thisExp.addData('key_text.rt', key_text.rt)
        thisExp.addData('key_text.duration', key_text.duration)
    thisExp.nextEntry()
    # the Routine "start_word" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practise_instruction" ---
    # create an object to store info about Routine practise_instruction
    practise_instruction = data.Routine(
        name='practise_instruction',
        components=[text, key_resp],
    )
    practise_instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for practise_instruction
    practise_instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practise_instruction.tStart = globalClock.getTime(format='float')
    practise_instruction.status = STARTED
    thisExp.addData('practise_instruction.started', practise_instruction.tStart)
    practise_instruction.maxDuration = None
    # keep track of which components have finished
    practise_instructionComponents = practise_instruction.components
    for thisComponent in practise_instruction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practise_instruction" ---
    practise_instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            practise_instruction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practise_instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practise_instruction" ---
    for thisComponent in practise_instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practise_instruction
    practise_instruction.tStop = globalClock.getTime(format='float')
    practise_instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practise_instruction.stopped', practise_instruction.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "practise_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "练习_时间限制指导语" ---
    # create an object to store info about Routine 练习_时间限制指导语
    练习_时间限制指导语 = data.Routine(
        name='练习_时间限制指导语',
        components=[text_5, key_resp_6],
    )
    练习_时间限制指导语.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_6
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # store start times for 练习_时间限制指导语
    练习_时间限制指导语.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    练习_时间限制指导语.tStart = globalClock.getTime(format='float')
    练习_时间限制指导语.status = STARTED
    thisExp.addData('练习_时间限制指导语.started', 练习_时间限制指导语.tStart)
    练习_时间限制指导语.maxDuration = None
    # keep track of which components have finished
    练习_时间限制指导语Components = 练习_时间限制指导语.components
    for thisComponent in 练习_时间限制指导语.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "练习_时间限制指导语" ---
    练习_时间限制指导语.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            练习_时间限制指导语.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in 练习_时间限制指导语.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "练习_时间限制指导语" ---
    for thisComponent in 练习_时间限制指导语.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for 练习_时间限制指导语
    练习_时间限制指导语.tStop = globalClock.getTime(format='float')
    练习_时间限制指导语.tStopRefresh = tThisFlipGlobal
    thisExp.addData('练习_时间限制指导语.stopped', 练习_时间限制指导语.tStop)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "练习_时间限制指导语" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler2(
        name='trials_3',
        nReps=1.0, 
        method='fullRandom', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('altruism_High.xlsx'), 
        seed=10, 
    )
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            globals()[paramName] = thisTrial_3[paramName]
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        
        # --- Prepare to start Routine "practise_time_limited" ---
        # create an object to store info about Routine practise_time_limited
        practise_time_limited = data.Routine(
            name='practise_time_limited',
            components=[Title_L, Self_L, Others_L, Title_R, Self_R, Others_R, key_prac_limited],
        )
        practise_time_limited.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Title_L.setColor('white', colorSpace='rgb')
        Title_L.setOpacity(None)
        Title_L.setContrast(1.0)
        Title_L.setPos((-0.4, 0.5))
        Title_L.setOri(0.0)
        Title_L.setText(Title_Left)
        Title_L.setFont('Arial')
        Title_L.setHeight(0.05)
        Title_L.setFlip('None')
        Self_L.setPos((-0.4, 0.3))
        Self_L.setOri(0.0)
        Self_L.setText('自己:$Self_A')
        Self_L.setFlip('None')
        Others_L.setPos((-0.4, 0.1))
        Others_L.setOri(0.0)
        Others_L.setText('他人:$Others_A')
        Others_L.setHeight(0.04)
        Others_L.setFlip('None')
        Title_R.setColor('white', colorSpace='rgb')
        Title_R.setOpacity(None)
        Title_R.setContrast(1.0)
        Title_R.setPos((0.4, 0.5))
        Title_R.setOri(0.0)
        Title_R.setText(Title_Right)
        Title_R.setFont('Arial')
        Title_R.setHeight(0.05)
        Title_R.setFlip('None')
        Self_R.setColor('white', colorSpace='rgb')
        Self_R.setOpacity(None)
        Self_R.setContrast(1.0)
        Self_R.setPos((0.4, 0.3))
        Self_R.setOri(0.0)
        Self_R.setText('自己:$Self_B')
        Self_R.setFont('Arial')
        Self_R.setHeight(0.04)
        Self_R.setFlip('None')
        Others_R.setColor('white', colorSpace='rgb')
        Others_R.setOpacity(None)
        Others_R.setContrast(1.0)
        Others_R.setPos((0.4, 0.1))
        Others_R.setOri(0.0)
        Others_R.setText('他人:$Others_B')
        Others_R.setFont('Arial')
        Others_R.setHeight(0.04)
        Others_R.setFlip('None')
        # create starting attributes for key_prac_limited
        key_prac_limited.keys = []
        key_prac_limited.rt = []
        _key_prac_limited_allKeys = []
        # store start times for practise_time_limited
        practise_time_limited.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practise_time_limited.tStart = globalClock.getTime(format='float')
        practise_time_limited.status = STARTED
        thisExp.addData('practise_time_limited.started', practise_time_limited.tStart)
        practise_time_limited.maxDuration = None
        # keep track of which components have finished
        practise_time_limitedComponents = practise_time_limited.components
        for thisComponent in practise_time_limited.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practise_time_limited" ---
        # if trial has changed, end Routine now
        if isinstance(trials_3, data.TrialHandler2) and thisTrial_3.thisN != trials_3.thisTrial.thisN:
            continueRoutine = False
        practise_time_limited.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Title_L* updates
            
            # if Title_L is starting this frame...
            if Title_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Title_L.frameNStart = frameN  # exact frame index
                Title_L.tStart = t  # local t and not account for scr refresh
                Title_L.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Title_L, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Title_L.started')
                # update status
                Title_L.status = STARTED
                Title_L.setAutoDraw(True)
            
            # if Title_L is active this frame...
            if Title_L.status == STARTED:
                # update params
                pass
            
            # if Title_L is stopping this frame...
            if Title_L.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Title_L.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Title_L.tStop = t  # not accounting for scr refresh
                    Title_L.tStopRefresh = tThisFlipGlobal  # on global time
                    Title_L.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Title_L.stopped')
                    # update status
                    Title_L.status = FINISHED
                    Title_L.setAutoDraw(False)
            
            # *Self_L* updates
            
            # if Self_L is starting this frame...
            if Self_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Self_L.frameNStart = frameN  # exact frame index
                Self_L.tStart = t  # local t and not account for scr refresh
                Self_L.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Self_L, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Self_L.started')
                # update status
                Self_L.status = STARTED
                Self_L.setAutoDraw(True)
            
            # if Self_L is active this frame...
            if Self_L.status == STARTED:
                # update params
                pass
            
            # if Self_L is stopping this frame...
            if Self_L.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Self_L.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Self_L.tStop = t  # not accounting for scr refresh
                    Self_L.tStopRefresh = tThisFlipGlobal  # on global time
                    Self_L.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Self_L.stopped')
                    # update status
                    Self_L.status = FINISHED
                    Self_L.setAutoDraw(False)
            
            # *Others_L* updates
            
            # if Others_L is starting this frame...
            if Others_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Others_L.frameNStart = frameN  # exact frame index
                Others_L.tStart = t  # local t and not account for scr refresh
                Others_L.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Others_L, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Others_L.started')
                # update status
                Others_L.status = STARTED
                Others_L.setAutoDraw(True)
            
            # if Others_L is active this frame...
            if Others_L.status == STARTED:
                # update params
                pass
            
            # if Others_L is stopping this frame...
            if Others_L.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Others_L.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Others_L.tStop = t  # not accounting for scr refresh
                    Others_L.tStopRefresh = tThisFlipGlobal  # on global time
                    Others_L.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Others_L.stopped')
                    # update status
                    Others_L.status = FINISHED
                    Others_L.setAutoDraw(False)
            
            # *Title_R* updates
            
            # if Title_R is starting this frame...
            if Title_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Title_R.frameNStart = frameN  # exact frame index
                Title_R.tStart = t  # local t and not account for scr refresh
                Title_R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Title_R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Title_R.started')
                # update status
                Title_R.status = STARTED
                Title_R.setAutoDraw(True)
            
            # if Title_R is active this frame...
            if Title_R.status == STARTED:
                # update params
                pass
            
            # if Title_R is stopping this frame...
            if Title_R.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Title_R.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Title_R.tStop = t  # not accounting for scr refresh
                    Title_R.tStopRefresh = tThisFlipGlobal  # on global time
                    Title_R.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Title_R.stopped')
                    # update status
                    Title_R.status = FINISHED
                    Title_R.setAutoDraw(False)
            
            # *Self_R* updates
            
            # if Self_R is starting this frame...
            if Self_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Self_R.frameNStart = frameN  # exact frame index
                Self_R.tStart = t  # local t and not account for scr refresh
                Self_R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Self_R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Self_R.started')
                # update status
                Self_R.status = STARTED
                Self_R.setAutoDraw(True)
            
            # if Self_R is active this frame...
            if Self_R.status == STARTED:
                # update params
                pass
            
            # if Self_R is stopping this frame...
            if Self_R.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Self_R.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Self_R.tStop = t  # not accounting for scr refresh
                    Self_R.tStopRefresh = tThisFlipGlobal  # on global time
                    Self_R.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Self_R.stopped')
                    # update status
                    Self_R.status = FINISHED
                    Self_R.setAutoDraw(False)
            
            # *Others_R* updates
            
            # if Others_R is starting this frame...
            if Others_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Others_R.frameNStart = frameN  # exact frame index
                Others_R.tStart = t  # local t and not account for scr refresh
                Others_R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Others_R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Others_R.started')
                # update status
                Others_R.status = STARTED
                Others_R.setAutoDraw(True)
            
            # if Others_R is active this frame...
            if Others_R.status == STARTED:
                # update params
                pass
            
            # if Others_R is stopping this frame...
            if Others_R.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Others_R.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Others_R.tStop = t  # not accounting for scr refresh
                    Others_R.tStopRefresh = tThisFlipGlobal  # on global time
                    Others_R.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Others_R.stopped')
                    # update status
                    Others_R.status = FINISHED
                    Others_R.setAutoDraw(False)
            
            # *key_prac_limited* updates
            waitOnFlip = False
            
            # if key_prac_limited is starting this frame...
            if key_prac_limited.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_prac_limited.frameNStart = frameN  # exact frame index
                key_prac_limited.tStart = t  # local t and not account for scr refresh
                key_prac_limited.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_prac_limited, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_prac_limited.started')
                # update status
                key_prac_limited.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_prac_limited.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_prac_limited.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_prac_limited is stopping this frame...
            if key_prac_limited.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_prac_limited.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_prac_limited.tStop = t  # not accounting for scr refresh
                    key_prac_limited.tStopRefresh = tThisFlipGlobal  # on global time
                    key_prac_limited.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_prac_limited.stopped')
                    # update status
                    key_prac_limited.status = FINISHED
                    key_prac_limited.status = FINISHED
            if key_prac_limited.status == STARTED and not waitOnFlip:
                theseKeys = key_prac_limited.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_prac_limited_allKeys.extend(theseKeys)
                if len(_key_prac_limited_allKeys):
                    key_prac_limited.keys = _key_prac_limited_allKeys[-1].name  # just the last key pressed
                    key_prac_limited.rt = _key_prac_limited_allKeys[-1].rt
                    key_prac_limited.duration = _key_prac_limited_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practise_time_limited.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practise_time_limited.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practise_time_limited" ---
        for thisComponent in practise_time_limited.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practise_time_limited
        practise_time_limited.tStop = globalClock.getTime(format='float')
        practise_time_limited.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practise_time_limited.stopped', practise_time_limited.tStop)
        # check responses
        if key_prac_limited.keys in ['', [], None]:  # No response was made
            key_prac_limited.keys = None
        trials_3.addData('key_prac_limited.keys',key_prac_limited.keys)
        if key_prac_limited.keys != None:  # we had a response
            trials_3.addData('key_prac_limited.rt', key_prac_limited.rt)
            trials_3.addData('key_prac_limited.duration', key_prac_limited.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if practise_time_limited.maxDurationReached:
            routineTimer.addTime(-practise_time_limited.maxDuration)
        elif practise_time_limited.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "worn_page_prac" ---
        # create an object to store info about Routine worn_page_prac
        worn_page_prac = data.Routine(
            name='worn_page_prac',
            components=[worn_prac],
        )
        worn_page_prac.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        worn_prac.setFillColor('red')
        worn_prac.setOpacity(None)
        worn_prac.setContrast(1.0)
        worn_prac.setPos((0, -0.5))
        worn_prac.setSize((0.5, 0.5))
        worn_prac.setLineColor('white')
        worn_prac.setLineWidth(1.0)
        # Run 'Begin Routine' code from code_prac
        # 检查练习阶段的按键
        if key_prac_limited.keys:
            continueRoutine = False
        else:
            continueRoutine = True
        # store start times for worn_page_prac
        worn_page_prac.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        worn_page_prac.tStart = globalClock.getTime(format='float')
        worn_page_prac.status = STARTED
        thisExp.addData('worn_page_prac.started', worn_page_prac.tStart)
        worn_page_prac.maxDuration = None
        # keep track of which components have finished
        worn_page_pracComponents = worn_page_prac.components
        for thisComponent in worn_page_prac.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "worn_page_prac" ---
        # if trial has changed, end Routine now
        if isinstance(trials_3, data.TrialHandler2) and thisTrial_3.thisN != trials_3.thisTrial.thisN:
            continueRoutine = False
        worn_page_prac.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *worn_prac* updates
            
            # if worn_prac is starting this frame...
            if worn_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                worn_prac.frameNStart = frameN  # exact frame index
                worn_prac.tStart = t  # local t and not account for scr refresh
                worn_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(worn_prac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'worn_prac.started')
                # update status
                worn_prac.status = STARTED
                worn_prac.setAutoDraw(True)
            
            # if worn_prac is active this frame...
            if worn_prac.status == STARTED:
                # update params
                pass
            
            # if worn_prac is stopping this frame...
            if worn_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > worn_prac.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    worn_prac.tStop = t  # not accounting for scr refresh
                    worn_prac.tStopRefresh = tThisFlipGlobal  # on global time
                    worn_prac.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'worn_prac.stopped')
                    # update status
                    worn_prac.status = FINISHED
                    worn_prac.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                worn_page_prac.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in worn_page_prac.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "worn_page_prac" ---
        for thisComponent in worn_page_prac.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for worn_page_prac
        worn_page_prac.tStop = globalClock.getTime(format='float')
        worn_page_prac.tStopRefresh = tThisFlipGlobal
        thisExp.addData('worn_page_prac.stopped', worn_page_prac.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if worn_page_prac.maxDurationReached:
            routineTimer.addTime(-worn_page_prac.maxDuration)
        elif worn_page_prac.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
    # completed 1.0 repeats of 'trials_3'
    
    
    # --- Prepare to start Routine "练习_非时间限制指导语" ---
    # create an object to store info about Routine 练习_非时间限制指导语
    练习_非时间限制指导语 = data.Routine(
        name='练习_非时间限制指导语',
        components=[text_4, key_resp_3],
    )
    练习_非时间限制指导语.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_3
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # store start times for 练习_非时间限制指导语
    练习_非时间限制指导语.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    练习_非时间限制指导语.tStart = globalClock.getTime(format='float')
    练习_非时间限制指导语.status = STARTED
    thisExp.addData('练习_非时间限制指导语.started', 练习_非时间限制指导语.tStart)
    练习_非时间限制指导语.maxDuration = None
    # keep track of which components have finished
    练习_非时间限制指导语Components = 练习_非时间限制指导语.components
    for thisComponent in 练习_非时间限制指导语.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "练习_非时间限制指导语" ---
    练习_非时间限制指导语.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            练习_非时间限制指导语.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in 练习_非时间限制指导语.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "练习_非时间限制指导语" ---
    for thisComponent in 练习_非时间限制指导语.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for 练习_非时间限制指导语
    练习_非时间限制指导语.tStop = globalClock.getTime(format='float')
    练习_非时间限制指导语.tStopRefresh = tThisFlipGlobal
    thisExp.addData('练习_非时间限制指导语.stopped', 练习_非时间限制指导语.tStop)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "练习_非时间限制指导语" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler2(
        name='trials_4',
        nReps=1.0, 
        method='fullRandom', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('altruism_Low.xlsx'), 
        seed=10, 
    )
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            globals()[paramName] = thisTrial_4[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_4 in trials_4:
        currentLoop = trials_4
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                globals()[paramName] = thisTrial_4[paramName]
        
        # --- Prepare to start Routine "prac_time_none_limited" ---
        # create an object to store info about Routine prac_time_none_limited
        prac_time_none_limited = data.Routine(
            name='prac_time_none_limited',
            components=[Title_Left_NL, Self_Left_NL, Others_Left_NL, Title_Right_NL, Self_Right_NL, Others_Right_NL, key_prac_limited_NL, worn_NL],
        )
        prac_time_none_limited.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Title_Left_NL.setColor('white', colorSpace='rgb')
        Title_Left_NL.setOpacity(None)
        Title_Left_NL.setContrast(1.0)
        Title_Left_NL.setPos((-0.4, 0.2))
        Title_Left_NL.setOri(0.0)
        Title_Left_NL.setText(Title_Left)
        Title_Left_NL.setFont('Arial')
        Title_Left_NL.setHeight(0.05)
        Title_Left_NL.setFlip('None')
        Self_Left_NL.setPos((-0.4, 0))
        Self_Left_NL.setOri(0.0)
        Self_Left_NL.setText('自己:$Self_A')
        Self_Left_NL.setFlip('None')
        Others_Left_NL.setPos((-0.4, -0.2))
        Others_Left_NL.setOri(0.0)
        Others_Left_NL.setText('他人:$Others_A')
        Others_Left_NL.setHeight(0.04)
        Others_Left_NL.setFlip('None')
        Title_Right_NL.setColor('white', colorSpace='rgb')
        Title_Right_NL.setOpacity(None)
        Title_Right_NL.setContrast(1.0)
        Title_Right_NL.setPos((0.4, 0.2))
        Title_Right_NL.setOri(0.0)
        Title_Right_NL.setText(Title_Right)
        Title_Right_NL.setFont('Arial')
        Title_Right_NL.setHeight(0.05)
        Title_Right_NL.setFlip('None')
        Self_Right_NL.setColor('white', colorSpace='rgb')
        Self_Right_NL.setOpacity(None)
        Self_Right_NL.setContrast(1.0)
        Self_Right_NL.setPos((0.4, 0))
        Self_Right_NL.setOri(0.0)
        Self_Right_NL.setText('自己:$Self_B')
        Self_Right_NL.setFont('Arial')
        Self_Right_NL.setHeight(0.04)
        Self_Right_NL.setFlip('None')
        Others_Right_NL.setColor('white', colorSpace='rgb')
        Others_Right_NL.setOpacity(None)
        Others_Right_NL.setContrast(1.0)
        Others_Right_NL.setPos((0.4, -0.2))
        Others_Right_NL.setOri(0.0)
        Others_Right_NL.setText('他人:$Others_B')
        Others_Right_NL.setFont('Arial')
        Others_Right_NL.setHeight(0.04)
        Others_Right_NL.setFlip('None')
        # create starting attributes for key_prac_limited_NL
        key_prac_limited_NL.keys = []
        key_prac_limited_NL.rt = []
        _key_prac_limited_NL_allKeys = []
        worn_NL.setFillColor('green')
        worn_NL.setOpacity(None)
        worn_NL.setContrast(1.0)
        worn_NL.setPos((0, -0.5))
        worn_NL.setSize((0.5, 0.5))
        worn_NL.setLineColor('white')
        worn_NL.setLineWidth(1.0)
        # store start times for prac_time_none_limited
        prac_time_none_limited.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        prac_time_none_limited.tStart = globalClock.getTime(format='float')
        prac_time_none_limited.status = STARTED
        thisExp.addData('prac_time_none_limited.started', prac_time_none_limited.tStart)
        prac_time_none_limited.maxDuration = None
        # keep track of which components have finished
        prac_time_none_limitedComponents = prac_time_none_limited.components
        for thisComponent in prac_time_none_limited.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_time_none_limited" ---
        # if trial has changed, end Routine now
        if isinstance(trials_4, data.TrialHandler2) and thisTrial_4.thisN != trials_4.thisTrial.thisN:
            continueRoutine = False
        prac_time_none_limited.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Title_Left_NL* updates
            
            # if Title_Left_NL is starting this frame...
            if Title_Left_NL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Title_Left_NL.frameNStart = frameN  # exact frame index
                Title_Left_NL.tStart = t  # local t and not account for scr refresh
                Title_Left_NL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Title_Left_NL, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Title_Left_NL.started')
                # update status
                Title_Left_NL.status = STARTED
                Title_Left_NL.setAutoDraw(True)
            
            # if Title_Left_NL is active this frame...
            if Title_Left_NL.status == STARTED:
                # update params
                pass
            
            # if Title_Left_NL is stopping this frame...
            if Title_Left_NL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Title_Left_NL.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Title_Left_NL.tStop = t  # not accounting for scr refresh
                    Title_Left_NL.tStopRefresh = tThisFlipGlobal  # on global time
                    Title_Left_NL.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Title_Left_NL.stopped')
                    # update status
                    Title_Left_NL.status = FINISHED
                    Title_Left_NL.setAutoDraw(False)
            
            # *Self_Left_NL* updates
            
            # if Self_Left_NL is starting this frame...
            if Self_Left_NL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Self_Left_NL.frameNStart = frameN  # exact frame index
                Self_Left_NL.tStart = t  # local t and not account for scr refresh
                Self_Left_NL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Self_Left_NL, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Self_Left_NL.started')
                # update status
                Self_Left_NL.status = STARTED
                Self_Left_NL.setAutoDraw(True)
            
            # if Self_Left_NL is active this frame...
            if Self_Left_NL.status == STARTED:
                # update params
                pass
            
            # if Self_Left_NL is stopping this frame...
            if Self_Left_NL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Self_Left_NL.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Self_Left_NL.tStop = t  # not accounting for scr refresh
                    Self_Left_NL.tStopRefresh = tThisFlipGlobal  # on global time
                    Self_Left_NL.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Self_Left_NL.stopped')
                    # update status
                    Self_Left_NL.status = FINISHED
                    Self_Left_NL.setAutoDraw(False)
            
            # *Others_Left_NL* updates
            
            # if Others_Left_NL is starting this frame...
            if Others_Left_NL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Others_Left_NL.frameNStart = frameN  # exact frame index
                Others_Left_NL.tStart = t  # local t and not account for scr refresh
                Others_Left_NL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Others_Left_NL, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Others_Left_NL.started')
                # update status
                Others_Left_NL.status = STARTED
                Others_Left_NL.setAutoDraw(True)
            
            # if Others_Left_NL is active this frame...
            if Others_Left_NL.status == STARTED:
                # update params
                pass
            
            # if Others_Left_NL is stopping this frame...
            if Others_Left_NL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Others_Left_NL.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Others_Left_NL.tStop = t  # not accounting for scr refresh
                    Others_Left_NL.tStopRefresh = tThisFlipGlobal  # on global time
                    Others_Left_NL.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Others_Left_NL.stopped')
                    # update status
                    Others_Left_NL.status = FINISHED
                    Others_Left_NL.setAutoDraw(False)
            
            # *Title_Right_NL* updates
            
            # if Title_Right_NL is starting this frame...
            if Title_Right_NL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Title_Right_NL.frameNStart = frameN  # exact frame index
                Title_Right_NL.tStart = t  # local t and not account for scr refresh
                Title_Right_NL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Title_Right_NL, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Title_Right_NL.started')
                # update status
                Title_Right_NL.status = STARTED
                Title_Right_NL.setAutoDraw(True)
            
            # if Title_Right_NL is active this frame...
            if Title_Right_NL.status == STARTED:
                # update params
                pass
            
            # if Title_Right_NL is stopping this frame...
            if Title_Right_NL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Title_Right_NL.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Title_Right_NL.tStop = t  # not accounting for scr refresh
                    Title_Right_NL.tStopRefresh = tThisFlipGlobal  # on global time
                    Title_Right_NL.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Title_Right_NL.stopped')
                    # update status
                    Title_Right_NL.status = FINISHED
                    Title_Right_NL.setAutoDraw(False)
            
            # *Self_Right_NL* updates
            
            # if Self_Right_NL is starting this frame...
            if Self_Right_NL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Self_Right_NL.frameNStart = frameN  # exact frame index
                Self_Right_NL.tStart = t  # local t and not account for scr refresh
                Self_Right_NL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Self_Right_NL, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Self_Right_NL.started')
                # update status
                Self_Right_NL.status = STARTED
                Self_Right_NL.setAutoDraw(True)
            
            # if Self_Right_NL is active this frame...
            if Self_Right_NL.status == STARTED:
                # update params
                pass
            
            # if Self_Right_NL is stopping this frame...
            if Self_Right_NL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Self_Right_NL.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Self_Right_NL.tStop = t  # not accounting for scr refresh
                    Self_Right_NL.tStopRefresh = tThisFlipGlobal  # on global time
                    Self_Right_NL.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Self_Right_NL.stopped')
                    # update status
                    Self_Right_NL.status = FINISHED
                    Self_Right_NL.setAutoDraw(False)
            
            # *Others_Right_NL* updates
            
            # if Others_Right_NL is starting this frame...
            if Others_Right_NL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Others_Right_NL.frameNStart = frameN  # exact frame index
                Others_Right_NL.tStart = t  # local t and not account for scr refresh
                Others_Right_NL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Others_Right_NL, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Others_Right_NL.started')
                # update status
                Others_Right_NL.status = STARTED
                Others_Right_NL.setAutoDraw(True)
            
            # if Others_Right_NL is active this frame...
            if Others_Right_NL.status == STARTED:
                # update params
                pass
            
            # if Others_Right_NL is stopping this frame...
            if Others_Right_NL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Others_Right_NL.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Others_Right_NL.tStop = t  # not accounting for scr refresh
                    Others_Right_NL.tStopRefresh = tThisFlipGlobal  # on global time
                    Others_Right_NL.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Others_Right_NL.stopped')
                    # update status
                    Others_Right_NL.status = FINISHED
                    Others_Right_NL.setAutoDraw(False)
            
            # *key_prac_limited_NL* updates
            waitOnFlip = False
            
            # if key_prac_limited_NL is starting this frame...
            if key_prac_limited_NL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_prac_limited_NL.frameNStart = frameN  # exact frame index
                key_prac_limited_NL.tStart = t  # local t and not account for scr refresh
                key_prac_limited_NL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_prac_limited_NL, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_prac_limited_NL.started')
                # update status
                key_prac_limited_NL.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_prac_limited_NL.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_prac_limited_NL.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_prac_limited_NL is stopping this frame...
            if key_prac_limited_NL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_prac_limited_NL.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    key_prac_limited_NL.tStop = t  # not accounting for scr refresh
                    key_prac_limited_NL.tStopRefresh = tThisFlipGlobal  # on global time
                    key_prac_limited_NL.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_prac_limited_NL.stopped')
                    # update status
                    key_prac_limited_NL.status = FINISHED
                    key_prac_limited_NL.status = FINISHED
            if key_prac_limited_NL.status == STARTED and not waitOnFlip:
                theseKeys = key_prac_limited_NL.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_prac_limited_NL_allKeys.extend(theseKeys)
                if len(_key_prac_limited_NL_allKeys):
                    key_prac_limited_NL.keys = _key_prac_limited_NL_allKeys[-1].name  # just the last key pressed
                    key_prac_limited_NL.rt = _key_prac_limited_NL_allKeys[-1].rt
                    key_prac_limited_NL.duration = _key_prac_limited_NL_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *worn_NL* updates
            
            # if worn_NL is starting this frame...
            if worn_NL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                worn_NL.frameNStart = frameN  # exact frame index
                worn_NL.tStart = t  # local t and not account for scr refresh
                worn_NL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(worn_NL, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'worn_NL.started')
                # update status
                worn_NL.status = STARTED
                worn_NL.setAutoDraw(True)
            
            # if worn_NL is active this frame...
            if worn_NL.status == STARTED:
                # update params
                pass
            
            # if worn_NL is stopping this frame...
            if worn_NL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > worn_NL.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    worn_NL.tStop = t  # not accounting for scr refresh
                    worn_NL.tStopRefresh = tThisFlipGlobal  # on global time
                    worn_NL.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'worn_NL.stopped')
                    # update status
                    worn_NL.status = FINISHED
                    worn_NL.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                prac_time_none_limited.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_time_none_limited.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_time_none_limited" ---
        for thisComponent in prac_time_none_limited.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for prac_time_none_limited
        prac_time_none_limited.tStop = globalClock.getTime(format='float')
        prac_time_none_limited.tStopRefresh = tThisFlipGlobal
        thisExp.addData('prac_time_none_limited.stopped', prac_time_none_limited.tStop)
        # check responses
        if key_prac_limited_NL.keys in ['', [], None]:  # No response was made
            key_prac_limited_NL.keys = None
        trials_4.addData('key_prac_limited_NL.keys',key_prac_limited_NL.keys)
        if key_prac_limited_NL.keys != None:  # we had a response
            trials_4.addData('key_prac_limited_NL.rt', key_prac_limited_NL.rt)
            trials_4.addData('key_prac_limited_NL.duration', key_prac_limited_NL.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if prac_time_none_limited.maxDurationReached:
            routineTimer.addTime(-prac_time_none_limited.maxDuration)
        elif prac_time_none_limited.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_4'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "实验_正式实验指导语" ---
    # create an object to store info about Routine 实验_正式实验指导语
    实验_正式实验指导语 = data.Routine(
        name='实验_正式实验指导语',
        components=[text_2, key_resp_2],
    )
    实验_正式实验指导语.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # store start times for 实验_正式实验指导语
    实验_正式实验指导语.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    实验_正式实验指导语.tStart = globalClock.getTime(format='float')
    实验_正式实验指导语.status = STARTED
    thisExp.addData('实验_正式实验指导语.started', 实验_正式实验指导语.tStart)
    实验_正式实验指导语.maxDuration = None
    # keep track of which components have finished
    实验_正式实验指导语Components = 实验_正式实验指导语.components
    for thisComponent in 实验_正式实验指导语.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "实验_正式实验指导语" ---
    实验_正式实验指导语.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            实验_正式实验指导语.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in 实验_正式实验指导语.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "实验_正式实验指导语" ---
    for thisComponent in 实验_正式实验指导语.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for 实验_正式实验指导语
    实验_正式实验指导语.tStop = globalClock.getTime(format='float')
    实验_正式实验指导语.tStopRefresh = tThisFlipGlobal
    thisExp.addData('实验_正式实验指导语.stopped', 实验_正式实验指导语.tStop)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "实验_正式实验指导语" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "实验_时间限制指导语" ---
    # create an object to store info about Routine 实验_时间限制指导语
    实验_时间限制指导语 = data.Routine(
        name='实验_时间限制指导语',
        components=[text_7, key_resp_4],
    )
    实验_时间限制指导语.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_4
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # store start times for 实验_时间限制指导语
    实验_时间限制指导语.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    实验_时间限制指导语.tStart = globalClock.getTime(format='float')
    实验_时间限制指导语.status = STARTED
    thisExp.addData('实验_时间限制指导语.started', 实验_时间限制指导语.tStart)
    实验_时间限制指导语.maxDuration = None
    # keep track of which components have finished
    实验_时间限制指导语Components = 实验_时间限制指导语.components
    for thisComponent in 实验_时间限制指导语.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "实验_时间限制指导语" ---
    实验_时间限制指导语.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        
        # if text_7 is starting this frame...
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            # update status
            text_7.status = STARTED
            text_7.setAutoDraw(True)
        
        # if text_7 is active this frame...
        if text_7.status == STARTED:
            # update params
            pass
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            实验_时间限制指导语.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in 实验_时间限制指导语.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "实验_时间限制指导语" ---
    for thisComponent in 实验_时间限制指导语.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for 实验_时间限制指导语
    实验_时间限制指导语.tStop = globalClock.getTime(format='float')
    实验_时间限制指导语.tStopRefresh = tThisFlipGlobal
    thisExp.addData('实验_时间限制指导语.stopped', 实验_时间限制指导语.tStop)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    thisExp.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        thisExp.addData('key_resp_4.rt', key_resp_4.rt)
        thisExp.addData('key_resp_4.duration', key_resp_4.duration)
    thisExp.nextEntry()
    # the Routine "实验_时间限制指导语" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_5 = data.TrialHandler2(
        name='trials_5',
        nReps=3.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('altruism_High.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_5)  # add the loop to the experiment
    thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            globals()[paramName] = thisTrial_5[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_5 in trials_5:
        currentLoop = trials_5
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                globals()[paramName] = thisTrial_5[paramName]
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler2(
            name='trials',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('altruism_High.xlsx'), 
            seed=56, 
        )
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial in trials:
            currentLoop = trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            # --- Prepare to start Routine "Trail_loop_limited" ---
            # create an object to store info about Routine Trail_loop_limited
            Trail_loop_limited = data.Routine(
                name='Trail_loop_limited',
                components=[T_L, S_L, O_L, T_R, S_R, O_R, key_formal_limited, worn_formal],
            )
            Trail_loop_limited.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            T_L.setColor('white', colorSpace='rgb')
            T_L.setOpacity(None)
            T_L.setContrast(1.0)
            T_L.setPos((-0.4, 0.2))
            T_L.setOri(0.0)
            T_L.setText(Title_Left)
            T_L.setFont('Arial')
            T_L.setHeight(0.05)
            T_L.setFlip('None')
            S_L.setPos((-0.4, 0))
            S_L.setOri(0.0)
            S_L.setText('自己:$Self_A')
            S_L.setFlip('None')
            O_L.setPos((-0.4, -0.2))
            O_L.setOri(0.0)
            O_L.setText('他人:$Others_A')
            O_L.setHeight(0.04)
            O_L.setFlip('None')
            T_R.setColor('white', colorSpace='rgb')
            T_R.setOpacity(None)
            T_R.setContrast(1.0)
            T_R.setPos((0.4, 0.2))
            T_R.setOri(0.0)
            T_R.setText(Title_Right)
            T_R.setFont('Arial')
            T_R.setHeight(0.05)
            T_R.setFlip('None')
            S_R.setColor('white', colorSpace='rgb')
            S_R.setOpacity(None)
            S_R.setContrast(1.0)
            S_R.setPos((0.4, 0))
            S_R.setOri(0.0)
            S_R.setText('自己:$Self_B')
            S_R.setFont('Arial')
            S_R.setHeight(0.04)
            S_R.setFlip('None')
            O_R.setColor('white', colorSpace='rgb')
            O_R.setOpacity(None)
            O_R.setContrast(1.0)
            O_R.setPos((0.4, -0.2))
            O_R.setOri(0.0)
            O_R.setText('他人:$Others_B')
            O_R.setFont('Arial')
            O_R.setHeight(0.04)
            O_R.setFlip('None')
            # create starting attributes for key_formal_limited
            key_formal_limited.keys = []
            key_formal_limited.rt = []
            _key_formal_limited_allKeys = []
            worn_formal.setFillColor('red')
            worn_formal.setOpacity(None)
            worn_formal.setContrast(1.0)
            worn_formal.setPos((0, -0.5))
            worn_formal.setSize((0.5, 0.5))
            worn_formal.setLineColor('white')
            worn_formal.setLineWidth(1.0)
            # store start times for Trail_loop_limited
            Trail_loop_limited.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Trail_loop_limited.tStart = globalClock.getTime(format='float')
            Trail_loop_limited.status = STARTED
            thisExp.addData('Trail_loop_limited.started', Trail_loop_limited.tStart)
            Trail_loop_limited.maxDuration = None
            # keep track of which components have finished
            Trail_loop_limitedComponents = Trail_loop_limited.components
            for thisComponent in Trail_loop_limited.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Trail_loop_limited" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            Trail_loop_limited.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *T_L* updates
                
                # if T_L is starting this frame...
                if T_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    T_L.frameNStart = frameN  # exact frame index
                    T_L.tStart = t  # local t and not account for scr refresh
                    T_L.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(T_L, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'T_L.started')
                    # update status
                    T_L.status = STARTED
                    T_L.setAutoDraw(True)
                
                # if T_L is active this frame...
                if T_L.status == STARTED:
                    # update params
                    pass
                
                # if T_L is stopping this frame...
                if T_L.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > T_L.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        T_L.tStop = t  # not accounting for scr refresh
                        T_L.tStopRefresh = tThisFlipGlobal  # on global time
                        T_L.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'T_L.stopped')
                        # update status
                        T_L.status = FINISHED
                        T_L.setAutoDraw(False)
                
                # *S_L* updates
                
                # if S_L is starting this frame...
                if S_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    S_L.frameNStart = frameN  # exact frame index
                    S_L.tStart = t  # local t and not account for scr refresh
                    S_L.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(S_L, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'S_L.started')
                    # update status
                    S_L.status = STARTED
                    S_L.setAutoDraw(True)
                
                # if S_L is active this frame...
                if S_L.status == STARTED:
                    # update params
                    pass
                
                # if S_L is stopping this frame...
                if S_L.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > S_L.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        S_L.tStop = t  # not accounting for scr refresh
                        S_L.tStopRefresh = tThisFlipGlobal  # on global time
                        S_L.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'S_L.stopped')
                        # update status
                        S_L.status = FINISHED
                        S_L.setAutoDraw(False)
                
                # *O_L* updates
                
                # if O_L is starting this frame...
                if O_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    O_L.frameNStart = frameN  # exact frame index
                    O_L.tStart = t  # local t and not account for scr refresh
                    O_L.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(O_L, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'O_L.started')
                    # update status
                    O_L.status = STARTED
                    O_L.setAutoDraw(True)
                
                # if O_L is active this frame...
                if O_L.status == STARTED:
                    # update params
                    pass
                
                # if O_L is stopping this frame...
                if O_L.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > O_L.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        O_L.tStop = t  # not accounting for scr refresh
                        O_L.tStopRefresh = tThisFlipGlobal  # on global time
                        O_L.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'O_L.stopped')
                        # update status
                        O_L.status = FINISHED
                        O_L.setAutoDraw(False)
                
                # *T_R* updates
                
                # if T_R is starting this frame...
                if T_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    T_R.frameNStart = frameN  # exact frame index
                    T_R.tStart = t  # local t and not account for scr refresh
                    T_R.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(T_R, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'T_R.started')
                    # update status
                    T_R.status = STARTED
                    T_R.setAutoDraw(True)
                
                # if T_R is active this frame...
                if T_R.status == STARTED:
                    # update params
                    pass
                
                # if T_R is stopping this frame...
                if T_R.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > T_R.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        T_R.tStop = t  # not accounting for scr refresh
                        T_R.tStopRefresh = tThisFlipGlobal  # on global time
                        T_R.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'T_R.stopped')
                        # update status
                        T_R.status = FINISHED
                        T_R.setAutoDraw(False)
                
                # *S_R* updates
                
                # if S_R is starting this frame...
                if S_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    S_R.frameNStart = frameN  # exact frame index
                    S_R.tStart = t  # local t and not account for scr refresh
                    S_R.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(S_R, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'S_R.started')
                    # update status
                    S_R.status = STARTED
                    S_R.setAutoDraw(True)
                
                # if S_R is active this frame...
                if S_R.status == STARTED:
                    # update params
                    pass
                
                # if S_R is stopping this frame...
                if S_R.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > S_R.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        S_R.tStop = t  # not accounting for scr refresh
                        S_R.tStopRefresh = tThisFlipGlobal  # on global time
                        S_R.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'S_R.stopped')
                        # update status
                        S_R.status = FINISHED
                        S_R.setAutoDraw(False)
                
                # *O_R* updates
                
                # if O_R is starting this frame...
                if O_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    O_R.frameNStart = frameN  # exact frame index
                    O_R.tStart = t  # local t and not account for scr refresh
                    O_R.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(O_R, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'O_R.started')
                    # update status
                    O_R.status = STARTED
                    O_R.setAutoDraw(True)
                
                # if O_R is active this frame...
                if O_R.status == STARTED:
                    # update params
                    pass
                
                # if O_R is stopping this frame...
                if O_R.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > O_R.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        O_R.tStop = t  # not accounting for scr refresh
                        O_R.tStopRefresh = tThisFlipGlobal  # on global time
                        O_R.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'O_R.stopped')
                        # update status
                        O_R.status = FINISHED
                        O_R.setAutoDraw(False)
                
                # *key_formal_limited* updates
                waitOnFlip = False
                
                # if key_formal_limited is starting this frame...
                if key_formal_limited.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_formal_limited.frameNStart = frameN  # exact frame index
                    key_formal_limited.tStart = t  # local t and not account for scr refresh
                    key_formal_limited.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_formal_limited, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_formal_limited.started')
                    # update status
                    key_formal_limited.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_formal_limited.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_formal_limited.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if key_formal_limited is stopping this frame...
                if key_formal_limited.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_formal_limited.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        key_formal_limited.tStop = t  # not accounting for scr refresh
                        key_formal_limited.tStopRefresh = tThisFlipGlobal  # on global time
                        key_formal_limited.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_formal_limited.stopped')
                        # update status
                        key_formal_limited.status = FINISHED
                        key_formal_limited.status = FINISHED
                if key_formal_limited.status == STARTED and not waitOnFlip:
                    theseKeys = key_formal_limited.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                    _key_formal_limited_allKeys.extend(theseKeys)
                    if len(_key_formal_limited_allKeys):
                        key_formal_limited.keys = _key_formal_limited_allKeys[-1].name  # just the last key pressed
                        key_formal_limited.rt = _key_formal_limited_allKeys[-1].rt
                        key_formal_limited.duration = _key_formal_limited_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *worn_formal* updates
                
                # if worn_formal is starting this frame...
                if worn_formal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    worn_formal.frameNStart = frameN  # exact frame index
                    worn_formal.tStart = t  # local t and not account for scr refresh
                    worn_formal.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(worn_formal, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'worn_formal.started')
                    # update status
                    worn_formal.status = STARTED
                    worn_formal.setAutoDraw(True)
                
                # if worn_formal is active this frame...
                if worn_formal.status == STARTED:
                    # update params
                    pass
                
                # if worn_formal is stopping this frame...
                if worn_formal.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > worn_formal.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        worn_formal.tStop = t  # not accounting for scr refresh
                        worn_formal.tStopRefresh = tThisFlipGlobal  # on global time
                        worn_formal.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'worn_formal.stopped')
                        # update status
                        worn_formal.status = FINISHED
                        worn_formal.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Trail_loop_limited.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Trail_loop_limited.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Trail_loop_limited" ---
            for thisComponent in Trail_loop_limited.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Trail_loop_limited
            Trail_loop_limited.tStop = globalClock.getTime(format='float')
            Trail_loop_limited.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Trail_loop_limited.stopped', Trail_loop_limited.tStop)
            # check responses
            if key_formal_limited.keys in ['', [], None]:  # No response was made
                key_formal_limited.keys = None
            trials.addData('key_formal_limited.keys',key_formal_limited.keys)
            if key_formal_limited.keys != None:  # we had a response
                trials.addData('key_formal_limited.rt', key_formal_limited.rt)
                trials.addData('key_formal_limited.duration', key_formal_limited.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Trail_loop_limited.maxDurationReached:
                routineTimer.addTime(-Trail_loop_limited.maxDuration)
            elif Trail_loop_limited.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.500000)
            
            # --- Prepare to start Routine "worn_page" ---
            # create an object to store info about Routine worn_page
            worn_page = data.Routine(
                name='worn_page',
                components=[worn],
            )
            worn_page.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            worn.setFillColor('red')
            worn.setOpacity(None)
            worn.setContrast(1.0)
            worn.setPos((0, -0.5))
            worn.setSize((0.5, 0.5))
            worn.setLineColor('white')
            worn.setLineWidth(1.0)
            # Run 'Begin Routine' code from code
            # 检查上一个按键组件是否有反应
            # 如果有按键记录 (keys不为空)，则跳过警告
            if key_formal_limited.keys:
                continueRoutine = False
            else:
                # 如果没按键 (超时)，则记录这次超时，并显示警告
                continueRoutine = True
                # (可选) 在数据中标记超时
                thisExp.addData('timed_out', 1)
            # store start times for worn_page
            worn_page.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            worn_page.tStart = globalClock.getTime(format='float')
            worn_page.status = STARTED
            thisExp.addData('worn_page.started', worn_page.tStart)
            worn_page.maxDuration = None
            # keep track of which components have finished
            worn_pageComponents = worn_page.components
            for thisComponent in worn_page.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "worn_page" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            worn_page.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *worn* updates
                
                # if worn is starting this frame...
                if worn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    worn.frameNStart = frameN  # exact frame index
                    worn.tStart = t  # local t and not account for scr refresh
                    worn.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(worn, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'worn.started')
                    # update status
                    worn.status = STARTED
                    worn.setAutoDraw(True)
                
                # if worn is active this frame...
                if worn.status == STARTED:
                    # update params
                    pass
                
                # if worn is stopping this frame...
                if worn.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > worn.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        worn.tStop = t  # not accounting for scr refresh
                        worn.tStopRefresh = tThisFlipGlobal  # on global time
                        worn.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'worn.stopped')
                        # update status
                        worn.status = FINISHED
                        worn.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    worn_page.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in worn_page.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "worn_page" ---
            for thisComponent in worn_page.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for worn_page
            worn_page.tStop = globalClock.getTime(format='float')
            worn_page.tStopRefresh = tThisFlipGlobal
            thisExp.addData('worn_page.stopped', worn_page.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if worn_page.maxDurationReached:
                routineTimer.addTime(-worn_page.maxDuration)
            elif worn_page.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.500000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "间歇休息" ---
        # create an object to store info about Routine 间歇休息
        间歇休息 = data.Routine(
            name='间歇休息',
            components=[text_6],
        )
        间歇休息.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        # 假设您的Excel总共有 60 行，您想每 20 个试次休息一次
        # trials.thisN 是当前试次的索引（从0开始计数）
        
        # 这里的逻辑是：如果当前做完的试次数量（thisN+1）不是20或40，就跳过休息
        if (trials.thisN + 1) not in [56, 112]:
            continueRoutine = False
        # store start times for 间歇休息
        间歇休息.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        间歇休息.tStart = globalClock.getTime(format='float')
        间歇休息.status = STARTED
        thisExp.addData('间歇休息.started', 间歇休息.tStart)
        间歇休息.maxDuration = None
        # keep track of which components have finished
        间歇休息Components = 间歇休息.components
        for thisComponent in 间歇休息.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "间歇休息" ---
        # if trial has changed, end Routine now
        if isinstance(trials_5, data.TrialHandler2) and thisTrial_5.thisN != trials_5.thisTrial.thisN:
            continueRoutine = False
        间歇休息.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 30.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            
            # if text_6 is starting this frame...
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.started')
                # update status
                text_6.status = STARTED
                text_6.setAutoDraw(True)
            
            # if text_6 is active this frame...
            if text_6.status == STARTED:
                # update params
                pass
            
            # if text_6 is stopping this frame...
            if text_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_6.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    text_6.tStop = t  # not accounting for scr refresh
                    text_6.tStopRefresh = tThisFlipGlobal  # on global time
                    text_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_6.stopped')
                    # update status
                    text_6.status = FINISHED
                    text_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                间歇休息.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in 间歇休息.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "间歇休息" ---
        for thisComponent in 间歇休息.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for 间歇休息
        间歇休息.tStop = globalClock.getTime(format='float')
        间歇休息.tStopRefresh = tThisFlipGlobal
        thisExp.addData('间歇休息.stopped', 间歇休息.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if 间歇休息.maxDurationReached:
            routineTimer.addTime(-间歇休息.maxDuration)
        elif 间歇休息.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-30.000000)
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'trials_5'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "实验_非时间限制指导语" ---
    # create an object to store info about Routine 实验_非时间限制指导语
    实验_非时间限制指导语 = data.Routine(
        name='实验_非时间限制指导语',
        components=[text_8, key_resp_5],
    )
    实验_非时间限制指导语.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_5
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # store start times for 实验_非时间限制指导语
    实验_非时间限制指导语.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    实验_非时间限制指导语.tStart = globalClock.getTime(format='float')
    实验_非时间限制指导语.status = STARTED
    thisExp.addData('实验_非时间限制指导语.started', 实验_非时间限制指导语.tStart)
    实验_非时间限制指导语.maxDuration = None
    # keep track of which components have finished
    实验_非时间限制指导语Components = 实验_非时间限制指导语.components
    for thisComponent in 实验_非时间限制指导语.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "实验_非时间限制指导语" ---
    实验_非时间限制指导语.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        
        # if text_8 is starting this frame...
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_8.started')
            # update status
            text_8.status = STARTED
            text_8.setAutoDraw(True)
        
        # if text_8 is active this frame...
        if text_8.status == STARTED:
            # update params
            pass
        
        # *key_resp_5* updates
        waitOnFlip = False
        
        # if key_resp_5 is starting this frame...
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_5.started')
            # update status
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            实验_非时间限制指导语.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in 实验_非时间限制指导语.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "实验_非时间限制指导语" ---
    for thisComponent in 实验_非时间限制指导语.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for 实验_非时间限制指导语
    实验_非时间限制指导语.tStop = globalClock.getTime(format='float')
    实验_非时间限制指导语.tStopRefresh = tThisFlipGlobal
    thisExp.addData('实验_非时间限制指导语.stopped', 实验_非时间限制指导语.tStop)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    thisExp.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        thisExp.addData('key_resp_5.rt', key_resp_5.rt)
        thisExp.addData('key_resp_5.duration', key_resp_5.duration)
    thisExp.nextEntry()
    # the Routine "实验_非时间限制指导语" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler2(
        name='trials_2',
        nReps=3.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('altruism_Low.xlsx'), 
        seed=56, 
    )
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "Trail_loop_no_limited" ---
        # create an object to store info about Routine Trail_loop_no_limited
        Trail_loop_no_limited = data.Routine(
            name='Trail_loop_no_limited',
            components=[T_L_N, S_L_N, O_L_N, T_R_N, S_R_L, O_R_N, key_formal_no_limited, worn_Nl],
        )
        Trail_loop_no_limited.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        T_L_N.setColor('white', colorSpace='rgb')
        T_L_N.setOpacity(None)
        T_L_N.setContrast(1.0)
        T_L_N.setPos((-0.4, 0.2))
        T_L_N.setOri(0.0)
        T_L_N.setText(Title_Left)
        T_L_N.setFont('Arial')
        T_L_N.setHeight(0.05)
        T_L_N.setFlip('None')
        S_L_N.setPos((-0.4, 0))
        S_L_N.setOri(0.0)
        S_L_N.setText('自己:$Self_A')
        S_L_N.setFlip('None')
        O_L_N.setPos((-0.4, -0.2))
        O_L_N.setOri(0.0)
        O_L_N.setText('他人:$Others_A')
        O_L_N.setHeight(0.04)
        O_L_N.setFlip('None')
        T_R_N.setColor('white', colorSpace='rgb')
        T_R_N.setOpacity(None)
        T_R_N.setContrast(1.0)
        T_R_N.setPos((0.4, 0.2))
        T_R_N.setOri(0.0)
        T_R_N.setText(Title_Right)
        T_R_N.setFont('Arial')
        T_R_N.setHeight(0.05)
        T_R_N.setFlip('None')
        S_R_L.setColor('white', colorSpace='rgb')
        S_R_L.setOpacity(None)
        S_R_L.setContrast(1.0)
        S_R_L.setPos((0.4, 0))
        S_R_L.setOri(0.0)
        S_R_L.setText('自己:$Self_B')
        S_R_L.setFont('Arial')
        S_R_L.setHeight(0.04)
        S_R_L.setFlip('None')
        O_R_N.setColor('white', colorSpace='rgb')
        O_R_N.setOpacity(None)
        O_R_N.setContrast(1.0)
        O_R_N.setPos((0.4, -0.2))
        O_R_N.setOri(0.0)
        O_R_N.setText('他人:$Others_B')
        O_R_N.setFont('Arial')
        O_R_N.setHeight(0.04)
        O_R_N.setFlip('None')
        # create starting attributes for key_formal_no_limited
        key_formal_no_limited.keys = []
        key_formal_no_limited.rt = []
        _key_formal_no_limited_allKeys = []
        worn_Nl.setFillColor('green')
        worn_Nl.setOpacity(None)
        worn_Nl.setContrast(1.0)
        worn_Nl.setPos((0, -0.5))
        worn_Nl.setSize((0.5, 0.5))
        worn_Nl.setLineColor('white')
        worn_Nl.setLineWidth(1.0)
        # store start times for Trail_loop_no_limited
        Trail_loop_no_limited.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Trail_loop_no_limited.tStart = globalClock.getTime(format='float')
        Trail_loop_no_limited.status = STARTED
        thisExp.addData('Trail_loop_no_limited.started', Trail_loop_no_limited.tStart)
        Trail_loop_no_limited.maxDuration = None
        # keep track of which components have finished
        Trail_loop_no_limitedComponents = Trail_loop_no_limited.components
        for thisComponent in Trail_loop_no_limited.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Trail_loop_no_limited" ---
        # if trial has changed, end Routine now
        if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
            continueRoutine = False
        Trail_loop_no_limited.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T_L_N* updates
            
            # if T_L_N is starting this frame...
            if T_L_N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_L_N.frameNStart = frameN  # exact frame index
                T_L_N.tStart = t  # local t and not account for scr refresh
                T_L_N.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_L_N, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T_L_N.started')
                # update status
                T_L_N.status = STARTED
                T_L_N.setAutoDraw(True)
            
            # if T_L_N is active this frame...
            if T_L_N.status == STARTED:
                # update params
                pass
            
            # if T_L_N is stopping this frame...
            if T_L_N.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_L_N.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    T_L_N.tStop = t  # not accounting for scr refresh
                    T_L_N.tStopRefresh = tThisFlipGlobal  # on global time
                    T_L_N.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'T_L_N.stopped')
                    # update status
                    T_L_N.status = FINISHED
                    T_L_N.setAutoDraw(False)
            
            # *S_L_N* updates
            
            # if S_L_N is starting this frame...
            if S_L_N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                S_L_N.frameNStart = frameN  # exact frame index
                S_L_N.tStart = t  # local t and not account for scr refresh
                S_L_N.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(S_L_N, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'S_L_N.started')
                # update status
                S_L_N.status = STARTED
                S_L_N.setAutoDraw(True)
            
            # if S_L_N is active this frame...
            if S_L_N.status == STARTED:
                # update params
                pass
            
            # if S_L_N is stopping this frame...
            if S_L_N.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > S_L_N.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    S_L_N.tStop = t  # not accounting for scr refresh
                    S_L_N.tStopRefresh = tThisFlipGlobal  # on global time
                    S_L_N.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'S_L_N.stopped')
                    # update status
                    S_L_N.status = FINISHED
                    S_L_N.setAutoDraw(False)
            
            # *O_L_N* updates
            
            # if O_L_N is starting this frame...
            if O_L_N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                O_L_N.frameNStart = frameN  # exact frame index
                O_L_N.tStart = t  # local t and not account for scr refresh
                O_L_N.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(O_L_N, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'O_L_N.started')
                # update status
                O_L_N.status = STARTED
                O_L_N.setAutoDraw(True)
            
            # if O_L_N is active this frame...
            if O_L_N.status == STARTED:
                # update params
                pass
            
            # if O_L_N is stopping this frame...
            if O_L_N.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > O_L_N.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    O_L_N.tStop = t  # not accounting for scr refresh
                    O_L_N.tStopRefresh = tThisFlipGlobal  # on global time
                    O_L_N.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'O_L_N.stopped')
                    # update status
                    O_L_N.status = FINISHED
                    O_L_N.setAutoDraw(False)
            
            # *T_R_N* updates
            
            # if T_R_N is starting this frame...
            if T_R_N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T_R_N.frameNStart = frameN  # exact frame index
                T_R_N.tStart = t  # local t and not account for scr refresh
                T_R_N.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T_R_N, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T_R_N.started')
                # update status
                T_R_N.status = STARTED
                T_R_N.setAutoDraw(True)
            
            # if T_R_N is active this frame...
            if T_R_N.status == STARTED:
                # update params
                pass
            
            # if T_R_N is stopping this frame...
            if T_R_N.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > T_R_N.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    T_R_N.tStop = t  # not accounting for scr refresh
                    T_R_N.tStopRefresh = tThisFlipGlobal  # on global time
                    T_R_N.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'T_R_N.stopped')
                    # update status
                    T_R_N.status = FINISHED
                    T_R_N.setAutoDraw(False)
            
            # *S_R_L* updates
            
            # if S_R_L is starting this frame...
            if S_R_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                S_R_L.frameNStart = frameN  # exact frame index
                S_R_L.tStart = t  # local t and not account for scr refresh
                S_R_L.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(S_R_L, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'S_R_L.started')
                # update status
                S_R_L.status = STARTED
                S_R_L.setAutoDraw(True)
            
            # if S_R_L is active this frame...
            if S_R_L.status == STARTED:
                # update params
                pass
            
            # if S_R_L is stopping this frame...
            if S_R_L.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > S_R_L.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    S_R_L.tStop = t  # not accounting for scr refresh
                    S_R_L.tStopRefresh = tThisFlipGlobal  # on global time
                    S_R_L.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'S_R_L.stopped')
                    # update status
                    S_R_L.status = FINISHED
                    S_R_L.setAutoDraw(False)
            
            # *O_R_N* updates
            
            # if O_R_N is starting this frame...
            if O_R_N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                O_R_N.frameNStart = frameN  # exact frame index
                O_R_N.tStart = t  # local t and not account for scr refresh
                O_R_N.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(O_R_N, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'O_R_N.started')
                # update status
                O_R_N.status = STARTED
                O_R_N.setAutoDraw(True)
            
            # if O_R_N is active this frame...
            if O_R_N.status == STARTED:
                # update params
                pass
            
            # if O_R_N is stopping this frame...
            if O_R_N.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > O_R_N.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    O_R_N.tStop = t  # not accounting for scr refresh
                    O_R_N.tStopRefresh = tThisFlipGlobal  # on global time
                    O_R_N.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'O_R_N.stopped')
                    # update status
                    O_R_N.status = FINISHED
                    O_R_N.setAutoDraw(False)
            
            # *key_formal_no_limited* updates
            waitOnFlip = False
            
            # if key_formal_no_limited is starting this frame...
            if key_formal_no_limited.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_formal_no_limited.frameNStart = frameN  # exact frame index
                key_formal_no_limited.tStart = t  # local t and not account for scr refresh
                key_formal_no_limited.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_formal_no_limited, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_formal_no_limited.started')
                # update status
                key_formal_no_limited.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_formal_no_limited.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_formal_no_limited.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_formal_no_limited is stopping this frame...
            if key_formal_no_limited.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_formal_no_limited.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    key_formal_no_limited.tStop = t  # not accounting for scr refresh
                    key_formal_no_limited.tStopRefresh = tThisFlipGlobal  # on global time
                    key_formal_no_limited.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_formal_no_limited.stopped')
                    # update status
                    key_formal_no_limited.status = FINISHED
                    key_formal_no_limited.status = FINISHED
            if key_formal_no_limited.status == STARTED and not waitOnFlip:
                theseKeys = key_formal_no_limited.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_formal_no_limited_allKeys.extend(theseKeys)
                if len(_key_formal_no_limited_allKeys):
                    key_formal_no_limited.keys = _key_formal_no_limited_allKeys[-1].name  # just the last key pressed
                    key_formal_no_limited.rt = _key_formal_no_limited_allKeys[-1].rt
                    key_formal_no_limited.duration = _key_formal_no_limited_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *worn_Nl* updates
            
            # if worn_Nl is starting this frame...
            if worn_Nl.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                worn_Nl.frameNStart = frameN  # exact frame index
                worn_Nl.tStart = t  # local t and not account for scr refresh
                worn_Nl.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(worn_Nl, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'worn_Nl.started')
                # update status
                worn_Nl.status = STARTED
                worn_Nl.setAutoDraw(True)
            
            # if worn_Nl is active this frame...
            if worn_Nl.status == STARTED:
                # update params
                pass
            
            # if worn_Nl is stopping this frame...
            if worn_Nl.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > worn_Nl.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    worn_Nl.tStop = t  # not accounting for scr refresh
                    worn_Nl.tStopRefresh = tThisFlipGlobal  # on global time
                    worn_Nl.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'worn_Nl.stopped')
                    # update status
                    worn_Nl.status = FINISHED
                    worn_Nl.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Trail_loop_no_limited.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trail_loop_no_limited.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trail_loop_no_limited" ---
        for thisComponent in Trail_loop_no_limited.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Trail_loop_no_limited
        Trail_loop_no_limited.tStop = globalClock.getTime(format='float')
        Trail_loop_no_limited.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Trail_loop_no_limited.stopped', Trail_loop_no_limited.tStop)
        # check responses
        if key_formal_no_limited.keys in ['', [], None]:  # No response was made
            key_formal_no_limited.keys = None
        trials_2.addData('key_formal_no_limited.keys',key_formal_no_limited.keys)
        if key_formal_no_limited.keys != None:  # we had a response
            trials_2.addData('key_formal_no_limited.rt', key_formal_no_limited.rt)
            trials_2.addData('key_formal_no_limited.duration', key_formal_no_limited.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Trail_loop_no_limited.maxDurationReached:
            routineTimer.addTime(-Trail_loop_no_limited.maxDuration)
        elif Trail_loop_no_limited.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "间歇休息" ---
        # create an object to store info about Routine 间歇休息
        间歇休息 = data.Routine(
            name='间歇休息',
            components=[text_6],
        )
        间歇休息.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        # 假设您的Excel总共有 60 行，您想每 20 个试次休息一次
        # trials.thisN 是当前试次的索引（从0开始计数）
        
        # 这里的逻辑是：如果当前做完的试次数量（thisN+1）不是20或40，就跳过休息
        if (trials.thisN + 1) not in [56, 112]:
            continueRoutine = False
        # store start times for 间歇休息
        间歇休息.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        间歇休息.tStart = globalClock.getTime(format='float')
        间歇休息.status = STARTED
        thisExp.addData('间歇休息.started', 间歇休息.tStart)
        间歇休息.maxDuration = None
        # keep track of which components have finished
        间歇休息Components = 间歇休息.components
        for thisComponent in 间歇休息.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "间歇休息" ---
        # if trial has changed, end Routine now
        if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
            continueRoutine = False
        间歇休息.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 30.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            
            # if text_6 is starting this frame...
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.started')
                # update status
                text_6.status = STARTED
                text_6.setAutoDraw(True)
            
            # if text_6 is active this frame...
            if text_6.status == STARTED:
                # update params
                pass
            
            # if text_6 is stopping this frame...
            if text_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_6.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    text_6.tStop = t  # not accounting for scr refresh
                    text_6.tStopRefresh = tThisFlipGlobal  # on global time
                    text_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_6.stopped')
                    # update status
                    text_6.status = FINISHED
                    text_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                间歇休息.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in 间歇休息.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "间歇休息" ---
        for thisComponent in 间歇休息.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for 间歇休息
        间歇休息.tStop = globalClock.getTime(format='float')
        间歇休息.tStopRefresh = tThisFlipGlobal
        thisExp.addData('间歇休息.stopped', 间歇休息.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if 间歇休息.maxDurationReached:
            routineTimer.addTime(-间歇休息.maxDuration)
        elif 间歇休息.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-30.000000)
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'trials_2'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end_word" ---
    # create an object to store info about Routine end_word
    end_word = data.Routine(
        name='end_word',
        components=[text_3],
    )
    end_word.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for end_word
    end_word.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end_word.tStart = globalClock.getTime(format='float')
    end_word.status = STARTED
    thisExp.addData('end_word.started', end_word.tStart)
    end_word.maxDuration = None
    # keep track of which components have finished
    end_wordComponents = end_word.components
    for thisComponent in end_word.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_word" ---
    end_word.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end_word.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_word.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_word" ---
    for thisComponent in end_word.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end_word
    end_word.tStop = globalClock.getTime(format='float')
    end_word.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end_word.stopped', end_word.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if end_word.maxDurationReached:
        routineTimer.addTime(-end_word.maxDuration)
    elif end_word.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
