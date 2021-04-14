import pygame

N_TRIALS = 100 # total number of trials
MAX_RESPONSE_DELAY = 2000
RESULT_FILE = 'Random_input.csv'


def create_window():
    screen = pygame.display.set_mode((1280, 960))
    # screen = pygame.display.set_mode((0, 0),
    #                                  pygame.DOUBLEBUF | pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)
    return screen

def clear_screen(screen):
    screen.fill(pygame.Color('black'))
    pygame.display.flip()

def display_instruction(screen, x, y):
    pygame.font.init()
    myfont = pygame.font.SysFont(pygame.font.get_default_font(), 40)
    line0 = myfont.render("In this experiment, you will be tested on your ability to be random.",1, pygame.Color('white'))
    line1 = myfont.render("You will have to press the left arrow key or the right arrow key", 1, pygame.Color('white'))
    line2 = myfont.render("as randomly as you can for 100 trials.", 1, pygame.Color('white'))
    line3 = myfont.render("Press the space bar to start.", 1, pygame.Color('white'))
    screen.blit(line0, (x, y - 120))
    screen.blit(line1, (x, y - 60))
    screen.blit(line2, (x, y - 30))
    screen.blit(line3, (x, y + 60))
    pygame.display.flip()

def wait_for_keypress():
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_pressed = True

def display_number_trial(screen, x ,y, i):
    pygame.font.init()
    myfont = pygame.font.SysFont(pygame.font.get_default_font(), 40)
    line0 = myfont.render("Trial {}/100".format(i), 1, pygame.Color('white'))
    screen.blit(line0, (x-80, y-120))
    pygame.display.flip()

def present_arrow_right(x, y, color):
    pygame.draw.polygon(screen, color, ((x+30, y+50), (x+30, y+100), (x+130, y+100), (x+130, y+150), (x+180, y+75), (x+130, y), (x+130, y+50)))
    pygame.display.flip()

def present_arrow_left(x, y, color):
    pygame.draw.polygon(screen, color, ((x-30, y+50), (x-30, y+100), (x-130, y+100), (x-130, y+150), (x-180, y+75), (x-130, y), (x-130, y+50)))
    pygame.display.flip()

def Left_or_right():
    status = False
    key_pressed = 0
    while not status:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    key_pressed = "Left"
                    status = True
                    clear_screen(screen)
                    present_arrow_left(center_x, center_y, pygame.Color('white'))
                if event.key == pygame.K_RIGHT:
                    key_pressed = "Right"
                    status = True
                    clear_screen(screen)
                    present_arrow_right(center_x, center_y, pygame.Color('white'))
    return key_pressed

def save_data(array, filename=RESULT_FILE):
    with open(filename, 'wt') as f:
        f.write('Responses\n')
        for resp in zip(array):
            f.write(f"{resp}\n")


##### main

pygame.init()
screen = create_window()
r = screen.get_rect()
W, H = r.width, r.height
center_x = W // 2
center_y = H // 2

Responses = []

display_instruction(screen, 20, center_y)
wait_for_keypress()
clear_screen(screen)

pygame.time.delay(1000)
clear_screen(screen)

for i_trial in range(N_TRIALS):
    display_number_trial(screen, center_x, center_y, i_trial)
    key_pressed = Left_or_right()
    Responses.append(key_pressed)
    print(i_trial, key_pressed)

save_data(Responses)
pygame.quit()