#vvvvvv PUT ALL CHARACTER TIME SCHEDULES HERE vvvvvv

label position_characters:
    call reset_all_rooms from _call_reset_all_rooms
    $rebecca_location = "void"
    $mom_location = "void"
    $sis_location = "void"
    if global_events.rebecca_bedroom:
        call position_mom_rebecca_after from _call_position_mom_rebecca_after
    elif not global_events.sis:
        call position_mom_rebecca from _call_position_mom_rebecca
    elif not global_events.rebecca:
        call position_mom_sis from _call_position_mom_sis
    else:
        call position_mom_sis_rebecca from _call_position_mom_sis_rebecca
    return

label position_mom_sis:
    python:
        if (clock == 7):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
        elif (clock == 8):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            sis_location = "bedroom"
            station.get_room("bedroom").sis = True
        elif (clock == 9):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            sis_location = "mess_hall"
            station.get_room("mess_hall").sis = True
        elif (clock == 10):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            sis_location = "vr_room"
            station.get_room("vr_room").sis = True
        elif (clock == 11):
            mom_location = "comm"
            station.get_room("comm").mom = True
            sis_location = "life_support"
            station.get_room("life_support").sis = True
        elif (clock == 12):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            if (global_events.megan):
                sis_location = "vr_room"
                station.get_room("vr_room").sis = True
            else:
                sis_location = "med_bay"
                station.get_room("med_bay").sis = True
        elif (clock == 13):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "vr_room"
            station.get_room("vr_room").sis = True
        elif (clock == 14):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "comm"
            station.get_room("comm").sis = True
        elif (clock == 15):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            sis_location = "comm"
            station.get_room("comm").sis = True
        elif (clock == 16):
            if (global_events.megan):
                mom_location = "vr_room"
                station.get_room("vr_room").mom = True
            else:
                mom_location = "med_bay"
                station.get_room("med_bay").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
        elif (clock == 17):
            if (global_events.megan):
                mom_location = "vr_room"
                station.get_room("vr_room").mom = True
            else:
                mom_location = "med_bay"
                station.get_room("med_bay").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
        elif (clock == 18):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            sis_location = "comm"
            station.get_room("comm").sis = True
        elif (clock == 19):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            sis_location = "mess_hall"
            station.get_room("mess_hall").sis = True
        elif (clock == 20):
            mom_location = "vr_room"
            station.get_room("vr_room").mom = True
            sis_location = "bedroom"
            station.get_room("bedroom").sis = True
        elif (clock == 21):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
        elif (clock == 22):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
        elif (clock == 23):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
        elif (clock == 0):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
        elif (clock == 1):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
        elif (clock == 2):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
    return

