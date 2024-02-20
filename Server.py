import socket
import threading
import json
import time


class Player:
    def __init__(self, conn, addr, side=None):
        self.conn = conn
        self.addr = addr
        self.side = side  



class ChessServer:
    def __init__(self, host='localhost', port=6000):
        self.players = []
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
    
    def listen_for_clients(self):
        self.sock.listen()
        print("Chess Server listening for connections...")
        
        while len(self.players) < 2:  
            conn, addr = self.sock.accept()
            if len(self.players) == 0:
                player = Player(conn, addr, side='white')
                team_command = {'command': 'team', 'team':'White'}
                player.conn.sendall(json.dumps(team_command).encode('utf-8'))
            else:
                player = Player(conn, addr, side='black')
                team_command = {'command': 'team', 'team':'Black'}
                player.conn.sendall(json.dumps(team_command).encode('utf-8'))
            self.players.append(player)
            threading.Thread(target=self.handle_client, args=(player,)).start()
            
            print(f"Player connected from {addr}, assigned as {player.side}")

    def handle_client(self, player):
       
        while True:
            try:
                data = player.conn.recv(1024).decode('utf-8')
                print(data)
                if not data:
                    break  # Connection closed
                self.relay_move(player, data)
                
            except ConnectionResetError:
                break  # Handle client disconnect
            except Exception as e:
                print(f"Error: {e}")
                break
        
        # Remove player from list and close connection
        self.players.remove(player)
        player.conn.close()
        print(f"Player {player.side} disconnected.")

    def relay_move(self, sender, data):
        for player in self.players:
            if player != sender:
                player.conn.sendall(data.encode('utf-8'))

if __name__ == "__main__":
    server = ChessServer()
    server.listen_for_clients()