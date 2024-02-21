import Window
import Buttons
import Pieces
import pygame
import GameState
import Player
import Board
import socket
import MouseActions
import GameFunctions
import threading
import sys
import json
import UI

active = True
Board.create_board()
Board.setup_board()
client_team = None
global active_piece 
active_piece =None
offset_x = 17
offset_y = 25
s = None
has_connected = False
host = 'localhost'
port = 6000
font_path = "./files/fonts/Savigny.ttf"
font= pygame.font.Font(font_path,24)


ScrollBox = UI.UIScrollBox((700, 100),(300, 500),font,(0,0,0))
Input = UI.UITextInput((700,600),(300,30),font,(0,0,0),None, ScrollBox)
Logo = UI.UIImage("./files/images/logo.png",(275,10),(500,75))
current_socket= None

def connect_to_server():
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        global current_socket
        current_socket = s
        print("Connected to Chess Server.")

def chess_client_receive():
        global client_team
        while True:
         data = current_socket.recv(1024).decode('utf-8')
         if not data:
             break
         
         try:
             message = json.loads(data)
             command = message.get('command')

             if command == 'move':
                 MouseActions.update_piece_position_server(message.get('from'), message.get('to'),Board.tiles)
             elif command == 'team':
                client_team = message.get('team')

         except json.JSONDecodeError as e:
          print(f"Error decoding JSON: {e}")



# Glavni main loop, ovde se desavaju provere svakog frejma
while active:
    if has_connected == False:
     connect_to_server()
     receiving_thread = threading.Thread(target=chess_client_receive)
     receiving_thread.start()
     has_connected = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False


        elif event.type == pygame.MOUSEBUTTONDOWN  :
           active_piece = MouseActions.OnPieceClicked(Pieces, event.pos,Board,Buttons, GameState.current_turn,client_team)
           if active_piece is not None:
            active_piece_start_loc = [active_piece.ABSOLUTE_X,active_piece.ABSOLUTE_Y]
             
             

        elif event.type == pygame.MOUSEBUTTONUP and active_piece is not None:
            hasSnapped = MouseActions.snap_to_target(active_piece,50,current_socket)
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

        Input.handle_event(event)
       
   
    
    #Filuje pozadinu da bude bela
    Window.window.fill((41, 68, 81))

    #Crta sve dugmice, u slucaju da postoje 
    Buttons.draw_render_list(Window.window)

    #Crta polja
    Board.render_tiles(Window.window)

    Input.draw(Window.window)
    ScrollBox.draw(Window.window)
    Logo.draw(Window.window)

    #Renderuje figure
    Pieces.render_pieces(Window.window)

    #Apdejtuje ceo displej
    pygame.display.flip()

    


# Izlazak iz igre
pygame.quit()
sys.exit()
