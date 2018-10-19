label event_lana_rebecca_sleep_start:
    $event_lana_rebecca_sleep.active = True
    return

label event_lana_rebecca_sleep_advance_to_second_dream:
    $event_lana_rebecca_sleep.reset()
    $event_lana_rebecca_sleep.advance_phase()
    $event_lana_rebecca_sleep.req_day = day + 2
    $event_lana_rebecca_sleep.day_mode = "at_least"
    return
    
label event_lana_rebecca_sleep_finish:
    $event_lana_rebecca_sleep.reset()
    $event_lana_rebecca_sleep.advance_phase()
    return

label lana_rebecca_sleep_start:
    scene blank
    $renpy.pause()
    scene shared_beds_rebecca_sis_13
    sis flirting "Ohhh..."
    sis flirting "That's so good..."
    scene shared_beds_rebecca_sis_14
    rebecca "What the..."
    rebecca flirting "Oh, my girl is enjoying her present!"
    sis flirting "Oh yes!"
    sis flirting "Right there!"
    scene shared_beds_rebecca_sis_15
    rebecca flirting "This gets me horny too!"
    rebecca flirting "Oh yeah!"
    sis flirting "Yes! That's it!"
    sis flirting "I'm so close!"
    rebecca flirting "Oh yeah!"
    sis flirting "I'm cumming!"
    rebecca flirting "Yes! Yes!"
    scene blank
    $renpy.pause()
    call event_lana_rebecca_sleep_advance_to_second_dream from _call_event_lana_rebecca_sleep_advance_to_second_dream
    jump morning
    
label lana_rebecca_sleep_dream_1:
    scene blank
    $renpy.pause()
    scene shared_beds_rebecca_sis_16
    sis flirting "Ohhh..."
    sis flirting "Oh yes!"
    rebecca happy "Again?"
    scene shared_beds_rebecca_sis_17
    sis flirting "I want the vibrator!"
    sis "Where is it?"
    scene shared_beds_rebecca_sis_18
    rebecca happy "Looking for this?"
    sis "Mom!"
    sis "Give it back!"
    scene shared_beds_rebecca_sis_20
    rebecca flirting "I will, but first I need to make sure that you are wet!"
    sis flirting "Mom, this is wrong!"
    rebecca flirting "Is it? Does it feel wrong?"
    sis flirting "... It feels good!"
    rebecca happy "And it will only get better!"
    scene shared_beds_rebecca_sis_19
    sis flirting "Oh, mom!"
    rebecca flirting "So you don't think we should stop?"
    sis flirting "No! Please don't stop!"
    rebecca flirting "What if Greg was watching you right now? Would you like it?"
    sis flirting "Oh yes!"
    player "{i}I wish I could be there to get a close-up on what Rebecca is doing with Lana!{/i}"
    player "{i}... Wait! What if I could? Those cameras are surely equipped with zooming lens!{/i}"
    player "{i}...{/i}"
    scene shared_beds_rebecca_sis_21
    player "{i}Yes!{/i}"
    rebecca flirting "Do you imagine Greg stroking his big cock while watching you?"
    sis flirting "Oh yes!"
    rebecca flirting "Cumming all over your ass..."
    sis flirting "Oh yes! Yes!"
    rebecca flirting "And then pulling your hair and sticking his dick in your mouth!"
    sis flirting "Yes! I'm cumming!"
    scene blank
    player "{i}Rebecca is such a slut... Talking dirty to her own daughter... Making her cum...{/i}"
    call event_lana_rebecca_sleep_finish from _call_event_lana_rebecca_sleep_finish
    jump morning
    