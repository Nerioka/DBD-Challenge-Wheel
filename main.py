import discord
import os
import random
from keep_alive import keep_alive

keep_alive()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!surv'):
        challenge_surv = [
          "Les survivants doivent completer un gen en équipe. Tout le monde doit être présent pour sa complétion",

          "Les survivants doivent designer un joueur qui ne peut pas être soigner autrement que par 'Self-Care' ou 'Inner Strength'. Soigner pour relever est une exception",

          "Les survivants doivent étourdir le tueur avec head on 4 fois",

          "Les survivants doivent réussir une Dumb tech",

          "Tous les survivants doivent prendre au moins un coup pour un autre survivant en chase",

          "Chaque survivant doit purifier un totem pour pouvoir sortir",

          "Les survivants doivent intentionnellement ce 3 gen",

          "Aucun survivants n'a le droit de partir sans que les deux portes soient ouvertes",

          "Les survivants doivent relever 4 palettes tombées lors d'une chase",

          "Désigner un survivant qui aura des poux. Ce survivant ne peux toucher aucun autre survivants hormis par nécessité (décrochage ou relever). Les poux se transmettent dans si nécessité il y a eu, le survivant ayant les poux doit sortir en dernier",
          
          "Désigner un survivant qui ne pourra pas effectuer ses skill checks jusqu'a ce que 3 generateurs soient réparés",

          "Les survivants doivent utiliser la perk 'Diversion' pour jeter 8 cailloux dans le visage du tueur",

          "Les survivants doivent trouver un objet de rareté violette ou mieux, au moins un survivant doit s'échapper avec cet objet",

          "Les survivants doivent crafter 5 flash et les jeter sur le point le plus haut de la map",

          "Les survivants doivent terminer un generateur par gen-tapping",

          "Désigner un survivant pour être le mastodonte, ce survivant doit faire tomber chaque palettes sur lequelles il court",

          "Les survivants doivent forcer le tueur à ouvrir 2 armoires vides en utilisant la perk 'Deception'",

          "Désigner un survivant qui doit jouer les yeux bandés jusqu'a la complétion du premier generateur",

          "Les survivants ne peuvent jeter aucune palettes tant que le premier generateur n'est pas fini",

          "Désigner un survivant pour être le president, Ce survivant doit absolument s'échapper",

          "Les survivants doivent fouiller tous les coffres avant que chaque survivant ait été accroché. Tous les survivants doivent apporter comme offrande Shiny Coin",

          "Désigner un survivant, les trois autres doivent sandbag au moins une fois ce survivant",

          "Les survivants doivent fouiller tous les coffres et rassembler les objets dans le basement, tous les survivants doivent utiliser la perk 'Appraisal'",

          "Les survivants doivent sonner le tueur 2 fois avec la perk 'Blast Mine'",

          "Les survivants ne peuvent purifier aucun totem",

          "Un survivant doit se sauver tout seul avec la perk 'Power Struggle'",

          "A partir du 4ème générateur pas plus d'un survivant par générateur",

          "Les survivants doivent se séparer en deux groupe de deux amis, Les survivants ne peuvent être soignés que par leurs amis",

          "Un survivant doit kobe uniquement par la chance, la perk 'Deliverance' est exclue",

          "Désigner un survivant qui jouera à la manette et survivre 3 générateurs OU jouer avec les touches inversés et survivre 2 générateurs",

          "Tous les survivants doivent faire un tour de la map en longeant les bords",

          "Les survivants doivent sonner le tueur 8 fois peu importe la façon",

          "Désigner un survivant qui utilisera la perk 'Urban Evasion'. Ce survivant ne doit pas être accroché avant la complétion de 3 générateurs",

          "Au moins 2 survivants doivent s'échapper du tueur par wiggle",

          "Les survivants ne peuvent pas choisir leurs perk, le hasard le fera",

          "Tous les survivants doivent utiliser 'Autodidact' et avoir le maximum de stack avant de s'enfuir",

          ]
        await message.author.send("Le challenge est : {}!".format(random.choice(challenge_surv)))
    if message.content.startswith('!tueur'):
        challenge_tueur = [

          "Le tueur n'a pas le droit de taper les générateurs",

          "Le tueur ne peut pas ouvrir les placards",

          "Le tueur doit casser tous les murs",

          "Le tueur ne peut pas casser les palettes lors d'un nombre pair de générateurs restants",

          "Le tueur n'a pas le doit d'accéder à la shack",

          "Si une palette tombe, le tueur doit la casser immédiatement",

          "Le tueur ne peut pas slug et doit ramasser immédiatement un survivant",

          "Le tueur ne peut pas frapper plusieurs survivants, une fois qu'un survivant est blessé le tueur doit le mettre au crochet avant de pouvoir blesser un autre survivant",

          "Le tueur ne peut pas choisir ses perk, le hasard le fera",
          
          "Le tueur doit mettre un addon négatif (à bloodpoint)",

          "Avec 'Play With Your Food', le tueur doit dépasser 2 fois un survivant et lui mettre un coup",
          
          "Tous les survivants doivent devenir au moins une fois votre obsession",

          "Avec 'Franklin's Demise' aucun survivant ne doit s'enfuir avec des objets",

          "Le tueur doit attraper au moins 2 fois un survivant (Les pièges du Trapper fonctionne)",

          "Le tueur doit mettre à terre 3 fois en exposant les survivants (tous les moyens sont permis, perks, pouvoir de tueur...)",
          

          ]
        await message.author.send("Le défi est : {}!".format(random.choice(challenge_tueur)))
    if message.content.startswith('!roulette_surv'):
      surv_perks = [
      "Ace in the hole",
      "Adrenaline",
      "Aftercare",
      "Alert",
      "Any Means Necessary",
      "Appraisal",
      "Autodidact",
      "Babysitter",
      "Balanced Landing",
      "Better Together",
      "Bite the Bullet",
      "Blast Mine",
      "Blood Pact",
      "Boil Over",
      "Bond",
      "Borrowed Time",
      "Botany Knowledge",
      "Breakdown",
      "Breakout",
      "Buckle Up",
      "Built to Last",
      "Calm Spirit",
      "Camaraderie",
      "Counterforce",
      "Dance With Me",
      "Dark Sense",
      "Dead Hard",
      "Deception",
      "Decisive Strike",
      "Déjà Vu",
      "Deliverance",
      "Desperate Measures",
      "Detective's Hunch",
      "Distortion",
      "Diversion",
      "Empathy",
      "Fast Track",
      "Fixated",
      "Flashbang",
      "Flip-Flop",
      "For The People",
      "Head On",
      "Hope",
      "Inner Strength",
      "Iron will",
      "Kindred",
      "Leader",
      "Left Behind",
      "Lightweight",
      "Lithe",
      "Lucky Break",
      "Mettle Of Man",
      "No Mither",
      "No One Left Behind",
      "Object of Obsession",
      "Off The Record",
      "Open-Handed",
      "Pharmacy",
      "Plunderer's Instinct",
      "Poised",
      "Power Struggle",
      "Premonition",
      "Prove Thyself",
      "Quick & Quiet",
      "Red Herring",
      "Repressed Alliance",
      "Resilience",
      "Resurgence",
      "Rookie Spirit",
      "Saboteur",
      "Second Wind",
      "Self-Care",
      "Self-Preservation",
      "Slippery Meat",
      "Small Game",
      "Smash Hit",
      "Sole Survivor",
      "Solidarity",
      "Soul Guard",
      "Spine Chill",
      "Sprint Burst",
      "Stake Out",
      "Streetwise",
      "Technician",
      "Tenacity",
      "This Is Not Happening",
      "Up The Ante",
      "Unbreakable",
      "Urban Evasion",
      "Vigil",
      "Visionary",
      "Wake Up",
      "We'll Make It",
      "We're Gonna Live Forever",
      "Windows Of Opportunity",
      ] 
      await message.author.send("Tes perks sont : {}\n Bonne chance :)".format(random.sample(surv_perks,10)))

    if message.content.startswith('!roulette_tueur'):
      killer_perks = [

      "A Nurse's Calling",
      "Agitation",
      "Bamboozle",
      "Barbecue & Chilli",
      "Beast of Prey",
      "Bitter Murmur",
      "Blood Echo",
      "Blood Warden",
      "Bloodhound",
      "Brutal Strength",
      "Corrupt Intervention",
      "Coulrophobia",
      "Coup de Grâce",
      "Cruel Limits",
      "Dark Devotion",
      "Dead Man's Switch",
      "Deathbound",
      "Deerstalker",
      "Discordance",
      "Distressing",
      "Dragon's Grip",
      "Dying Light",
      "Enduring",
      "Eruption",
      "Fire Up",
      "Forced Penance",
      "Franklin's Demise",
      "Furtive Chase",
      "Gearhead",
      "Hangman's Trick",
      "Hex:Blood Favour",
      "Hex:Crowd Control",
      "Hex:Devour hope",
      "Hex:Haunted Ground",
      "Hex:Huntress Lullaby",
      "Hex:No One Escapes Death",
      "Hex:Retribution",
      "Hex:Ruin",
      "Hex:The Third Seal",
      "Hex:Thrill of the Hunt",
      "Hex:Undying",
      "Hoarder",
      "Hysteria",
      "I'm All Ears",
      "Infectious Fright",
      "Insidious",
      "Iron Grasp",
      "Iron Maiden",
      "Knock Out",
      "Lethal Pursuer",
      "Lightborn",
      "Mad Grit",
      "Make Your Choice",
      "Mindbreaker",
      "Monitor & Abuse",
      "Monstrous Shrine",
      "Nemesis",
      "No Way out",
      "Oppresion",
      "Overcharge",
      "Overwhelming Presence",
      "Play with Your Food",
      "Pop Goes the Weasel",
      "Predator",
      "Rancor",
      "Remember Me",
      "Save the Best for Last",
      "Shadowborn",
      "Sloppy Butcher",
      "Spies from the Shadows",
      "Spirit Fury",
      "Starstruck",
      "Stridor",
      "Surge",
      "Surveillance",
      "Territorial Imperative",
      "Thanatophobia",
      "Thrilling Tremors",
      "Tinkerer",
      "Trail of Torment",
      "Unnerving Presence",
      "Unrelenting",
      "Whispers",
      "Zanshin Tactics",
    ]
      await message.author.send("Tes perks sont : {}\n Bonne chance :)".format(random.sample(killer_perks,10)))

client.run(os.getenv('TOKEN'))