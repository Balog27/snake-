from Domain.Board import Board
from random import randint
import  random
from UI.ui import Ui

class Service:
    def __init__(self):
        self.__board = Board(7)
        self.__board_size = self.__board.board_size
        self.__snake = self.__board.snake
        self.__apples = self.__board.apples
        self.__ui = Ui()
        self.__direction = "up"
        self.__lose = False



    @property
    def lose(self):
        return self.__lose

    @property
    def apples(self):
        return self.__apples

    @property
    def board_size(self):
        return self.__board_size

    @property
    def snake(self):
        return self.__snake



    # def draw_board(self):
        #
        # for i in range(self.__board_size):
        #     for j in range(self.__board_size):
        #         print("+-", end="")
        #     print("+")
        #
        #     for j in range(self.__board_size + 1):
        #         coord = [i, j ]
        #         if coord in self.__snake and coord == self.__snake[0]:
        #             print("|*", end="")
        #         elif coord in self.__snake:
        #             print("|+", end="")
        #         elif coord in self.__apples:
        #             print("|a", end="")
        #         else:
        #             print("| ", end="")
        #
        #     print()
        #
        # # Print the last row of horizontal lines
        # for j in range(self.__board_size):
        #     print("+-", end="")
        # print("+")
        #
        # print()




    def move(self,option):
        """
        with this function we either decide if we move n steps in the already set direction or we change direction or we raise
        an error if the direction can't be changed in entered way by user
        :param option: the user input
        :return:
        """
        if option != self.__direction:
            if option == "up" and self.__direction == "down":
                self.__ui.direction_error()
            elif option == "down" and self.__direction == "up":
                self.__ui.direction_error()
            elif option == "left" and self.__direction == "right":
                self.__ui.direction_error()
            elif option == "right" and self.__direction == "left":
                self.__ui.direction_error()
            elif option in ["up", "down", "left", "right"]:
                self.__direction = option
                self.snake_movement(1)
                self.check_for_collision_with_his_own_body()

            else:
                distance = int(option)
                self.check_if_snake_outside(distance)
                self.snake_movement(distance)
                self.check_for_collision_with_his_own_body()


    def snake_movement(self,distance):
        """
        Depending on the direction of the head snake we move his entaier body 'distance' cells in  that direction
        If the snake finds an apple on its way he will grow by 1 unit in his size
        :param distance: The number of cells that the snake is going to travel
        :return:
        """
        if self.__direction == "up":
            for i in range(distance):
                self.__snake.insert(0, [self.__snake[0][0] - 1, self.__snake[0][1]])
                if self.__snake[0] in self.__apples:
                    self.__apples.remove(self.__snake[0])
                    self.generate_a_new_apple()
                else:
                    self.__snake.pop()
        elif self.__direction == "down":
            for i in range(distance):
                self.__snake.insert(0, [self.__snake[0][0] + 1, self.__snake[0][1]])
                if self.__snake[0] in self.__apples:
                    self.__apples.remove(self.__snake[0])
                    self.generate_a_new_apple()
                else:
                    self.__snake.pop()
        elif self.__direction == "left":
            for i in range(distance):
                self.__snake.insert(0, [self.__snake[0][0], self.__snake[0][1] - 1])
                if self.__snake[0] in self.__apples:
                    self.__apples.remove(self.__snake[0])
                    self.generate_a_new_apple()
                else:
                    self.__snake.pop()
        elif self.__direction == "right":
            for i in range(distance):
                self.__snake.insert(0, [self.__snake[0][0], self.__snake[0][1] + 1])
                if self.__snake[0] in self.__apples:
                    self.__apples.remove(self.__snake[0])
                    self.generate_a_new_apple()
                else:
                    self.__snake.pop()
    def check_if_snake_outside(self,distance):
        """
        With this function we can check if the snaked is still inside the game board or he went outside the boarders
        :param distance: The distance of cells that that snakes move
        :return:
        """
        head = self.__snake[0]
        if self.__direction == 'up':
            if head[0]-distance<0:
                self.__ui.lose_border()
                self.__lose = True
        if self.__direction == 'down':
            if head[0]+distance>=self.__board_size:
                self.__ui.lose_border()
                self.__lose = True
        if self.__direction == 'right':
            if head[1]+distance>=self.__board_size:
                self.__ui.lose_border()
                self.__lose = True
        if self.__direction == 'left':
            if head[1]-distance <0:
                self.__ui.lose_border()
                self.__lose = True

    def check_for_collision_with_his_own_body(self):
        """
        We check if the snake has collided(with his head) with the rest of his body
        :return:
        """
        for i in self.__snake:
            cont = 0
            for j in self.__snake:
                if i == j :
                    cont+=1
            if cont > 1:
                self.__ui.lose_snake()
                self.__lose = True
                break

    def generate_a_new_apple(self):
        """
        Generates an apples
        It is needed only if the snake eats an apple
        """
        while True:

            apple_x = randint(0, self.__board_size - 1)
            apple_y = randint(0, self.__board_size - 1)
            ok = 0  # 0 - apple is ok, 1 - apple is not ok
            for i in self.__apples:
                if (apple_x == i[0] or apple_x - 1 == i[0] or apple_x + 1 == i[0]) and apple_y == i[1]:
                    ok = 1
                if apple_x == i[0] and (apple_y == i[1] or apple_y - 1 == i[1] or apple_y + 1 == i[1]):
                    ok = 1

            if ok == 0 and [apple_x, apple_y] not in self.__snake:
                self.__apples.append([apple_x, apple_y])
                break



# s = Service()
# s.draw_board()