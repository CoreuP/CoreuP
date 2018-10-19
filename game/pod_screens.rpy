screen s_pod_night:
    hbox:
        xpos 10
        ypos 50
        spacing 10
        imagebutton:
            idle "gui/pod_icon.png"
            hover "gui/pod_icon_hl.png"
            action Jump("pod_night")
        imagebutton:
            idle "gui/bedroom2.png"
            hover "gui/bedroom2_hl.png"
            action Jump("bedroom_night")
        imagebutton:
            idle "gui/bedroom_icon.png"
            hover "gui/bedroom_icon_hl.png"
            action Jump("bunk_night")
        imagebutton:
            idle "gui/outpost.png"
            hover "gui/outpost_hl.png"
            action Jump("outpost_night")
        imagebutton:
            idle "gui/lab.png"
            hover "gui/lab_hl.png"
            action Jump("lab_night")

screen s_pod_stats:
    hbox:
        xpos 10
        ypos 10
        spacing 40
        text "TIME: [pod_time_text]" style "calendar_text"
        text "SOLVED: [pod_player.equation]%" style "calendar_text"
        text "STRESS: [pod_player.stress]" style "calendar_text"
        text "AROUSAL: [pod_player.arousal]" style "calendar_text"

screen s_pod_day:
    if (quest_released.phase < 4):
        hbox:
            xalign 1.0
            ypos 50
            box_reverse True
            spacing 10
            imagebutton:
                idle "gui/wait_icon.png"
                hover "gui/wait_icon_hl.png"
                action Jump("pod_advance_time")
            imagebutton:
                idle "gui/talk_icon.png"
                hover "gui/talk_icon_hl.png"
                action Jump("pod_talk")

    else:
        hbox:
            xpos 10
            ypos 50
            spacing 10
            imagebutton:
                idle "gui/pod_icon.png"
                hover "gui/pod_icon_hl.png"
                action Jump("pod_day")
            imagebutton:
                idle "gui/bedroom2.png"
                hover "gui/bedroom2_hl.png"
                action Jump("bedroom_day")
            imagebutton:
                idle "gui/bedroom_icon.png"
                hover "gui/bedroom_icon_hl.png"
                action Jump("bunk_day")
            imagebutton:
                idle "gui/outpost.png"
                hover "gui/outpost_hl.png"
                action Jump("outpost_day")
            imagebutton:
                idle "gui/dining_icon.png"
                hover "gui/dining_icon_hl.png"
                action Jump("dining_day")
            imagebutton:
                idle "gui/lab.png"
                hover "gui/lab_hl.png"
                action Jump("lab_day")
            imagebutton:
                idle "gui/door_icon.png"
                hover "gui/door_icon_hl.png"
                action Jump("armory_day")
            imagebutton:
                idle "gui/machine_icon.png"
                hover "gui/machine_icon_hl.png"
                action Jump("machine_day")

#        $talk_icon = (pod_station.get(location).sis and talk_with_sis.has_topics())
#        $talk_icon = talk_icon or (pod_station.get(location).mom and talk_with_mom.has_topics())
#        $talk_icon = talk_icon or (pod_station.get(location).rebecca and talk_with_rebecca.has_topics())
#        $talk_icon = talk_icon or (pod_station.get(location).megan and talk_with_megan.has_topics())
#        $talk_icon = talk_icon or (pod_station.get(location).tiara and talk_with_tiara.has_topics())
        $talk_icon = location == "pod" and quest_final.phase < 3

        if (talk_icon):
            hbox:
                xalign 1.0
                ypos 50
                box_reverse True
                spacing 10
                imagebutton:
                    idle "gui/wait_icon.png"
                    hover "gui/wait_icon_hl.png"
                    action Jump("pod_advance_time")
                imagebutton:
                    idle "gui/talk_icon.png"
                    hover "gui/talk_icon_hl.png"
                    action Jump("pod_talk")

        else:
            hbox:
                xalign 1.0
                ypos 50
                box_reverse True
                spacing 10
                imagebutton:
                    idle "gui/wait_icon.png"
                    hover "gui/wait_icon_hl.png"
                    action Jump("pod_advance_time")


label hide_pod_screens:
    hide screen s_pod_night
    hide screen s_pod_day
    return