label position_mom_sis_rebecca:
    python:
        if (clock == 7):
            if (global_events.mom):
                mom_location = "bedroom"
                station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
            rebecca_location = "shared_beds"
            station.get_room("shared_beds").rebecca = True
        elif (clock == 8):
            if (global_events.mom):
                mom_location = "mess_hall"
                station.get_room("mess_hall").mom = True
            sis_location = "bedroom"
            station.get_room("bedroom").sis = True
            rebecca_location = "vr_room"
            station.get_room("vr_room").rebecca = True
        elif (clock == 9):
            if (global_events.mom):
                mom_location = "mess_hall"
                station.get_room("mess_hall").mom = True
            sis_location = "mess_hall"
            station.get_room("mess_hall").sis = True
            rebecca_location = "mess_hall"
            station.get_room("mess_hall").rebecca = True
        elif (clock == 10):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            sis_location = "vr_room"
            station.get_room("vr_room").sis = True
            rebecca_location = "med_bay"
            station.get_room("med_bay").rebecca = True
        elif (clock == 11):
            mom_location = "comm"
            station.get_room("comm").mom = True
            sis_location = "life_support"
            station.get_room("life_support").sis = True
            rebecca_location = "med_bay"
            station.get_room("med_bay").rebecca = True
        elif (clock == 12):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            sis_location = "med_bay"
            station.get_room("med_bay").sis = True
            rebecca_location = "bedroom"
            station.get_room("bedroom").rebecca = True
        elif (clock == 13):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "vr_room"
            station.get_room("vr_room").sis = True
            rebecca_location = "shared_beds"
            station.get_room("shared_beds").rebecca = True
        elif (clock == 14):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "comm"
            station.get_room("comm").sis = True
            rebecca_location = "vr_room"
            station.get_room("vr_room").rebecca = True
        elif (clock == 15):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            sis_location = "comm"
            station.get_room("comm").sis = True
            rebecca_location = "med_bay"
            station.get_room("med_bay").rebecca = True
        elif (clock == 16):
            mom_location = "med_bay"
            station.get_room("med_bay").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
            rebecca_location = "comm"
            station.get_room("comm").rebecca = True
        elif (clock == 17):
            mom_location = "med_bay"
            station.get_room("med_bay").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
            rebecca_location = "vr_room"
            station.get_room("vr_room").rebecca = True
        elif (clock == 18):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            sis_location = "comm"
            station.get_room("comm").sis = True
            rebecca_location = "med_bay"
            station.get_room("med_bay").rebecca = True
        elif (clock == 19):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            sis_location = "mess_hall"
            station.get_room("mess_hall").sis = True
            rebecca_location = "mess_hall"
            station.get_room("mess_hall").rebecca = True
        elif (clock == 20):
            mom_location = "vr_room"
            station.get_room("vr_room").mom = True
            sis_location = "bedroom"
            station.get_room("bedroom").sis = True
            rebecca_location = "life_support"
            station.get_room("life_support").rebecca = True
        elif (clock == 21):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
            rebecca_location = "life_support"
            station.get_room("life_support").rebecca = True
        elif (clock == 22):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
            rebecca_location = "comm"
            station.get_room("comm").rebecca = True
        elif (clock == 23):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
            rebecca_location = "shared_beds"
            station.get_room("shared_beds").rebecca = True
        elif (clock == 0):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
            if (quest_meet_rebecca.phase == 8 or event_rebecca_dice_game.phase == 1):
                rebecca_location = "life_support"
                station.get_room("life_support").rebecca = True
            else:
                rebecca_location = "shared_beds"
                station.get_room("shared_beds").rebecca = True
        elif (clock == 1):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
            rebecca_location = "shared_beds"
            station.get_room("shared_beds").rebecca = True
        elif (clock == 2):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            sis_location = "shared_beds"
            station.get_room("shared_beds").sis = True
            rebecca_location = "shared_beds"
            station.get_room("shared_beds").rebecca = True
    return

