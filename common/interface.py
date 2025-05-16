from .config import *

glabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (200, 20)), text=f"Gravity magnitude: {gmag}", manager=manager)
gslider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0, 20), (200, 20)), start_value=gmag, value_range=(-10, 10), manager=manager)

deglabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 40), (200, 20)), text=f"Gravity angle: {deg - 90}", manager=manager)
degslider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0, 60), (200, 20)), start_value=deg - 90, value_range=(-180, 180), manager=manager)

restlabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 80), (200, 20)), text=f"Restitution: {restitution}", manager=manager)
restslider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0, 100), (200, 20)), start_value=restitution * 10, value_range=(0, 10), manager=manager)

friclabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 120), (200, 20)), text=f"Friction: {friction}", manager=manager)
fricslider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0, 140), (200, 20)), start_value=friction * 10, value_range=(0, 10), manager=manager)