label event_outpost_start:
    $event_outpost.active = True
    $event_outpost.req_day = day + 1
    $event_outpost.day_mode = "exactly"
    return
    
label event_outpost_conversation:
    hide screen station_rooms
    scene blank
    $renpy.pause()
    scene outpost_susan_1
    female "Finally Megan is back! I was starting to worry about her."
    male "I've told you she'd be OK. She is more than capable of handling herself."
    scene outpost_susan_2
    megan "I've forgotten how good it felt to take a bath!"
    megan "They kept me locked in a medical room for days."
    female "Couldn't you just escape?"
    scene outpost_susan_3
    megan "But then how would have I gotten access to the boy?"
    male "Have you managed to complete your task?"
    scene outpost_susan_4
    female "You know she did! You checked the recordings."
    male "So what's the plan now?"
    megan "We should wait for the interface to become fully operational."
    female "I still don't get why we don't just kill them."
    megan happy "I think Susan is jealous..."
    male "Enough! He is smart, we can use him."
    scene blank
    $renpy.pause()
    call event_mom_bedroom_start from _call_event_mom_bedroom_start
    $global_events.outpost_conversation = day
    jump morning