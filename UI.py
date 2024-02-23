import pygame
import time
import threading
import json
class UIElement:
    def __init__(self, parent=None):
        self.children = []
        self.parent = parent
        if parent:
            parent.add_child(self)
    
    def add_child(self, child):
        self.children.append(child)
    
    def draw(self, surface):
        for child in self.children:
            child.draw(surface)

class UIImage(UIElement):
    def __init__(self, image_path, position, size, parent=None):
        super().__init__(parent)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.position = position
    
    def draw(self, surface):
        surface.blit(self.image, self.position)
        super().draw(surface)

class UIText(UIElement):
    def __init__(self, text, position, font, color=(255, 255, 255), parent=None):
        super().__init__(parent)
        self.text = text
        self.position = position
        self.font = font
        self.color = color
    
    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, self.position)
        super().draw(surface)
    
class UITextInput(UIElement):
    def __init__(self, position, size, font, socket_in, color=(255, 255, 255), parent=None, scrl_box=None, ):
        super().__init__(parent)
        self.position = position
        self.size = size
        self.font = font
        self.color = color
        self.text = ""
        self.background_color = 220, 220, 220
        self.active = False
        self.scrl_box = scrl_box
        self.deleting = False
        self.socket = socket_in
        self.input_box = pygame.Rect(position[0], position[1], size[0], size[1])
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.background_color, self.input_box)
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, (self.position[0] + 5, self.position[1] + 2))
        super().draw(surface)

    def handle_event(self, event):
        
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.active = not self.active
                self.text = "|"
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            
            if event.key == pygame.K_BACKSPACE:
                
                self.text = self.text[:-1]
            elif event.key != pygame.K_RETURN:
                if len(self.text) == 1 and self.text == "|":
                    self.text = self.text[1:]
                    self.text += event.unicode
                self.text += event.unicode  
        if event.type == pygame.KEYDOWN and self.active:
           if event.key == pygame.K_RETURN:
               self.active = False
               self.scrl_box.add_line(self.text)
               
               message = {'command': 'chat', 'message': self.text}
               self.socket.sendall(json.dumps(message).encode('utf-8'))
               self.text = ""
        

   
        


class UIScrollBox(UIElement):
    def __init__(self, position, size, font, color=(255, 255, 255), parent=None):
        super().__init__(parent)
        self.position = position
        self.size = size
        self.font = font
        self.color = color
        self.lines = []
        self.background_color = (253, 245, 230)
        self.offset = 0 
    
    class line:
        text = None
        color = None

    def add_line(self, text, color= (0,0,0)):
        line = self.line()
        line.text = text
        line.color = color


        self.lines.append(line)
    
    def draw(self, surface):
        box_rect = pygame.Rect(self.position, self.size)
        pygame.draw.rect(surface, self.background_color, box_rect)  
        for i, line in enumerate(self.lines[-10:]): 
            text_surface = self.font.render(line.text, True, line.color)
            surface.blit(text_surface, (self.position[0] + 5, self.position[1] + 5 + i * 20))
        super().draw(surface)