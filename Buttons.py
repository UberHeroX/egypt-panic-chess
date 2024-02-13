import pygame
# Boje za bar meni

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (200, 200 ,200)

render_list = []

class Button:
     def __init__ (self, X,Y,SIZE_X,SIZE_Y):
         self.ABSOLUTE_X = X
         self.ABSOLUTE_Y = Y
         self.SIZE_X = SIZE_X
         self.SIZE_Y = SIZE_Y
         self.IS_VISIBILE = True
         self.TEXT = None

     COLOR = None
     ABSOLUTE_X = None
     ABSOLUTE_Y = None
     SIZE_X = None
     SIZE_Y = None
     TEXT = None
     PARENT_WINDOW  = None
     IS_VISIBILE = True
     FONT = None
     FONT_SIZE = 30
     BOUND_FUNCT = None
     TEXT_COLOR = BLACK

     def render(self):
         render_list.append(self)
     def remove(self):
        render_list.remove(self)
        del self
     def bind(self,function):
         self.BOUND_FUNCT = function
     def onClick(self):
         if self.BOUND_FUNCT is not None:
             self.BOUND_FUNCT(self)
         else: 
             print("No function has been bound")
         


# Opcije za meni

menu_options = ["Game", "Edit", "About"]
option_width = 100
option_height = 30

# font

Button1= Button(700,25,100,30)
Button1.TEXT = "Sranje"
Button1.TEXT_COLOR= WHITE
Button1.COLOR = BLACK
Button1.bind(Button.remove)
Button1.render()


font = pygame.font.Font(None, 30)

def draw_button(Button: Button):
    pygame.draw.rect(Button.PARENT_WINDOW,Button.COLOR,(Button.ABSOLUTE_X,Button.ABSOLUTE_Y,Button.SIZE_X,Button.SIZE_Y))
    if Button.TEXT is not None:
        font = pygame.font.Font(Button.FONT, Button.FONT_SIZE)
        text = font.render(Button.TEXT, True, Button.TEXT_COLOR)
        Button.PARENT_WINDOW.blit(text,(Button.ABSOLUTE_X+5,Button.ABSOLUTE_Y+5))
    
    
def draw_button_ellipse(Button: Button):
    pygame.draw.ellipse(Button.PARENT_WINDOW,Button.COLOR,(Button.ABSOLUTE_X,Button.ABSOLUTE_Y,Button.SIZE_X,Button.SIZE_Y))
    if Button.TEXT is not None:
        font = pygame.font.Font(Button.FONT, Button.FONT_SIZE)
        text = font.render(Button.TEXT, True, Button.TEXT_COLOR)
        Button.PARENT_WINDOW.blit(text,(Button.ABSOLUTE_X+5,Button.ABSOLUTE_Y+5))


def draw_render_list(window):
     for i, button in enumerate(render_list):
         button.PARENT_WINDOW = window
         draw_button(button)
        


def check_click(position):
    MOUSE_X, MOUSE_Y = position
    
    for i, button in enumerate(render_list):
      
       if button.IS_VISIBILE == True and button.ABSOLUTE_X < MOUSE_X and button.ABSOLUTE_Y < MOUSE_Y and (button.ABSOLUTE_X + button.SIZE_X) > MOUSE_X and (button.ABSOLUTE_Y + button.SIZE_Y) > MOUSE_Y:
           button.onClick()
       
          