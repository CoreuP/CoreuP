label add_event_sis_strip_beach:
    $event_sis_strip_beach.active = True
    $event_sis_strip_beach.req_day = day + 1
    $event_sis_strip_beach.day_mode = "at_least"
    $event_sis_strip_beach.location = "vr_room"
    $event_sis_strip_beach.sis_location = "vr_room"
    $talk_with_sis.add_topic("Ask if she wants some sun screen", "sis_strip_beach", event_sis_strip_beach, 0)
    return
    
label sis_strip_beach:
    hide screen station_rooms
    player "Hi Lana!"
    scene beach_sis_4
    player "Do you want some sun screen?"
    sis "Sure!"
    scene beach_sis_6
    sis "Let me take off my bra."
    scene beach_sis_7
    $renpy.pause()
    scene beach_sis_8
    sis "And my panties."
    scene beach_sis_10
    sis "OK, I'm ready. Do my back first."
    scene beach_sis_11
    sis "Do you like the view?"
    player "Very much!"
    sis happy "The ocean is so beautiful..."
    player "Yes, sure... the ocean..."
    scene beach_sis_12
    sis "Now do the front!"
    player "Really?"
    sis happy "No dummy, I'm just teasing you!"
    sis happy "I need to get dressed before mom arrives."
    scene beach_sis_4
    sis happy "Thanks for the help!"
    player "Thank you for the show!"
    sis happy "Anytime!"
    call add_event_sis_strip_beach from _call_add_event_sis_strip_beach_1
    jump wait_action