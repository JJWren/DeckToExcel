# "1x Academy Rector (UDS)\r\n1x Adarkar Wastes (7ED)\r\n1x Ajani Steadfast (M15) *F*\r\n1x Ajani Unyielding (AER) *F*\r\n1x Ancient Tomb (V12) *F*\r\n1x Atraxa, Praetors' Voice (C16) *F* *CMDR*\r\n1x Basalt Monolith (C15)\r\n1x Bloodstained Mire (KTK)\r\n1x Breeding Pool (GTC)\r\n1x Canopy Vista (BFZ) *F*\r\n1x Catastrophe (USG)\r\n1x Chromatic Lantern (MPS) *F*\r\n1x City of Brass (MMA)\r\n1x Command Tower (C15)\r\n1x Constant Mists (STH)\r\n1x Cyclonic Rift (RTR)\r\n1x Deepglow Skate (C16)\r\n1x Demonic Tutor (3ED)\r\n1x Doubling Season (000) *F*\r\n1x Dovin Baan (KLD)\r\n1x Elspeth, Knight-Errant (DDF) *F*\r\n1x Elspeth, Sun's Champion (DDO) *F*\r\n1x Enlightened Tutor\r\n1x Exotic Orchard (CN2)\r\n1x Farseek (000) *F*\r\n1x Fetid Heath (EVE)\r\n1x Flooded Grove (EXP) *F*\r\n1x Flooded Strand (KTK)\r\n2x Forest (UNH)\r\n1x Garruk, Apex Predator (M15) *F*\r\n1x Gilded Lotus (V13) *F*\r\n1x Godless Shrine (GTC)\r\n1x Hallowed Fountain (RTR)\r\n1x Humility (TMP)\r\n2x Island (UNH)\r\n1x Jace, Architect of Thought (DDM) *F*\r\n1x Jace, the Mind Sculptor (V13) *F*\r\n1x Karmic Justice (C15)\r\n1x Karn Liberated (NPH)\r\n1x Lethal Vapors (SCG) *F*\r\n1x Liliana Vess (M11)\r\n1x Mana Confluence (EXP) *F*\r\n1x Mana Crypt (EMA)\r\n1x Mana Reflection (SHM)\r\n1x Mana Vault (3ED)\r\n1x Merciless Eviction (GTC) *F*\r\n1x Mirari's Wake (CMA) *F*\r\n1x Mystical Tutor (V09) *F*\r\n1x Narset Transcendent (DTK)\r\n1x Nissa, Vital Force (KLD)\r\n1x Norn's Annex (NPH) *F*\r\n1x Ob Nixilis Reignited (DDR) *F*\r\n1x Overburden (PCY) *F*\r\n1x Overgrown Tomb (RTR)\r\n1x Paradox Engine (KLD)\r\n2x Plains (UNH)\r\n1x Polluted Delta (KTK)\r\n1x Prairie Stream (BFZ) *F*\r\n1x Prismatic Omen (SHM)\r\n1x Privileged Position (RAV)\r\n1x Reflecting Pool (CNS)\r\n1x Reliquary Tower (000) *F*\r\n1x Rhystic Study (PCY)\r\n1x Rings of Brighthearth (LRW)\r\n1x Sensei's Divining Top (V09) *F*\r\n1x Skyshroud Claim\r\n1x Sol Ring (V10) *F*\r\n1x Sorin Markov (ZEN)\r\n1x Sorin, Grim Nemesis (SOI)\r\n1x Sphere of Safety (RTR) *F*\r\n1x Spike Weaver (EXO)\r\n1x Sterling Grove (INV)\r\n1x Sunken Hollow (BFZ) *F*\r\n1x Sunken Ruins (SHM)\r\n1x Supreme Verdict (RTR) *F*\r\n2x Swamp (UNH)\r\n1x Sylvan Library (EMA)\r\n1x Tamiyo, Field Researcher (EMN)\r\n1x Tamiyo, the Moon Sage (AVR)\r\n1x Teferi, Temporal Archmage (C14)\r\n1x Temple Garden (RTR)\r\n1x Terminus (V14) *F*\r\n1x Tezzeret the Seeker (DDF) *F*\r\n1x Tithe (VIS)\r\n1x Toxic Deluge (EMA)\r\n1x Traverse the Ulvenwald (SOI)\r\n1x Twilight Mire (EVE)\r\n1x Ugin, the Spirit Dragon (FRF)\r\n1x Urborg, Tomb of Yawgmoth (V12) *F*\r\n1x Vampiric Tutor (VIS)\r\n1x Venser, the Sojourner (DDI) *F*\r\n1x Watery Grave (RAV)\r\n1x Windswept Heath (KTK)\r\n1x Wooded Bastion (SHM)\r\n1x Wooded Foothills (KTK)\r\n1x Yawgmoth's Will (USG)"

import os
import re
from genericpath import exists
from prettytable import PrettyTable

# AtraxaSuperfriends.txt


class DeckRecord:
    def __init__(self, quantity, name, edition, is_foil):
        self.quantity = quantity
        self.name = name
        self.edition = edition
        self.is_foil = is_foil


ptable = PrettyTable()
ptable.field_names = ["Quantity", "Card Name", "Edition", "Is Foil"]
complete_deck = []

try:
    directory = os.path.abspath(os.getcwd())
    filepath = input(
        f'Please enter the file name with extension (eg: "deckname.txt"): ')
    fullpath = f'{directory}\\{filepath}'
    deck_name = filepath[:-4]
    ptable.title = deck_name
except Exception as e:
    print(f'\r\nSomething with the path went wrong...\n\t[ERROR]: {e}')

print(f'\r\nThe path you gave: {fullpath}')

if exists(fullpath):
    with open(fullpath) as file:
        lines = file.readlines()

        for line in lines:
            line_stripped = line.rstrip()

            quantity = re.search("[0-9]+[x]", line_stripped).group()
            quantity = quantity[:-1]

            name = re.search("[x ]+[a-zA-Z,' \-]+\(", line_stripped).group()
            name = name[2:]
            name = name[:-2]

            if re.search("\(+[A-Z0-9]+\)", line_stripped):
                edition = re.search("\(+[A-Z0-9]+\)", line_stripped).group()
            else:
                edition = None

            if re.search("\*+F+\*", line_stripped):
                is_foil = True
            else:
                is_foil = False

            dr = DeckRecord(quantity, name, edition, is_foil)

            complete_deck.append(dr)

            ptable.add_row([quantity, name, edition, is_foil])

    print(ptable.get_string())

    with open(f'{directory}\\{deck_name}.csv', 'w') as new_file:
        new_file.write(ptable.get_csv_string())

else:
    print('That path does not exist.')