label position_mom_rebecca:
    python:
        if (clock == 7):
            if (global_events.mom):
                mom_location = "bedroom"
                station.get_room("bedroom").mom = True
            rebecca_location = "shared_beds"
            station.get_room("shared_beds").rebecca = True
        elif (clock == 8):
            if (global_events.mom):
                mom_location = "mess_hall"
                station.get_room("mess_hall").mom = True
            rebecca_location = "comm"
            station.get_room("comm").rebecca = True
        elif (clock == 9):
            if (global_events.mom):
                mom_location = "mess_hall"
                station.get_room("mess_hall").mom = True
            rebecca_location = "mess_hall"
            station.get_room("mess_hall").rebecca = True
        elif (clock == 10):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            rebecca_location = "med_bay"
            station.get_room("med_bay").rebecca = True
        elif (clock == 11):
            mom_location = "comm"
            station.get_room("comm").mom = True
            rebecca_location = "med_bay"
            station.get_room("med_bay").rebecca = True
        elif (clock == 12):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            rebecca_location = "bedroom"
            station.get_room("bedroom").rebecca = True
        elif (clock == 13):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            rebecca_location = "shared_beds"
            station.get_room("shared_beds").rebecca = True
        elif (clock == 14):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            rebecca_location = "vr_room"
            station.get_room("vr_room").rebecca = True
        elif (clock == 15):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            rebecca_location = "med_bay"
            station.get_room("med_bay").rebecca = True
        elif (clock == 16):
            mom_location = "med_bay"
            station.get_room("med_bay").mom = True
            rebecca_location = "comm"
            station.get_room("comm").rebecca = True
        elif (clock == 17):
            mom_location = "med_bay"
            station.get_room("med_bay").mom = True
            rebecca_location = "vr_room"
            station.get_room("vr_room").rebecca = True
        elif (clock == 18):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            rebecca_location = "med_bay"
            station.get_room("med_bay").rebecca = True
        elif (clock == 19):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            rebecca_location = "mess_hall"
            station.get_room("mess_hall").rebecca = True
        elif (clock == 20):
            mom_location = "vr_room"
            station.get_room("vr_room").mom = True
            rebecca_location = "life_support"
            station.get_room("life_support").rebecca = True
        elif (clock == 21):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            rebecca_location = "life_support"
            station.get_room("life_support").rebecca = True
        elif (clock == 22):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            rebecca_location = "comm"
            station.get_room("comm").rebecca = True
        elif (clock == 23):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            rebecca_location = "shared_beds"
            station.get_room("shared_beds").rebecca = True
        elif (clock == 0):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            if (quest_meet_rebecca.phase == 8 or event_rebecca_dice_game.phase == 1):
                rebecca_location = "life_support"
                station.get_room("life_support").rebecca = True
            else:
                rebecca_location = "shared_beds"
                station.get_room("shared_beds").rebecca = True
        elif (clock == 1):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            rebecca_location = "shared_beds"
            station.get_room("shared_beds").rebecca = True
        elif (clock == 2):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            rebecca_location = "shared_beds"
            station.get_room("shared_beds").rebecca = True
    return

label position_mom_rebecca_after:
    python:
        if (clock == 7):
            rebecca_location = "bedroom"
            station.get_room("bedroom").rebecca = True
            mom_location = "shared_beds"
            station.get_room("shared_beds").mom = True
        elif (clock == 8):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            rebecca_location = "comm"
            station.get_room("comm").rebecca = True
        elif (clock == 9):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            rebecca_location = "mess_hall"
            station.get_room("mess_hall").rebecca = True
        elif (clock == 10):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            rebecca_location = "med_bay"
            station.get_room("med_bay").rebecca = True
        elif (clock == 11):
            mom_location = "comm"
            station.get_room("comm").mom = True
            rebecca_location = "med_bay"
            station.get_room("med_bay").rebecca = True
        elif (clock == 12):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            rebecca_location = "mess_hall"
            station.get_room("mess_hall").rebecca = True
        elif (clock == 13):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            rebecca_location = "shared_beds"
            station.get_room("shared_beds").rebecca = True
        elif (clock == 14):
            mom_location = "bedroom"
            station.get_room("bedroom").mom = True
            rebecca_location = "vr_room"
            station.get_room("vr_room").rebecca = True
        elif (clock == 15):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            rebecca_location = "med_bay"
            station.get_room("med_bay").rebecca = True
        elif (clock == 16):
            mom_location = "med_bay"
            station.get_room("med_bay").mom = True
            rebecca_location = "comm"
            station.get_room("comm").rebecca = True
        elif (clock == 17):
            mom_location = "med_bay"
            station.get_room("med_bay").mom = True
            rebecca_location = "vr_room"
            station.get_room("vr_room").rebecca = True
        elif (clock == 18):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            rebecca_location = "med_bay"
            station.get_room("med_bay").rebecca = True
        elif (clock == 19):
            mom_location = "mess_hall"
            station.get_room("mess_hall").mom = True
            rebecca_location = "mess_hall"
            station.get_room("mess_hall").rebecca = True
        elif (clock == 20):
            mom_location = "vr_room"
            station.get_room("vr_room").mom = True
            rebecca_location = "life_support"
            station.get_room("life_support").rebecca = True
        elif (clock == 21):
            mom_location = "comm"
            station.get_room("comm").mom = True
            rebecca_location = "life_support"
            station.get_room("life_support").rebecca = True
        elif (clock == 22):
            mom_location = "shared_beds"
            station.get_room("shared_beds").mom = True
            rebecca_location = "bedroom"
            station.get_room("bedroom").rebecca = True
        elif (clock == 23):
            mom_location = "shared_beds"
            station.get_room("shared_beds").mom = True
            rebecca_location = "bedroom"
            station.get_room("bedroom").rebecca = True
        elif (clock == 0):
            mom_location = "shared_beds"
            station.get_room("shared_beds").mom = True
            if (event_rebecca_dice_game.phase == 1):
                rebecca_location = "life_support"
                station.get_room("life_support").rebecca = True
            else:
                rebecca_location = "bedroom"
                station.get_room("bedroom").rebecca = True
        elif (clock == 1):
            mom_location = "shared_beds"
            station.get_room("shared_beds").mom = True
            rebecca_location = "bedroom"
            station.get_room("bedroom").rebecca = True
        elif (clock == 2):
            mom_location = "shared_beds"
            station.get_room("shared_beds").mom = True
            rebecca_location = "bedroom"
            station.get_room("bedroom").rebecca = True
    return


