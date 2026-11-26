

infiltration = "relies on stealth , manipulation, and agile combat"
combat = " highly skill spy and assasin combining acrobatic martial arts"
marksmanship =  "relies on precision shooting, agility, and tactical positioning"
tech = "possess expert level intellingence, and hacking abilities"
reflex = "known for fast reaction time"
adaptability = "known for adapt quickly through battles"
baleful_omen = "dealing initial aoe electro dmg"
musou_shintetsu = "unleashing an aoe electro strike"
raiden_shogun = [baleful_omen,musou_shintetsu]
leon = [marksmanship,combat,reflex,adaptability]
ada = [combat,marksmanship,infiltration,tech]
resident_evil_4 = [leon,ada]
genshin_impact = [raiden_shogun]
open_world = [genshin_impact,resident_evil_4]
game_type = {"open world")


print(game_type,["open world"], [4],[3],[0])
