from tree import Node

class KnightPathFinder:
    def __init__(self,position):
        self._postition = position
        self._root = Node(0,0)
        self._considered_positions = set(self._root)

    
    def get_valid_move(self, pos):
        (x,y) = pos

        move_set = {
            move1 = (x + 2, y + 1)
            move2 = (x + 2, y - 1)
            move3 = (x - 2, y + 1)
            move4 = (x - 2, y - 1)
            move5 = (x + 1, y + 2)
            move6 = (x - 1, y + 2)
            move7 = (x + 1, y - 2)
            move8 = (x - 1, y - 2)
        }

        valid_move_set = set()

        for key in move_set:
            new_pos = (position[0]+move_set[key][0], position[1]+move_set[key][1])
            if (new_pos[0] < 0 or new_pos[1] < 0) or (new_pos[0] > 7 or new_pos[1] > 7):
                continue
            else:
                valid_move_set.add(new_pos)

        return valid_move_set


