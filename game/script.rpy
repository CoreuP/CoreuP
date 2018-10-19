# The script of the game goes in this file.

style calendar_text is text:
    size 24
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]

init python:

    import math

    class TalkWith:
        def __init__(self, name):
            self.name = name
            self.topics = []

        def add_topic(self, text, label, quest, phase, params = None):
            for t in self.topics:
                if (t.txt == text):
                    return
            self.topics.append(Topic(text, label, quest, phase, params))

        def remove_topic_by_txt(self, txt):
            self.topics = [t for t in self.topics if t.txt != txt]

        def remove_topic(self, topic):
            self.topics = [t for t in self.topics if t.txt != topic.txt]

        def get_topics(self):
            return [t for t in self.topics if t.quest.meets_requirements(t.phase)]

        def has_topics(self):
            return len(self.get_topics()) > 0

    class Topic:
        def __init__(self, text, label, quest, phase, params = None):
            self.txt = text
            self.lbl = label
            self.quest = quest
            self.phase = phase
            self.params = params

        def get_text(self):
            if self.params is None:
                return self.txt
            else:
                txt = self.txt;
                for t in self.params:
                    txt = txt.replace("%param", str(getattr(self.quest, t)), 1)
                return txt

    class PlayerStat:
        def __init__(self):
            self.programming = 0

        def learn_programming(self):
            self.programming += self.get_advance(self.programming, 100)
            return

        def get_advance(self, current, max):
            advance = (max - current) / 2
            if (advance > 5):
                advance = 5
            return advance

    class Stat:
        def __init__(self, name, affection, dominance, horny):
            self.name = name
            self.affection = affection
            self.dominance = dominance
            self.horny = horny

    class Stats:
        def __init__(self):
            self.characters = []

        def get_character(self, name):
            for c in self.characters:
                if (c.name == name):
                    return c
            return Stat(name, 0, 0, 0)

    class GlobalEvents:
        def __init__(self):
            self.version = 4
            self.spied_on_sis = False
            self.spied_on_mom = False
            self.mom_lock_door = True
            self.sis_lock_door = False
            self.player_knows_sis_lock_door = False
            self.simple_clothes = False
            self.black_market = False
            self.deadline = -1
            self.sis_bikini = False
            self.mom_bikini = False
            self.sis_beach = False
            self.mom_beach = False
            self.megan = False
            self.meet_megan = False
            self.contact_others = False
            self.outpost_conversation = False
            self.had_dream = False
            self.rebecca = False
            self.meet_rebecca = False
            self.sleep_bedroom = False
            self.rebecca_topless = False

        def update(self):
            if not hasattr(self, 'version'):
                self.version = 3



    class Station:
        def __init__(self):
            self.rooms = []

        def get_room(self, name):
            for r in self.rooms:
                if (r.name == name):
                    return r
            return Room(name, False)

        def reset(self):
            for r in self.rooms:
                r.mom = False
                r.sis = False
                r.rebecca = False

        def move_to(self, room):
            for r in self.rooms:
                r.player = r.name == room

    class Room:
        def __init__(self, name, terminal):
            self.player = False
            self.mom = False
            self.sis = False
            self.rebecca = False
            self.name = name
            self.terminal = terminal

        def reset(self):
            self.player = False
            self.mom = False
            self.sis = False
            self.rebecca = False
            return

        def is_occupied(self):
            return (self.mom or self.sis or self.rebecca) and clock >= 7

    class WorkRequirement:
        def __init__(self):
            self.phase = 0
            self.active = False
            self.location = "any"
            self.mom_location = "any"
            self.sis_location = "any"
            self.alone = False
            self.req_efficiency = -1;
            self.req_energy = -1;
            self.req_capacity = -1;
            self.req_day = -1;
            self.req_clock = -1;
            self.day_mode = "at_least"
            self.clock_mode = "exactly"
            self.help = ""

        def fail_reason(self, phase):
            result = self.active and phase == self.phase;
            if not result:
                return "inactive/wrong phase"

            efficiency_result = (efficiency >= self.req_efficiency)
            result = result and efficiency_result
            if not result:
                return "efficiency"

            energy_result = (energy >= self.req_energy)
            result = result and energy_result
            if not result:
                return "energy"

            capacity_result = (capacity >= self.req_capacity)
            result = result and capacity_result
            if not result:
                return "capacity"

            day_result = False
            if (self.day_mode == "at_least" and day >= self.req_day):
                day_result = True
            if (self.day_mode == "exactly" and day == self.req_day):
                day_result = True
            if (self.req_day == -1):
                day_result = True
            result = result and day_result
            if not result:
                return "day"

            clock_result = False
            if (self.clock_mode == "at_least" and clock >= self.req_clock):
                clock_result = True
            if (self.clock_mode == "at_most" and clock <= self.req_clock):
                clock_result = True
            if (self.clock_mode == "exactly" and clock == self.req_clock):
                clock_result = True
            if (self.clock_mode == "absolute" and (day * 24 + clock >= self.req_clock)):
                clock_result = True
            if (self.req_clock == -1):
                clock_result = True
            result = result and clock_result
            if not result:
                return "clock"

            location_result = False
            if (station.get_room(self.location).player):
                location_result = True
            if (self.location == "any"):
                location_result = True
            result = result and location_result
            if not result:
                return "location"

            mom_location_result = False
            if (station.get_room(self.mom_location).mom):
                mom_location_result = True
            if (self.mom_location == "any"):
                mom_location_result = True
            result = result and mom_location_result
            if not result:
                return "mom_location"

            sis_location_result = False
            if (station.get_room(self.sis_location).sis):
                sis_location_result = True
            if (self.sis_location == "any"):
                sis_location_result = True
            result = result and sis_location_result
            if not result:
                return "sis_location"

            alone_result = True
            if (self.alone and self.mom_location == "any" and station.get_room(location).mom):
                alone_result = False
            if (self.alone and self.sis_location == "any" and station.get_room(location).sis):
                alone_result = False
            if (self.alone and self.rebecca_location == "any" and station.get_room(location).sis):
                alone_result = False
            result = result and alone_result
            if not result:
                return "alone"

            return "success";

        def meets_requirements(self, phase):
            result = self.active and phase == self.phase;

            efficiency_result = (efficiency >= self.req_efficiency)
            result = result and efficiency_result

            energy_result = (energy >= self.req_energy)
            result = result and energy_result

            capacity_result = (capacity >= self.req_capacity)
            result = result and capacity_result

            day_result = False
            if (self.day_mode == "at_least" and day >= self.req_day):
                day_result = True
            if (self.day_mode == "exactly" and day == self.req_day):
                day_result = True
            if (self.req_day == -1):
                day_result = True
            result = result and day_result

            clock_result = False
            if (self.clock_mode == "at_least" and clock >= self.req_clock):
                clock_result = True
            if (self.clock_mode == "at_most" and clock <= self.req_clock):
                clock_result = True
            if (self.clock_mode == "exactly" and clock == self.req_clock):
                clock_result = True
            if (self.clock_mode == "absolute" and (day * 24 + clock >= self.req_clock)):
                clock_result = True
            if (self.req_clock == -1):
                clock_result = True
            result = result and clock_result

            location_result = False
            if (station.get_room(self.location).player):
                location_result = True
            if (self.location == "any"):
                location_result = True
            result = result and location_result

            mom_location_result = False
            if (station.get_room(self.mom_location).mom):
                mom_location_result = True
            if (self.mom_location == "any"):
                mom_location_result = True
            result = result and mom_location_result

            sis_location_result = False
            if (station.get_room(self.sis_location).sis):
                sis_location_result = True
            if (self.sis_location == "any"):
                sis_location_result = True
            result = result and sis_location_result

            alone_result = True
            if (self.alone and self.mom_location == "any" and station.get_room(location).mom):
                alone_result = False
            if (self.alone and self.sis_location == "any" and station.get_room(location).sis):
                alone_result = False
            if (self.alone and self.rebecca_location == "any" and station.get_room(location).sis):
                alone_result = False
            result = result and alone_result

            return result;

        def set_clock_offset(self, offset):
            self.req_clock = day * 24 + clock + offset
            self.clock_mode = "absolute"
            return

    class QuestRequirement:
        def __init__(self, title):
            self.title = title
            self.phase = 0
            self.active = False
            self.location = "any"
            self.mom_location = "any"
            self.sis_location = "any"
            self.rebecca_location = "any"
            self.alone = False
            self.req_efficiency = -1;
            self.req_energy = -1;
            self.req_capacity = -1;
            self.req_day = -1;
            self.req_clock = -1;
            self.day_mode = "at_least"
            self.clock_mode = "exactly"
            self.help = ""

        def advance_phase(self):
            self.phase += 1
            return

        def fail_reason(self, phase):
            result = self.active and phase == self.phase;
            if not result:
                return "active / phase"

            efficiency_result = (efficiency >= self.req_efficiency)
            result = result and efficiency_result
            if not result:
                return "efficiency"

            energy_result = (energy >= self.req_energy)
            result = result and energy_result
            if not result:
                return "energy"

            capacity_result = (capacity >= self.req_capacity)
            result = result and capacity_result
            if not result:
                return "capacity"

            day_result = False
            if (self.day_mode == "at_least" and day >= self.req_day):
                day_result = True
            if (self.day_mode == "exactly" and day == self.req_day):
                day_result = True
            if (self.req_day == -1):
                day_result = True
            result = result and day_result
            if not result:
                return "day"

            clock_result = False
            if (self.clock_mode == "at_least" and clock >= self.req_clock):
                clock_result = True
            if (self.clock_mode == "at_most" and clock <= self.req_clock):
                clock_result = True
            if (self.clock_mode == "exactly" and clock == self.req_clock):
                clock_result = True
            if (self.req_clock == -1):
                clock_result = True
            result = result and clock_result
            if not result:
                return "clock"

            location_result = False
            if (station.get_room(self.location).player):
                location_result = True
            if (self.location == "any"):
                location_result = True
            result = result and location_result
            if not result:
                return "location"

            mom_location_result = False
            if (station.get_room(self.mom_location).mom):
                mom_location_result = True
            if (self.mom_location == "any"):
                mom_location_result = True
            result = result and mom_location_result
            if not result:
                return "mom location"

            sis_location_result = False
            if (station.get_room(self.sis_location).sis):
                sis_location_result = True
            if (self.sis_location == "any"):
                sis_location_result = True
            result = result and sis_location_result
            if not result:
                return "sis_location"

            rebecca_location_result = False
            if (station.get_room(self.rebecca_location).rebecca):
                rebecca_location_result = True
            if (self.rebecca_location == "any"):
                rebecca_location_result = True
            result = result and rebecca_location_result
            if not result:
                return "rebecca location"

            alone_result = True
            if (self.alone and self.mom_location == "any" and station.get_room(location).mom):
                alone_result = False
            if (self.alone and self.sis_location == "any" and station.get_room(location).sis):
                alone_result = False
            if (self.alone and self.rebecca_location == "any" and station.get_room(location).rebecca):
                alone_result = False
            result = result and alone_result
            if not result:
                return "alone"

            return "success";

        def meets_requirements(self, phase):
            result = self.active and phase == self.phase;

            efficiency_result = (efficiency >= self.req_efficiency)
            result = result and efficiency_result

            energy_result = (energy >= self.req_energy)
            result = result and energy_result

            capacity_result = (capacity >= self.req_capacity)
            result = result and capacity_result

            day_result = False
            if (self.day_mode == "at_least" and day >= self.req_day):
                day_result = True
            if (self.day_mode == "exactly" and day == self.req_day):
                day_result = True
            if (self.req_day == -1):
                day_result = True
            result = result and day_result

            clock_result = False
            if (self.clock_mode == "at_least" and clock >= self.req_clock):
                clock_result = True
            if (self.clock_mode == "at_most" and clock <= self.req_clock):
                clock_result = True
            if (self.clock_mode == "exactly" and clock == self.req_clock):
                clock_result = True
            if (self.req_clock == -1):
                clock_result = True
            result = result and clock_result

            location_result = False
            if (station.get_room(self.location).player):
                location_result = True
            if (self.location == "any"):
                location_result = True
            result = result and location_result

            mom_location_result = False
            if (station.get_room(self.mom_location).mom):
                mom_location_result = True
            if (self.mom_location == "any"):
                mom_location_result = True
            result = result and mom_location_result

            sis_location_result = False
            if (station.get_room(self.sis_location).sis):
                sis_location_result = True
            if (self.sis_location == "any"):
                sis_location_result = True
            result = result and sis_location_result

            rebecca_location_result = False
            if (station.get_room(self.rebecca_location).rebecca):
                rebecca_location_result = True
            if (self.rebecca_location == "any"):
                rebecca_location_result = True
            result = result and rebecca_location_result

            alone_result = True
            if (self.alone and self.mom_location == "any" and station.get_room(location).mom):
                alone_result = False
            if (self.alone and self.sis_location == "any" and station.get_room(location).sis):
                alone_result = False
            if (self.alone and self.rebecca_location == "any" and station.get_room(location).rebecca):
                alone_result = False
            result = result and alone_result

            return result;

        def reset(self):
            self.location = "any"
            self.mom_location = "any"
            self.sis_location = "any"
            self.rebecca_location = "any"
            self.alone = False
            self.req_efficiency = -1;
            self.req_energy = -1;
            self.req_capacity = -1;
            self.req_day = -1;
            self.req_clock = -1;
            self.day_mode = "at_least"
            self.clock_mode = "exactly"
            self.help = ""
            return

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Player name "Greg"
define player = Character("You", image="player")

