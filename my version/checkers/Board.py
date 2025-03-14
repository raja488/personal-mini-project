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
    main(); 
    
import pygame   


# Board class
class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)
    
    
    def get_all_pieces(self,color):
        Pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    Pieces.append(piece)
        return Pieces

    
    
    def move(self, piece, row, col):
        if piece:  
            self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
            piece.move(row, col)

            if row == ROWS - 1 or row == 0:
                piece.make_king()
                if piece.color == WHITE:
                    self.white_kings += 1
                else:
                    self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
    
    def remove(self,pieces):
        for piece in pieces :
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -=1
                else:
                    self.white_left -=1
    
    def winner(self):
        if self.red_left <=0:
            return WHITE
        elif self.white_left <=0:
            return RED
        
        return None
            
                    
    def get_valid_moves(self,piece):
        moves = {}
        left = piece.col -1
        right = piece.col +1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row -1, max(row -3,-1 ),-1,piece.color,left))
            moves.update(self._traverse_right(row -1, max(row -3,-1 ),-1,piece.color,right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row +1, min(row +3,ROWS ),1,piece.color,left))
            moves.update(self._traverse_right(row +1, min(row +3,ROWS ),1,piece.color,right))

        return moves

    def _traverse_left(self,start,stop,step,color,left,skipped=[]):
        moves = {}
        last = []
        for r in range(start,stop,step):
            if left <0:
                break
            current=self.board[r][left]
            if current == 0:
                if skipped  and not last:
                    break
                elif skipped:
                    moves[(r,left)]= last + skipped
                else:
                    moves[(r, left )]  = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row , step , color , left-1 , skipped=last))
                    moves.update(self._traverse_right(r+step, row , step , color , left+1 , skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self,start,stop,step,color,right,skipped=[]):
        moves = {}
        last = []
        for r in range(start,stop,step):
            if right >=COLLS:
                break
            current=self.board[r][right]
            if current == 0:
                if skipped  and not last:
                    break
                elif skipped:
                    moves[(r,right)]= last + skipped
                else:
                    moves[(r, right )]  = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row , step , color , right-1 , skipped=last))
                    moves.update(self._traverse_right(r+step, row , step , color , right+1 , skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
    


# Piece class
class Piece:
    PADDING = 20
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)

#game.py
class Game:
    def __init__(self,win):
       self._init()
       self.win = win 

    def update(self):
        self.board.draw(WIN)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected=None
        self.board=Board()
        self.turn = RED
        self.valid_moves= {}

    def winner(self):
        return self.board.winner()


    def reset(self):
        self._init()

    def select(self, row , col):
        if self.selected:
            result = self._move(row,col)
            if not result:
                self.selected = None
                self.select(row,col)
                
        piece = self.board.get_piece(row,col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        
        return False



    
    def _move(self, row, col):
        Piece = self.board.get_piece(row, col)
        if self.selected and Piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves.get((row, col))
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)


    def change_turn(self):
        self.valid_moves = {}
        if self.turn ==RED:
            self.turn = WHITE
        else:
            self.turn=RED

    def get_board(self):
        return self.board
    
    def ai_move(self,board):
        self.board=board
        self.change_turn()


#algorith.py
from copy import deepcopy
def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):  # Use WHITE as color
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):  # Use RED as color
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move


def get_all_moves(board, color, game):
    moves = []
    for piece in Board.get_all_pieces(color):
        valid_moves = Board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            new_board = simulate_move(piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves


def simulate_move(piece,move,board,game,skip):
    board.move(piece,move[0],move[1])
    if skip:
        board.remove(skip)

    return board


# Main game
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CHECKERS")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn==WHITE:
            value , new_board = minimax(game.get_board(),3,WHITE,game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


if __name__ == "__main__":
    main()





