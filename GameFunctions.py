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
    
    if Tile.get_left_up_diagonal(current_tile, all_tiles) is not None:
        tile_to_send= Tile.get_left_up_diagonal(current_tile, all_tiles)
        print("Left up detected")
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King":
           print("King Detected Left up ")
           return tile_to_send
    
    if Tile.get_right_up_diagonal(current_tile, all_tiles) is not None:
        tile_to_send= Tile.get_right_up_diagonal(current_tile, all_tiles)
        print("Right up detected")
        if Pieces.is_piece_on_tile(tile_to_send):
         if Pieces.piece_on_tile(tile_to_send,all_tiles).Name == "King":
           print(" king Right up detected")
           return tile_to_send
         
    print("shit wack")
   




        