#Mom name "Amelia/Amy" model Rebekah
define mom = Character("Mom", image="mom")

image side mom = "side/mom.png"
image side mom scared = "side/mom_scared.png"
image side mom angry = "side/mom_angry.png"
image side mom happy = "side/mom_happy.png"
image side mom flirting = "side/mom_flirting.png"

#Sis name "Lana"
define sis = Character("Sis", image="sis")

image side sis = "side/sis.png"
image side sis scared = "side/sis_scared.png"
image side sis angry = "side/sis_angry.png"
image side sis happy = "side/sis_happy.png"
image side sis flirting = "side/sis_flirting.png"

#model Olympia
define megan = Character("Megan", image="megan")

image side megan = "side/megan.png"
image side megan scared = "side/megan_scared.png"
image side megan angry = "side/megan_angry.png"
image side megan happy = "side/megan_happy.png"
image side megan flirting = "side/megan_flirting.png"

#model ???
define rebecca = Character("Rebecca", image="rebecca")

image side rebecca = "side/rebecca.png"
image side rebecca scared = "side/rebecca_scared.png"
image side rebecca angry = "side/rebecca_angry.png"
image side rebecca happy = "side/rebecca_happy.png"
image side rebecca flirting = "side/rebecca_flirting.png"

#model ???
define susan = Character("Susan", image="susan")

