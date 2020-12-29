.open dialogue.db

DROP TABLE IF EXISTS root_dialogues;
CREATE TABLE root_dialogues AS 
    SELECT "new_horizons" AS version, 
           "Might there be something with which I can assist you?" AS dialogue ;
    --        UNION
    -- SELECT "new_leaf",
    --        "Unavailable" UNION
    -- SELECT "city_folk",
    --        "Unavailabe" UNION
    -- SELECT "wild_world",
    --        "Unavailabe" UNION
    -- SELECT "gamecube",
    --        "Unavailabe" UNION

DROP TABLE IF EXISTS new_horizons_bugs;
CREATE TABLE new_horizons_bugs AS
    SELECT "Common butterfly" AS bug, 
        "The common butterfly would have you believe it is but a beautiful friend flitting prettily about the flowers. Bah, I say! They may seem innocent things with their pretty white wings, but they hide a dark side! The common butterfly caterpillar is called a cabbage worm, you see, and it's a most voracious pest. The ravenous beasts chew through cabbage, broccoli, kale and the like with a devastating gusto. And my feathers! Their green coloring is truly GROSS! A hoo-rrific hue, I say." AS description UNION
    SELECT "Yellow buttefly",
        "Allow me to enlighten you... The yellow butterfly is named for its yellow wings. Need I say more? If I must, then allow me to note that the female yellow butterfly can lay up to 600 eggs at a time! Bleech! And their creepy crawly caterpillars just love to chomp on clover plants. A recipe for disaster, I say. Just imagine reaching for a four-leaf clover, only to touch a larva instead! Yuck! The worst of luck!" UNION
    SELECT "Tiger buttefly",
        "Tiger butterflies are known for their majestic wings, which many consider quite beautiful. Truth be told, I find them monstrous! Those strange striped patterns... They give this owl the goose bumps! And while you may imagine young tiger butterfly larvae to look like lovely green caterpillars... it's not so! Why, when tiger butterflies are but babes, they're covered in unsightly white, brown, and black spots. In this way, they camouflage themselves as...as...bird droppings! Putrid pests, indeed!" UNION
    SELECT "Peacock buttefly",
        "Pretty as a peacock? Bah, I say! The wings of the peacock butterfly may have a pattern similar to that of the beautiful bird... But its forewings are also covered in a dark, velvety hair! You heard right! HAIRY wings! A hair-raising revelation indeed!";