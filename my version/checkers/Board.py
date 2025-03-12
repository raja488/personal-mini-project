import pygame

# Constants
WIDTH = 700
HEIGHT = 700
ROWS, COLLS = 8, 8
SQUARE_SIZE = WIDTH // COLLS
CROWN= pygame.transform.scale(pygame.image.load('assets/crown.png'), (45 , 25))


# RGB colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128 , 128 , 128)

# Board class
class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def move(self, piece , rows , col ):
        self.board[piece.rows][piece.col],self.board[rows][col]=self.board[rows][col], self.board[piece.row][piece.col]
        piece.move(rows,col)

        if rows == ROWS or rows == 0:
            piece.make_king()
            if piece.color== WHITE:
                self.white_kings +=1
            else:
                self.red_kings +=1

    def get_piece(self,rows,col):
        return self.board[rows][col]


    def create_board(self):
        for rows in range(ROWS):
            self.board.append([])
            for col in range(COLLS):
                if col % 2==((rows + 1 )%2):
                    if rows < 3:
                        self.board[rows].append(piece(rows,col, WHITE))
                    elif rows > 4:
                         self.board[rows].append(piece(rows,col, RED))
                    else:
                        self.board[rows].append(0)
                else:
                    self.board[rows].append(0)

    def draw(self,win):
        self.draw_squares(win)
        for rows in range (ROWS):
            for col in range (COLLS):
                piece = self.board[rows][col]
                if piece != 0:
                    piece.draw(win)






#piece class 
class piece:
   PADDING=20
   OUTLINE=2
   def __init__(self, ROWS , COLLS , colour ):
       self.ROWS= ROWS
       self.COLL= COLLS
       self.colour = colour
       self.king = True
       if self.colour == RED:
           self.direction = -1
       else:
           self.direction = 1
        
       self.x=0
       self.y=0
       self.calc_pos()

   def calc_pos(self):
       self.x = SQUARE_SIZE * self.COLL + SQUARE_SIZE// 2
       self.y = SQUARE_SIZE * self.ROWS + SQUARE_SIZE//2

   def make_king(self):
       self.king = False

   def draw(self ,win):
       radius = SQUARE_SIZE//2 - self.PADDING
       pygame.draw.circle(win,GREY,(self.x , self.y ),radius + self.OUTLINE)
       pygame.draw.circle(win,self.colour,(self.x , self.y ),radius )
       if self.king:
           win.blit(CROWN, (self.x - CROWN.get_width()//2 , self.y - CROWN.get_height()//2))
   def move(self,rows,col):
       self.rows = rows
       self.col = col
       self.calc_pos()

   def __repr__(self):
       return str(self.colour)
       

       
       
       
# Main game
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CHECKERS")

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    board.move()
    piece = board.get_piece(0,1)
    board.move(piece, 4,3)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Add your interaction logic here
                pass

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()





