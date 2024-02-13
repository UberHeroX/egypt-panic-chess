import pygame
import Tile

class Piece:
    Image = None
    Tile = None
    Name = None
    ABSOLUTE_X = None
    ABSOLUTE_Y = None
    Team = None
    IS_MOVED = False
    Collider = None
    def create_collider(self):
       self.Collider = self.Image.get_rect(center=(self.ABSOLUTE_X + 27, self.ABSOLUTE_Y +27 ))
       self.Collider.inflate_ip(10, 10)
    HAS_MOVED = False
    OFFSET_X= None
    OFFSET_Y = None
       


white_pawn = pygame.image.load("./files/pieces/white_pawn.png")
black_pawn = pygame.image.load("./files/pieces/black_pawn.png")
white_rook = pygame.image.load("./files/pieces/white_rook.png")
black_rook = pygame.image.load("./files/pieces/black_rook.png")
white_knight = pygame.image.load("./files/pieces/white_knight.png")
black_knight = pygame.image.load("./files/pieces/black_knight.png")
white_bishop = pygame.image.load("./files/pieces/white_bishop.png")
black_bishop = pygame.image.load("./files/pieces/black_bishop.png")
white_queen = pygame.image.load("./files/pieces/white_queen.png")
black_queen = pygame.image.load("./files/pieces/black_queen.png")
white_king = pygame.image.load("./files/pieces/white_king.png")
black_king = pygame.image.load("./files/pieces/black_king.png")



pieces_to_render = []

def setup_pawn(team, ABSOLUTE_X, ABSOLUTE_Y, Tile):
    pawn = Piece()
    if team == "White":
        pawn.Team = "White"
        pawn.Image = white_pawn
    else:
        pawn.Team = "Black"
        pawn.Image = black_pawn
    pawn.Name = "Pawn"
    pawn.Tile = Tile
    pawn.ABSOLUTE_X = ABSOLUTE_X
    pawn.ABSOLUTE_Y = ABSOLUTE_Y
    pawn.OFFSET_X = 15
    pawn.OFFSET_Y = 5
    Tile.Piece = pawn
    return pawn

def setup_rook(team, ABSOLUTE_X, ABSOLUTE_Y, Tile):
    rook = Piece()
    if team == "White":
        rook.Team = "White"
        rook.Image = white_rook
    else:
        rook.Team = "Black"
        rook.Image = black_rook
    rook.Name = "Rook"
    rook.Tile = Tile
    rook.ABSOLUTE_X = ABSOLUTE_X
    rook.ABSOLUTE_Y = ABSOLUTE_Y
    rook.OFFSET_X = 15
    rook.OFFSET_Y = 5
    Tile.Piece = rook
    return rook

def setup_knight(team, ABSOLUTE_X, ABSOLUTE_Y, Tile):
    knight = Piece()
    if team == "White":
        knight.Team = "White"
        knight.Image = white_knight
    else:
        knight.Team = "Black"
        knight.Image = black_knight
    knight.Name = "Knight"
    knight.Tile = Tile
    knight.ABSOLUTE_X = ABSOLUTE_X
    knight.ABSOLUTE_Y = ABSOLUTE_Y
    Tile.Piece = knight
    return knight

def setup_bishop(team, ABSOLUTE_X, ABSOLUTE_Y, Tile):
    bishop = Piece()
    if team == "White":
        bishop.Team = "White"
        bishop.Image = white_bishop
    else:
        bishop.Team = "Black"
        bishop.Image = black_bishop
    bishop.Name = "Bishop"
    bishop.Tile = Tile
    bishop.ABSOLUTE_X = ABSOLUTE_X
    bishop.ABSOLUTE_Y = ABSOLUTE_Y
    Tile.Piece = bishop
    return bishop

def setup_queen(team, ABSOLUTE_X, ABSOLUTE_Y, Tile):
    queen = Piece()
    if team == "White":
        queen.Team = "White"
        queen.Image = white_queen
    else:
        queen.Team = "Black"
        queen.Image = black_queen
    queen.Name = "Queen"
    queen.Tile = Tile
    queen.ABSOLUTE_X = ABSOLUTE_X
    queen.ABSOLUTE_Y = ABSOLUTE_Y
    Tile.Piece = queen
    return queen


