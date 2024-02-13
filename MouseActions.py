import pygame

global available_tiles_glob 
available_tiles_glob = None
def OnPieceClicked(Pieces, event, Board, Buttons):
    for i, piece in enumerate(Pieces.pieces_to_render):
                 
                 if piece.Collider.collidepoint(event):
                    active_piece = piece 
                    piece.IS_MOVED = True
                    mouse_x, mouse_y = event
                    available_tiles = Pieces.get_piece_available_tiles(active_piece, Board.tiles)
                    global available_tiles_glob 
                    available_tiles_glob = available_tiles
                    for tiles in available_tiles:
                        for tile in tiles:
                            tile.CachedImage = tile.Image
                            tile.Image= Board.Highlight

                    return active_piece
                 
                 Buttons.check_click(event)


def snap_to_target(piece, range):

    for tiles in available_tiles_glob:
        
        for tile in tiles:
          if piece.Collider.colliderect(tile.Collider):
        
           print(tile.Row)
           if abs(piece.Collider.x - tile.Collider.x) <= range and \
              abs(piece.Collider.y - tile.Collider.y) <= range:
               piece.Collider.center = tile.Collider.center
               piece.ABSOLUTE_X = tile.ABSOLUTE_X + piece.OFFSET_X
               piece.ABSOLUTE_Y = tile.ABSOLUTE_Y + piece.OFFSET_Y
               piece.HAS_MOVED = True
               return True
           
    return False          
    

                 
   

