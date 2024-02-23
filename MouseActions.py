import pygame
import GameFunctions
import GameState
import json
import time
global available_tiles_glob 
available_tiles_glob = None
def OnPieceClicked(Pieces, event, Board, Buttons,Player,client_team):
    for i, piece in enumerate(Pieces.pieces_to_render):
                 
                 if piece.Collider.collidepoint(event) and piece.Team == Player and piece.Team == client_team:
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


def snap_to_target(piece, range, socket, Board):

    for tiles in available_tiles_glob:
        
        for tile in tiles:
          if piece.Collider.colliderect(tile.Collider):
        
           
           if abs(piece.Collider.x - tile.Collider.x) <= range and \
              abs(piece.Collider.y - tile.Collider.y) <= range:
               piece.Collider.center = tile.Collider.center
               piece.ABSOLUTE_X = tile.ABSOLUTE_X + piece.OFFSET_X
               piece.ABSOLUTE_Y = tile.ABSOLUTE_Y + piece.OFFSET_Y
               piece.HAS_MOVED = True
               
               GameFunctions.can_eat_figure(piece, tile, tiles)
               update_piece_position(piece,tile,socket)
               tile_to_change = GameFunctions.get_piece_check(piece,Board.tiles)
               if tile_to_change is not None:
                 tile_to_change.CachedImage = tile_to_change.Image
                 tile_to_change.Image = Board.check_highlight
                 tile_to_change.Reset_Image = False
                 piece.Tile.CachedImage = piece.Tile.CachedImage
                 piece.Tile.Image = Board.check_highlight
                 piece.Tile.Reset_Image = False
                 send_server_check(piece,tile_to_change, socket)
               else: 
                 for tile_image in Board.tiles:
                  tile_image.Reset_Image = True
                  if tile_image.CachedImage is not None:
                      tile_image.Image = tile_image.CachedImage
     
               return True
        
           
    return False          
    

def send_server_move(socket,BeginTileRegistry,EndTileRegistry):
   start= BeginTileRegistry
   end =  EndTileRegistry
   move = {'command': 'move', 'from': start, 'to': end}
   socket.sendall(json.dumps(move).encode('utf-8'))

def update_piece_position(piece, tile, socket):

    send_server_move(socket,piece.Tile.TileRegistry,tile.TileRegistry)
    piece.Tile.Piece = None
    piece.Tile = tile
    tile.Piece = piece
    GameState.next_turn()

def send_server_check(piece, tile,socket):
    start_check_tile = piece.Tile.TileRegistry
    checked_tile = tile.TileRegistry
    check = {'command' : 'check', 'from':start_check_tile, 'to': checked_tile}
    socket.sendall(json.dumps(check).encode('utf-8'))


def update_piece_position_server(from_target, to_target, tiles):
    
    for tile in tiles:
        if tile.TileRegistry == from_target:
            start_tile=tile
            break
    
    for tile in tiles:
        if tile.TileRegistry == to_target:
            end_tile=tile
    for tile_image in tiles:
                  tile_image.Reset_Image = True
                  if tile_image.CachedImage is not None:
                      tile_image.Image = tile_image.CachedImage
    piece = start_tile.Piece
    piece.Collider.center = end_tile.Collider.center
    piece.ABSOLUTE_X = end_tile.ABSOLUTE_X + piece.OFFSET_X
    piece.ABSOLUTE_Y = end_tile.ABSOLUTE_Y + piece.OFFSET_Y
    GameFunctions.can_eat_figure(piece, end_tile, tiles)
    start_tile.Piece = None
    piece.Tile = end_tile
    end_tile.Piece = piece
    GameState.next_turn()