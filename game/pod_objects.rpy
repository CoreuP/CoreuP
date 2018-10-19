init python:
    class PodPlayer:
        def __init__(self):
            self.came = False
            self.stress = 20
            self.equation = 15
            self.arousal = 0

        def add_stress(self, value):
            self.stress += value
            if (self.stress > 100):
                self.stress = 100
            if (self.stress < 0):
                self.stress = 0

        def add_arousal(self, value):
            self.arousal += value
            if (self.arousal > 100):
                self.arousal = 100
            if (self.arousal < 0):
                self.arousal = 0

        def add_equation(self, value):
            self.equation += value
            if (self.equation > pod_equation_cap):
                self.equation = pod_equation_cap
            if (self.equation < 0):
                self.equation = 0

    class PodCharacter:
        def __init__(self, name):
            self.name = name
            self.arousal = 20
            self.angry = 20
            self.love = 20

        def add_arousal(self, value):
            self.arousal += value
            if (self.arousal > 100):
                self.arousal = 100
            if (self.arousal < 0):
                self.arousal = 0

        def add_angry(self, value):
            self.angry += value
            if (self.angry > 100):
                self.angry = 100
            if (self.angry < 0):
                self.angry = 0

        def add_love(self, value):
            self.love += value
            if (self.love > 100):
                self.love = 100
            if (self.love < 0):
                self.love = 0

    class Room2:
        def __init__(self, name):
            self.name = name
            self.people = []

        def clear(self):
            self.people = []

        def put(self, name):
            if name not in self.people:
                self.people.append(name)

        def has(self, name):
            if name in self.people:
                return True
            else:
                return False

    class PodStation:
        def __init__(self):
            self.rooms = []
            self.rooms.append(Room2("pod"))
            self.rooms.append(Room2("bedroom"))
            self.rooms.append(Room2("bunk"))
            self.rooms.append(Room2("outpost"))
            self.rooms.append(Room2("lab"))

        def clear(self):
            for room in self.rooms:
                room.clear()

        def get(self, name):
            for room in self.rooms:
                if room.name == name:
                    return room

    class PodQuest:
        def __init__(self):
            self.time = "void"
            self.arousal = -1
            self.equation = -1
            self.stress = -1
            self.phase = 0
            self.started = False

        def reset(self):
            self.time = "void"
            self.arousal = -1
            self.equation = -1
            self.stress = -1

        def advance_phase(self):
            self.reset()
            self.phase += 1

        def meets_requirements(self, phase):
            if (not self.started or self.phase != phase):
                return False
            if (self.time != "void" and self.time != pod_time_text):
                return False
            if (self.arousal != -1 and self.arousal > pod_player.arousal):
                return False
            if (self.equation != -1 and self.equation > pod_player.equation):
                return False
            if (self.stress != -1 and self.stress > pod_player.stress):
                return False
            return True