image side susan = "side/susan.png"
image side susan scared = "side/susan_scared.png"
image side susan angry = "side/susan_angry.png"
image side susan happy = "side/susan_happy.png"
image side susan flirting = "side/susan_flirting.png"

#model Monique
define tiara = Character("Tiara", image="tiara")

image side tiara = "side/tiara.png"
image side tiara scared = "side/tiara_scared.png"
image side tiara angry = "side/tiara_angry.png"
image side tiara happy = "side/tiara_happy.png"
image side tiara flirting = "side/tiara_flirting.png"

define jack = Character("Jack", image="jack")
define automated = Character("Automated voice", image="automated")

image side jack = "side/jack.png"


define female = Character("Female voice", image="female")
define male = Character("Male voice", image="male")

label __init_variables:
    python:
        if not hasattr(renpy.store,'global_events'):
            global_events = GlobalEvents()
        if not hasattr(global_events, 'mom_beach'):
            global_events.mom_beach = False
        if not hasattr(global_events, 'megan'):
            global_events.megan = False
        if not hasattr(global_events, 'meet_megan'):
            global_events.meet_megan = False
        if not hasattr(global_events, 'contact_others'):
            global_events.contact_others = False
        if not hasattr(global_events, 'megan'):
            global_events.megan = False
        if not hasattr(global_events, 'outpost_conversation'):
            global_events.outpost_conversation = -1
        if not hasattr(global_events, 'had_dream'):
            global_events.had_dream = False
        if not hasattr(global_events, 'version'):
            global_events.version = 3

        if not hasattr(renpy.store,'work_polish_panels'):
            work_polish_panels = WorkRequirement()
        if not hasattr(renpy.store,'work_learn_programming'):
            work_learn_programming = WorkRequirement()

        if not hasattr(renpy.store,'event_sis_strip_beach'):
            event_sis_strip_beach = QuestRequirement("_event_sis_strip_beach")
        if not hasattr(renpy.store,'event_mom_strip_beach'):
            event_mom_strip_beach = QuestRequirement("_event_mom_strip_beach")
        if not hasattr(renpy.store,'event_sis_shower'):
            event_sis_shower = QuestRequirement("_event_sis_shower")
        if not hasattr(renpy.store,'event_mom_bedroom'):
            event_mom_bedroom = QuestRequirement("_event_mom_bedroom")
        if not hasattr(renpy.store,'event_outpost'):
            event_outpost = QuestRequirement("_event_outpost")
        if not hasattr(renpy.store,'event_outpost_sex'):
            event_outpost_sex = QuestRequirement("_event_outpost_sex")
        if not hasattr(renpy.store,'event_rebecca_dice_game'):
            event_rebecca_dice_game = QuestRequirement("_event_rebecca_dice_game")
        if not hasattr(renpy.store,'event_lana_rebecca_sleep'):
            event_lana_rebecca_sleep = QuestRequirement("_event_lana_rebecca_sleep")

        if not hasattr(renpy.store,'quest_simple_clothes'):
            quest_simple_clothes = QuestRequirement("Simple Clothes")
        if not hasattr(quest_simple_clothes,'finished'):
            quest_simple_clothes.finished = quest_simple_clothes.phase >= 8

        if not hasattr(renpy.store,'quest_black_market'):
            quest_black_market = QuestRequirement("Contact Earth")
        if not hasattr(quest_black_market,'finished'):
            quest_black_market.finished = quest_black_market.phase >= 8

        if not hasattr(renpy.store,'quest_sis_beach'):
            quest_sis_beach = QuestRequirement("Lana on the Beach")
        if not hasattr(quest_sis_beach,'finished'):
            quest_sis_beach.finished = quest_sis_beach.phase >= 11

        if not hasattr(renpy.store,'quest_mom_beach'):
            quest_mom_beach = QuestRequirement("Mom on the Beach")
        if not hasattr(quest_mom_beach,'finished'):
            quest_mom_beach.finished = quest_mom_beach.phase >= 4

        if not hasattr(renpy.store,'quest_meet_megan'):
            quest_meet_megan = QuestRequirement("Meet Megan")
        if not hasattr(quest_meet_megan,'finished'):
            quest_meet_megan.finished = quest_meet_megan.phase >= 8

        if not hasattr(renpy.store,'quest_lanas_vibrations'):
            quest_lanas_vibrations = QuestRequirement("Lana's Vibrations")
        if not hasattr(quest_lanas_vibrations,'finished'):
            quest_lanas_vibrations.finished = quest_lanas_vibrations.phase >= 14

        if not hasattr(renpy.store,'quest_investigate_bedroom'):
            quest_investigate_bedroom = QuestRequirement("Investigate the Bedroom")
        if not hasattr(quest_investigate_bedroom,'finished'):
            quest_investigate_bedroom.finished = quest_investigate_bedroom.phase >= 3

        if not hasattr(renpy.store,'quest_meet_rebecca'):
            quest_meet_rebecca = QuestRequirement("Meet Rebecca")
        if not hasattr(quest_meet_rebecca,'finished'):
            quest_meet_rebecca.finished = quest_meet_rebecca.phase >= 9

        if not hasattr(renpy.store,'quest_sis_missing'):
            quest_sis_missing = QuestRequirement("Lana's Kidnap")
        if not hasattr(quest_sis_missing,'finished'):
            quest_sis_missing.finished = quest_sis_missing.phase >= 12

        if not hasattr(renpy.store,'quest_make_a_plan'):
            quest_make_a_plan = QuestRequirement("Make a Plan")
        if not hasattr(quest_make_a_plan,'finished'):
            quest_make_a_plan.finished = quest_make_a_plan.phase >= 11

        if not hasattr(renpy.store,'quest_captured'):
            quest_captured = QuestRequirement("Captured")
        if not hasattr(quest_captured,'finished'):
            quest_captured.finished = False

        if not hasattr(renpy.store,'talk_with_rebecca'):
            talk_with_rebecca = TalkWith("rebecca")
        if not hasattr(renpy.store,'talk_with_sis'):
            talk_with_sis = TalkWith("sis")
        if not hasattr(renpy.store,'talk_with_mom'):
            talk_with_mom = TalkWith("mom")
        if not hasattr(renpy.store,'talk_with_mom_sis'):
            talk_with_mom_sis = TalkWith("mom_sis")
        if not hasattr(renpy.store,'talk_with_terminal'):
            talk_with_terminal = TalkWith("terminal")
        if not hasattr(renpy.store,'station'):
            station = Station()
            station.rooms.append(Room("shared_beds", False))
            station.rooms.append(Room("bedroom", False))
            station.rooms.append(Room("mess_hall", True))
            station.rooms.append(Room("med_bay", True))
            station.rooms.append(Room("comm", True))
            station.rooms.append(Room("vr_room", False))
            station.rooms.append(Room("life_support", True))
        if not hasattr(renpy.store,'stats'):
            stats = Stats()
            stats.characters.append(Stat('mom', 0, 0, 0))
            stats.characters.append(Stat('sis', 0, 0, 0))
        if not hasattr(renpy.store,'player_stat'):
            player_stat = PlayerStat()
        if not hasattr(renpy.store,'rebecca_location'):
            rebecca_location = "void"
        if not hasattr(renpy.store,'mom_location'):
            mom_location = "void"
        if not hasattr(renpy.store,'sis_location'):
            sis_location = "void"
        if not hasattr(renpy.store,'location'):
            location = "void"
        station.get_room(mom_location).mom = True
        station.get_room(sis_location).sis = True
        station.get_room(location).player = True
    call initialize_global_events from _call_initialize_global_events
    return

