import pygame

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Constants
WHITE = [255, 255, 255]
GAMELENGTH = 75000  # Game Length in milliSeconds
START_POS = 25
LEFT_POS = 100
UP_POS = 170
DOWN_POS = 240
RIGHT_POS = 310
END_POS = 550
MARGIN = 10

width, height = 480, 640  # Width and Height of the Screen
screen = pygame.display.set_mode((width, height))  # Set up the Screen

# Load the Images of the arrows and the End Box
arrow_u = pygame.image.load("resources/images/arrow_up.png").convert_alpha()
arrow_d = pygame.image.load("resources/images/arrow_down.png").convert_alpha()
arrow_l = pygame.image.load("resources/images/arrow_left.png").convert_alpha()
arrow_r = pygame.image.load("resources/images/arrow_right.png").convert_alpha()
box = pygame.image.load("resources/images/box.png").convert_alpha()

# Set up the Release times of the Arrows
release = [
    [833, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [1666, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [2499, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [3332, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [4165, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [4998, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [5831, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [6664, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [7497, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [8330, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [9163, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [10000, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [10833, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [11666, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [12499, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [13332, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [14165, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [14998, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [15831, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [16664, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [17497, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [18330, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [19163, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [20000, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [20833, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [21666, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [22499, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [23332, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [24165, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [24998, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [25831, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [26664, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [27497, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [28330, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [29163, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [30000, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [30833, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [31666, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [32499, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [33332, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [34165, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [34998, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [35831, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [36664, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [37497, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [38330, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [39163, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [40000, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [40833, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [41666, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [42499, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [43332, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [44165, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [44998, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [45831, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [46664, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [47497, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [48330, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [49163, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [50000, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [50833, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [51666, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [52499, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [53332, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [54165, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [54998, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [55831, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [56664, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [57497, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [58330, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [59163, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [60000, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [60833, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [61666, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [62499, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [63332, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [64165, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [64998, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [65831, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [66664, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [67497, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [68330, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [69163, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [70000, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}]
]
key = {pygame.K_LEFT: arrow_l, pygame.K_RIGHT: arrow_r, pygame.K_UP: arrow_u, pygame.K_DOWN: arrow_d}
# Begin Play Music

pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# End Play Music
score = 0
activeArrows = []
running = 1
exitcode = 0


def hit(top, arrowType, keyType):
    if (END_POS - MARGIN <= top and top <= END_POS + MARGIN) and arrowType == keyType:
        return True
    else:
        return False


while running:
    # Clear screen before drawing it again
    screen.fill(WHITE)
    # Set up the start and end boxes
    screen.blit(arrow_l, (LEFT_POS, START_POS))
    screen.blit(arrow_u, (UP_POS, START_POS))
    screen.blit(arrow_d, (DOWN_POS, START_POS))
    screen.blit(arrow_r, (RIGHT_POS, START_POS))

    screen.blit(box, (LEFT_POS, END_POS))
    screen.blit(box, (UP_POS, END_POS))
    screen.blit(box, (DOWN_POS, END_POS))
    screen.blit(box, (RIGHT_POS, END_POS))

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is then quit the game immediately
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if hit(activeArrows[0]["top"], activeArrows[0]["keyType"], event.key):
                # print "Success"
                score += 10
                activeArrows.pop(0)
            else:
                # print "Failure"
                score -= 10

    # Start Draw clock
    font = pygame.font.SysFont("Courier", 12)
    scoreText = "Score :" + str(score) + " | Time : " + str((GAMELENGTH - pygame.time.get_ticks()) / 60000) + ":" + str(
        (GAMELENGTH - pygame.time.get_ticks()) / 1000 % 60).zfill(2)
    timerText = font.render(scoreText, True, (0, 0, 0))
    textRect = timerText.get_rect()
    textRect.topright = [440, 5]
    screen.blit(timerText, textRect)
    # End Draw Clock

    for arrow in activeArrows:
        arrow["top"] += 5
        if arrow["top"] > END_POS + 50:
            activeArrows.remove(arrow)
        else:
            screen.blit(arrow['image'], (arrow['left'], arrow['top']))

    if pygame.time.get_ticks() >= GAMELENGTH:
        running = 0
        exitcode = 1

    # Add arrows from the release array to the active arrows array
    if len(release) > 0:
        if pygame.time.get_ticks() > release[0][0]:
            activeArrows.append(release[0][1])
            release.pop(0)
    pygame.display.flip()
