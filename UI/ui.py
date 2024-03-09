


class Ui():





    def user_input(self):

        while True:
            user = input("Enter command ( move [n] / <direction> ): ")
            user = user.strip()
            user = user.lower()
            user = user.split(" ")
            if len(user) == 1:
                if user[0] not in ["up", "down", "left", "right"]:
                    print("Invalid command!")
                else:
                    return user[0]
            elif len(user) == 2:
                if user[0] != "move":
                    print("Invalid command!")
                else:
                    if user[1].isdigit() == False:
                        print("Invalid command!")
                    else:
                        return user[1]
            else:
                print("Invalid command!")


    def draw_board(self,board_size, snake, apples):

        print()
        for i in range(board_size):
            for j in range(board_size):
                print("+-", end="")
            print("+")

            for j in range(board_size + 1):
                coord = [i, j ]
                if coord in snake and coord == snake[0]:
                    print("|*", end="")
                elif coord in snake:
                    print("|+", end="")
                elif coord in apples:
                    print("|a", end="")
                else:
                    print("| ", end="")

            print()

        # Print the last row of horizontal lines
        for j in range(board_size):
            print("+-", end="")
        print("+")

        print()

    def direction_error(self):
        print("Invalid direction - the snake can't turn 180 degrees!")

    def lose_border(self):
        print("The snake hit the border, you lost!")

    def lose_snake(self):
        print("The snake collided with his body, you lost!")

    def print_board_size(self,x):
        print("The board size is: ", x)
#
# ui = Ui()
# ui.user_input()