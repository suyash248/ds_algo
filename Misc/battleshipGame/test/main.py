from src.service.battle import Battle
from src.util.commons import to_index
import settings

# Sample input -
# 5 E                               - battlearea dimensions for each player
# 2                                 - number of battleships
# Q 1 1 A1 B2                       - battleship size and co-ordinates for both players
# P 2 1 D4 C3
# A1 B2 B2 B3                       - missiles locations for player-1
# A1 B2 B3 A1 D1 E1 D4 D4 D5 D5     - missiles locations for player-2

def parse_and_start():
    """
    Testing the sample input present under `/test/input.txt` file.
    :return:
    """
    input_file = settings.project_root + '/test/input.txt'
    with open(input_file, "r") as lines:
        battlearea_dimensions = lines.next()
        battleship_count = int(lines.next())

        battleships_size_locs_list = []
        for i in range(0, battleship_count):  # battleship size and co-ordinates for both players
            bs_attrs = lines.next().strip().split(" ")  # P 2 1 D4 C3
            battleships_size_locs_list.append({
                "bs_type": bs_attrs[0],  # P or Q
                "bs_width": int(bs_attrs[1]),  # col
                "bs_height": int(bs_attrs[2]),  # row
                "bs_loc": {
                    "p1": (to_index(bs_attrs[3][0]), int(bs_attrs[3][1])),  # (y, x) -> (row, col)
                    "p2": (to_index(bs_attrs[4][0]), int(bs_attrs[4][1]))  # (y, x) -> (row, col)
                }
            })

        target_missile_locs_p1 = map(lambda tm: tm.strip(), lines.next().split(" "))  # A1 B2 B2 B3
        target_missile_locs_p2 = map(lambda tm: tm.strip(), lines.next().split(" "))  # A1 B2 B3 A1 D1 E1 D4 D4 D5 D5

        # battlearea attributes...
        battlearea_dimensions = battlearea_dimensions.split(" ")
        ba_width = int(battlearea_dimensions[0].strip())
        ba_height = battlearea_dimensions[1].strip()

        battle = Battle((ba_width, ba_height), battleships_size_locs_list,
                        (target_missile_locs_p1, target_missile_locs_p2),
                        p1_uid=1, p2_uid=2)
        battle.start()

if __name__ == '__main__':
    parse_and_start()