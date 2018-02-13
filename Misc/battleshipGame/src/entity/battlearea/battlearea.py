from src.util.commons import to_index, empty_2d_array

class BattleArea(object):
    """
    Represents `battle area`, uses 2-D matrix in order to store the battleship's locations.
    """
    def __init__(self, height=0, width=0):
        self.width = width
        self.height = to_index(height)

        # Count representing number of `live` cells in underlying battlearea.
        self.__limit__ = 0

        # Matrix, each cell will contain a count(0 or 1 depending on battle ship type) representing
        # the number of hits required to destroy that cell.
        # A cell is considered as `Live` if it stores value greater than 0.
        self.__battlearea__ = empty_2d_array(self.height+1, self.width+1, fill_default=0)

    def place_battleship(self, bs_type, bs_width, bs_height, bs_loc):
        """
        Places a battleship in underlying battle area on specified co-ordinates/locations.
        :param bs_type: `P` or `Q`
        :param bs_width: Width of battleship
        :param bs_height: Height of battleship
        :param bs_loc: Tuple representing starting co-ordinates in battle area where ship needs to be placed.
        :return:
        """
        limit = 1 if bs_type == "P" else 2
        row_start = bs_loc[0]
        col_start = bs_loc[1]

        for row in range(row_start, row_start + bs_height):
            for col in range(col_start, col_start + bs_width):
                # Update matrix cell values accordingly.
                self.__battlearea__[row][col] = limit
                self.__limit__ += limit

    def hit(self, loc):
        """
        To fire a missile on underlying battle area.
        :param loc: Missile target, i.e. matrix cell in underlying battle area.
        :return: `True` if hits, `False` otherwise
        """
        if self.__battlearea__[loc[0]][loc[1]] > 0:
            self.__battlearea__[loc[0]][loc[1]] -= 1
            self.__limit__ -= 1
            return True

        return False

    def is_destroyed(self):
        """
        Checks if underlying battle area is completely destroyed(i.e. no live cells remaining).
        :return:
        """
        return self.__limit__ == 0


    def __str__(self):
        return "Width: {}\nHeight: {}\nBattle area: \n{}".format(self.width, self.height, str(self.__battlearea__))