#^^^^^^ PUT ALL CHARACTER TIME SCHEDULES HERE ^^^^^^
#---------------------------------------------------

#vvvvvv PUT ALL HARD-CODED TIME EVENTS HERE (SLEEP, EAT, ETC.) vvvvvv
label advance_time:
    $clock = clock + 1;
    call generate_power from _call_generate_power
    if (quest_meet_megan.meets_requirements(0)):
        jump quest_meet_megan_open_door
    if (quest_meet_rebecca.meets_requirements(1)):
        jump quest_meet_rebecca_sleep_talk
    if (quest_lanas_vibrations.meets_requirements(10)):
        jump quest_lanas_vibrations_breakfast_no_mom
    if (quest_sis_missing.meets_requirements(8)):
        jump quest_sis_missing_med_bay
    if (quest_sis_missing.meets_requirements(9)):
        jump quest_sis_missing_lesb_show
    if (quest_make_a_plan.meets_requirements(4)):
        jump quest_make_a_plan_start_training
    if (quest_make_a_plan.meets_requirements(6)):
        jump quest_make_a_plan_next_training
    if clock == 2:
        call position_characters from _call_position_characters_1
        jump sleep
    if (clock == 8 and quest_black_market.meets_requirements(1)):
        jump black_market_spy_sis_shower
    if (clock == 9 or clock == 19):
        call position_characters from _call_position_characters_2
        jump room_mess_hall
    if clock == 24:
        $day = day + 1;
        $clock = 0;
    call position_characters from _call_position_characters_3
    if (quest_meet_rebecca.meets_requirements(8)):
        jump room_life_support
    if (quest_lanas_vibrations.meets_requirements(6)):
        jump quest_lanas_vibrations_meet_midnight
    show screen day_time
    show screen energy
    jump jump_to_location

label generate_power:
    $energy = energy + generator * efficiency / 200.0;
    if (energy > capacity):
        $energy = capacity
    return

#^^^^^^ PUT ALL HARD-CODED TIME EVENTS HERE (SLEEP, EAT, ETC.) ^^^^^^

#---------------------------------------------------------------------

label show_sis_sleep:
    if global_events.simple_clothes:
        scene shared_beds_sis_sleep_2
    else:
        scene shared_beds_sis_sleep_1
    return

label show_mom_sleep:
    scene bedroom_mom_sleep_1
    return

label show_rebecca_sleep:
    scene bedroom_rebecca_sleep_1
    return

label sleep:
    if (global_events.sleep_bedroom):
        jump sleep_bedroom
    else:
        jump sleep_shared_beds

label sleep_shared_beds:
    show screen day_time
    hide screen station_rooms
    $location = "shared_beds"
    $station.move_to(location)
    call show_sis_sleep from _call_show_sis_sleep
    player "It's getting late, I should go to sleep"
    if (event_outpost.meets_requirements(0)):
        jump event_outpost_conversation
    if (event_mom_bedroom.meets_requirements(0)):
        jump event_mom_bedroom_dream
    else:
        jump morning

