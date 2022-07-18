
SKILL_MOD_NAME = [
    "dex",
    "wis",
    "int",
    "str",
    "cha",
    "int",
    "wis",
    "cha",
    "int",
    "wis",
    "int",
    "wis",
    "cha",
    "cha",
    "int",
    "dex",
    "dex",
    "wis"
    ]

class Character:
    def __init__():
        self.level = 0
        self.exp = 0
        self.class = "Fighter"
        self.race = "Human"
        self.alignment = 5
        self.maxHP = 1
        self.curHP = 1
        self.profMod = 2

        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0
        self.skillNames = [
            "Acrobatics",
            "Animal Handling",
            "Arcana",
            "Athletics",
            "Deception",
            "History",
            "Insight",
            "Intimidation",
            "Investigation",
            "Medicine",
            "Nature",
            "Perception",
            "Performance",
            "Persuasion",
            "Religion",
            "Sleight of Hand",
            "Stealth",
            "Survival"
        ]
        self.skillMod = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.skillProf = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

        self.coinPlatinum = 0
        self.coinGold = 0
        self.coinSilver = 0
        self.coinCopper = 0
        

    def claculateStats():
        self.strMod = int((self.str - 10) / 2)
        self.dexMod = int((self.dex - 10) / 2)
        self.conMod = int((self.con - 10) / 2)
        self.intMod = int((self.int - 10) / 2)
        self.wisMod = int((self.wis - 10) / 2)
        self.chaMod = int((self.cha - 10) / 2)

        for i in range(self.skillMod):
            switch SKILL_MOD_NAME[i]:
                case "str":
                    self.skillMod[i] = self.strMod + self.profMod if self.skillProf[i] else self.strMod
                    break
                case "dex":
                    self.skillMod[i] = self.dexMod + self.profMod if self.skillProf[i] else self.dexMod
                    break
                case "con":
                    self.skillMod[i] = self.conMod + self.profMod if self.skillProf[i] else self.conMod
                    break
                case "int":
                    self.skillMod[i] = self.intMod + self.profMod if self.skillProf[i] else self.intMod
                    break
                case "wis":
                    self.skillMod[i] = self.wisMod + self.profMod if self.skillProf[i] else self.wisMod
                    break
                case "cha":
                    self.skillMod[i] = self.chaMod + self.profMod if self.skillProf[i] else self.chaMod
                    break
                default:
                    self.skillMod[i] = 0