label initialize_global_events:
    if (global_events.version == 3):
        if global_events.meet_megan and quest_investigate_bedroom.phase >= 2:
            call start_quest_meet_rebecca from _call_start_quest_meet_rebecca_2
        if (quest_investigate_bedroom.active):
            call quest_investigate_bedroom_start from _call_quest_investigate_bedroom_start_2
        $station.get_room("shared_beds").rebecca = False
        $station.get_room("bedroom").rebecca = False
        $station.get_room("comm").rebecca = False
        $station.get_room("life_support").rebecca = False
        $station.get_room("med_bay").rebecca = False
        $station.get_room("vr_room").rebecca = False
        $station.get_room("mess_hall").rebecca = False
        $quest_simple_clothes.rebecca_location = "any"
        $quest_black_market.rebecca_location = "any"
        $quest_sis_beach.rebecca_location = "any"
        $quest_mom_beach.rebecca_location = "any"
        $quest_meet_megan.rebecca_location = "any"
        $quest_lanas_vibrations.rebecca_location = "any"
        $quest_investigate_bedroom.rebecca_location = "any"
        $event_sis_strip_beach.rebecca_location = "any"
        $event_mom_strip_beach.rebecca_location = "any"
        $event_sis_shower.rebecca_location = "any"
        $event_mom_bedroom.rebecca_location = "any"
        $event_outpost.rebecca_location = "any"
        $global_events.rebecca = False
        $global_events.meet_rebecca = False
        $global_events.sleep_bedroom = False
        $global_events.rebecca_topless = False
        $global_events.version = 4
    if (global_events.version == 4):
        if (quest_lanas_vibrations.active):
            call start_quest_lanas_vibrations from _call_start_quest_lanas_vibrations_1
        $global_events.rebecca_vibrations = False
        $global_events.played_game_with_lana = False
        $global_events.version = 5
    if (global_events.version == 5):
        if not hasattr(global_events,'mom'):
            $global_events.mom = True
        $global_events.sis = True
        $global_events.greg_threesome = False
        $global_events.mom_leather = False
        $global_events.mom_vr_first = False
        if (global_events.played_game_with_lana):
            call quest_sis_missing_start from _call_quest_sis_missing_start_1
        if not global_events.mom and quest_lanas_vibrations.phase >= 11:
            $global_events.mom = True
        $global_events.version = 6
    if (global_events.version == 6):
        if (quest_sis_missing.finished):
            $quest_sis_missing.finished = False
            $quest_sis_missing.location = "comm"
            $quest_sis_missing.req_clock = 3
            $quest_sis_missing.clock_mode = "at_most"
            $talk_with_terminal.add_topic("Obtain the plans", "quest_sis_missing_get_plans", quest_sis_missing, 11)
        if not hasattr(global_events,'greg_threesome'):
            $global_events.greg_threesome = False
        if not hasattr(global_events,'rebecca_bedroom'):
            $global_events.rebecca_bedroom = False
        $global_events.version = 7
    if (global_events.version == 7):
        $global_events.know_time_machine = False
        $global_events.know_die = False
        $global_events.know_abuse = False
        $global_events.version = 8
    if (global_events.version == 8):
        $global_events.bedroom2_phase = 0
        $global_events.lab_phase = 0
        $global_events.pod_phase = 0
        $global_events.dinner_phase = 0
        $global_events.bunk_phase = 0
        $global_events.outpost_phase = 0
        $pod_player = PodPlayer()
        $pod_station = PodStation()
        $pod_mom = PodCharacter("mom")
        $pod_tiara = PodCharacter("tiara")
        $pod_lana = PodCharacter("lana")
        $pod_rebecca = PodCharacter("rebecca")
        $pod_megan = PodCharacter("megan")
        $pod_susan = PodCharacter("susan")
        $pod_had_sex = 1
        $last_sex = ""
        $global_events.pod_started = False
        $pod_equation_cap = 30

        $global_events.version = 9
    if (global_events.version == 9):
        $global_events.pod_shower = False
        $quest_released = PodQuest()
        $pod_equation_cap = 60
        $talk_with_megan = TalkWith("megan")
        $talk_with_tiara = TalkWith("tiara")
        $bedroom2_talk = PodQuest()
        $outpost_talk = PodQuest()
        $armory_talk = PodQuest()

        $global_events.version = 10
    if (global_events.version == 10):
        $quest_final = PodQuest()
        $pod_equation_cap = 90
        if (quest_released.phase >= 13 and quest_final.phase == 0):
            call final_start from _call_final_start_1

        $global_events.version = 11
    return

label jump_to_location:
    if (station.get_room(location).name == "shared_beds"):
        jump room_shared_beds
    elif (station.get_room(location).name == "bedroom"):
        jump room_bedroom
    elif (station.get_room(location).name == "comm"):
        jump room_comm
    elif (station.get_room(location).name == "life_support"):
        jump room_life_support
    elif (station.get_room(location).name == "med_bay"):
        jump room_med_bay
    elif (station.get_room(location).name == "vr_room"):
        jump room_vr
    elif (station.get_room(location).name == "mess_hall"):
        jump room_mess_hall

screen day_time:
    hbox:
        xpos 10
        ypos 10
        spacing 40
        text "{b}DAY: [day]{/b}" style "calendar_text"
        text "{b}TIME: [clock]:00{/b}" style "calendar_text"

screen energy:
    hbox:
        xalign 1.0
        ypos 10
        box_reverse True
        text "{b}PANELS: [efficiency]%{/b}" style "calendar_text"
        text "{b}BATTERY: [energy]/[capacity]kWh{/b}" style "calendar_text"