label sleep_bedroom:
    show screen day_time
    hide screen station_rooms
    $location = "bedroom"
    $station.move_to(location)
    if (global_events.rebecca_bedroom):
        call show_rebecca_sleep from _call_show_rebecca_sleep
    else:
        call show_mom_sleep from _call_show_mom_sleep
    player "It's getting late, I should go to sleep"
    if (event_outpost_sex.meets_requirements(0)):
        jump event_outpost_sex_shared_beds_dream
    elif (event_outpost_sex.meets_requirements(1)):
        jump event_outpost_sex_first_dream
    elif (event_outpost_sex.meets_requirements(2)):
        jump event_outpost_sex_second_dream
    elif (event_lana_rebecca_sleep.meets_requirements(0)):
        jump lana_rebecca_sleep_start
    elif (event_lana_rebecca_sleep.meets_requirements(1)):
        jump lana_rebecca_sleep_dream_1
    elif (quest_make_a_plan.meets_requirements(2)):
        jump quest_make_a_plan_sleep
    else:
        jump morning

label room_shared_beds_sleep:
    call show_sis_sleep from _call_show_sis_sleep_1
    jump map

label morning:
    if (global_events.sleep_bedroom):
        jump morning_bedroom
    else:
        jump morning_shared_beds

label morning_shared_beds:
    $clock = 7
    $efficiency -= 1
    $event_mom_bedroom.visited_midnight = False
    call position_characters from _call_position_characters
    show screen day_time
    show screen energy
    if (event_outpost.req_day == day + 1):
        call morning_after_megan from _call_morning_after_megan
    if (global_events.had_dream):
        scene blank
        player "{i}I had this weird dream again... what's wrong with me?{/i}"
        $global_events.had_dream = False
    jump room_shared_beds

label morning_bedroom:
    $clock = 7
    $efficiency -= 1
    call position_characters from _call_position_characters_4
    show screen day_time
    show screen energy
    if (quest_lanas_vibrations.meets_requirements(9)):
        jump quest_lanas_vibrations_mom_disappear
    if (global_events.had_dream):
        scene blank
        player "{i}I had this weird dream again... what's wrong with me?{/i}"
        $global_events.had_dream = False
    if global_events.rebecca_bedroom:
        jump rebecca_shower
    else:
        jump mom_shower_scene

label mom_shower:
    hide screen station_rooms
    scene door_1
    player "Sound like mom is taking a shower. Should I leave?"
    menu:
        "Open the door slightly":
            jump mom_shower_scene
        "Leave her alone":
            jump map

label mom_shower_scene:
    hide screen station_rooms
    if (global_events.sleep_bedroom):
        scene shower_mom_bed_3
        player "Mom is taking a shower."
        player "Should I let her know I'm awake?"
        menu:
            "Pretend to be asleep":
                scene shower_mom_bed_2
                $renpy.pause()
                scene shower_mom_bed_1
                $renpy.pause()
                player "{i}I think she is coming out, I'll close my eyes and pretend to be asleep{/i}"
                scene blank
                $renpy.pause()
                scene shower_mom_bed_4
                mom "Greg, wake up..."
                player "Huh..."
                player "Five more minutes, mom!"
                if (quest_sis_missing.meets_requirements(4)):
                    jump quest_sis_missing_mom_shower
                mom "Greg, please go out while I get dressed."
                player "Can't I just turn around?"
                mom "Greg, please leave! I'm not comfortable dressing while you are in the room."
                player "OK, mom..."
                scene door_1
                player "{i}Shit...{/i}"
                jump advance_time
            "Let her know you are awake":
                player "Mom?"
                scene shower_mom_bed_5
                mom "Greg! You are awake?"
                player "Yes, I am..."
                if (quest_sis_missing.meets_requirements(4)):
                    jump quest_sis_missing_mom_shower
                mom "Please leave while I get dressed."
                player "OK mom."
                scene door_1
                player "{i}Maybe I should've watched...{/i}"
                jump advance_time
    elif global_events.mom_lock_door:
        player "She must have locked the door."
        jump map
    else:
        scene shower_mom_1
        player "Spying on my mom feels weird."
        scene shower_mom_2
        player "..."
        scene shower_mom_3
        player "I think I should leave before she sees me."
        $global_events.spied_on_mom = True
        if (quest_investigate_bedroom.meets_requirements(1)):
            menu:
                "Talk with her":
                    jump quest_investigate_bedroom_shower_mom
                "Leave":
                    player "I'd better leave before she sees me."
                    scene door_1
        jump wait_action

