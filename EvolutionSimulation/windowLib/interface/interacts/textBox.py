import pygame, pyperclip
from .interact import Interact
from ..visuals.text import Text
from .entity import Entity

class TextBox(Interact):
    TEXT_MARGIN = 20
    CURSOR_BLINK_TIME = 600
    BACKSPACE_SPEED = 9
    SHIFT_CHARS = {"1":"!","2":"@","3":"#",
    "4":"$","5":"%","6":"^","7":"&","8":"*",
    "9":"(","0":")","-":"_","=":"+","`":"~",
     "/": "?", ";": ":", "\\": "\|"}
    def __init__(self, x, y, width, height, triggers, label=None, color=(255, 255, 255), font_size=30, positioner=None):
        super().__init__(label, triggers, True)
        self.entity = Entity(x, y, width, height)
        self.color = color
        self.text = Text(x+TextBox.TEXT_MARGIN, y, "", size=font_size)
        self.text.center_y(self.entity.rect)

        self.selected = False
        self.cursor_blink = True
        self.cursor_timer = pygame.time.get_ticks()

        self.backspace_count = 0

        if positioner:
            positioner.position_interact(self)

    def appendable(self, string):
        text_size = Text.get_text_size(self.text.string + string, size=self.text.size)
        if text_size[0] >= (self.entity.width-TextBox.TEXT_MARGIN*2):
            return False
        return True

    
    def update(self):
        keys = pygame.key.get_pressed()
        if self.selected:
            if keys[pygame.K_BACKSPACE]:
                self.backspace_count += 1
                if self.backspace_count == self.BACKSPACE_SPEED:
                    self.backspace_count = 0
                    if self.text.string:
                        self.text.pop()

    def eventloop(self, event):
        keys = pygame.key.get_pressed()
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.entity.rect.collidepoint(pos):
                self.selected = True
            else:
                self.selected = False

        if self.selected:
            if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                if key_name == "space":
                    if self.appendable(" "):
                        self.text.add(" ")
                elif key_name == "backspace":
                    if self.text.string:
                        self.text.pop()
                elif key_name == "return":
                    self.trigger()
                elif key_name == "v" and event.mod and pygame.KMOD_CTRL:
                    if self.appendable(pyperclip.paste()):
                        self.text.add(pyperclip.paste())

                elif len(key_name) == 1:
                    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                        key_name = key_name.upper()
                        if key_name in TextBox.SHIFT_CHARS.keys():
                            key_name = TextBox.SHIFT_CHARS[key_name]
                    if self.appendable(key_name):
                        self.text.add(key_name)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    self.backspace_count = 0
        
            
        
    def render(self, screen):
        surf = pygame.Surface((self.entity.width, self.entity.height))
        surf.fill(self.color)
        screen.blit(surf, self.entity.get_pos())
        self.text.render(screen)
        if self.selected:
            x = self.entity.x+TextBox.TEXT_MARGIN+self.text.get_width()
            string = ""
            if self.cursor_blink:
                string = "|"
            
            now = pygame.time.get_ticks()
            if now - self.cursor_timer > TextBox.CURSOR_BLINK_TIME:
                self.cursor_blink = not self.cursor_blink
                self.cursor_timer = now
            

            text = Text(x, 0, string)
            text.center_y(self.entity.rect)
            text.render(screen)

    def get(self):
        return self.text.string
        