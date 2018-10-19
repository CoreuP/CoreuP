label activate_work_learn_programming:
    $talk_with_terminal.add_topic("Learn how to program the processor", "learn_programming", work_learn_programming, 0)
    $work_learn_programming.active = True
    $work_learn_programming.location = "life_support"
    $work_learn_programming.set_clock_offset(0)
    return

label learn_programming:
    $talk_with_terminal.add_topic("Learn how to program the processor", "learn_programming", work_learn_programming, 0)
    player "{i}I'll read the manual - there should be some instructions on how to program this processor.{/i}"
    $work_learn_programming.location = "life_support"
    $work_learn_programming.set_clock_offset(2)
    player "{i}...{/i}"
    $player_stat.learn_programming()
    call reset_all_programming_topics from _call_reset_all_programming_topics
    player "{i}My head hurts. I need to rest for a couple of hours before I can learn something new again.{/i}"
    jump wait_action
    
label reset_all_programming_topics:
    $quest_mom_beach.cost = 400 - 2 * player_stat.programming
    $quest_mom_beach.chance = 10 + player_stat.programming * 9 / 10