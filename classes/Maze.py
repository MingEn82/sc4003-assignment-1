class Maze:
    def __init__(self, layout):
        self.layout = layout
        self.height = len(self.layout)
        self.width = len(self.layout[0])

    def update_prev_values(self):
        for i in range(self.height):
            for j in range(self.width):
                self.layout[i][j].prev_value = self.layout[i][j].value

    def get_values(self):
        return [tile.value for row in self.layout for tile in row]
    
    def display(self):
        print(f"{'Reward':^{9*len(self.layout[0])}}", end="   ")
        print(f"{'Value':^{9*len(self.layout[0])}}", end="   ")
        print(f"{'Policy':^{7*len(self.layout[0])}}")

        for line in self.layout:
            print("+-------+"*len(line), end="   ")
            print("+-------+"*len(line), end="   ")
            print("+-----+"*len(line))

            for tile in line:
                print(tile.display_reward(), end="")
            print("   ", end="")
            for tile in line:
                print(tile.display_value(), end="")
            print("   ", end="")
            for tile in line:
                print(tile.display_direction(), end="")
            print()

            print("+-------+"*len(line), end="   ")
            print("+-------+"*len(line), end="   ")
            print("+-----+"*len(line))