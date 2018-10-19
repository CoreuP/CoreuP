label add_event_mom_strip_beach:
    $event_mom_strip_beach.active = True
    $event_mom_strip_beach.req_day = day + 1
    $event_mom_strip_beach.day_mode = "at_least"
    $event_mom_strip_beach.location = "vr_room"
    $event_mom_strip_beach.mom_location = "vr_room"
    $talk_with_mom.add_topic("Ask to put on sunblock", "mom_strip_beach", event_mom_strip_beach, 0)
    return
    
label mom_strip_beach:
    hide screen station_rooms
    player "Hi mom!"
    mom "Oh, hi Greg!"
    mom "Can you put some sunblock on me?"
    player "I was just going to ask you this!"
    player "Turn around."
    scene beach_mom_5
    mom "Can you help me with the straps?"
    player "Sure!"
    scene beach_mom_6
    player "Hold still!"
    player "All done!"
    mom "Thank you!"
    scene beach_mom_7
    mom "The sun feels so good on my skin!"
    call add_event_mom_strip_beach from _call_add_event_mom_strip_beach_1
    jump wait_action