import pygame

N_TRIALS = 10 # total number of trials
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
    line1 = myfont.render("You will have to press the left arrow key or the right arrow key as randomly as you can a 100 times.", 1, pygame.Color('white'))
    line2 = myfont.render("Press the space bar to start.", 1, pygame.Color('white'))
    screen.blit(line1, (x, y))
    screen.blit(line2, (x, y + 60))
    pygame.display.flip()

def wait_for_keypress():
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_pressed = True

def Left_or_right():
    status = False
    key_pressed = 0
    while not status:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    key_pressed = "Left"
                    status = True
                if event.key == pygame.K_RIGHT:
                    key_pressed = "Right"
                    status = True
    return key_pressed

def save_data(waiting_times, filename=RESULT_FILE):
    with open(filename, 'wt') as f:
        f.write('Wait\n')
        for wt in zip(waiting_times[5:]):
            f.write(f"{wt}\n")

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

for i_trial in range(N_TRIALS):
    clear_screen(screen)
    key_pressed = Left_or_right()
    Responses.append(key_pressed)
    print(i_trial, key_pressed)

save_data(Responses)
pygame.quit()