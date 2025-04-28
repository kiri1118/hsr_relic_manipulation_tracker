import sys
from utilities import calc_shift, search_csv, DBConnect

usage = '''
    Here are the usage cases for the script:

    py main.py -add {relic_set} {relic_part} {main_stat} {stat_one} {stat_two} {stat_three} {stat_four} {key_stat}
    py main.py -remove {relic_set} {relic_part} {main_stat} {stat_one} {stat_two} {stat_three} {stat_four} {key_stat}
    py main.py -search {prev_updated_stat} {shifted_by}
    py main.py -searchall
'''

args = sys.argv[1:]
if not args:
    print(usage)
    sys.exit(1)
else:
    match args[0]:
        case "-add":
            if (len(args) < 9) or (len(args[8]) != 4):
                print(usage)
                sys.exit(1)
            db = DBConnect()
            key_one, key_two, key_three, key_four = args[8]
            db.add_to_relics(*args[1:8], key_one, key_two, key_three, key_four)

        case "-remove":
            if len(args) < 8:
                print(usage)
                sys.exit(1)
            db = DBConnect()
            db.remove_from_relics(*args[1:8])
        case "-search":
            if len(args) < 3:
                print(usage)
                sys.exit(1)
            db = DBConnect()
            start, shift = int(args[1]), int(args[2])
            key_stat = calc_shift(start, shift)
            column_names = ["key_one", "key_two", "key_three", "key_four"]
            db.search_db(column_names[key_stat - 1])
            
            # print(search_csv(column_names[key_stat - 1]))
        case "-searchall":
            db = DBConnect()
            db.search_db("", True)
        case _:
            print(usage)
            sys.exit(1)