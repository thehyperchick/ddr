# import pygame
# gameDisplay = pygame.display.set_mode((800,600))
# pygame.display.set_caption('A bit Racey')
# clock = pygame.time.Clock()
# crashed = False
# while not crashed:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             crashed = True
#         print(event)
#     pygame.display.update()
#     clock.tick(60)
# pygame.quit()
#
# quit()
import pygame, time, thread

pygame.init()
screen = pygame.display.set_mode((1024, 480))
clock = pygame.time.Clock()
done = False
font = pygame.font.SysFont("courier", 24)
starttime = time.time()
kptime = 0
kptype = 0
beat_time = [
    (starttime + 1, pygame.K_LEFT),
    (starttime + 2, pygame.K_LEFT),
    (starttime + 3, pygame.K_LEFT),
    (starttime + 4, pygame.K_LEFT),
    (starttime + 5, pygame.K_LEFT),
    (starttime + 6, pygame.K_LEFT)]
score = 0;
i = 0
def updateScore(keytime, keypressed):
    i = 0
    for item in beat_time:
        if keypressed == item[1]:
            print('{} : {}:{}|{}:{}'.format(i, item[0], keytime, item[1], keypressed))
            if item[0] - 0.08 <= keytime <= item[0] + 0.08:
                print("Strike")
        i = i + 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or
                                             event.key == pygame.K_DOWN or
                                             event.key == pygame.K_LEFT or
                                             event.key == pygame.K_RIGHT):
            kptime = time.time()
            kptype = event.key
            thread.start_new_thread(updateScore, (kptime, kptype))

    screen.fill((255, 255, 255))
    outstring = str(time.time()) + " : " +str(kptime) + " : " + str(kptype) +" : " + str(score)
    text = font.render(outstring + " ", True, (0, 128, 0))
    screen.blit(text, (512 - text.get_width() // 2, 240 - text.get_height() // 2))

    pygame.display.flip()
pygame.quit()
quit()


