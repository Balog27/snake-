from random import randint

class Board:
    def __init__(self, n):
        self.__board_size =  n
        self.__matrix = [[0 for _ in range(self.__board_size)] for _ in range(self.__board_size)]
        self.__empty_space = 0
        self.__snake = [[self.__board_size//2-1,self.__board_size//2],[self.__board_size//2,self.__board_size//2],[self.__board_size//2+1,self.__board_size//2]]
        self.__apples = generate_apples(self.board_size,self.snake)
    @property
    def board_size(self):
        return self.__board_size

    @property
    def matrix(self):
        return self.__matrix

    @property
    def snake(self):
        return self.__snake

    @property
    def apples(self):
        return self.__apples



def get_nr_of_apples():
    with open('Domain/apples.txt', 'r') as file:
        nr_apples = file.read()
        return  int(nr_apples)


def generate_apples(board_size,snake):
        apples = []
        for i in range (get_nr_of_apples()):
            while True:

                apple_x = randint(0,board_size-1)
                apple_y = randint(0,board_size-1)
                ok = 0 # 0 - apple is ok, 1 - apple is not ok
                for i in apples:
                    if (apple_x == i[0] or apple_x - 1 == i[0] or apple_x + 1 == i[0]) and apple_y == i[1] :
                        ok = 1
                    if apple_x == i[0] and (apple_y == i[1] or apple_y - 1 == i[1] or apple_y + 1 == i[1]):
                        ok = 1

                if ok == 0 and [apple_x,apple_y] not in snake:
                    apples.append([apple_x,apple_y])
                    break
        return apples

# b = Board(7)
# print(b.apples)
# print(b.board_size)
# print(b.snake)