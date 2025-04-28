# hsr_relic_manipulation_tracker
This is a complementary tool for upgrading relics in HSR. It helps keep track of relics that are potentially interesting to upgrade with the relic manipulation method. It is NOT usable without understanding the idea behind relic manipulation by pattern.

# Script Usage
This adds the relic of interest into the SQLite DB:

    py main.py -add {relic_set} {relic_part} {main_stat} {stat_one} {stat_two} {stat_three} {stat_four} {key_stat}

This removes the relic from SQLite DB as it is no longer of interest:

    py main.py -remove {relic_set} {relic_part} {main_stat} {stat_one} {stat_two} {stat_three} {stat_four} {key_stat}

This searches the DB for interesting relics to upgrade based on the pattern method for relic upgrade manipulation:

    py main.py -search {prev_updated_stat} {shifted_by}

This fetches all the relics that are currently stored in the DB:

    py main.py -searchall

# Input Args
**relic_set**: Any name of your choice

**relic_part**: Any name of your choice

**main_stat**: Any name of your choice

**stat_one**: Any name of your choice

**stat_two**: Any name of your choice

**stat_three**: Any name of your choice

**stat_four**: Any name of your choice

**key_stat**: Four digit number that consists of only 0s and 1s. Each digit represent whether or not the corresponding substat is important. For example, 1010 means the first and third substat (stat_one and stat_three) are desirable upgrades.

**prev_updated_stat**: A number 1-4 that represent the LAST substat that was just upgraded.

**shifted_by**: x is the last substat that got upgraded and y is the next substat that is likely to get upgraded, both between 1-4. This value is calculated by how many rightward shifts are required for x to get to the y position on an infinite and continuous sequence of 12341234... For example, if x is 4 and y is 3, this value would be 3. If x is 3 and y is 1, this value would be 2.

