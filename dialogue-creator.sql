.open dialogue.db

DROP TABLE IF EXISTS root_dialogues;
CREATE TABLE root_dialogues AS 
    SELECT "new_horizons" AS version, 
           "Might there be something with which I can assist you?" AS dialogue UNION
    SELECT "new_leaf",
           "Hoo! How may I be of service?" UNION
    SELECT "city_folk",
           "Hoo there! Welcome to the museum. Make yourself at home, won't you?" UNION
    SELECT "wild_world",
           "Might there be something with which I can assist you?" UNION
    SELECT "animal_crossing",
           "Welcome! Please, do come in! It's so very nice to see you!";

-- To see how all the animal descriptions were found, see:
-- https://github.com/pangene/acwiki-scraper

-- This little sql file is only for really small pieces of dialogue that I manually
-- add or change.

-- If you find an error in the dialogue, let me know! Or fix it yourself here.