label sis_shower:
    hide screen station_rooms
    scene door_1
    player "Lana is taking a shower... should I take a peek?"
    menu:
        "Take a peek":
            jump sis_shower_scene
        "Leave her alone":
            jump map

label sis_shower_scene:
    if global_events.sis_lock_door:
        player "Shit... the door is locked!"
        player "She doesn't like me peeking on her while she is in the shower."
        $global_events.player_knows_sis_lock_door = True
        jump map
    elif global_events.spied_on_sis:
        scene shower_sis_1
        player "Oh, she has such a nice body!"
        scene shower_sis_2
        $renpy.pause()
        scene shower_sis_3
        if (quest_sis_beach.phase >= 10):
            player "Should I let her know that I'm here?"
            menu:
                "Talk with her":
                    if (event_sis_shower.active):
                        jump event_sis_shower_talk
                    else:
                        jump quest_sis_beach_sis_shower
                "Leave":
                    player "I'd better leave before she sees me again."
        else:
            player "I'd better leave before she sees me again."
        jump wait_action
    else:
        scene shower_sis_1
        player "Oh, she has such a nice body!"
        scene shower_sis_2
        $renpy.pause()
        scene shower_sis_3
        $renpy.pause()
        scene shower_sis_4
        player "Shit! She saw me!"
        sis angry "What are you doing here!?! Get out this instant!"
        player "I was looking for mom..."
        sis angry "I don't care! Get out now!"
        scene door_1
        player "I'm in trouble now..."
        $global_events.spied_on_sis = True
        $global_events.sis_lock_door = True
        jump wait_action

label eating:
    hide screen station_rooms
    if not global_events.sis:
        scene mess_hall_mom_rebecca_1
        if (quest_sis_missing.meets_requirements(3)):
            jump quest_sis_missing_dinner
        if (quest_sis_missing.meets_requirements(5)):
            jump quest_sis_missing_talk_breakfast
        if (quest_sis_missing.meets_requirements(7)):
            jump quest_sis_missing_setup_scene
        if (quest_sis_missing.meets_requirements(10)):
            jump quest_sis_missing_dinner_talk
        if (quest_make_a_plan.meets_requirements(0)):
            jump quest_make_a_plan_discuss
        if (quest_make_a_plan.meets_requirements(3)):
            jump quest_make_a_plan_morning
        if (quest_make_a_plan.meets_requirements(8)):
            jump quest_make_a_plan_brakfast
        mom sad "Let's just eat..."
        rebecca sad "Yeah..."
    elif (global_events.rebecca):
        scene mess_hall_mom_sis_rebecca_1
        if (quest_lanas_vibrations.meets_requirements(7)):
            jump quest_lanas_vibrations_breakfast
        if (quest_sis_missing.meets_requirements(0)):
            jump quest_sis_missing_breakfast
        mom "Bon apetit, everyone!"
        rebecca "This food is disgusting!"
        mom "If you want to cook something else, be my guest!"
        rebecca "You call this 'cooking'?"
        sis "Mom, please! Let's just eat..."
    else:
        scene mess_hall_mom_sis_1
        mom "Bon apetit, everyone!"
        sis "I hope we don't have to eat those cookies for too long..."
        mom "It's the best that machine can do right now."
        sis "I know mom. Sorry for complaining."
        player "I'll try to make it do something else than protein cookies."
    jump wait_action

label study:
    scene bedroom_mom_3
    mom "Today's lesson is..."
    jump wait_action