def setup_king(team, ABSOLUTE_X, ABSOLUTE_Y, Tile):
    king = Piece()
    if team == "White":
        king.Team = "White"
        king.Image = white_king
    else:
        king.Team = "Black"
        king.Image = black_king
    king.Name = "King"
    king.Tile = Tile
    king.ABSOLUTE_X = ABSOLUTE_X
    king.ABSOLUTE_Y = ABSOLUTE_Y
    Tile.Piece = king
    return king


def is_piece_on_tile(Tile):
    if Tile is not None:
      if Tile.Piece is not None:
        return True
      else:
        return False
    
def piece_on_tile(Tile: Tile, tiles):
    for tile in tiles:
        if Tile == tile:
            return tile.Piece
    


def pawn_move(Piece:Piece, tiles):

    c_tile = Piece.Tile
    all_tiles = tiles
    tiles_to_move = []
    if Piece.Team == "White":
        if Piece.HAS_MOVED == True:
                above_tile = Tile.get_above_tile(c_tile, all_tiles)
                above_left_tile = Tile.get_left_up_diagonal(c_tile, all_tiles)
                above_right_tile = Tile.get_right_up_diagonal(c_tile, all_tiles)

                if is_piece_on_tile(above_left_tile) and piece_on_tile(above_left_tile,tiles).Team == "Black":
                    tiles_to_move.append(above_left_tile)
                   

                if is_piece_on_tile(above_right_tile) and piece_on_tile(above_right_tile,tiles).Team == "Black":
                    tiles_to_move.append(above_right_tile)
                   
               
                if not is_piece_on_tile(above_tile):
                    tiles_to_move.append(above_tile)



        else:
                
                above_left_tile = Tile.get_left_up_diagonal(c_tile, all_tiles)
                above_right_tile = Tile.get_right_up_diagonal(c_tile, all_tiles)
                above_tile = Tile.get_above_tile(c_tile, all_tiles)

                if is_piece_on_tile(above_left_tile) and piece_on_tile(above_left_tile,tiles).Team == "Black":
                    tiles_to_move.append(above_left_tile)
                   
              

                first_move_tile = Tile.get_above_tile(above_tile, all_tiles)
                if is_piece_on_tile(above_right_tile) and piece_on_tile(above_right_tile,tiles).Team == "Black":
                    tiles_to_move.append(above_right_tile)
                   
                if not is_piece_on_tile(above_tile):
                    tiles_to_move.append(above_tile)
                    if not is_piece_on_tile(first_move_tile):
                       tiles_to_move.append(first_move_tile)

                
                

    else:
        if Piece.HAS_MOVED == True:
                below_tile = Tile.get_below_tile(c_tile, all_tiles)
                below_left_tile = Tile.get_left_down_diagonal(c_tile, all_tiles)
                below_right_tile = Tile.get_right_down_diagonal(c_tile, all_tiles)

                if is_piece_on_tile(below_left_tile) and piece_on_tile(below_left_tile,tiles).Team == "White":
                    tiles_to_move.append(below_left_tile)
                   

                if is_piece_on_tile(below_right_tile) and piece_on_tile(below_right_tile,tiles).Team == "White":
                    tiles_to_move.append(below_right_tile)
                   

                if not is_piece_on_tile(below_tile):
                    tiles_to_move.append(below_tile)

        else:
                below_tile = Tile.get_below_tile(c_tile, all_tiles)
                if not is_piece_on_tile(below_tile):
                    tiles_to_move.append(below_tile)
                first_move_tile = Tile.get_below_tile(below_tile, all_tiles)
                if not is_piece_on_tile(first_move_tile):
                    tiles_to_move.append(first_move_tile)
               
    
    return tiles_to_move

