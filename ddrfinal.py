import pygame
import time
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Constants
WHITE = [255, 255, 255]
GAMELENGTH = 30000  # Game Length in milliSeconds
START_POS = 25
LEFT_POS = 100
UP_POS = 170
DOWN_POS = 240
RIGHT_POS = 310
END_POS = 550
MARGIN = 20


width, height = 480, 640  # Width and Height of the Screen
screen = pygame.display.set_mode((width, height))  # Set up the Screen

# Load the Images of the arrows and the End Box
arrow_u = pygame.image.load("C:\\Users\\msr\\python\\arrow_up.png").convert_alpha()
arrow_d = pygame.image.load("C:\\Users\\msr\\python\\arrow_down.png").convert_alpha()
arrow_l = pygame.image.load("C:\\Users\\msr\\python\\arrow_left.png").convert_alpha()
arrow_r = pygame.image.load("C:\\Users\\msr\\python\\arrow_right.png").convert_alpha()
box = pygame.image.load("C:\\Users\\msr\\python\\box.png").convert_alpha()

### Set up the Release times of the Arrows
release = [
    [0500, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
##    [2650, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
##    [5130, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [7300, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [9400, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [11700, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [13900, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [16200, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [17500, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],

    [18600, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [19400, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [20600, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [21600, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [25400, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    
    [26600, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [27500, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [28500, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [29000, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [29900, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [30600, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [31500, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [32300, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [33300, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [34100, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [35200, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [36650, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [37300, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [38000, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],

    [38600, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [39400, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    
    [40200, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [40900, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [41300, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    
    [41900, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [42400, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [43800, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [44600, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [45400, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
    [46400, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [46700, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [47500, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [48500, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [48900, {'image': arrow_r, 'keyType': pygame.K_RIGHT, 'left': RIGHT_POS, 'top': START_POS}],
##    [30833, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [49600, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [51000, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],
    [50600, {'image': arrow_l, 'keyType': pygame.K_LEFT, 'left': LEFT_POS, 'top': START_POS}],
    [51200, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [52300, {'image': arrow_d, 'keyType': pygame.K_DOWN, 'left': DOWN_POS, 'top': START_POS}],
    [53100, {'image': arrow_u, 'keyType': pygame.K_UP, 'left': UP_POS, 'top': START_POS}],

]
key = {pygame.K_LEFT: arrow_l, pygame.K_RIGHT: arrow_r, pygame.K_UP: arrow_u, pygame.K_DOWN: arrow_d}
# Begin Play Music

clock = pygame.time.Clock()


  

    
pygame.mixer.music.load('C:\\Users\\msr\\Documents\\Audacity\\springday3.WAV')
pygame.mixer.music.play(1, 0.0)
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
            if activeArrows<>[]:
                if hit(activeArrows[0]["top"], activeArrows[0]["keyType"], event.key):
                    score += 10
                    activeArrows.pop(0)

         
                else:
                    # print "Failure"
                    score -= 10
            else:
                print"no"

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
        arrow["top"] += 1
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
end_it=False
while (end_it==False):
    screen.fill(WHITE)
    myfont=pygame.font.SysFont("Britannic Bold", 40)
    nlabel=myfont.render("score"+str(score) , 1, (255, 0, 0))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            end_it=True
    screen.blit(nlabel,(100,100))
    pygame.display.flip()
