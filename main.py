import Window
import Buttons
import Pieces
import pygame
import GameState
import Board
import MouseActions
import sys



active = True
Board.create_board()
Board.setup_board()

global active_piece 
active_piece =None
offset_x = 17
offset_y = 25

# Glavni main loop, ovde se desavaju provere svakog frejma
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False


        elif event.type == pygame.MOUSEBUTTONDOWN :
           active_piece = MouseActions.OnPieceClicked(Pieces, event.pos,Board,Buttons,) 
           if active_piece is not None:
            active_piece_start_loc = [active_piece.ABSOLUTE_X,active_piece.ABSOLUTE_Y]
             
             

        elif event.type == pygame.MOUSEBUTTONUP and active_piece is not None:
            hasSnapped = MouseActions.snap_to_target(active_piece,50)
            if not hasSnapped:
               active_piece.ABSOLUTE_X = (active_piece_start_loc[0])
               active_piece.ABSOLUTE_Y = (active_piece_start_loc[1])
               active_piece.Collider.x = (active_piece_start_loc[0])
               active_piece.Collider.y = (active_piece_start_loc[1])

            active_piece.IS_MOVED = False
            active_piece = None
            MouseActions.available_tiles_glob.clear()
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
