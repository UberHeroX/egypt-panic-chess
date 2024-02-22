import Pieces
import socket
import Tile


def can_eat_figure(Piece, Tile, tiles):
    if Pieces.piece_on_tile(Tile, tiles) is not None:
     piece_to_destroy = Pieces.piece_on_tile(Tile, tiles)
     print(Piece.Team)
     if Pieces.piece_on_tile(Tile, tiles).Team != Piece.Team:
        Pieces.pieces_to_render.remove(piece_to_destroy)




def check_pawn(Piece, tiles):
    c_tile = Piece.Tile
    current_tile = c_tile
    all_tiles = tiles
    tile_to_send = None
    team = None
    if Piece.Team == "Black":
        team = "White"
    else:
        team = "Black"

    if Piece.Team =="White":
     if Tile.get_left_up_diagonal(current_tile, all_tiles) is not None:
        tile_to_send= Tile.get_left_up_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
    
     if Tile.get_right_up_diagonal(current_tile, all_tiles) is not None:
        tile_to_send= Tile.get_right_up_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
         
    else:
     if Tile.get_left_down_diagonal(current_tile, all_tiles) is not None:
        tile_to_send= Tile.get_left_up_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
    
     if Tile.get_right_down_diagonal(current_tile, all_tiles) is not None:
        tile_to_send= Tile.get_right_up_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
    
    if Piece.Team =="Black":
     if Tile.get_left_down_diagonal(current_tile, all_tiles) is not None:
        tile_to_send= Tile.get_left_down_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
    
     if Tile.get_right_down_diagonal(current_tile, all_tiles) is not None:
        tile_to_send= Tile.get_right_down_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
         
    else:
     if Tile.get_left_down_diagonal(current_tile, all_tiles) is not None:
        tile_to_send= Tile.get_left_down_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
    
     if Tile.get_right_down_diagonal(current_tile, all_tiles) is not None:
        tile_to_send= Tile.get_right_down_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
    
def check_bishop(Piece, tiles):
   c_tile = Piece.Tile
   current_tile = c_tile
   all_tiles = tiles
   tile_to_send = None
   team = None
   if Piece.Team == "Black":
        team = "White"
   else:
        team = "Black"

   for i in range(8):
        if Tile.get_left_up_diagonal(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_left_up_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile   

   for i in range(8):
        if Tile.get_right_up_diagonal(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_right_up_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile   

   for i in range(8):
        if Tile.get_right_down_diagonal(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_right_down_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile   

   for i in range(8):
        if Tile.get_left_down_diagonal(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_left_down_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send
 
def check_rook(Piece,tiles):
   c_tile = Piece.Tile
   current_tile = c_tile
   all_tiles = tiles
   tile_to_send = None
   team = None
   if Piece.Team == "Black":
        team = "White"
   else:
        team = "Black"

   for i in range(8):
        if Tile.get_left_tile(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_left_tile(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile   

   for i in range(8):
        if Tile.get_right_tile(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_right_tile(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile   

   for i in range(8):
        if Tile.get_above_tile(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_above_tile(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile   

   for i in range(8):
        if Tile.get_below_tile(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_below_tile(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

def check_knight(Piece, tiles):
    c_tile = Piece.Tile
    current_tile = c_tile
    all_tiles = tiles
    tile_to_send = None
    team = None
    if Piece.Team == "Black":
        team = "White"
    else:
        team = "Black"
    
    if Tile.get_tile_by_row_and_col(c_tile.Row - 2, c_tile.Column +1, all_tiles) is not None:
        tile_to_send= Tile.get_tile_by_row_and_col(c_tile.Row - 2, c_tile.Column +1, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send

    if Tile.get_tile_by_row_and_col(c_tile.Row +2 , c_tile.Column +1, all_tiles) is not None:
        tile_to_send= Tile.get_tile_by_row_and_col(c_tile.Row +2 , c_tile.Column +1, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
         
    if Tile.get_tile_by_row_and_col(c_tile.Row +2 , c_tile.Column -1, all_tiles) is not None:
        tile_to_send= Tile.get_tile_by_row_and_col(c_tile.Row +2 , c_tile.Column -1, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send

    if Tile.get_tile_by_row_and_col(c_tile.Row -2 , c_tile.Column -1, all_tiles) is not None:
        tile_to_send= Tile.get_tile_by_row_and_col(c_tile.Row -2 , c_tile.Column -1, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
         
    if Tile.get_tile_by_row_and_col(c_tile.Row -1 , c_tile.Column -2, all_tiles) is not None:
        tile_to_send= Tile.get_tile_by_row_and_col(c_tile.Row -1 , c_tile.Column -2, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
         
    if Tile.get_tile_by_row_and_col(c_tile.Row -1 , c_tile.Column +2, all_tiles) is not None:
        tile_to_send= Tile.get_tile_by_row_and_col(c_tile.Row -1 , c_tile.Column +2, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
    
    if Tile.get_tile_by_row_and_col(c_tile.Row +1 , c_tile.Column +2, all_tiles) is not None:
        tile_to_send= Tile.get_tile_by_row_and_col(c_tile.Row +1 , c_tile.Column +2, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send
         
    if Tile.get_tile_by_row_and_col(c_tile.Row +1 , c_tile.Column -2, all_tiles) is not None:
        tile_to_send= Tile.get_tile_by_row_and_col(c_tile.Row +1 , c_tile.Column -2, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
           return tile_to_send

def check_queen(Piece, tiles):

   c_tile = Piece.Tile
   current_tile = c_tile
   all_tiles = tiles
   tile_to_send = None
   team = None
   if Piece.Team == "Black":
        team = "White"
   else:
        team = "Black"

   for i in range(8):
        if Tile.get_left_tile(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_left_tile(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile   

   for i in range(8):
        if Tile.get_right_tile(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_right_tile(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile   

   for i in range(8):
        if Tile.get_above_tile(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_above_tile(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile   

   for i in range(8):
        if Tile.get_below_tile(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_below_tile(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile

   for i in range(8):
        if Tile.get_left_up_diagonal(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_left_up_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile   

   for i in range(8):
        if Tile.get_right_up_diagonal(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_right_up_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile   

   for i in range(8):
        if Tile.get_right_down_diagonal(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_right_down_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send

   current_tile = c_tile   

   for i in range(8):
        if Tile.get_left_down_diagonal(current_tile, all_tiles) is None:
            break
        tile_to_send= Tile.get_left_down_diagonal(current_tile, all_tiles)
        if Pieces.is_piece_on_tile(tile_to_send):
           if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King" and Pieces.piece_on_tile(tile_to_send,all_tiles).Team == team:
            return tile_to_send
           else:
              break
        else:
         current_tile = tile_to_send



    



def get_piece_check(Piece, tiles):
    #
    check_tile= None

    match(Piece.Name):
        
        #U slucaju da je figura pijun
        case "Pawn": 
           check_tile = check_pawn(Piece, tiles)

        case "Rook":
            
           check_tile = check_rook(Piece, tiles)


        case "Bishop":

            check_tile = check_bishop(Piece, tiles)
    
        case "Knight":

            check_tile = check_knight(Piece, tiles)

        case "Queen":

            check_tile = check_queen(Piece, tiles)
        

        case _:
            print("Cannot move")
          
    return check_tile


        