def rook_move(Piece:Piece, tiles):

    c_tile = Piece.Tile
    all_tiles = tiles
    tiles_to_move = []


    leftTile = Tile.get_left_tile(c_tile,all_tiles)
    if leftTile is not None:
        if is_piece_on_tile(leftTile):
            if piece_on_tile(leftTile, all_tiles).Team == "Black":
                 tiles_to_move.append(leftTile)
        else: 
            tiles_to_move.append(leftTile)

       
    rightTile = Tile.get_right_tile(c_tile,all_tiles)
    if rightTile is not None:
        if is_piece_on_tile(rightTile):
            if piece_on_tile(rightTile, all_tiles).Team == "Black":
                 tiles_to_move.append(rightTile)
        else: 
            tiles_to_move.append(rightTile)


    upTile = Tile.get_above_tile(c_tile,all_tiles)
    if upTile is not None:
        if is_piece_on_tile(upTile):
            if piece_on_tile(upTile, all_tiles).Team == "Black":
                 tiles_to_move.append(upTile)
        else: 
            tiles_to_move.append(upTile)

    downTile = Tile.get_below_tile(c_tile,all_tiles)
    if downTile is not None:
        if is_piece_on_tile(downTile):
            if piece_on_tile(downTile, all_tiles).Team == "Black":
                 tiles_to_move.append(downTile)
        else: 
            tiles_to_move.append(downTile)


    if Piece.Team == "White":

       for i in range(8):
         
         if  Tile.get_left_tile(leftTile,all_tiles) is not None:
          leftTile = Tile.get_left_tile(leftTile,all_tiles)
         if is_piece_on_tile(leftTile) :
            if piece_on_tile(leftTile,tiles).Team == "Black":
                tiles_to_move.append(leftTile)
                print("FAFAF")
                break
         elif leftTile is not None:
             tiles_to_move.append(leftTile)

       for i in range(8):
         if Tile.get_right_tile(rightTile, all_tiles) is not None:
          rightTile= Tile.get_right_tile(rightTile, all_tiles)
         if is_piece_on_tile(rightTile) :
            if piece_on_tile(rightTile,tiles).Team == "Black":
                tiles_to_move.append(rightTile)
                break
         elif rightTile is not None:
             tiles_to_move.append(rightTile)

       for i in range(8):
         if Tile.get_above_tile(upTile, all_tiles) is not None:
          upTile= Tile.get_above_tile(upTile, all_tiles)
          if upTile.Piece.Team == "Black":
              print("asdas")
         if is_piece_on_tile(upTile) :
            if piece_on_tile(upTile,tiles).Team == "Black":
                tiles_to_move.append(upTile)
                break
         elif upTile is not None:
             tiles_to_move.append(upTile)

       for i in range(8):
         if Tile.get_below_tile(downTile, all_tiles) is not None:
          downTile= Tile.get_below_tile(downTile, all_tiles)
         if is_piece_on_tile(downTile) :
            if piece_on_tile(downTile,tiles).Team == "Black":
                tiles_to_move.append(downTile)
                break
         elif downTile is not None:
             tiles_to_move.append(downTile)




       
    
                
                

    else:
        if Piece.HAS_MOVED == True:
                below_tile = Tile.get_below_tile(c_tile, all_tiles)
                below_left_tile = Tile.get_left_down_diagonal(c_tile, all_tiles)
                below_right_tile = Tile.get_right_down_diagonal(c_tile, all_tiles)

                if is_piece_on_tile(below_left_tile) and piece_on_tile(below_left_tile,tiles).Team == "White":
                    tiles_to_move.append(below_left_tile)
                   

                if is_piece_on_tile(below_right_tile) and piece_on_tile(below_right_tile,tiles).Team == "White":
                    tiles_to_move.append(below_right_tile)
                   

                if not is_piece_on_tile(below_tile):
                    tiles_to_move.append(below_tile)

        else:
                below_tile = Tile.get_below_tile(c_tile, all_tiles)
                if not is_piece_on_tile(below_tile):
                    tiles_to_move.append(below_tile)
                first_move_tile = Tile.get_below_tile(below_tile, all_tiles)
                if not is_piece_on_tile(first_move_tile):
                    tiles_to_move.append(first_move_tile)
               
    
    return tiles_to_move






def get_piece_available_tiles(Piece: Piece, tiles):
    #
    
    available_tiles = []


    match(Piece.Name):
        
        #U slucaju da je figura pijun
        case "Pawn": 
           available_tiles.append(pawn_move(Piece, tiles))

        case "Rook":
            print("s")
            available_tiles.append(rook_move(Piece, tiles))
    
 




        case _:
            print("Cannot move")
          
    return available_tiles


   
     

def render_pieces(window):
    for i, piece in enumerate(pieces_to_render):
        window.blit(piece.Image, (piece.ABSOLUTE_X, piece.ABSOLUTE_Y + 5 ))


    



