label event_sis_shower_five_days:
    $event_sis_shower.active = True
    $event_sis_shower.req_day = day + 5
    $event_sis_shower.day_mode = "at_least"
    $event_sis_shower.angry = True
    $event_sis_shower.location = "bedroom"
    $event_sis_shower.sis_location = "bedroom"
    $event_sis_shower.req_clock = 8;
    $event_sis_shower.clock_mode = "exactly"
    return
    
label event_sis_shower_two_days:
    $event_sis_shower.active = True
    $event_sis_shower.req_day = day + 2
    $event_sis_shower.day_mode = "at_least"
    $event_sis_shower.angry = False
    $event_sis_shower.location = "bedroom"
    $event_sis_shower.sis_location = "bedroom"
    $event_sis_shower.req_clock = 8;
    $event_sis_shower.clock_mode = "exactly"
    return
    
label event_sis_shower_talk:
    player "Lana..."
    if (quest_lanas_vibrations.meets_requirements(13)):
        jump quest_lanas_vibrations_shower
    elif (event_sis_shower.meets_requirements(0)):
        jump event_sis_shower_masturbate
    elif (event_sis_shower.angry):
        jump event_sis_shower_angry
    else:
        jump event_sis_shower_not_angry
    
label event_sis_shower_angry:
    sis angry "What the hell, Greg!"
    sis angry "How long have you been standing there?"
    player "I was wondering if you want us to have some fun..."
    sis angry "After what you did last time? Hell, no!"
    player "OK, maybe tomorrow then?"
    if (event_sis_shower.req_day == day + 1):
        sis "Maybe."
        sis "Would you get out now?"
    else:
        sis angry "Don't bother!"
        sis angry "Get out now!"
    scene door_1
    player "{i}I shouldn't have cum on her. She is still angry at me.{/i}"
    jump advance_time
    
label event_sis_shower_not_angry:
    sis "Greg? What are you doing here?"
    player "Well, I was wondering..."
    sis "Not now Greg."
    player "Tomorrow then?"
    sis "Whatever. Please leave."
    scene door_1
    player "{i}Hmmm... she is not angry at me but still she didn't want us to have some fun together...{/i}"
    jump advance_time
    
label event_sis_shower_masturbate:
    sis flirting "I knew you would come!"
    sis flirting "Let me get a towel and make myself comfortable."
    scene shower_sis_6
    sis "So what do you want to talk about?"
    player "I didn't actually come here to talk."
    sis happy "I know silly! I'm just pulling your leg!"
    scene shower_sis_7
    sis flirting "You came here for this, right?"
    sis flirting "You came to look at my ass!"
    player "Who wouldn't? You have a great ass!"
    scene shower_sis_9
    sis happy "Oh, you are so sweet!"
    sis flirting "You know what to say to make me wet."
    scene shower_sis_10
    player "And you know what to do to make me hard."
    sis flirting "Keep talking."
    sis flirting "Tell me how hard I make you!"
    player "Why don't you see for yourself?"
    scene shower_sis_11
    sis flirting "Oh, just thinking about that cock of yours will make me cum!"
    player "Do you want me to cum too?"
    sis flirting "Right now?"
    sis "...No."
    player "I don't know if I can hold it off much longer..."
    sis flirting "Do I turn you on that much?"
    player "Oh yes!"
    sis flirting "Then cum for me!"
    jump shower_sis_cum
    