screen station_rooms:
    if (global_events.black_market):
        $vr_icon = "gui/beach_icon.png"
        $vr_icon_hl = "gui/beach_icon_hl.png"
    else:
        $vr_icon = "gui/vr_icon.png"
        $vr_icon_hl = "gui/vr_icon_hl.png"
    hbox:
        xpos 10
        ypos 50
        spacing 10
        imagebutton:
            idle "gui/info_icon.png"
            hover "gui/info_icon_hl.png"
            action Jump("show_help")
        imagebutton:
            idle "gui/bunk_icon.png"
            hover "gui/bunk_icon_hl.png"
            action Jump("room_shared_beds")
        imagebutton:
            idle "gui/bedroom_icon.png"
            hover "gui/bedroom_icon_hl.png"
            action Jump("room_bedroom")
        imagebutton:
            idle "gui/mess_hall_icon.png"
            hover "gui/mess_hall_icon_hl.png"
            action Jump("room_mess_hall")
        imagebutton:
            idle "gui/comm_icon.png"
            hover "gui/comm_icon_hl.png"
            action Jump("room_comm")
        imagebutton:
            idle "gui/life_support_icon.png"
            hover "gui/life_support_icon_hl.png"
            action Jump("room_life_support")
        imagebutton:
            idle "gui/med_bay_icon.png"
            hover "gui/med_bay_icon_hl.png"
            action Jump("room_med_bay")
        imagebutton:
            idle vr_icon
            hover vr_icon_hl
            action Jump("room_vr")

    $location_offset = 70
    if (station.get_room("shared_beds").player):
        $location_offset = 70
    elif (station.get_room("bedroom").player):
        $location_offset = 170
    elif (station.get_room("mess_hall").player):
        $location_offset = 270
    elif (station.get_room("comm").player):
        $location_offset = 370
    elif (station.get_room("life_support").player):
        $location_offset = 470
    elif (station.get_room("med_bay").player):
        $location_offset = 570
    elif (station.get_room("vr_room").player):
        $location_offset = 670
    hbox:
        xpos location_offset
        ypos 50
        image "gui/location.png"

    $mom_offset = 70
    if (station.get_room("shared_beds").mom):
        $mom_offset = 130
    elif (station.get_room("bedroom").mom):
        $mom_offset = 230
    elif (station.get_room("mess_hall").mom):
        $mom_offset = 330
    elif (station.get_room("comm").mom):
        $mom_offset = 430
    elif (station.get_room("life_support").mom):
        $mom_offset = 530
    elif (station.get_room("med_bay").mom):
        $mom_offset = 630
    elif (station.get_room("vr_room").mom):
        $mom_offset = 730
    hbox:
        xpos mom_offset
        ypos 75
        image "gui/mom_location.png"

    $sis_offset = -1
    if (station.get_room("shared_beds").sis):
        $sis_offset = 130
    elif (station.get_room("bedroom").sis):
        $sis_offset = 230
    elif (station.get_room("mess_hall").sis):
        $sis_offset = 330
    elif (station.get_room("comm").sis):
        $sis_offset = 430
    elif (station.get_room("life_support").sis):
        $sis_offset = 530
    elif (station.get_room("med_bay").sis):
        $sis_offset = 630
    elif (station.get_room("vr_room").sis):
        $sis_offset = 730
    if (sis_offset != -1 and mom_location == sis_location):
        $sis_offset = sis_offset - 30
    if (sis_offset != -1):
        hbox:
            xpos sis_offset
            ypos 75
            image "gui/sis_location.png"

    $rebecca_offset = -1
    if (station.get_room("shared_beds").rebecca):
        $rebecca_offset = 130

    elif (station.get_room("bedroom").rebecca):
        $rebecca_offset = 230
    elif (station.get_room("mess_hall").rebecca):
        $rebecca_offset = 330
    elif (station.get_room("comm").rebecca):
        $rebecca_offset = 430
    elif (station.get_room("life_support").rebecca):
        $rebecca_offset = 530
    elif (station.get_room("med_bay").rebecca):
        $rebecca_offset = 630
    elif (station.get_room("vr_room").rebecca):
        $rebecca_offset = 730
    if (mom_location == rebecca_location):
        $rebecca_offset = rebecca_offset - 30
    if (sis_location == rebecca_location):
        $rebecca_offset = rebecca_offset - 30
    if (rebecca_offset != -1):
        hbox:
            xpos rebecca_offset
            ypos 75
            image "gui/rebecca_location.png"

    if (global_events.megan):
        $megan_offset = 630
        hbox:
            xpos megan_offset
            ypos 75
            image "gui/megan_location.png"

    $terminal_icon = (station.get_room(location).name == "comm" or (station.get_room(location).terminal and talk_with_terminal.has_topics()))
    $talk_icon = (station.get_room(location).sis and talk_with_sis.has_topics())
    $talk_icon = talk_icon or (station.get_room(location).mom and talk_with_mom.has_topics())
    $talk_icon = talk_icon or (station.get_room(location).rebecca and talk_with_rebecca.has_topics())
    $talk_icon = talk_icon or (station.get_room(location).sis and station.get_room(location).mom and talk_with_mom_sis.has_topics())

    if (global_events.rebecca):
        $sleep_location = "bedroom"
    else:
        $sleep_location = "shared_beds"
    if (station.get_room(location).name == sleep_location and clock < 3):
        hbox:
            xalign 1.0
            ypos 50
            box_reverse True
            spacing 10
            imagebutton:
                idle "gui/wait_icon.png"
                hover "gui/wait_icon_hl.png"
                action Jump("wait_action")
            imagebutton:
                idle "gui/sleep_icon.png"
                hover "gui/sleep_icon_hl.png"
                action Jump("sleep")
    elif (terminal_icon and talk_icon):
        hbox:
            xalign 1.0
            ypos 50
            box_reverse True
            spacing 10
            imagebutton:
                idle "gui/wait_icon.png"
                hover "gui/wait_icon_hl.png"
                action Jump("wait_action")
            imagebutton:
                idle "gui/terminal_icon.png"
                hover "gui/terminal_icon_hl.png"
                action Jump("terminal")
            imagebutton:
                idle "gui/talk_icon.png"
                hover "gui/talk_icon_hl.png"
                action Jump("talk")

    elif (terminal_icon):
        hbox:
            xalign 1.0
            ypos 50
            box_reverse True
            spacing 10
            imagebutton:
                idle "gui/wait_icon.png"
                hover "gui/wait_icon_hl.png"
                action Jump("wait_action")
            imagebutton:
                idle "gui/terminal_icon.png"
                hover "gui/terminal_icon_hl.png"
                action Jump("terminal")

    elif (talk_icon):
        hbox:
            xalign 1.0
            ypos 50
            box_reverse True
            spacing 10
            imagebutton:
                idle "gui/wait_icon.png"
                hover "gui/wait_icon_hl.png"
                action Jump("wait_action")
            imagebutton:
                idle "gui/talk_icon.png"
                hover "gui/talk_icon_hl.png"
                action Jump("talk")
    else:
        hbox:
            xalign 1.0
            ypos 50
            box_reverse True
            spacing 10
            imagebutton:
                idle "gui/wait_icon.png"
                hover "gui/wait_icon_hl.png"
                action Jump("wait_action")

