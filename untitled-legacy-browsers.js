/***************** 
 * Untitled *
 *****************/


// store info about the experiment session:
let expName = 'untitled';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(start_wordRoutineBegin());
flowScheduler.add(start_wordRoutineEachFrame());
flowScheduler.add(start_wordRoutineEnd());
flowScheduler.add(practise_instructionRoutineBegin());
flowScheduler.add(practise_instructionRoutineEachFrame());
flowScheduler.add(practise_instructionRoutineEnd());
flowScheduler.add(练习_时间限制指导语RoutineBegin());
flowScheduler.add(练习_时间限制指导语RoutineEachFrame());
flowScheduler.add(练习_时间限制指导语RoutineEnd());
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);



flowScheduler.add(练习_非时间限制指导语RoutineBegin());
flowScheduler.add(练习_非时间限制指导语RoutineEachFrame());
flowScheduler.add(练习_非时间限制指导语RoutineEnd());
const trials_4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_4LoopBegin(trials_4LoopScheduler));
flowScheduler.add(trials_4LoopScheduler);
flowScheduler.add(trials_4LoopEnd);


flowScheduler.add(实验_正式实验指导语RoutineBegin());
flowScheduler.add(实验_正式实验指导语RoutineEachFrame());
flowScheduler.add(实验_正式实验指导语RoutineEnd());
flowScheduler.add(实验_时间限制指导语RoutineBegin());
flowScheduler.add(实验_时间限制指导语RoutineEachFrame());
flowScheduler.add(实验_时间限制指导语RoutineEnd());
const trials_5LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_5LoopBegin(trials_5LoopScheduler));
flowScheduler.add(trials_5LoopScheduler);
flowScheduler.add(trials_5LoopEnd);






flowScheduler.add(实验_非时间限制指导语RoutineBegin());
flowScheduler.add(实验_非时间限制指导语RoutineEachFrame());
flowScheduler.add(实验_非时间限制指导语RoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);



