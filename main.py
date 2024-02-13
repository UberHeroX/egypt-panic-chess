import Window
import Buttons
import Pieces
import pygame
import GameState
import Board
import sys



active = True
Board.create_board()
Board.setup_board()
active_piece= None
Highlight = pygame.image.load("./files/tiles/tile_highlight.png")
# Glavni main loop, ovde se desavaju provere svakog frejma
offset_x = 17
offset_y = 25
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False


        elif event.type == pygame.MOUSEBUTTONDOWN :
             
             for i, piece in enumerate(Pieces.pieces_to_render):
                 
                 if piece.Collider.collidepoint(event.pos):
                    active_piece = piece 
                    piece.IS_MOVED = True
                    mouse_x, mouse_y = event.pos
                    available_tiles = Pieces.get_piece_available_tiles(active_piece, Board.tiles)
                    
                    for tiles in available_tiles:
                        for tile in tiles:
                            tile.CachedImage = tile.Image
                            tile.Image= Highlight
                 Buttons.check_click(event.pos)


        elif event.type == pygame.MOUSEBUTTONUP and active_piece is not None:
            active_piece.IS_MOVED = False
            for tile in Board.tiles:
                if tile.CachedImage is not None:
                    tile.Image = tile.CachedImage

                
            
        elif active_piece is not None:
         if event.type == pygame.MOUSEMOTION and active_piece.IS_MOVED:

            mouse_x, mouse_y = event.pos
            active_piece.ABSOLUTE_X = mouse_x - offset_x
            active_piece.ABSOLUTE_Y = mouse_y - offset_y
            active_piece.Collider.x = mouse_x - offset_x
            active_piece.Collider.y = mouse_y - offset_y


    #Filuje pozadinu da bude bela
    Window.window.fill(Buttons.WHITE)

    #Crta sve dugmice, u slucaju da postoje 
    Buttons.draw_render_list(Window.window)

    #Crta polja
    Board.render_tiles(Window.window)
    
    #Renderuje figure
    Pieces.render_pieces(Window.window)

    #Apdejtuje ceo displej
    pygame.display.flip()

# Izlazak iz igre
pygame.quit()
sys.exit()