screen quest_help:
    $xoffset = 315
    $yoffset = 80
    if (quest_simple_clothes.active and quest_simple_clothes.help is not ""):
        $quest_title = "> " + quest_simple_clothes.title
        if (quest_simple_clothes.finished):
            $quest_title += "*"
        button:
            xpos xoffset
            ypos yoffset
            text quest_title
            action Jump("help_simple_clothes")
        $yoffset += 30
    if (quest_black_market.active and quest_black_market.help is not ""):
        $quest_title = "> " + quest_black_market.title
        if (quest_black_market.finished):
            $quest_title += "*"
        button:
            xpos xoffset
            ypos yoffset
            text quest_title
            action Jump("help_black_market")
        $yoffset += 30
    if (quest_sis_beach.active and quest_sis_beach.help is not ""):
        $quest_title = "> " + quest_sis_beach.title
        if (quest_sis_beach.finished):
            $quest_title += "*"
        button:
            xpos xoffset
            ypos yoffset
            text quest_title
            action Jump("help_sis_beach")
        $yoffset += 30
    if (quest_mom_beach.active and quest_mom_beach.help is not ""):
        $quest_title = "> " + quest_mom_beach.title
        if (quest_mom_beach.finished):
            $quest_title += "*"
        button:
            xpos xoffset
            ypos yoffset
            text quest_title
            action Jump("help_mom_beach")
        $yoffset += 30
    if (quest_meet_megan.active and quest_meet_megan.help is not ""):
        $quest_title = "> " + quest_meet_megan.title
        if (quest_meet_megan.finished):
            $quest_title += "*"
        button:
            xpos xoffset
            ypos yoffset
            text quest_title
            action Jump("help_meet_megan")
        $yoffset += 30
    if (quest_lanas_vibrations.active and quest_lanas_vibrations.help is not ""):
        $quest_title = "> " + quest_lanas_vibrations.title
        if (quest_lanas_vibrations.finished):
            $quest_title += "*"
        button:
            xpos xoffset
            ypos yoffset
            text quest_title
            action Jump("help_lanas_vibrations")
        $yoffset += 30
    if (quest_investigate_bedroom.active and quest_investigate_bedroom.help is not ""):
        $quest_title = "> " + quest_investigate_bedroom.title
        if (quest_investigate_bedroom.finished):
            $quest_title += "*"
        button:
            xpos xoffset
            ypos yoffset
            text quest_title
            action Jump("help_investigate_bedroom")
        $yoffset += 30
    if (quest_meet_rebecca.active and quest_meet_rebecca.help is not ""):
        $quest_title = "> " + quest_meet_rebecca.title
        if (quest_meet_rebecca.finished):
            $quest_title += "*"
        button:
            xpos xoffset
            ypos yoffset
            text quest_title
            action Jump("help_meet_rebecca")
        $yoffset += 30
    if (quest_sis_missing.active and quest_sis_missing.help is not ""):
        $quest_title = "> " + quest_sis_missing.title
        if (quest_sis_missing.finished):
            $quest_title += "*"
        button:
            xpos xoffset
            ypos yoffset
            text quest_title
            action Jump("quest_sis_missing_help")
        $yoffset += 30
    if (quest_make_a_plan.active and quest_make_a_plan.help is not ""):
        $quest_title = "> " + quest_make_a_plan.title
        if (quest_make_a_plan.finished):
            $quest_title += "*"
        button:
            xpos xoffset
            ypos yoffset
            text quest_title
            action Jump("quest_make_a_plan_help")
        $yoffset += 30
    button:
        xpos xoffset
        ypos 500
        text "> EXIT"
        action Jump("exit_help")

#------------------------------------------------------

#vvvvvv DETERMINE QUEST SPECIFIC EVENTS HERE vvvvvvv

label room_shared_beds:
    $location = "shared_beds"
    $station.move_to(location)
    $room = station.get_room(location)
    #this is not a quest based check but should be run before any of them to ensure going to sleep
    if clock == 2:
        jump sleep
    if quest_simple_clothes.meets_requirements(0):
        jump day_1_morning
    if (quest_simple_clothes.meets_requirements(3)):
        jump check_tags
    if (quest_make_a_plan.meets_requirements(5)):
        jump quest_make_a_plan_talk_mom_beds

    if (room.rebecca and room.sis and clock >= 7):
        scene shared_beds_rebecca_sis_1
    elif (room.rebecca and clock >= 7):
        scene shared_beds_rebecca_1
    elif (room.rebecca and room.sis and clock < 2):
        scene shared_beds_sleep_rebecca_sis_1
    elif (clock < 2 and room.sis):
        jump room_shared_beds_sleep
    elif (clock < 2 and room.rebecca):
        scene shared_beds_sleep_rebecca_1
    elif (station.get_room(location).sis):
        if (global_events.outpost_conversation == day):
            scene blank
            player "{i}What a strange dream!{/i}"
            player "{i}It felt almost real, but at the same time so distant...{/i}"
        if (global_events.simple_clothes):
            scene shared_beds_sis_9
        else:
            scene shared_beds_sis_2
        jump map
    elif (room.mom and clock >= 7):
        scene shared_beds_mom_1
    elif (room.mom and clock < 2):
        scene shared_beds_mom_2
    else:
        jump room_shared_beds_empty
    jump map

label room_bedroom:
    $location = "bedroom"
    $station.move_to(location)
    if (quest_make_a_plan.meets_requirements(7)):
        jump quest_make_a_plan_make_hack
    if (clock == 7 and not global_events.rebecca_bedroom):
        jump mom_shower
    elif (clock == 7):
        jump rebecca_shower
    elif (clock == 8 and global_events.sis):
        jump sis_shower
    elif (clock == 12 and global_events.rebecca and not global_events.rebecca_bedroom):
        jump rebecca_shower
    elif (station.get_room(location).mom):
        if (clock < 3 and global_events.mom_lock_door):
            scene door_1
            player "The door is locked."
        elif (clock < 3):
            $event_mom_bedroom.visited_midnight = True
            scene bedroom_mom_sleep_1
        elif (global_events.simple_clothes and clock >= 20):
            scene bedroom_mom_5
        else:
            scene bedroom_mom_4
        jump map
    elif (station.get_room(location).sis):
        scene bedroom_sis_1
        jump map
    elif (station.get_room(location).rebecca):
        if (clock < 3 and global_events.rebecca_bedroom):
            scene bedroom_rebecca_sleep_1
        else:
            scene bedroom_rebecca_12
        jump map
    else:
        if (quest_sis_beach.meets_requirements(7)):
            jump quest_sis_beach_shower
        else:
            jump room_bedroom_empty

label room_comm:
    $location = "comm"
    $station.move_to(location)

    if (station.get_room(location).mom and station.get_room(location).sis):
        scene comm_mom_sis_2
        jump map
    elif (station.get_room(location).mom):
        scene comm_mom_1
        jump map
    elif (station.get_room(location).sis):
        scene comm_sis_1
        jump map
    elif (station.get_room(location).rebecca):
        scene comm_rebecca_1
        jump map
    else:
        jump room_comm_empty

label room_life_support:
    $location = "life_support"
    $station.move_to(location)
    if (station.get_room(location).sis):
        scene life_support_sis_1
        jump map
    elif (station.get_room(location).rebecca):
        scene life_support_rebecca_1
        if (quest_meet_rebecca.meets_requirements(8)):
            jump quest_meet_rebecca_play_game
        elif (event_rebecca_dice_game.meets_requirements(1)):
            jump event_rebecca_dice_game_play
        else:
            jump map
    else:
        jump room_life_support_empty

