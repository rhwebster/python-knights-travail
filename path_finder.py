from tree import Node

class KnightPathFinder:
    def __init__(self,pos):
        self._root = pos
        self._considered_positions = set(self._root)


    def get_valid_move(self, pos):
        (x,y) = pos

        move_set = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (-1, 2),
            (1, -2),
            (-1, -2),
        ]

        valid_move_set = set()

        for key in move_set:
            new_pos_x = (x + key[0])
            new_pos_y = (y + key[1])
            if (0 <= new_pos_x < 8) and (0 <= new_pos_y < 8):
                valid_move_set.add((new_pos_x, new_pos_y))

        return valid_move_set

    def new_move_position(self, pos):
        moves = self.get_valid_move(pos)

        filtered_moves = moves.difference(self._considered_positions)

        self._considered_positions.update(filtered_moves)

        return filtered_moves

    def build_move_tree(self):
        queue = list(self._root)

        while(len(queue) > 0):
            node = queue.pop(0)
            moves = self.new_move_position(node)
            for move in moves:
                child = Node(move)
                node.add_child(child)
                queue.append(child)




finder = KnightPathFinder((0, 0))
print(finder.get_valid_move(finder._root))
print(finder.new_move_position((4,1)))

finder.build_move_tree()
print(finder._root.children)
