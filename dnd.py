import math
import json


def modifier(attr):
    return math.floor((attr - 10) / 2)


def proficiencyBonus(value, xpMode=False):
    if xpMode:
        if value >= 355000:
            return +6
        elif value >= 305000:
            return +6
        elif value >= 265000:
            return +6
        elif value >= 225000:
            return +6
        elif value >= 195000:
            return +5
        elif value >= 165000:
            return +5
        elif value >= 140000:
            return +5
        elif value >= 120000:
            return +5
        elif value >= 100000:
            return +4
        elif value >= 85000:
            return +4
        elif value >= 64000:
            return +4
        elif value >= 48000:
            return +4
        elif value >= 34000:
            return +3
        elif value >= 23000:
            return +3
        elif value >= 14000:
            return +3
        elif value >= 6500:
            return +3
        elif value >= 2700:
            return +2
        elif value >= 900:
            return +2
        elif value >= 300:
            return +2
        else:
            return +2
    else:
        if value >= 20:
            return +6
        elif value >= 17:
            return +6
        elif value >= 13:
            return +5
        elif value >= 9:
            return +4
        elif value >= 5:
            return +3
        else:
            return +2



class character:
    def __init__(self, name, classes, background, race, alignment, xp, abScores, savingProfs, regProfs, miscProfs, ac,
                 initiative, speed, hpMax, hp, tempHp, hitDice, dSaves, cp, sp, ep, gp, pp, equipment, pTraits, ideals, bonds, flaws, features):

        self.sheet = self.sheet(self)
        self.name = name
        self.classes = classes
        self.totalLevel = 0
        for c, l in self.classes.items():
            self.totalLevel += l
        self.background = background
        self.race = race
        self.alignment = alignment
        self.xp = xp

        self.str = abScores[0]
        self.dex = abScores[1]
        self.con = abScores[2]
        self.int = abScores[3]
        self.wis = abScores[4]
        self.cha = abScores[5]

        self.savingProfs = savingProfs
        self.regProfs = regProfs
        self.miscProfs = miscProfs
        self.profBonus = proficiencyBonus(self.totalLevel)
        self.passivePerception = 0
        self.passivePerception += modifier(self.wis)
        if "Perception" in regProfs:
            self.passivePerception += self.profBonus

        self.ac = ac
        self.initiative = initiative
        self.speed = speed
        self.hpMax = hpMax
        self.hp = hp
        self.tempHp = tempHp
        self.hitDice = hitDice
        self.dSaves = dSaves

        self.cp = cp
        self.sp = sp
        self.ep = ep
        self.gp = gp
        self.pp = pp
        self.equipment = equipment

        self.pTraits = pTraits
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws

        self.features = features

    def __str__(self):
        return self.name

    class sheet:
        def __init__(self, char):
            self.character = char

        def __str__(self):
            lines = []
            lines.append("=======================================")
            lines.append("          CHARACTER SHEET              ")
            lines.append("=======================================")
            lines.append(f"Name: {self.character.name}")
            lines.append("Classes: ")
            for c, l in self.character.classes.items():
                lines.append(f"  - {c}: Level {l}")
            lines.append(f"Level: {self.character.totalLevel}")
            lines.append(f"Background: {self.character.background}")
            lines.append(f"Race: {self.character.race}")
            lines.append(f"Alignment: {self.character.alignment}")
            lines.append(f"XP: {self.character.xp}")

            lines.append("=======================================")
            lines.append("                STATS                  ")
            lines.append("=======================================")
            lines.append("--------        --------        -------")
            lines.append("|      |        |      |        |     |")
            lines.append(
                f"|  {modifier(self.character.str):<2}  |        |  {modifier(self.character.dex):<2}  |        |  {modifier(self.character.con):<2} |")
            lines.append("|      |        |      |        |     |")
            lines.append("--------        --------        -------")
            lines.append(
                f"  [{self.character.str}]            [{self.character.dex:<2}]            [{self.character.con:<2}] ")
            lines.append("STRENGTH        DEXTERITY  CONSTITUTION")
            lines.append("--------        --------        -------")
            lines.append("|      |        |      |        |     |")
            lines.append(
                f"|  {modifier(self.character.int):<2}  |        |  {modifier(self.character.wis):<2}  |        |  {modifier(self.character.cha):<2} |")
            lines.append("|      |        |      |        |     |")
            lines.append("--------        --------        -------")
            lines.append(
                f"  [{self.character.int}]            [{self.character.wis:<2}]            [{self.character.cha:<2}] ")
            lines.append("INTELLIGENCE     WISDOM         Charisma")

            lines.append("=======================================")
            lines.append("            Proficiencies              ")
            lines.append("=======================================")
            lines.append(f"[{self.character.profBonus}] Proficiency Bonus")
            lines.append("Saving Throws: ")
            for p in self.character.savingProfs:
                lines.append(f"  - {p}")
            lines.append("Skills: ")
            for p in self.character.regProfs:
                lines.append(f"  - {p}")
            lines.append("Other Proficiencies & Languages: ")
            for p in self.character.miscProfs:
                lines.append(f"  - {p}")
            lines.append(f"[{self.character.passivePerception}] Passive Wisdom (Perception)")

            lines.append("=======================================")
            lines.append("                Stats                  ")
            lines.append("=======================================")
            lines.append("--------        --------        -------")
            lines.append("|      |        |      |        |     |")
            lines.append(
                f"|  {self.character.ac}  |        |  {self.character.initiative}  |        | {self.character.speed}  |")
            lines.append("|      |        |      |        |     |")
            lines.append("--------        --------        -------")
            lines.append("   AC         INITITIATIVE       SPEED ")
            lines.append("---------------------------------------")
            lines.append(f"Max Hit Points: {self.character.hpMax}")
            lines.append('')
            lines.append(f"Current Hit Points: {self.character.hp}")
            lines.append("---------------------------------------")
            lines.append(f"Hit Dice d{self.character.hitDice}")
            lines.append('')
            lines.append("Saving Throws:")
            savingThrows = str(self.character.dSaves)
            savingThrows = savingThrows.replace("'", '')
            savingThrows = savingThrows.replace(",", '')
            savingThrows = savingThrows.replace("[", '', 1)
            savingThrows = savingThrows.rstrip("]")
            savingThrows += ']'
            lines.append(savingThrows)

            lines.append("=======================================")
            lines.append("              Inventory                ")
            lines.append("=======================================")
            lines.append(f"CP: {self.character.cp}")
            lines.append(f"SP: {self.character.sp}")
            lines.append(f"EP: {self.character.ep}")
            lines.append(f"GP: {self.character.gp}")
            lines.append(f"PP: {self.character.pp}")
            lines.append('')
            lines.append("Equipment:")
            for item in self.character.equipment:
                lines.append(f"  - {item}")

            lines.append("=======================================")
            lines.append("                About                  ")
            lines.append("=======================================")
            lines.append("Personality Traits:")
            for trait in self.character.pTraits:
                lines.append(f"  - {trait}")
            lines.append("Ideals:")
            for ideal in self.character.ideals:
                lines.append(f"  - {ideal}")
            lines.append("Bonds:")
            for bond in self.character.bonds:
                lines.append(f"  - {bond}")
            lines.append("Flaws:")
            for flaw in self.character.flaws:
                lines.append(f"  - {flaw}")

            lines.append("=======================================")
            lines.append("           Features & Traits           ")
            lines.append("=======================================")
            for feature in self.character.features:
                lines.append(f"- {feature}")

            return '\n'.join(lines)

        def exportJson(self, filePath="character_sheet.json"):
            data = {
                "name": self.character.name,
                "classes": self.character.classes,
                "totalLevel": self.character.totalLevel,
                "background": self.character.background,
                "race": self.character.race,
                "alignment": self.character.alignment,
                "xp": self.character.xp,
                "str": self.character.str,
                "dex": self.character.dex,
                "con": self.character.con,
                "int": self.character.int,
                "wis": self.character.wis,
                "cha": self.character.cha,
                "savingProfs": self.character.savingProfs,
                "regProfs": self.character.regProfs,
                "miscProfs": self.character.miscProfs,
                "profBonus": self.character.profBonus,
                "passivePerception": self.character.passivePerception,
                "ac": self.character.ac,
                "initiative": self.character.initiative,
                "speed": self.character.speed,
                "hpMax": self.character.hpMax,
                "hp": self.character.hp,
                "tempHp": self.character.tempHp,
                "hitDice": self.character.hitDice,
                "dSaves": self.character.dSaves,
                "cp": self.character.cp,
                "sp": self.character.sp,
                "ep": self.character.ep,
                "gp": self.character.gp,
                "pp": self.character.pp,
                "equipment": self.character.equipment,
                "pTraits": self.character.pTraits,
                "ideals": self.character.ideals,
                "bonds": self.character.bonds,
                "flaws": self.character.flaws,
                "features": self.character.features
            }
            with open(filePath, 'w') as file:
                json.dump(data, file)

        def importJson(self, filePath="character_sheet.json"):
            with open(filePath, 'r') as file:
                data = json.load(file)

            return character(
                data["name"],
                data["classes"],
                data["background"],
                data["race"],
                data["alignment"],
                data["xp"],
                [
                    data["str"],
                    data["dex"],
                    data["con"],
                    data["int"],
                    data["wis"],
                    data["cha"]
                ],
                data["savingProfs"],
                data["regProfs"],
                data["miscProfs"],
                data["ac"],
                data["initiative"],
                data["speed"],
                data["hpMax"],
                data["hp"],
                data["tempHp"],
                data["hitDice"],
                data["dSaves"],
                data["cp"],
                data["sp"],
                data["ep"],
                data["gp"],
                data["pp"],
                data["equipment"],
                data["pTraits"],
                data["ideals"],
                data["bonds"],
                data["flaws"],
                data["features"]
            )

