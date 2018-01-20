import pygame

pygame.init()
pygame.mixer.init()

# Constants
WHITE = [255, 255, 255]
GAMELENGTH = 12000  # Game Length in milliSeconds

width, height = 480, 640  # Width and Height of the Screen
screen = pygame.display.set_mode((width, height))  # Set up the Screen

# Load the Images of the arrows and the End Box
arrow_u = pygame.image.load("resources/images/arrow_up.png")
arrow_d = pygame.image.load("resources/images/arrow_down.png")
arrow_l = pygame.image.load("resources/images/arrow_left.png")
arrow_r = pygame.image.load("resources/images/arrow_right.png")
box = pygame.image.load("resources/images/box.png")

# Set up the Release times of the Arrows
release = [
    [1000, {'type': arrow_l, 'left': 100, 'top': 25}],
    [2000, {'type': arrow_u, 'left': 170, 'top': 25}],
    [3000, {'type': arrow_d, 'left': 240, 'top': 25}],
    [4000, {'type': arrow_r, 'left': 310, 'top': 25}],
    [5000, {'type': arrow_l, 'left': 100, 'top': 25}],
    [6000, {'type': arrow_u, 'left': 170, 'top': 25}],
    [7000, {'type': arrow_d, 'left': 240, 'top': 25}],
    [8000, {'type': arrow_r, 'left': 310, 'top': 25}]
]

# Begin Play Music

pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# End Play Music

activeArrows = []
running = 1
exitcode = 0
while running:
    # Clear screen before drawing it again
    screen.fill(WHITE)
    # Set up the start and end boxes
    screen.blit(arrow_l, (100, 25))
    screen.blit(arrow_u, (170, 25))
    screen.blit(arrow_d, (240, 25))
    screen.blit(arrow_r, (310, 25))

    screen.blit(box, (100, 550))
    screen.blit(box, (170, 550))
    screen.blit(box, (240, 550))
    screen.blit(box, (310, 550))

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is then quit the game immediately
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if (
                        540 < activeArrows[0]["top"]
                        or activeArrows[0]["top"] < 560
                ) and activeArrows[0]["type"] == arrow_l:
                    print "Success"
                    activeArrows.pop(0)
                else:
                    print "Failure"
            if event.key == pygame.K_UP:
                if (
                        540 < activeArrows[0]["top"]
                        or activeArrows[0]["top"] < 560
                ) and activeArrows[0]["type"] == arrow_u:
                    print "Success"
                    activeArrows.pop(0)
                else:
                    print "Failure"
            if event.key == pygame.K_DOWN:
                if (
                        540 < activeArrows[0]["top"]
                        or activeArrows[0]["top"] < 560
                ) and activeArrows[0]["type"] == arrow_d:
                    print "Success"
                    activeArrows.pop(0)
                else:
                    print "Failure"
            if event.key == pygame.K_RIGHT:
                if (
                        540 < activeArrows[0]["top"]
                        or activeArrows[0]["top"] < 560
                ) and activeArrows[0]["type"] == arrow_r:
                    print "Success"
                    activeArrows.pop(0)
                else:
                    print "Failure"

    # Start Draw clock
    font = pygame.font.SysFont("Courier", 24)
    timerText = font.render(
        str((GAMELENGTH - pygame.time.get_ticks()) / 60000)
        + ":" + str((GAMELENGTH - pygame.time.get_ticks()) / 1000 % 60).zfill(2),
        True, (0, 0, 0))
    textRect = timerText.get_rect()
    textRect.topright = [440, 5]
    screen.blit(timerText, textRect)
    # End Draw Clock

    for arrow in activeArrows:
        arrow["top"] += 5
        if arrow["top"] > 600:
            activeArrows.remove(arrow)
        else:
            screen.blit(arrow['type'], (arrow['left'], arrow['top']))

    pygame.display.flip()
    if pygame.time.get_ticks() >= GAMELENGTH:
        running = 0
        exitcode = 1

    # Add arrows from the release array to the active arrows array
    if len(release) > 0:
        if pygame.time.get_ticks() > release[0][0]:
            activeArrows.append(release[0][1])
            release.pop(0)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