label room_med_bay:
    $location = "med_bay"
    $station.move_to(location)

    if (station.get_room(location).mom):
        scene med_bay_mom_1
        jump map
    elif (station.get_room(location).sis):
        scene med_bay_sis_1
        jump map
    elif (station.get_room(location).rebecca):
        scene med_bay_rebecca_1
        jump map
    else:
        jump room_med_bay_empty

label room_vr:
    $location = "vr_room"
    $station.move_to(location)
    if (station.get_room(location).mom):
        if global_events.black_market and global_events.mom_bikini:
            scene beach_mom_4
        elif global_events.black_market:
            scene beach_mom_3
        else:
            scene vr_mom_2
        jump map
    elif (station.get_room(location).sis):
        if global_events.sis_bikini:
            scene beach_sis_3
        elif global_events.black_market:
            scene beach_sis_5
            if not quest_sis_beach.active:
                call start_quest_sis_beach from _call_start_quest_sis_beach
        else:
            scene vr_sis_1
        jump map
    elif (station.get_room(location).rebecca):
        if global_events.rebecca_topless:
            scene beach_rebecca_13
        else:
            scene beach_rebecca_1
        jump map
    else:
        jump room_vr_empty

label room_mess_hall:
    $location = "mess_hall"
    $station.move_to(location)
    if (quest_sis_beach.meets_requirements(4)):
        jump quest_sis_beach_give_skimpy_bikini
    if (quest_simple_clothes.meets_requirements(7)):
        jump give_clothes_mom
    if (quest_black_market.meets_requirements(2)):
        jump black_market_breakfast
    if (quest_meet_megan.meets_requirements(3)):
        jump quest_meet_megan_dinner
    if (quest_meet_rebecca.meets_requirements(0)):
        jump quest_meet_rebecca_dinner
    if (clock == 9 and event_outpost.req_day == day + 1):
        jump breakfast_after_megan
    if (clock == 9 or clock == 19):
        jump eating

    if (station.get_room(location).mom and station.get_room(location).sis):
        scene mess_hall_mom_sis_1
        jump map
    elif (station.get_room(location).mom):
        scene mess_hall_mom_1
        jump map
    elif (station.get_room(location).sis):
        scene mess_hall_sis_1
        jump map
    elif (station.get_room(location).rebecca):
        scene mess_hall_rebecca_1
        jump map
    else:
        jump room_mess_hall_empty

#^^^^^^ DETERMINE QUEST SPECIFIC EVENTS HERE ^^^^^^^

#---------------------------------------------------------------------

label room_life_support_empty:
    scene life_support_1
    jump map

label room_shared_beds_empty:
    scene shared_beds_1
    jump map

label room_bedroom_empty:
    scene bedroom_1
    jump map

label room_vr_empty:
    if global_events.black_market:
        scene beach_1
    else:
        scene vr_1
    jump map

label room_control_empty:
    scene control_room_1
    jump map

label room_med_bay_empty:
    if (global_events.megan):
        scene door_3
    else:
        scene med_bay_1
    jump map

label room_comm_empty:
    scene comm_1
    jump map

label room_mess_hall_empty:
    scene mess_hall_1
    jump map

label after_load:
    $init_variables()
    return

# The game starts here.

label start:
    $init_variables()
    $day = 1;
    $clock = 0;
    $energy = 300.0;
    $capacity = 1000;
    $generator = 20;
    $efficiency = 30;
    $waiting = True;

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene door_mom_sis_1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    mom scared "Jack! Jack! Can you hear me?"
    mom scared "Jack, please open the door!"
    sis scared "Dad!"
    mom scared "... Jack, open the door and come inside! ... Please!"

    scene door_mom_sis_2
    sis scared "We need to override the console to let him in!"
    sis scared "Quick! Pass me the tools so I can open it!"

    mom scared "No! It's too dangerous - we don't know what is on the other side of that door."
    sis scared "Don't leave him out there!"
    mom scared "Your father sacrificed himself so we can have a chance to survive."
    mom scared "He knew that M.A.L. can't access this part of the station, that's why he locked us here."
    mom sad "We have to find a terminal and check on the life support systems."

    sis scared "But dad..."

    mom angry "Lana, stop it!"
    mom angry "Listen to me - we need the life support for this section running at 100\% or else we'll die too!"

    scene engineering_mom_1

    mom scared "Looks like M.A.L. disabled everything when we ran for this section."
    mom angry "Fuck! We'll have air for just a couple of hours if I can't get this thing running again."
    sis scared "Mom, I'm scared!"
    mom angry "Don't worry, I doubt M.A.L. could do much damage before your dad sealed this section."
    mom thinking "..."
    mom happy "Here! All done! Air flow is restored and CO2 scrubbers are working on optimal levels."
    player "The temperature is rising... 15 degrees Celsius, ..., 16 degrees Celsius"
    mom "Let's get the lights working and try to contact Earth to let them know what happened."

    scene comm_mom_sis_1

    mom "Lana, the comm unit is not working, can you please check what's wrong?"
    sis "Sure mom! ... Let's see... Hmmm, everything seems to be in order..."

    scene comm_sis_1

    sis thinking "Let's try to flush the configuration just in case M.A.L. messed up the frequencies."
    sis "..."
    sis "Done! Try it now!"

    scene comm_mom_sis_2

    mom "Station Antares to Control! Can you hear me?"
    #static
    female "This is Earth Control Center \"Liberty\". Who are you?"
    #mom talking on comm
    mom "My name is Amelia and my children and I are sealed off on Antares station."
    mom "The station's AI went haywire and started killing the personel."
    mom "My husband locked us on section D-5 of the station. The AI has no access to this section, but we don't know how long we can survive."
    #static
    female "Calm down! We've already received a message from M.A.L. telling us that it's in full control of the station and threatening to destroy any incoming object."
    female "Also it has targeted Earth's major cities with the station's nukes and as far as we can tell, you are the only people alive on the station."
    player "Is my father alive? He was locked on the other side of the D-5 door."
    female "We can't run full scan on the station. M.A.L. is interfering with our scanners and we don't want to provoke it."
    #mom and sis on comm
    sis "Is it aware that we are here?"
    female "... The truth is... we don't know."
    mom "We managed to get the life support running but I don't know if we have enough food or water to remain here."
    #static
    female "The plans for the station show an energy processor in you section, so you should be able to use it to produce basic items such as food and clothes."
    female "There are also several VR rooms which should be able to replicate any environment on Earth, if you feel the need to relax."
    female "Those will require some skills to be programmed and also will consume quite a lot of energy though."
    mom "You sound like we will be stuck here for quite a long time, can't you help us get out of here?"
    female "We can't risk it. I won't send anyone to board the station and I definitely won't endanger the people on Earth just to get you out."
    female "I'm sorry, but this is all I can do for now."
    female "Over and out!"
    #mom and sis on comm
    sis "So... we are on our own..."
    mom "Looks like it."
    mom "Let's take a look at the rooms in this section"

