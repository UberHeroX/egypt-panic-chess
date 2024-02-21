import pygame

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
    def __init__(self, position, size, font, color=(255, 255, 255), parent=None, scrl_box=None):
        super().__init__(parent)
        self.position = position
        self.size = size
        self.font = font
        self.color = color
        self.text = ""
        self.background_color = 220, 220, 220
        self.active = False
        self.scrl_box = scrl_box
        # Define the input box rect here based on position and size
        self.input_box = pygame.Rect(position[0], position[1], size[0], size[1])
    
    def draw(self, surface):
        # Use self.input_box instead of creating a new Rect
        pygame.draw.rect(surface, self.background_color, self.input_box)
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, (self.position[0] + 5, self.position[1] + 2))
        super().draw(surface)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the self.input_box rect
            if self.input_box.collidepoint(event.pos):
                # Toggle the active state
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]  # Remove the last character
            elif event.key != pygame.K_RETURN:
                self.text += event.unicode  # Add the typed character
        if event.type == pygame.KEYDOWN and self.active:
           if event.key == pygame.K_RETURN:
               self.active = False
               self.scrl_box.add_line(self.text)
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
        self.offset = 0  # Used for scrolling
    
    def add_line(self, text):
        self.lines.append(text)
    
    def draw(self, surface):
        box_rect = pygame.Rect(self.position, self.size)
        pygame.draw.rect(surface, self.background_color, box_rect)  # Draw the background
        for i, line in enumerate(self.lines[-10:]):  # Only draw the last 10 lines
            text_surface = self.font.render(line, True, self.color)
            surface.blit(text_surface, (self.position[0] + 5, self.position[1] + 5 + i * 20))
        super().draw(surface)