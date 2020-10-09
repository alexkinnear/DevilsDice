import pygame


class Button:

    def __init__(self, dis, color, x, y, width, height, action):
        self.dis = dis
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.action = None

    def draw(self):
        shaded_color = (self.color[0] + 25, self.color[1] + 25, self.color[2] + 25)
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height:
            pygame.draw.rect(self.dis, self.color, [self.x, self.y, self.width, self.height])
        else:
            pygame.draw.rect(self.dis, shaded_color, [self.x, self.y, self.width, self.height])

    def add_text(self, text, font_size, color):
        font = pygame.font.SysFont(None, font_size)
        text_obj = font.render(text, True, color)
        self.dis.blit(text_obj, (self.x + self.width/2 - 35, self.y + self.height/2 - 15))

    def isInside(self):
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height:
            return True
        else:
            return False