label explore_station:

    scene control_room_1

    mom "I think we'll be able to access most of the section's functions from this control room."
    mom "We'll need to keep the solar panels outside the section in good shape, so we'll have enough energy to produce food and water."
    mom "And who knows, if we can get some blueprints, maybe some other items too."

    scene comm_1

    sis "I think I will never get used to the view from here"
    sis "It's so beautiful..."
    mom "We can use the comm room to contact Earth, but please keep the calls to a minimum - we don't want to alert M.A.L. to our presence."
    sis "Mom, there is also a VR projector here - if we manage to connect it to the comm station, we might be able to see who we are talking to."
    player "This should be easy! Let me take a look."
    mom "Not now! VR projections cost energy and we don't have enough to spare."
    player "OK mom..."
    sis "Let's see if we can find a place to sleep."

    scene shared_beds_1

    sis "Doesn't look like much, but I guess it will do..."
    mom "Lana, we should be thankful we are alive - the station crew is dead."
    sis crying "Dad..."
    mom sad "We don't know that. He is a smart man, he could have managed to escape somehow."
    player sad "Didn't you hear what Earth said? Everyone is dead."
    mom angry "Earth said they couldn't scan the station, so he might be alive somewhere."
    sis sad "I hope so!"
    mom "Anyway, lets keep exploring the section."

    scene mess_hall_1

    mom "This must be the energy processor that Earth told us about."
    sis "I guess this will be our dining room until we can get back to Earth."
    player "I wonder what else can this machine do..."
    mom "No time for this right now, we can check it out tomorrow."
    player "Sure, mom! Let's keep exploring!"

    scene bedroom_1

    sis amazed "Wow! What a nice room!"
    player "And there is even a mist-shower in it."
    mom "We can share it. I think the bed is big enough for all of us."
    player "Don't worry mom, I'll sleep in the bunk room. You and Lana can stay here."
    sis "No need for this, I'll move to the bunk room as well. As long as we can use the shower, you can have the room."
    sis smiling "And with dad probably alive, he'll share the bedroom with you once he manages to come back."
    mom smiling "Let's pray that he will!"

    scene vr_1

    player "I guess these are the VR rooms that are in this section."
    sis "Let's make a beach!"
    mom smiling "I miss the sun and the sea as well Lana, but keep in mind that we don't know how to program the room and even if we knew, we don't have the energy to sustain it."
    player "There are probably some tutorials on VR programming in the control center's computers."
    sis "You should check them out. I'm good with hardware, but when it comes to software..."
    mom "That's a good idea - we should split the tasks!"
    player "I will take the solar panel maintenance and if we can get enough energy stored in the batteries, we can even have one of the VR rooms working."
    sis "I can take care of the living quarters maintenance and the life support systems."
    mom "I guess that leaves food preparation and health monitoring to me."
    mom "OK, enough for today - let's go to bed and starting tomorrow, we each have our tasks to take care of."

    scene shared_beds_sis_1

    sis "Do you think dad is alive?"
    player "We can only hope that he is. Once we get this section running at 100\% and manage to open the section door, we will go out and look for him."
    sis "He's not your real dad, you don't have to risk your life to rescue him."
    player "Does this mean that you won't risk your life for my mom or me?"
    sis "You know I would!"
    player "And you should know that I would do anything for you or dad."
    sis "Do you promise?"
    player "I promise!"
    sis "Let's go to sleep..."
    player "Good night!"
    call activate_work_polish_panels from _call_activate_work_polish_panels
    call start_quest_simple_clothes from _call_start_quest_simple_clothes
    jump morning

label wait:
    $renpy.pause()
    if (quest_make_a_plan.finished and not quest_captured.active):
        jump captured_wake_up
    elif (quest_captured.finished):
        $quest_captured.finished = False
        jump reunited_start
    jump wait

label not_now:
    player "Maybe later..."
    jump map

label talk:
    hide screen station_rooms
    if (station.get_room(location).mom and station.get_room(location).sis):
        jump talk_mom_sis
    elif (station.get_room(location).mom):
        jump talk_mom
    elif (station.get_room(location).sis and talk_with_sis.has_topics()):
        jump talk_sis
    elif (station.get_room(location).rebecca):
        jump talk_rebecca
    else:
        player "I don't think I should be talking to myself..."
        jump map

label talk_mom:
    $select=None
    $topics = talk_with_mom.get_topics()
    $menu_items=[(topic.get_text(), topic) for topic in topics]
    $menu_items.append(("Nevermind", Topic("", "map", None, 0)))
    $select = menu(menu_items)
    $talk_with_mom.remove_topic(select)
    $renpy.jump(select.lbl)

label talk_sis:
    $select=None
    $topics = talk_with_sis.get_topics()
    $menu_items=[(topic.get_text(), topic) for topic in topics]
    $menu_items.append(("Nevermind", Topic("", "map", None, 0)))
    $select = menu(menu_items)
    $talk_with_sis.remove_topic(select)
    $renpy.jump(select.lbl)

label talk_mom_sis:
    $select=None
    $topics = talk_with_mom_sis.get_topics()
    $menu_items=[(topic.get_text(), topic) for topic in topics]
    $menu_items.append(("Nevermind", Topic("", "map", None, 0)))
    $select = menu(menu_items)
    $talk_with_mom_sis.remove_topic(select)
    $renpy.jump(select.lbl)

label talk_rebecca:
    $select=None
    $topics = talk_with_rebecca.get_topics()
    $menu_items=[(topic.get_text(), topic) for topic in topics]
    if not quest_meet_rebecca.meets_requirements(0):
        $menu_items.append(("Nevermind", Topic("", "map", None, 0)))
    $select = menu(menu_items)
    $talk_with_rebecca.remove_topic(select)
    $renpy.jump(select.lbl)

label call_earth:
    if (clock <= 2):
        player "Hello"
        player "..."
        player "No answer, I should try calling them later."
        jump wait_action
    else:
        jump call_earth_day

label show_help:
    hide screen station_rooms
    scene terminal
    show screen quest_help
    jump wait

label exit_help:
    hide screen quest_help
    jump jump_to_location

label call_earth_day:
    player "Anybody there?"
    female "This is a restricted line, identify yourself!"
    player "My name is Greg and I'm one of the survivors on station Antares."
    female "Please keep this line clear. M.A.L. might be monitoring the communications and we don't want it to know you are still alive."
    player "Is there anyone else alive on the station?"
    female "..."
    player "Hello?"
    female "..."
    player "{i}I think they hang up.{/i}"
    if (global_events.simple_clothes and global_events.player_knows_sis_lock_door):
        player "{i}The night shift might be more willing to chat.{/i}"
        if not quest_black_market.active:
            call start_quest_black_market from _call_start_quest_black_market
    jump wait_action

label terminal:
    hide screen station_rooms
    if talk_with_terminal.has_topics():
        $select=None
        $topics = talk_with_terminal.get_topics()
        $menu_items=[(topic.get_text(), topic) for topic in topics]
        $menu_items.append(("Nevermind", Topic("", "map", None, 0)))
        $select = menu(menu_items)
        $talk_with_terminal.remove_topic(select)
        $renpy.jump(select.lbl)
    elif (station.get_room("comm").player):
        jump call_earth
    else:
        player "Probably in the next version..."
        jump map

label wait_action:
    jump advance_time

label map:
    show screen station_rooms
    window hide
    jump wait

label reset_all_rooms:
    $station.reset()
    return

    # This ends the game.

    return
