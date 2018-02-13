from src.entity.battlearea.battlearea import BattleArea
from src.entity.player.player import Player
from src.util.commons import get_battlearea_location


class Battle(object):

    def __init__(self, battlearea_dimensions, battleships_size_locs_list, missile_locs, p1_uid=None, p2_uid=None):
        """
        Instantiates players and Initializes `BattleArea`, `BattleShips` and `MissileTargets` for each player.

        :param battlearea_dimensions: BattleArea's dimensions as tuple. e.g. (5, 'E')
        :param battleships_size_locs_list: Dict containing battleship info(type, dimensions, starting co-ordinates)
        :param missile_locs: Tuple containing list of target missiles for each players
        :return: Players as a tuple
        """

        # Creating battlearea for each player...
        ba_width = battlearea_dimensions[0]
        ba_height = battlearea_dimensions[1]

        battlearea_p1 = BattleArea(width=ba_width, height=ba_height)
        battlearea_p2 = BattleArea(width=ba_width, height=ba_height)

        # Place battleships...
        for bs_size_locs in battleships_size_locs_list:
            battlearea_p1.place_battleship(bs_size_locs['bs_type'], bs_size_locs['bs_width'], bs_size_locs['bs_height'],
                                           bs_size_locs['bs_loc']['p1'])
            battlearea_p2.place_battleship(bs_size_locs['bs_type'], bs_size_locs['bs_width'], bs_size_locs['bs_height'],
                                           bs_size_locs['bs_loc']['p2'])

        # Instantiating players...
        self.p1 = Player(battlearea_p1, missile_locs[0], uid=p1_uid)
        self.p2 = Player(battlearea_p2, missile_locs[1], uid=p2_uid)
        self.__active_player_uid__ = self.p1.uid


    def start(self, active_player_uid=None):
        """
        Starts battle by firing missiles.
        :param active_player_uid:
        :return:
        """
        self.__active_player_uid__ = active_player_uid or self.p1.uid
        turns = max(len(self.p1.target_missile_locs), len(self.p2.target_missile_locs)) * 2
        while turns > 0:
            opp_player = self.get_opponent_player()
            active_player = self.get_active_player()

            opponent_ba = opp_player.battlearea
            hit = self.__fire__()

            if hit:
                if opponent_ba.is_destroyed():
                    print "Player-{} won the battle".format(active_player.uid)
                    break
            else:
                # If it's a miss, it's opponent's turn to fire.
                self.__active_player_uid__ = opp_player.uid
                turns -= 1


    def __fire__(self):
        """
        Fires next missile in opponent's battlearea.
        """
        hit = False
        opp_player = self.get_opponent_player()
        active_player = self.get_active_player()
        next_missile_target = active_player.get_missile_target()  # B4

        if next_missile_target is None:
            print "Player-{} has no more missiles left to launch".format(active_player.uid)
            return hit

        opponent_ba_target_loc = get_battlearea_location(next_missile_target)  # (2, 4)
        hit = opp_player.battlearea.hit(opponent_ba_target_loc)
        print "Player-{} fires a missile with target {} which got {}".format(active_player.uid, next_missile_target,
                                                                             "hit" if hit else "miss")
        return hit

    def get_active_player(self):
        """
        Gets active player. Active player will fire next missile.
        :return:
        """
        if self.__active_player_uid__ == self.p1.uid:
            return self.p1
        return self.p2

    def get_opponent_player(self):
        """
        Gets idle player. idle player has to wait until active player misses the target.
        :return:
        """
        if self.__active_player_uid__ == self.p1.uid:
            return self.p2
        return self.p1