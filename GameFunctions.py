import Pieces

def can_eat_figure(Piece, Tile, tiles):
    if Pieces.piece_on_tile(Tile, tiles) is not None:
     piece_to_destroy = Pieces.piece_on_tile(Tile, tiles)
     print(Piece.Team)
     if Pieces.piece_on_tile(Tile, tiles).Team != Piece.Team:
        Pieces.pieces_to_render.remove(piece_to_destroy)
        