class Game:
    def __init__(self,n,territory):
        self.__n=n
        self.__territory=territory
        self.__snake_pos=self.search_matrix(self.__territory,'S')
        self.game_over=False
        self.food_quantity=0
        self.NEEDED_FOOD=10
        self.ops={
    'up':lambda :self.move(-1,0),
    'down':lambda :self.move(1,0),
    'left':lambda :self.move(0,-1),
    'right':lambda :self.move(0,1),
     }


    def move(self,delta_y, delta_x):

        y,x =self.__snake_pos
        self.__territory[y][x]='.'
        new_y=y+delta_y
        new_x=x+delta_x
        if 0 >new_x or new_x>self.__n-1 or 0 >new_y or new_y>self.__n-1:
            self.game_over=True
            return
        at_pos=self.__territory[new_y][new_x]
        if at_pos=="B":
            self.__territory[new_y][new_x]='.'
            new_y,new_x=self.search_matrix(self.__territory,'B')
        if at_pos == "*":
            self.food_quantity+=1
            if self.food_quantity==self.NEEDED_FOOD:
                self.game_over=True
        self.__territory[new_y][new_x]='S'
        self.__snake_pos=(new_y,new_x)


# todo осмисли принта:


    def print_territory(self):
        print('\n'.join([''.join(row) for row in self.__territory]))

    def play(self):
        while not self.game_over:
            command = input()
            # todo tuk izvikwame taka funkciata move s razlichni koordinati
            move_fn = self.ops[command]
            move_fn()
    def print_stats(self):
        if self.game_over and self.food_quantity < 10:
            print("Game over!")
        else:
            print("You won! You fed the snake.")
        print(f"Food eaten: {self.food_quantity }")
        self.print_territory()

    def search_matrix(self,matrix,search):
        for y, row in enumerate(matrix):
            for x,char in enumerate(row):
                if char==search:
                    return y,x

n=int(input())
territory=[list(input()) for _ in range(n)]
game=Game(n,territory)
game.play()
game.print_stats()














game=Game(n,territory)
game.play()
game.print_stats()