flowScheduler.add(end_wordRoutineBegin());
flowScheduler.add(end_wordRoutineEachFrame());
flowScheduler.add(end_wordRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'altruism_High.xlsx', 'path': 'altruism_High.xlsx'},
    {'name': 'altruism_Low.xlsx', 'path': 'altruism_Low.xlsx'},
    {'name': 'altruism_High.xlsx', 'path': 'altruism_High.xlsx'},
    {'name': 'altruism_High.xlsx', 'path': 'altruism_High.xlsx'},
    {'name': 'altruism_Low.xlsx', 'path': 'altruism_Low.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.2';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var start_wordClock;
var start_text;
var key_text;
var practise_instructionClock;
var text;
var key_resp;
var 练习_时间限制指导语Clock;
var text_5;
var key_resp_6;
var practise_time_limitedClock;
var Title_L;
var Self_L;
var Others_L;
var Title_R;
var Self_R;
var Others_R;
var key_prac_limited;
var worn_page_pracClock;
var worn_prac;
var 练习_非时间限制指导语Clock;
var text_4;
var key_resp_3;
var prac_time_none_limitedClock;
var Title_Left_NL;
var Self_Left_NL;
var Others_Left_NL;
var Title_Right_NL;
var Self_Right_NL;
var Others_Right_NL;
var key_prac_limited_NL;
var worn_NL;
var 实验_正式实验指导语Clock;
var text_2;
var key_resp_2;
var 实验_时间限制指导语Clock;
var text_7;
var key_resp_4;
var Trail_loop_limitedClock;
var T_L;
var S_L;
var O_L;
var T_R;
var S_R;
var O_R;
var key_formal_limited;
var worn_formal;
var worn_pageClock;
var worn;
var 间歇休息Clock;
var text_6;
var 实验_非时间限制指导语Clock;
var text_8;
var key_resp_5;
var Trail_loop_no_limitedClock;
var T_L_N;
var S_L_N;
var O_L_N;
var T_R_N;
var S_R_L;
var O_R_N;
var key_formal_no_limited;
var worn_Nl;
var end_wordClock;
var text_3;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "start_word"
  start_wordClock = new util.Clock();
  start_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_text',
    text: '欢迎参加本次心理学实验。\n> 在本实验中，您将面临一系列关于金钱分配的选择。在每次选择中，屏幕上会出现两个不同的分配方案（例如“方案 A”和“方案 B”）。每个方案都包含两部分金额：一部分是分给您自己的，另一部分是分给另一位匿名参与者的。\n> 您的任务是根据自己的偏好，在两个方案中选择一个。请注意，实验中没有正确或错误的答案，请完全按照您的真实想法进行选择。\n\n> 按 [空格键] 继续。',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_text = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practise_instruction"
  practise_instructionClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '为了让您熟悉实验流程和按键操作，我们先进行一个简短的练习阶段。\n>  * 如果您认为屏幕左侧的方案更好，请按键盘上的 [A]。\n>  * 如果您认为屏幕右侧的方案更好，请按键盘上的 [L]。\n> 请注意：练习阶段的选择不计入最终报酬，但请您像对待正式实验一样认真对待每一次选择。\n\n> 按 [空格键] 开始练习。',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "练习_时间限制指导语"
  练习_时间限制指导语Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '【注意：本组练习有时间限制】\n> 在接下来的练习中，由于任务要求您凭直觉快速反应，您需要在2秒内做出选择。\n>  * 屏幕上会出现一个倒计时进度条，显示剩余时间。\n>  * 如果您未在规定时间内做出按键反应，该试次将自动结束，且您和匿名参与者在该试次中都将获得 0 元。\n> 请尽可能快地做出决定，不要超时。\n\n> 准备好后，按 [空格键] 开始。',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practise_time_limited"
  practise_time_limitedClock = new util.Clock();
  Title_L = new visual.TextStim({
    win: psychoJS.window,
    name: 'Title_L',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Self_L = new visual.TextStim({
    win: psychoJS.window,
    name: 'Self_L',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  Others_L = new visual.TextStim({
    win: psychoJS.window,
    name: 'Others_L',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  Title_R = new visual.TextStim({
    win: psychoJS.window,
    name: 'Title_R',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  Self_R = new visual.TextStim({
    win: psychoJS.window,
    name: 'Self_R',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  Others_R = new visual.TextStim({
    win: psychoJS.window,
    name: 'Others_R',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  key_prac_limited = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "worn_page_prac"
  worn_page_pracClock = new util.Clock();
  worn_prac = new visual.Rect ({
    win: psychoJS.window, name: 'worn_prac', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "练习_非时间限制指导语"
  练习_非时间限制指导语Clock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: ' 【注意：本组练习无时间限制】\n> 在接下来的练习中，请您仔细考虑每一个选项。\n>  * 本阶段没有时间限制。\n>  * 您可以根据需要花费任意长的时间来权衡利弊，直到您确信自己的选择反映了您的真实意愿。\n>  * 请不要为了追求速度而匆忙按键，准确表达您的偏好最为重要。\n\n> 准备好后，按 [空格键] 开始。',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_time_none_limited"
  prac_time_none_limitedClock = new util.Clock();
  Title_Left_NL = new visual.TextStim({
    win: psychoJS.window,
    name: 'Title_Left_NL',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Self_Left_NL = new visual.TextStim({
    win: psychoJS.window,
    name: 'Self_Left_NL',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  Others_Left_NL = new visual.TextStim({
    win: psychoJS.window,
    name: 'Others_Left_NL',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  Title_Right_NL = new visual.TextStim({
    win: psychoJS.window,
    name: 'Title_Right_NL',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  Self_Right_NL = new visual.TextStim({
    win: psychoJS.window,
    name: 'Self_Right_NL',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  Others_Right_NL = new visual.TextStim({
    win: psychoJS.window,
    name: 'Others_Right_NL',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  key_prac_limited_NL = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  worn_NL = new visual.Rect ({
    win: psychoJS.window, name: 'worn_NL', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -7, interpolate: true,
  });
  
  // Initialize components for Routine "实验_正式实验指导语"
  实验_正式实验指导语Clock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '练习阶段结束。现在我们将进入正式实验阶段。\n> 从现在开始，您的每一个选择都将真实有效。实验包含多个小节（Block），在每个小节开始前，我会告知您该小节的具体要求（是否有时间限制）。\n> 请保持专注，并在实验过程中尽量避免身体大幅度晃动。\n\n> 按 [空格键] 开始正式实验',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "实验_时间限制指导语"
  实验_时间限制指导语Clock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: '本小节任务要求：快速反应\n>  * 请依靠您的第一直觉，尽可能快地做出选择。\n>  * 您必须在2秒内完成按键，否则本试次作废，双方收益均为 0。\n>  * 请集中注意力，紧盯屏幕。\n\n> 准备好后，按 [空格键] 开始本小节。\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Trail_loop_limited"
  Trail_loop_limitedClock = new util.Clock();
  T_L = new visual.TextStim({
    win: psychoJS.window,
    name: 'T_L',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  S_L = new visual.TextStim({
    win: psychoJS.window,
    name: 'S_L',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  O_L = new visual.TextStim({
    win: psychoJS.window,
    name: 'O_L',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  T_R = new visual.TextStim({
    win: psychoJS.window,
    name: 'T_R',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  S_R = new visual.TextStim({
    win: psychoJS.window,
    name: 'S_R',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  O_R = new visual.TextStim({
    win: psychoJS.window,
    name: 'O_R',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  key_formal_limited = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  worn_formal = new visual.Rect ({
    win: psychoJS.window, name: 'worn_formal', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -7, interpolate: true,
  });
  
  // Initialize components for Routine "worn_page"
  worn_pageClock = new util.Clock();
  worn = new visual.Rect ({
    win: psychoJS.window, name: 'worn', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "间歇休息"
  间歇休息Clock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '间歇30s',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "实验_非时间限制指导语"
  实验_非时间限制指导语Clock = new util.Clock();
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: '本小节任务要求：深思熟虑\n>  * 请仔细权衡每一个选项，按照您的真实意愿进行分配。\n>  * 本小节没有时间限制，无论您思考多久都可以。\n>  * 请确保您看清了两个方案的具体数值后再做决定。\n\n> 准备好后，按 [空格键] 开始本小节。\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Trail_loop_no_limited"
  Trail_loop_no_limitedClock = new util.Clock();
  T_L_N = new visual.TextStim({
    win: psychoJS.window,
    name: 'T_L_N',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  S_L_N = new visual.TextStim({
    win: psychoJS.window,
    name: 'S_L_N',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  O_L_N = new visual.TextStim({
    win: psychoJS.window,
    name: 'O_L_N',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  T_R_N = new visual.TextStim({
    win: psychoJS.window,
    name: 'T_R_N',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  S_R_L = new visual.TextStim({
    win: psychoJS.window,
    name: 'S_R_L',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  O_R_N = new visual.TextStim({
    win: psychoJS.window,
    name: 'O_R_N',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  key_formal_no_limited = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  worn_Nl = new visual.Rect ({
    win: psychoJS.window, name: 'worn_Nl', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -7, interpolate: true,
  });
  
  // Initialize components for Routine "end_word"
  end_wordClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'jieshuyv',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var start_wordMaxDurationReached;
var _key_text_allKeys;
var start_wordMaxDuration;
var start_wordComponents;
function start_wordRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'start_word' ---
    t = 0;
    start_wordClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    start_wordMaxDurationReached = false;
    // update component parameters for each repeat
    key_text.keys = undefined;
    key_text.rt = undefined;
    _key_text_allKeys = [];
    psychoJS.experiment.addData('start_word.started', globalClock.getTime());
    start_wordMaxDuration = null
    // keep track of which components have finished
    start_wordComponents = [];
    start_wordComponents.push(start_text);
    start_wordComponents.push(key_text);
    
    start_wordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function start_wordRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'start_word' ---
    // get current time
    t = start_wordClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_text* updates
    if (t >= 0.0 && start_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_text.tStart = t;  // (not accounting for frame time here)
      start_text.frameNStart = frameN;  // exact frame index
      
      start_text.setAutoDraw(true);
    }
    
    
    // *key_text* updates
    if (t >= 0.0 && key_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_text.tStart = t;  // (not accounting for frame time here)
      key_text.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_text.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_text.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_text.clearEvents(); });
    }
    
    if (key_text.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_text.getKeys({keyList: ['space'], waitRelease: false});
      _key_text_allKeys = _key_text_allKeys.concat(theseKeys);
      if (_key_text_allKeys.length > 0) {
        key_text.keys = _key_text_allKeys[_key_text_allKeys.length - 1].name;  // just the last key pressed
        key_text.rt = _key_text_allKeys[_key_text_allKeys.length - 1].rt;
        key_text.duration = _key_text_allKeys[_key_text_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    start_wordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_wordRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'start_word' ---
    start_wordComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('start_word.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_text.corr, level);
    }
    psychoJS.experiment.addData('key_text.keys', key_text.keys);
    if (typeof key_text.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_text.rt', key_text.rt);
        psychoJS.experiment.addData('key_text.duration', key_text.duration);
        routineTimer.reset();
        }
    
    key_text.stop();
    // the Routine "start_word" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practise_instructionMaxDurationReached;
var _key_resp_allKeys;
var practise_instructionMaxDuration;
var practise_instructionComponents;
function practise_instructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practise_instruction' ---
    t = 0;
    practise_instructionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practise_instructionMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('practise_instruction.started', globalClock.getTime());
    practise_instructionMaxDuration = null
    // keep track of which components have finished
    practise_instructionComponents = [];
    practise_instructionComponents.push(text);
    practise_instructionComponents.push(key_resp);
    
    practise_instructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practise_instructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practise_instruction' ---
    // get current time
    t = practise_instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practise_instructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practise_instructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practise_instruction' ---
    practise_instructionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practise_instruction.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "practise_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var 练习_时间限制指导语MaxDurationReached;
var _key_resp_6_allKeys;
var 练习_时间限制指导语MaxDuration;
var 练习_时间限制指导语Components;
function 练习_时间限制指导语RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine '练习_时间限制指导语' ---
    t = 0;
    练习_时间限制指导语Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    练习_时间限制指导语MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    psychoJS.experiment.addData('练习_时间限制指导语.started', globalClock.getTime());
    练习_时间限制指导语MaxDuration = null
    // keep track of which components have finished
    练习_时间限制指导语Components = [];
    练习_时间限制指导语Components.push(text_5);
    练习_时间限制指导语Components.push(key_resp_6);
    
    练习_时间限制指导语Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function 练习_时间限制指导语RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine '练习_时间限制指导语' ---
    // get current time
    t = 练习_时间限制指导语Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }
    
    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }
    
    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        key_resp_6.duration = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    练习_时间限制指导语Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function 练习_时间限制指导语RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine '练习_时间限制指导语' ---
    练习_时间限制指导语Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('练习_时间限制指导语.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        psychoJS.experiment.addData('key_resp_6.duration', key_resp_6.duration);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "练习_时间限制指导语" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.FULLRANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'altruism_High.xlsx',
      seed: 10, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_3.forEach(function() {
      snapshot = trials_3.getSnapshot();
    
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(practise_time_limitedRoutineBegin(snapshot));
      trials_3LoopScheduler.add(practise_time_limitedRoutineEachFrame());
      trials_3LoopScheduler.add(practise_time_limitedRoutineEnd(snapshot));
      trials_3LoopScheduler.add(worn_page_pracRoutineBegin(snapshot));
      trials_3LoopScheduler.add(worn_page_pracRoutineEachFrame());
      trials_3LoopScheduler.add(worn_page_pracRoutineEnd(snapshot));
      trials_3LoopScheduler.add(trials_3LoopEndIteration(trials_3LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_4;
function trials_4LoopBegin(trials_4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.FULLRANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'altruism_Low.xlsx',
      seed: 10, name: 'trials_4'
    });
    psychoJS.experiment.addLoop(trials_4); // add the loop to the experiment
    currentLoop = trials_4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_4.forEach(function() {
      snapshot = trials_4.getSnapshot();
    
      trials_4LoopScheduler.add(importConditions(snapshot));
      trials_4LoopScheduler.add(prac_time_none_limitedRoutineBegin(snapshot));
      trials_4LoopScheduler.add(prac_time_none_limitedRoutineEachFrame());
      trials_4LoopScheduler.add(prac_time_none_limitedRoutineEnd(snapshot));
      trials_4LoopScheduler.add(trials_4LoopEndIteration(trials_4LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_5;
function trials_5LoopBegin(trials_5LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_5 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 3, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'altruism_High.xlsx',
      seed: undefined, name: 'trials_5'
    });
    psychoJS.experiment.addLoop(trials_5); // add the loop to the experiment
    currentLoop = trials_5;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_5.forEach(function() {
      snapshot = trials_5.getSnapshot();
    
      trials_5LoopScheduler.add(importConditions(snapshot));
      const trialsLoopScheduler = new Scheduler(psychoJS);
      trials_5LoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      trials_5LoopScheduler.add(trialsLoopScheduler);
      trials_5LoopScheduler.add(trialsLoopEnd);
      trials_5LoopScheduler.add(间歇休息RoutineBegin(snapshot));
      trials_5LoopScheduler.add(间歇休息RoutineEachFrame());
      trials_5LoopScheduler.add(间歇休息RoutineEnd(snapshot));
      trials_5LoopScheduler.add(trials_5LoopEndIteration(trials_5LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'altruism_High.xlsx',
      seed: 56, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(Trail_loop_limitedRoutineBegin(snapshot));
      trialsLoopScheduler.add(Trail_loop_limitedRoutineEachFrame());
      trialsLoopScheduler.add(Trail_loop_limitedRoutineEnd(snapshot));
      trialsLoopScheduler.add(worn_pageRoutineBegin(snapshot));
      trialsLoopScheduler.add(worn_pageRoutineEachFrame());
      trialsLoopScheduler.add(worn_pageRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trials_5LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_5);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_5LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 3, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'altruism_Low.xlsx',
      seed: 56, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(Trail_loop_no_limitedRoutineBegin(snapshot));
      trials_2LoopScheduler.add(Trail_loop_no_limitedRoutineEachFrame());
      trials_2LoopScheduler.add(Trail_loop_no_limitedRoutineEnd(snapshot));
      trials_2LoopScheduler.add(间歇休息RoutineBegin(snapshot));
      trials_2LoopScheduler.add(间歇休息RoutineEachFrame());
      trials_2LoopScheduler.add(间歇休息RoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var practise_time_limitedMaxDurationReached;
var _key_prac_limited_allKeys;
var practise_time_limitedMaxDuration;
var practise_time_limitedComponents;
function practise_time_limitedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practise_time_limited' ---
    t = 0;
    practise_time_limitedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    practise_time_limitedMaxDurationReached = false;
    // update component parameters for each repeat
    Title_L.setColor(new util.Color('white'));
    Title_L.setOpacity(None);
    Title_L.setContrast(1.0);
    Title_L.setPos([(- 0.4), 0.5]);
    Title_L.setOri(0.0);
    Title_L.setText(Title_Left);
    Title_L.setFont('Arial');
    Title_L.setHeight(0.05);
    Title_L.setFlip('None');
    Self_L.setPos([(- 0.4), 0.3]);
    Self_L.setOri(0.0);
    Self_L.setText('自己:$Self_A');
    Self_L.setFlip('None');
    Others_L.setPos([(- 0.4), 0.1]);
    Others_L.setOri(0.0);
    Others_L.setText('他人:$Others_A');
    Others_L.setHeight(0.04);
    Others_L.setFlip('None');
    Title_R.setColor(new util.Color('white'));
    Title_R.setOpacity(None);
    Title_R.setContrast(1.0);
    Title_R.setPos([0.4, 0.5]);
    Title_R.setOri(0.0);
    Title_R.setText(Title_Right);
    Title_R.setFont('Arial');
    Title_R.setHeight(0.05);
    Title_R.setFlip('None');
    Self_R.setColor(new util.Color('white'));
    Self_R.setOpacity(None);
    Self_R.setContrast(1.0);
    Self_R.setPos([0.4, 0.3]);
    Self_R.setOri(0.0);
    Self_R.setText('自己:$Self_B');
    Self_R.setFont('Arial');
    Self_R.setHeight(0.04);
    Self_R.setFlip('None');
    Others_R.setColor(new util.Color('white'));
    Others_R.setOpacity(None);
    Others_R.setContrast(1.0);
    Others_R.setPos([0.4, 0.1]);
    Others_R.setOri(0.0);
    Others_R.setText('他人:$Others_B');
    Others_R.setFont('Arial');
    Others_R.setHeight(0.04);
    Others_R.setFlip('None');
    key_prac_limited.keys = undefined;
    key_prac_limited.rt = undefined;
    _key_prac_limited_allKeys = [];
    psychoJS.experiment.addData('practise_time_limited.started', globalClock.getTime());
    practise_time_limitedMaxDuration = null
    // keep track of which components have finished
    practise_time_limitedComponents = [];
    practise_time_limitedComponents.push(Title_L);
    practise_time_limitedComponents.push(Self_L);
    practise_time_limitedComponents.push(Others_L);
    practise_time_limitedComponents.push(Title_R);
    practise_time_limitedComponents.push(Self_R);
    practise_time_limitedComponents.push(Others_R);
    practise_time_limitedComponents.push(key_prac_limited);
    
    practise_time_limitedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function practise_time_limitedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practise_time_limited' ---
    // get current time
    t = practise_time_limitedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Title_L* updates
    if (t >= 0.0 && Title_L.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Title_L.tStart = t;  // (not accounting for frame time here)
      Title_L.frameNStart = frameN;  // exact frame index
      
      Title_L.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Title_L.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Title_L.setAutoDraw(false);
    }
    
    
    // *Self_L* updates
    if (t >= 0.0 && Self_L.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Self_L.tStart = t;  // (not accounting for frame time here)
      Self_L.frameNStart = frameN;  // exact frame index
      
      Self_L.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Self_L.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Self_L.setAutoDraw(false);
    }
    
    
    // *Others_L* updates
    if (t >= 0.0 && Others_L.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Others_L.tStart = t;  // (not accounting for frame time here)
      Others_L.frameNStart = frameN;  // exact frame index
      
      Others_L.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Others_L.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Others_L.setAutoDraw(false);
    }
    
    
    // *Title_R* updates
    if (t >= 0.0 && Title_R.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Title_R.tStart = t;  // (not accounting for frame time here)
      Title_R.frameNStart = frameN;  // exact frame index
      
      Title_R.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Title_R.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Title_R.setAutoDraw(false);
    }
    
    
    // *Self_R* updates
    if (t >= 0.0 && Self_R.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Self_R.tStart = t;  // (not accounting for frame time here)
      Self_R.frameNStart = frameN;  // exact frame index
      
      Self_R.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Self_R.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Self_R.setAutoDraw(false);
    }
    
    
    // *Others_R* updates
    if (t >= 0.0 && Others_R.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Others_R.tStart = t;  // (not accounting for frame time here)
      Others_R.frameNStart = frameN;  // exact frame index
      
      Others_R.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Others_R.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Others_R.setAutoDraw(false);
    }
    
    
    // *key_prac_limited* updates
    if (t >= 0.0 && key_prac_limited.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_prac_limited.tStart = t;  // (not accounting for frame time here)
      key_prac_limited.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_prac_limited.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_prac_limited.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_prac_limited.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_prac_limited.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_prac_limited.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_prac_limited.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_prac_limited.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_prac_limited_allKeys = _key_prac_limited_allKeys.concat(theseKeys);
      if (_key_prac_limited_allKeys.length > 0) {
        key_prac_limited.keys = _key_prac_limited_allKeys[_key_prac_limited_allKeys.length - 1].name;  // just the last key pressed
        key_prac_limited.rt = _key_prac_limited_allKeys[_key_prac_limited_allKeys.length - 1].rt;
        key_prac_limited.duration = _key_prac_limited_allKeys[_key_prac_limited_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practise_time_limitedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practise_time_limitedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practise_time_limited' ---
    practise_time_limitedComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practise_time_limited.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_prac_limited.corr, level);
    }
    psychoJS.experiment.addData('key_prac_limited.keys', key_prac_limited.keys);
    if (typeof key_prac_limited.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_prac_limited.rt', key_prac_limited.rt);
        psychoJS.experiment.addData('key_prac_limited.duration', key_prac_limited.duration);
        routineTimer.reset();
        }
    
    key_prac_limited.stop();
    if (practise_time_limitedMaxDurationReached) {
        routineTimer.add(practise_time_limitedMaxDuration);
    } else {
        routineTimer.add(-1.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var worn_page_pracMaxDurationReached;
var worn_page_pracMaxDuration;
var worn_page_pracComponents;
function worn_page_pracRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'worn_page_prac' ---
    t = 0;
    worn_page_pracClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    worn_page_pracMaxDurationReached = false;
    // update component parameters for each repeat
    worn_prac.setFillColor(new util.Color('red'));
    worn_prac.setOpacity(None);
    worn_prac.setContrast(1.0);
    worn_prac.setPos([0, (- 0.5)]);
    worn_prac.setSize([0.5, 0.5]);
    worn_prac.setLineColor(new util.Color('white'));
    worn_prac.setLineWidth(1.0);
    psychoJS.experiment.addData('worn_page_prac.started', globalClock.getTime());
    worn_page_pracMaxDuration = null
    // keep track of which components have finished
    worn_page_pracComponents = [];
    worn_page_pracComponents.push(worn_prac);
    
    worn_page_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function worn_page_pracRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'worn_page_prac' ---
    // get current time
    t = worn_page_pracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *worn_prac* updates
    if (t >= 0.0 && worn_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      worn_prac.tStart = t;  // (not accounting for frame time here)
      worn_prac.frameNStart = frameN;  // exact frame index
      
      worn_prac.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (worn_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      worn_prac.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    worn_page_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function worn_page_pracRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'worn_page_prac' ---
    worn_page_pracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('worn_page_prac.stopped', globalClock.getTime());
    if (worn_page_pracMaxDurationReached) {
        routineTimer.add(worn_page_pracMaxDuration);
    } else {
        routineTimer.add(-1.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var 练习_非时间限制指导语MaxDurationReached;
var _key_resp_3_allKeys;
var 练习_非时间限制指导语MaxDuration;
var 练习_非时间限制指导语Components;
function 练习_非时间限制指导语RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine '练习_非时间限制指导语' ---
    t = 0;
    练习_非时间限制指导语Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    练习_非时间限制指导语MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    psychoJS.experiment.addData('练习_非时间限制指导语.started', globalClock.getTime());
    练习_非时间限制指导语MaxDuration = null
    // keep track of which components have finished
    练习_非时间限制指导语Components = [];
    练习_非时间限制指导语Components.push(text_4);
    练习_非时间限制指导语Components.push(key_resp_3);
    
    练习_非时间限制指导语Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function 练习_非时间限制指导语RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine '练习_非时间限制指导语' ---
    // get current time
    t = 练习_非时间限制指导语Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    练习_非时间限制指导语Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function 练习_非时间限制指导语RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine '练习_非时间限制指导语' ---
    练习_非时间限制指导语Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('练习_非时间限制指导语.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "练习_非时间限制指导语" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prac_time_none_limitedMaxDurationReached;
var _key_prac_limited_NL_allKeys;
var prac_time_none_limitedMaxDuration;
var prac_time_none_limitedComponents;
function prac_time_none_limitedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_time_none_limited' ---
    t = 0;
    prac_time_none_limitedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    prac_time_none_limitedMaxDurationReached = false;
    // update component parameters for each repeat
    Title_Left_NL.setColor(new util.Color('white'));
    Title_Left_NL.setOpacity(None);
    Title_Left_NL.setContrast(1.0);
    Title_Left_NL.setPos([(- 0.4), 0.2]);
    Title_Left_NL.setOri(0.0);
    Title_Left_NL.setText(Title_Left);
    Title_Left_NL.setFont('Arial');
    Title_Left_NL.setHeight(0.05);
    Title_Left_NL.setFlip('None');
    Self_Left_NL.setPos([(- 0.4), 0]);
    Self_Left_NL.setOri(0.0);
    Self_Left_NL.setText('自己:$Self_A');
    Self_Left_NL.setFlip('None');
    Others_Left_NL.setPos([(- 0.4), (- 0.2)]);
    Others_Left_NL.setOri(0.0);
    Others_Left_NL.setText('他人:$Others_A');
    Others_Left_NL.setHeight(0.04);
    Others_Left_NL.setFlip('None');
    Title_Right_NL.setColor(new util.Color('white'));
    Title_Right_NL.setOpacity(None);
    Title_Right_NL.setContrast(1.0);
    Title_Right_NL.setPos([0.4, 0.2]);
    Title_Right_NL.setOri(0.0);
    Title_Right_NL.setText(Title_Right);
    Title_Right_NL.setFont('Arial');
    Title_Right_NL.setHeight(0.05);
    Title_Right_NL.setFlip('None');
    Self_Right_NL.setColor(new util.Color('white'));
    Self_Right_NL.setOpacity(None);
    Self_Right_NL.setContrast(1.0);
    Self_Right_NL.setPos([0.4, 0]);
    Self_Right_NL.setOri(0.0);
    Self_Right_NL.setText('自己:$Self_B');
    Self_Right_NL.setFont('Arial');
    Self_Right_NL.setHeight(0.04);
    Self_Right_NL.setFlip('None');
    Others_Right_NL.setColor(new util.Color('white'));
    Others_Right_NL.setOpacity(None);
    Others_Right_NL.setContrast(1.0);
    Others_Right_NL.setPos([0.4, (- 0.2)]);
    Others_Right_NL.setOri(0.0);
    Others_Right_NL.setText('他人:$Others_B');
    Others_Right_NL.setFont('Arial');
    Others_Right_NL.setHeight(0.04);
    Others_Right_NL.setFlip('None');
    key_prac_limited_NL.keys = undefined;
    key_prac_limited_NL.rt = undefined;
    _key_prac_limited_NL_allKeys = [];
    worn_NL.setFillColor(new util.Color('green'));
    worn_NL.setOpacity(None);
    worn_NL.setContrast(1.0);
    worn_NL.setPos([0, (- 0.5)]);
    worn_NL.setSize([0.5, 0.5]);
    worn_NL.setLineColor(new util.Color('white'));
    worn_NL.setLineWidth(1.0);
    psychoJS.experiment.addData('prac_time_none_limited.started', globalClock.getTime());
    prac_time_none_limitedMaxDuration = null
    // keep track of which components have finished
    prac_time_none_limitedComponents = [];
    prac_time_none_limitedComponents.push(Title_Left_NL);
    prac_time_none_limitedComponents.push(Self_Left_NL);
    prac_time_none_limitedComponents.push(Others_Left_NL);
    prac_time_none_limitedComponents.push(Title_Right_NL);
    prac_time_none_limitedComponents.push(Self_Right_NL);
    prac_time_none_limitedComponents.push(Others_Right_NL);
    prac_time_none_limitedComponents.push(key_prac_limited_NL);
    prac_time_none_limitedComponents.push(worn_NL);
    
    prac_time_none_limitedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_time_none_limitedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_time_none_limited' ---
    // get current time
    t = prac_time_none_limitedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Title_Left_NL* updates
    if (t >= 0.0 && Title_Left_NL.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Title_Left_NL.tStart = t;  // (not accounting for frame time here)
      Title_Left_NL.frameNStart = frameN;  // exact frame index
      
      Title_Left_NL.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Title_Left_NL.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Title_Left_NL.setAutoDraw(false);
    }
    
    
    // *Self_Left_NL* updates
    if (t >= 0.0 && Self_Left_NL.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Self_Left_NL.tStart = t;  // (not accounting for frame time here)
      Self_Left_NL.frameNStart = frameN;  // exact frame index
      
      Self_Left_NL.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Self_Left_NL.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Self_Left_NL.setAutoDraw(false);
    }
    
    
    // *Others_Left_NL* updates
    if (t >= 0.0 && Others_Left_NL.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Others_Left_NL.tStart = t;  // (not accounting for frame time here)
      Others_Left_NL.frameNStart = frameN;  // exact frame index
      
      Others_Left_NL.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Others_Left_NL.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Others_Left_NL.setAutoDraw(false);
    }
    
    
    // *Title_Right_NL* updates
    if (t >= 0.0 && Title_Right_NL.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Title_Right_NL.tStart = t;  // (not accounting for frame time here)
      Title_Right_NL.frameNStart = frameN;  // exact frame index
      
      Title_Right_NL.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Title_Right_NL.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Title_Right_NL.setAutoDraw(false);
    }
    
    
    // *Self_Right_NL* updates
    if (t >= 0.0 && Self_Right_NL.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Self_Right_NL.tStart = t;  // (not accounting for frame time here)
      Self_Right_NL.frameNStart = frameN;  // exact frame index
      
      Self_Right_NL.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Self_Right_NL.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Self_Right_NL.setAutoDraw(false);
    }
    
    
    // *Others_Right_NL* updates
    if (t >= 0.0 && Others_Right_NL.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Others_Right_NL.tStart = t;  // (not accounting for frame time here)
      Others_Right_NL.frameNStart = frameN;  // exact frame index
      
      Others_Right_NL.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Others_Right_NL.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Others_Right_NL.setAutoDraw(false);
    }
    
    
    // *key_prac_limited_NL* updates
    if (t >= 0.0 && key_prac_limited_NL.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_prac_limited_NL.tStart = t;  // (not accounting for frame time here)
      key_prac_limited_NL.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_prac_limited_NL.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_prac_limited_NL.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_prac_limited_NL.clearEvents(); });
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_prac_limited_NL.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_prac_limited_NL.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_prac_limited_NL.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_prac_limited_NL.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_prac_limited_NL_allKeys = _key_prac_limited_NL_allKeys.concat(theseKeys);
      if (_key_prac_limited_NL_allKeys.length > 0) {
        key_prac_limited_NL.keys = _key_prac_limited_NL_allKeys[_key_prac_limited_NL_allKeys.length - 1].name;  // just the last key pressed
        key_prac_limited_NL.rt = _key_prac_limited_NL_allKeys[_key_prac_limited_NL_allKeys.length - 1].rt;
        key_prac_limited_NL.duration = _key_prac_limited_NL_allKeys[_key_prac_limited_NL_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *worn_NL* updates
    if (t >= 0.0 && worn_NL.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      worn_NL.tStart = t;  // (not accounting for frame time here)
      worn_NL.frameNStart = frameN;  // exact frame index
      
      worn_NL.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (worn_NL.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      worn_NL.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_time_none_limitedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_time_none_limitedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_time_none_limited' ---
    prac_time_none_limitedComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('prac_time_none_limited.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_prac_limited_NL.corr, level);
    }
    psychoJS.experiment.addData('key_prac_limited_NL.keys', key_prac_limited_NL.keys);
    if (typeof key_prac_limited_NL.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_prac_limited_NL.rt', key_prac_limited_NL.rt);
        psychoJS.experiment.addData('key_prac_limited_NL.duration', key_prac_limited_NL.duration);
        routineTimer.reset();
        }
    
    key_prac_limited_NL.stop();
    if (prac_time_none_limitedMaxDurationReached) {
        routineTimer.add(prac_time_none_limitedMaxDuration);
    } else {
        routineTimer.add(-10.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var 实验_正式实验指导语MaxDurationReached;
var _key_resp_2_allKeys;
var 实验_正式实验指导语MaxDuration;
var 实验_正式实验指导语Components;
function 实验_正式实验指导语RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine '实验_正式实验指导语' ---
    t = 0;
    实验_正式实验指导语Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    实验_正式实验指导语MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    psychoJS.experiment.addData('实验_正式实验指导语.started', globalClock.getTime());
    实验_正式实验指导语MaxDuration = null
    // keep track of which components have finished
    实验_正式实验指导语Components = [];
    实验_正式实验指导语Components.push(text_2);
    实验_正式实验指导语Components.push(key_resp_2);
    
    实验_正式实验指导语Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function 实验_正式实验指导语RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine '实验_正式实验指导语' ---
    // get current time
    t = 实验_正式实验指导语Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    实验_正式实验指导语Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function 实验_正式实验指导语RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine '实验_正式实验指导语' ---
    实验_正式实验指导语Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('实验_正式实验指导语.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "实验_正式实验指导语" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var 实验_时间限制指导语MaxDurationReached;
var _key_resp_4_allKeys;
var 实验_时间限制指导语MaxDuration;
var 实验_时间限制指导语Components;
function 实验_时间限制指导语RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine '实验_时间限制指导语' ---
    t = 0;
    实验_时间限制指导语Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    实验_时间限制指导语MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    psychoJS.experiment.addData('实验_时间限制指导语.started', globalClock.getTime());
    实验_时间限制指导语MaxDuration = null
    // keep track of which components have finished
    实验_时间限制指导语Components = [];
    实验_时间限制指导语Components.push(text_7);
    实验_时间限制指导语Components.push(key_resp_4);
    
    实验_时间限制指导语Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function 实验_时间限制指导语RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine '实验_时间限制指导语' ---
    // get current time
    t = 实验_时间限制指导语Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }
    
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }
    
    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        key_resp_4.duration = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    实验_时间限制指导语Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function 实验_时间限制指导语RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine '实验_时间限制指导语' ---
    实验_时间限制指导语Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('实验_时间限制指导语.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        psychoJS.experiment.addData('key_resp_4.duration', key_resp_4.duration);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "实验_时间限制指导语" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Trail_loop_limitedMaxDurationReached;
var _key_formal_limited_allKeys;
var Trail_loop_limitedMaxDuration;
var Trail_loop_limitedComponents;
function Trail_loop_limitedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Trail_loop_limited' ---
    t = 0;
    Trail_loop_limitedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    Trail_loop_limitedMaxDurationReached = false;
    // update component parameters for each repeat
    T_L.setColor(new util.Color('white'));
    T_L.setOpacity(None);
    T_L.setContrast(1.0);
    T_L.setPos([(- 0.4), 0.2]);
    T_L.setOri(0.0);
    T_L.setText(Title_Left);
    T_L.setFont('Arial');
    T_L.setHeight(0.05);
    T_L.setFlip('None');
    S_L.setPos([(- 0.4), 0]);
    S_L.setOri(0.0);
    S_L.setText('自己:$Self_A');
    S_L.setFlip('None');
    O_L.setPos([(- 0.4), (- 0.2)]);
    O_L.setOri(0.0);
    O_L.setText('他人:$Others_A');
    O_L.setHeight(0.04);
    O_L.setFlip('None');
    T_R.setColor(new util.Color('white'));
    T_R.setOpacity(None);
    T_R.setContrast(1.0);
    T_R.setPos([0.4, 0.2]);
    T_R.setOri(0.0);
    T_R.setText(Title_Right);
    T_R.setFont('Arial');
    T_R.setHeight(0.05);
    T_R.setFlip('None');
    S_R.setColor(new util.Color('white'));
    S_R.setOpacity(None);
    S_R.setContrast(1.0);
    S_R.setPos([0.4, 0]);
    S_R.setOri(0.0);
    S_R.setText('自己:$Self_B');
    S_R.setFont('Arial');
    S_R.setHeight(0.04);
    S_R.setFlip('None');
    O_R.setColor(new util.Color('white'));
    O_R.setOpacity(None);
    O_R.setContrast(1.0);
    O_R.setPos([0.4, (- 0.2)]);
    O_R.setOri(0.0);
    O_R.setText('他人:$Others_B');
    O_R.setFont('Arial');
    O_R.setHeight(0.04);
    O_R.setFlip('None');
    key_formal_limited.keys = undefined;
    key_formal_limited.rt = undefined;
    _key_formal_limited_allKeys = [];
    worn_formal.setFillColor(new util.Color('red'));
    worn_formal.setOpacity(None);
    worn_formal.setContrast(1.0);
    worn_formal.setPos([0, (- 0.5)]);
    worn_formal.setSize([0.5, 0.5]);
    worn_formal.setLineColor(new util.Color('white'));
    worn_formal.setLineWidth(1.0);
    psychoJS.experiment.addData('Trail_loop_limited.started', globalClock.getTime());
    Trail_loop_limitedMaxDuration = null
    // keep track of which components have finished
    Trail_loop_limitedComponents = [];
    Trail_loop_limitedComponents.push(T_L);
    Trail_loop_limitedComponents.push(S_L);
    Trail_loop_limitedComponents.push(O_L);
    Trail_loop_limitedComponents.push(T_R);
    Trail_loop_limitedComponents.push(S_R);
    Trail_loop_limitedComponents.push(O_R);
    Trail_loop_limitedComponents.push(key_formal_limited);
    Trail_loop_limitedComponents.push(worn_formal);
    
    Trail_loop_limitedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Trail_loop_limitedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Trail_loop_limited' ---
    // get current time
    t = Trail_loop_limitedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *T_L* updates
    if (t >= 0.0 && T_L.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      T_L.tStart = t;  // (not accounting for frame time here)
      T_L.frameNStart = frameN;  // exact frame index
      
      T_L.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (T_L.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      T_L.setAutoDraw(false);
    }
    
    
    // *S_L* updates
    if (t >= 0.0 && S_L.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      S_L.tStart = t;  // (not accounting for frame time here)
      S_L.frameNStart = frameN;  // exact frame index
      
      S_L.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (S_L.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      S_L.setAutoDraw(false);
    }
    
    
    // *O_L* updates
    if (t >= 0.0 && O_L.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      O_L.tStart = t;  // (not accounting for frame time here)
      O_L.frameNStart = frameN;  // exact frame index
      
      O_L.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (O_L.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      O_L.setAutoDraw(false);
    }
    
    
    // *T_R* updates
    if (t >= 0.0 && T_R.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      T_R.tStart = t;  // (not accounting for frame time here)
      T_R.frameNStart = frameN;  // exact frame index
      
      T_R.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (T_R.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      T_R.setAutoDraw(false);
    }
    
    
    // *S_R* updates
    if (t >= 0.0 && S_R.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      S_R.tStart = t;  // (not accounting for frame time here)
      S_R.frameNStart = frameN;  // exact frame index
      
      S_R.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (S_R.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      S_R.setAutoDraw(false);
    }
    
    
    // *O_R* updates
    if (t >= 0.0 && O_R.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      O_R.tStart = t;  // (not accounting for frame time here)
      O_R.frameNStart = frameN;  // exact frame index
      
      O_R.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (O_R.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      O_R.setAutoDraw(false);
    }
    
    
    // *key_formal_limited* updates
    if (t >= 0.0 && key_formal_limited.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_formal_limited.tStart = t;  // (not accounting for frame time here)
      key_formal_limited.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_formal_limited.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_formal_limited.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_formal_limited.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_formal_limited.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_formal_limited.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_formal_limited.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_formal_limited.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_formal_limited_allKeys = _key_formal_limited_allKeys.concat(theseKeys);
      if (_key_formal_limited_allKeys.length > 0) {
        key_formal_limited.keys = _key_formal_limited_allKeys[_key_formal_limited_allKeys.length - 1].name;  // just the last key pressed
        key_formal_limited.rt = _key_formal_limited_allKeys[_key_formal_limited_allKeys.length - 1].rt;
        key_formal_limited.duration = _key_formal_limited_allKeys[_key_formal_limited_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *worn_formal* updates
    if (t >= 0.0 && worn_formal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      worn_formal.tStart = t;  // (not accounting for frame time here)
      worn_formal.frameNStart = frameN;  // exact frame index
      
      worn_formal.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (worn_formal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      worn_formal.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Trail_loop_limitedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Trail_loop_limitedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Trail_loop_limited' ---
    Trail_loop_limitedComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Trail_loop_limited.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_formal_limited.corr, level);
    }
    psychoJS.experiment.addData('key_formal_limited.keys', key_formal_limited.keys);
    if (typeof key_formal_limited.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_formal_limited.rt', key_formal_limited.rt);
        psychoJS.experiment.addData('key_formal_limited.duration', key_formal_limited.duration);
        routineTimer.reset();
        }
    
    key_formal_limited.stop();
    if (Trail_loop_limitedMaxDurationReached) {
        routineTimer.add(Trail_loop_limitedMaxDuration);
    } else {
        routineTimer.add(-1.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var worn_pageMaxDurationReached;
var worn_pageMaxDuration;
var worn_pageComponents;
function worn_pageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'worn_page' ---
    t = 0;
    worn_pageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    worn_pageMaxDurationReached = false;
    // update component parameters for each repeat
    worn.setFillColor(new util.Color('red'));
    worn.setOpacity(None);
    worn.setContrast(1.0);
    worn.setPos([0, (- 0.5)]);
    worn.setSize([0.5, 0.5]);
    worn.setLineColor(new util.Color('white'));
    worn.setLineWidth(1.0);
    // Run 'Begin Routine' code from code
    if (key_formal_limited.keys) {
        continueRoutine = false;
    } else {
        continueRoutine = true;
        psychoJS.experiment.addData("timed_out", 1);
    }
    
    psychoJS.experiment.addData('worn_page.started', globalClock.getTime());
    worn_pageMaxDuration = null
    // keep track of which components have finished
    worn_pageComponents = [];
    worn_pageComponents.push(worn);
    
    worn_pageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function worn_pageRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'worn_page' ---
    // get current time
    t = worn_pageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *worn* updates
    if (t >= 0.0 && worn.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      worn.tStart = t;  // (not accounting for frame time here)
      worn.frameNStart = frameN;  // exact frame index
      
      worn.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (worn.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      worn.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    worn_pageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function worn_pageRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'worn_page' ---
    worn_pageComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('worn_page.stopped', globalClock.getTime());
    if (worn_pageMaxDurationReached) {
        routineTimer.add(worn_pageMaxDuration);
    } else {
        routineTimer.add(-1.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var 间歇休息MaxDurationReached;
var _pj;
var 间歇休息MaxDuration;
var 间歇休息Components;
function 间歇休息RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine '间歇休息' ---
    t = 0;
    间歇休息Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(30.000000);
    间歇休息MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if ((! _pj.in_es6((trials.thisN + 1), [56, 112]))) {
        continueRoutine = false;
    }
    
    psychoJS.experiment.addData('间歇休息.started', globalClock.getTime());
    间歇休息MaxDuration = null
    // keep track of which components have finished
    间歇休息Components = [];
    间歇休息Components.push(text_6);
    
    间歇休息Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function 间歇休息RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine '间歇休息' ---
    // get current time
    t = 间歇休息Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_6.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    间歇休息Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function 间歇休息RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine '间歇休息' ---
    间歇休息Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('间歇休息.stopped', globalClock.getTime());
    if (间歇休息MaxDurationReached) {
        routineTimer.add(间歇休息MaxDuration);
    } else {
        routineTimer.add(-30.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var 实验_非时间限制指导语MaxDurationReached;
var _key_resp_5_allKeys;
var 实验_非时间限制指导语MaxDuration;
var 实验_非时间限制指导语Components;
function 实验_非时间限制指导语RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine '实验_非时间限制指导语' ---
    t = 0;
    实验_非时间限制指导语Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    实验_非时间限制指导语MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    psychoJS.experiment.addData('实验_非时间限制指导语.started', globalClock.getTime());
    实验_非时间限制指导语MaxDuration = null
    // keep track of which components have finished
    实验_非时间限制指导语Components = [];
    实验_非时间限制指导语Components.push(text_8);
    实验_非时间限制指导语Components.push(key_resp_5);
    
    实验_非时间限制指导语Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function 实验_非时间限制指导语RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine '实验_非时间限制指导语' ---
    // get current time
    t = 实验_非时间限制指导语Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }
    
    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }
    
    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        key_resp_5.duration = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    实验_非时间限制指导语Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function 实验_非时间限制指导语RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine '实验_非时间限制指导语' ---
    实验_非时间限制指导语Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('实验_非时间限制指导语.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        psychoJS.experiment.addData('key_resp_5.duration', key_resp_5.duration);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "实验_非时间限制指导语" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Trail_loop_no_limitedMaxDurationReached;
var _key_formal_no_limited_allKeys;
var Trail_loop_no_limitedMaxDuration;
var Trail_loop_no_limitedComponents;
function Trail_loop_no_limitedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Trail_loop_no_limited' ---
    t = 0;
    Trail_loop_no_limitedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    Trail_loop_no_limitedMaxDurationReached = false;
    // update component parameters for each repeat
    T_L_N.setColor(new util.Color('white'));
    T_L_N.setOpacity(None);
    T_L_N.setContrast(1.0);
    T_L_N.setPos([(- 0.4), 0.2]);
    T_L_N.setOri(0.0);
    T_L_N.setText(Title_Left);
    T_L_N.setFont('Arial');
    T_L_N.setHeight(0.05);
    T_L_N.setFlip('None');
    S_L_N.setPos([(- 0.4), 0]);
    S_L_N.setOri(0.0);
    S_L_N.setText('自己:$Self_A');
    S_L_N.setFlip('None');
    O_L_N.setPos([(- 0.4), (- 0.2)]);
    O_L_N.setOri(0.0);
    O_L_N.setText('他人:$Others_A');
    O_L_N.setHeight(0.04);
    O_L_N.setFlip('None');
    T_R_N.setColor(new util.Color('white'));
    T_R_N.setOpacity(None);
    T_R_N.setContrast(1.0);
    T_R_N.setPos([0.4, 0.2]);
    T_R_N.setOri(0.0);
    T_R_N.setText(Title_Right);
    T_R_N.setFont('Arial');
    T_R_N.setHeight(0.05);
    T_R_N.setFlip('None');
    S_R_L.setColor(new util.Color('white'));
    S_R_L.setOpacity(None);
    S_R_L.setContrast(1.0);
    S_R_L.setPos([0.4, 0]);
    S_R_L.setOri(0.0);
    S_R_L.setText('自己:$Self_B');
    S_R_L.setFont('Arial');
    S_R_L.setHeight(0.04);
    S_R_L.setFlip('None');
    O_R_N.setColor(new util.Color('white'));
    O_R_N.setOpacity(None);
    O_R_N.setContrast(1.0);
    O_R_N.setPos([0.4, (- 0.2)]);
    O_R_N.setOri(0.0);
    O_R_N.setText('他人:$Others_B');
    O_R_N.setFont('Arial');
    O_R_N.setHeight(0.04);
    O_R_N.setFlip('None');
    key_formal_no_limited.keys = undefined;
    key_formal_no_limited.rt = undefined;
    _key_formal_no_limited_allKeys = [];
    worn_Nl.setFillColor(new util.Color('green'));
    worn_Nl.setOpacity(None);
    worn_Nl.setContrast(1.0);
    worn_Nl.setPos([0, (- 0.5)]);
    worn_Nl.setSize([0.5, 0.5]);
    worn_Nl.setLineColor(new util.Color('white'));
    worn_Nl.setLineWidth(1.0);
    psychoJS.experiment.addData('Trail_loop_no_limited.started', globalClock.getTime());
    Trail_loop_no_limitedMaxDuration = null
    // keep track of which components have finished
    Trail_loop_no_limitedComponents = [];
    Trail_loop_no_limitedComponents.push(T_L_N);
    Trail_loop_no_limitedComponents.push(S_L_N);
    Trail_loop_no_limitedComponents.push(O_L_N);
    Trail_loop_no_limitedComponents.push(T_R_N);
    Trail_loop_no_limitedComponents.push(S_R_L);
    Trail_loop_no_limitedComponents.push(O_R_N);
    Trail_loop_no_limitedComponents.push(key_formal_no_limited);
    Trail_loop_no_limitedComponents.push(worn_Nl);
    
    Trail_loop_no_limitedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Trail_loop_no_limitedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Trail_loop_no_limited' ---
    // get current time
    t = Trail_loop_no_limitedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *T_L_N* updates
    if (t >= 0.0 && T_L_N.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      T_L_N.tStart = t;  // (not accounting for frame time here)
      T_L_N.frameNStart = frameN;  // exact frame index
      
      T_L_N.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (T_L_N.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      T_L_N.setAutoDraw(false);
    }
    
    
    // *S_L_N* updates
    if (t >= 0.0 && S_L_N.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      S_L_N.tStart = t;  // (not accounting for frame time here)
      S_L_N.frameNStart = frameN;  // exact frame index
      
      S_L_N.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (S_L_N.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      S_L_N.setAutoDraw(false);
    }
    
    
    // *O_L_N* updates
    if (t >= 0.0 && O_L_N.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      O_L_N.tStart = t;  // (not accounting for frame time here)
      O_L_N.frameNStart = frameN;  // exact frame index
      
      O_L_N.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (O_L_N.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      O_L_N.setAutoDraw(false);
    }
    
    
    // *T_R_N* updates
    if (t >= 0.0 && T_R_N.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      T_R_N.tStart = t;  // (not accounting for frame time here)
      T_R_N.frameNStart = frameN;  // exact frame index
      
      T_R_N.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (T_R_N.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      T_R_N.setAutoDraw(false);
    }
    
    
    // *S_R_L* updates
    if (t >= 0.0 && S_R_L.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      S_R_L.tStart = t;  // (not accounting for frame time here)
      S_R_L.frameNStart = frameN;  // exact frame index
      
      S_R_L.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (S_R_L.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      S_R_L.setAutoDraw(false);
    }
    
    
    // *O_R_N* updates
    if (t >= 0.0 && O_R_N.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      O_R_N.tStart = t;  // (not accounting for frame time here)
      O_R_N.frameNStart = frameN;  // exact frame index
      
      O_R_N.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (O_R_N.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      O_R_N.setAutoDraw(false);
    }
    
    
    // *key_formal_no_limited* updates
    if (t >= 0.0 && key_formal_no_limited.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_formal_no_limited.tStart = t;  // (not accounting for frame time here)
      key_formal_no_limited.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_formal_no_limited.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_formal_no_limited.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_formal_no_limited.clearEvents(); });
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_formal_no_limited.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_formal_no_limited.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_formal_no_limited.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_formal_no_limited.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_formal_no_limited_allKeys = _key_formal_no_limited_allKeys.concat(theseKeys);
      if (_key_formal_no_limited_allKeys.length > 0) {
        key_formal_no_limited.keys = _key_formal_no_limited_allKeys[_key_formal_no_limited_allKeys.length - 1].name;  // just the last key pressed
        key_formal_no_limited.rt = _key_formal_no_limited_allKeys[_key_formal_no_limited_allKeys.length - 1].rt;
        key_formal_no_limited.duration = _key_formal_no_limited_allKeys[_key_formal_no_limited_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *worn_Nl* updates
    if (t >= 0.0 && worn_Nl.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      worn_Nl.tStart = t;  // (not accounting for frame time here)
      worn_Nl.frameNStart = frameN;  // exact frame index
      
      worn_Nl.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (worn_Nl.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      worn_Nl.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Trail_loop_no_limitedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Trail_loop_no_limitedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Trail_loop_no_limited' ---
    Trail_loop_no_limitedComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Trail_loop_no_limited.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_formal_no_limited.corr, level);
    }
    psychoJS.experiment.addData('key_formal_no_limited.keys', key_formal_no_limited.keys);
    if (typeof key_formal_no_limited.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_formal_no_limited.rt', key_formal_no_limited.rt);
        psychoJS.experiment.addData('key_formal_no_limited.duration', key_formal_no_limited.duration);
        routineTimer.reset();
        }
    
    key_formal_no_limited.stop();
    if (Trail_loop_no_limitedMaxDurationReached) {
        routineTimer.add(Trail_loop_no_limitedMaxDuration);
    } else {
        routineTimer.add(-10.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var end_wordMaxDurationReached;
var end_wordMaxDuration;
var end_wordComponents;
function end_wordRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_word' ---
    t = 0;
    end_wordClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    end_wordMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('end_word.started', globalClock.getTime());
    end_wordMaxDuration = null
    // keep track of which components have finished
    end_wordComponents = [];
    end_wordComponents.push(text_3);
    
    end_wordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function end_wordRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_word' ---
    // get current time
    t = end_wordClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    end_wordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_wordRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_word' ---
    end_wordComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('end_word.stopped', globalClock.getTime());
    if (end_wordMaxDurationReached) {
        routineTimer.add(end_wordMaxDuration);
    } else {
        routineTimer.add(-5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  // --- DataPipe 发送配置 ---
  const experimentID = "r5PIffrX9PYteiMvsp4tgBy0dUnZq9hJ6aIFTREKywdQejVYM7wbaetEij2xDkrV0ZNxDh";  // ★★★ 替换这里！ ★★★
  const filename = `${expInfo['participant']}_${expInfo['date']}.csv`;
  
  // 定义发送数据的函数
  function saveData(name, data) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://pipe.jspsych.org/api/data'); // DataPipe API地址
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
      if (xhr.readyState == XMLHttpRequest.DONE) {
        if (xhr.status == 200) {
          console.log("Data sent to DataPipe successfully.");
        } else {
          console.log("Data sending failed.");
        }
      }
    };
    xhr.send(JSON.stringify({
      experimentID: experimentID,
      filename: name,
      data: data
    }));
  }
  
  // 获取 PsychoJS 收集的数据
  // psychoJS.experiment.save() 会触发本地下载，同时返回数据对象
  // 我们在这里直接提取 CSV 格式的数据字符串
  let dataContent = psychoJS.experiment._trialsData; // 获取原始数据对象
  // 将数据转换为 CSV 格式 (需要调用 PsychoJS 内部转换函数)
  // 注意：不同版本 PsychoJS 获取 CSV 字符串的方法可能略有不同
  // 最稳妥的方法是利用 extraInfo 和 data 拼接，或者直接上传 dataContent (JSON格式)
  // 为了兼容性，这里我们先保存为 CSV 字符串格式上传
  let csvData = psychoJS.experiment.saveAsCSV(); 
  
  // 执行发送
  saveData(filename, csvData);
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
