import pygame
import Tile
import Pieces

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (200, 200 ,200)

tile_green = pygame.image.load("./files/tiles/tile_green.png")
tile_beige = pygame.image.load("./files/tiles/tile_beige.png")
Highlight = pygame.image.load("./files/tiles/tile_highlight.png")
check_highlight = pygame.image.load("./files/tiles/check.png")

tile_size = 64
grid_size = (8,8)
start_x, start_y = 50,100

tiles = []

letterings = ["a","b","c","d","e","f","g","h"]

def create_board():
 for row in range(grid_size[0]):
        
            

        for col in range(grid_size[1]):
            # Calculate the position for each tile
            x = start_x + col * 64
            y = start_y + row * 64
            BoardTile = Tile.Tile()
           
            font = pygame.font.Font(None, 20)
            if row % 2 == 0:
             if col % 2 == 0:
              BoardTile.Image = tile_beige
             else:
              BoardTile.Image = tile_green
            else:
               if col % 2 == 0:
                BoardTile.Image = tile_green
               else:
                BoardTile.Image = tile_beige
             
            
            BoardTile.Row = row
            BoardTile.Column = col
            BoardTile.ABSOLUTE_X = x
            BoardTile.ABSOLUTE_Y = y
            BoardTile.create_collider()
            
            if row == grid_size[1]-1 and col%2==0:
              text = letterings[col]
              BoardTile.TEXT_COL = font.render(str(text), True, (236,236,213))
            
            elif row ==grid_size[1]-1:
               text = letterings[col]
               BoardTile.TEXT_COL = font.render(str(text), True, (114,141,86))

            if col == 0 and row%2==0:
              text = 8-row
              
              BoardTile.TEXT_COLOR = (114,141,86)
              BoardTile.TEXT_ROW = font.render(str(text), True, (114,141,86))
              
            elif col == 0:
              text = 8-row
              BoardTile.TEXT_COLOR =  (236,236,213)
              BoardTile.TEXT_ROW = font.render(str(text), True, (236,236,213))
             
            rowRegistry = letterings[col] 
            BoardTile.TileRegistry = "".join((str(rowRegistry),str(8-row))) 

            
            tiles.append(BoardTile)

def setup_board():
  for i, tile in enumerate(tiles):
    #white pawns
    if tile.Row == 6:
      Pieces.pieces_to_render.append(Pieces.setup_pawn("White", tile.ABSOLUTE_X + 15, tile.ABSOLUTE_Y + 5, tile))
    #black pawns
    if tile.Row == 1:
      Pieces.pieces_to_render.append(Pieces.setup_pawn("Black", tile.ABSOLUTE_X + 15, tile.ABSOLUTE_Y + 5, tile))
    #white rooks
    if tile.Row == 7 and (tile.Column == 0 or tile.Column == 7):
      Pieces.pieces_to_render.append(Pieces.setup_rook("White", tile.ABSOLUTE_X + 13, tile.ABSOLUTE_Y + 5, tile))
    #black rooks
    if tile.Row == 0 and (tile.Column == 0 or tile.Column == 7):
      Pieces.pieces_to_render.append(Pieces.setup_rook("Black", tile.ABSOLUTE_X + 13, tile.ABSOLUTE_Y + 5, tile))
    #white knight
    if tile.Row == 7 and (tile.Column == 1 or tile.Column == 6):
      Pieces.pieces_to_render.append(Pieces.setup_knight("White", tile.ABSOLUTE_X + 8, tile.ABSOLUTE_Y + 5, tile))
    #black knight
    if tile.Row == 0 and (tile.Column == 1 or tile.Column == 6):
      Pieces.pieces_to_render.append(Pieces.setup_knight("Black", tile.ABSOLUTE_X + 8, tile.ABSOLUTE_Y + 5, tile))
    #white bishop
    if tile.Row == 7 and (tile.Column == 2 or tile.Column == 5):
      Pieces.pieces_to_render.append(Pieces.setup_bishop("White", tile.ABSOLUTE_X + 11, tile.ABSOLUTE_Y + 5, tile))
    #black bishop
    if tile.Row == 0 and (tile.Column == 2 or tile.Column == 5):
      Pieces.pieces_to_render.append(Pieces.setup_bishop("Black", tile.ABSOLUTE_X + 11, tile.ABSOLUTE_Y + 5, tile))
    #white bishop
    if tile.Row == 7 and tile.Column == 3 :
      Pieces.pieces_to_render.append(Pieces.setup_queen("White", tile.ABSOLUTE_X + 8, tile.ABSOLUTE_Y + 5, tile))
    #black bishop
    if tile.Row == 0 and tile.Column == 3 :
      Pieces.pieces_to_render.append(Pieces.setup_queen("Black", tile.ABSOLUTE_X + 8, tile.ABSOLUTE_Y + 5, tile))
    #white king
    if tile.Row == 7 and tile.Column == 4 :
      Pieces.pieces_to_render.append(Pieces.setup_king("White", tile.ABSOLUTE_X + 11, tile.ABSOLUTE_Y + 5, tile))
    #black king
    if tile.Row == 0 and tile.Column == 4 :
      Pieces.pieces_to_render.append(Pieces.setup_king("Black", tile.ABSOLUTE_X + 11, tile.ABSOLUTE_Y + 5, tile))

    for i, piece in enumerate(Pieces.pieces_to_render):
      piece.create_collider()

def render_tiles(window):
  for i, tile in enumerate(tiles):
    window.blit(tile.Image,(tile.ABSOLUTE_X,tile.ABSOLUTE_Y))
    if tile.TEXT_ROW is not None:
        window.blit(tile.TEXT_ROW, (tile.ABSOLUTE_X +5, tile.ABSOLUTE_Y + 5 ))
    if tile.TEXT_COL is not None:
        window.blit(tile.TEXT_COL, (tile.ABSOLUTE_X +50, tile.ABSOLUTE_Y + 50 ))
   


  

   


