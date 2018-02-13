import uuid

class Player(object):
    """
    An instance of this class represents a player.
    """
    def __init__(self, battlearea, target_missile_locs, uid=None):
        """
        :param battlearea: Underlying player's battlearea
        :param target_missile_locs: Missile targets. e.e. [A1, B2, C6, D2]
        :param uid Unique id of player.
        """
        self.uid = uid or str(uuid.uuid4())
        self.battlearea = battlearea
        self.target_missile_locs = target_missile_locs

    def get_missile_target(self):
        """
        Get and remove next missile to be fired.
        :return: Next missile/target to be fired.
        """
        target = None
        if len(self.target_missile_locs) > 0:
            target = self.target_missile_locs.pop(0)  # B4
        return target