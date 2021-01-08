from tree import Node

class KnightPathFinder:
    def __init__(self,pos):
        self._root = Node(pos)
        self._considered_positions = set(pos)


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
        queue = [self._root]

        while(len(queue) > 0):
            node = queue.pop(0)
            moves = self.new_move_position(node.value)
            for move in moves:
                child = Node(move)
                node.add_child(child)
                queue.append(child)

    def find_path(self,end_position):
        end_node = self._root.depth_search(end_position)

        root_trace = [position.value for position in self.trace_to_root(end_node)]

        return sorted(root_trace)

    def trace_to_root(self,end_node):
        trace = []

        node = end_node

        while node != None:
            trace.append(node)
            if node.parent is not None:
                node = node.parent
            else:
                node = None
        return trace


finder = KnightPathFinder((0, 0))
# print(finder.get_valid_move(finder._root.value))
# print(finder.new_move_position((4,1)))

finder.build_move_tree()
print(finder.find_path((2, 1)))  # => [(0, 0), (2, 1)]
print(finder.find_path((3, 3)))  # => [(0, 0), (2, 1), (3, 3)]
print(finder.find_path((6, 2)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
print(finder.find_path((7, 6)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
