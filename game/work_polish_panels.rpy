label activate_work_polish_panels:
    $talk_with_terminal.add_topic("Polish the solar panels", "polish_panels", work_polish_panels, 0)
    $work_polish_panels.active = True
    $work_polish_panels.location = "life_support"
    $work_polish_panels.set_clock_offset(0)
    return

label polish_panels:
    $talk_with_terminal.add_topic("Polish the solar panels", "polish_panels", work_polish_panels, 0)
    player "{i}I'll send the robots to polish the solar panels. This should give us a bit more efficiency.{/i}"
    $work_polish_panels.location = "life_support"
    $work_polish_panels.set_clock_offset(6)
    player "{i}...{/i}"
    $efficiency += 3
    player "{i}All done. The robots are now recharging and will be ready in 6 hours.{/i}"
    jump wait_action