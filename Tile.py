
class Tile:

    Column = None
    Row = None
    Piece = None
    ABSOLUTE_X = None
    ABSOLUTE_Y = None
    Image = None
    TEXT_ROW = None
    TEXT_COLOR = None
    TEXT_COL = None
    
def get_above_tile(Tile: Tile, tiles):
    current_tile = Tile.Tile
    for i, tile in enumerate(tiles):
        if current_tile.Row == tile.Row -1 and current_tile.Column == tile.Column:
            return tile 


def get_below_tile(Tile: Tile, tiles):
    current_tile = Tile.Tile
    for i, tile in enumerate(tiles):
        if current_tile.Row == tile.Row + 1 and current_tile.Column == tile.Column:
            return tile 
        
def get_left_tile(Tile: Tile, tiles):
    current_tile = Tile.Tile
    for i, tile in enumerate(tiles):
        if current_tile.Row == tile.Row and current_tile.Column -1   == tile.Column:
            return tile 
        
def get_right_tile(Tile: Tile, tiles):
    current_tile = Tile.Tile
    for i, tile in enumerate(tiles):
        if current_tile.Row == tile.Row and current_tile.Column  +1 == tile.Column:
            return tile 
        
def get_right_up_diagonal(Tile: Tile, tiles):
    current_tile = Tile.Tile
    for i, tile in enumerate(tiles):
        if current_tile.Row == tile.Row -1 and current_tile.Column +1 == tile.Column:
            return tile 
        
def get_left_up_diagonal(Tile: Tile, tiles):
    current_tile = Tile.Tile
    for i, tile in enumerate(tiles):
        if current_tile.Row == tile.Row -1 and current_tile.Column -1 == tile.Column:
            return tile 
        
def get_right_down_diagonal(Tile: Tile, tiles):
    current_tile = Tile.Tile
    for i, tile in enumerate(tiles):
        if current_tile.Row == tile.Row +1 and current_tile.Column +1 == tile.Column:
            return tile 
        
def get_left_up_diagonal(Tile: Tile, tiles):
    current_tile = Tile.Tile
    for i, tile in enumerate(tiles):
        if current_tile.Row == tile.Row -1 and current_tile.Column -1 == tile.Column:
            return tile 
        

