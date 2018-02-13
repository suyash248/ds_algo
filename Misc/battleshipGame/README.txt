>>>> How to run?

1. Move to <project-dir>, create virtual environment and then activate it as follows -
$ cd <project-dir>
$ virtualenv .environment
$ source .environment/bin/activate
Note: Step-1 is optional but recommended.

2. Add project to PYTHONPATH as follows -
$ export PYTHONPATH="$PYTHONPATH:." # . corresponds to current directory(project-dir)

If you are using PyCharm then it can be done under run configuration.

##################################################################################################################

>>>> Design -

In this approach, we've following entities/models -
A. Battle Area
B. Player

- An instance of `Player` entity represents a player. Similarly an instance of `BattleArea` represents a battle area. battle are is associated
with a player.

- Underlying data structure used for representing the battle area is 2-D array. Where each cell contains a numeric value.

- Cell value under the matrix in underlying battle area represents number of hits required to destroy that cell(partial ship) at anytime.

Note: For simplicity `Cell` is not considered as a separate entity. But for more complex requirements we can consider `Cell` as an entity.
Similarly, battleships differs only on the basis single attribute i.e. their strength(Strong-P or Weak-Q).
If we have different "behaviours" and different attributes for ships then `BattleShip` can be considered as separate entity.

##################################################################################################################