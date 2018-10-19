label event_mom_bedroom_start:
    $event_mom_bedroom.active = True
    $event_mom_bedroom.req_clock = 0
    $event_mom_bedroom.clock_mode = "exactly"
    $event_mom_bedroom.repeated = False
    return
    
label event_mom_bedroom_dream:
    $rand = renpy.random.randint(0, 100)
    if not event_mom_bedroom.repeated:
        jump event_mom_bedroom_dream_first
    elif (rand > 80 and not event_mom_bedroom.visited_midnight):
        jump morning
    else:
        jump event_mom_bedroom_dream_repeat

label event_mom_bedroom_dream_first:
    scene bedroom_mom_dream_1
    player "{i}What is going on? Why am I in mom's bedroom?{/i}"
    player "{i}Am I dreaming?{/i}"
    player "{i}I guess I am dreaming - mom would never do something like that with me around.{/i}"
    scene bedroom_mom_dream_2
    player "{i}Wow! Mom is really horny!{/i}"
    player "{i}What am I saying - this is my dream, so this is not really her!{/i}"
    scene bedroom_mom_dream_3
    player "{i}Weird... it doesn't feel like a dream though...{/i}"
    player "{i}I wonder who is she thinking about... probably Jack...{/i}"
    $event_mom_bedroom.repeated = True
    $global_events.had_dream = True
    jump morning
    
label event_mom_bedroom_dream_repeat:
    scene bedroom_mom_dream_1
    player "{i}There is this dream again.{/i}"
    player "{i}But it doesn't feel like a dream...{/i}"
    scene bedroom_mom_dream_2
    $renpy.pause()
    scene bedroom_mom_dream_3
    player "{i}Not that I don't enjoy those dreams, but they started after my encounter with Megan.{/i}"
    player "{i}I wonder if she has something to do with that...{/i}"
    jump morning