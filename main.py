import pygame
import random
def main():
    #screen settings and basic commands
    start = False
    pygame.display.set_caption("jakies gowno")
    pygame.init()
    clock = pygame.time.Clock()
    X=800
    Y=600
    screen = pygame.display.set_mode((X, Y)  )
    running=True
    #player and other objects
    player_pos = pygame.Vector2(X/4, Y/2)
    default_X=X
    default_Y=0
    obstacle_pos = pygame.Vector2(default_X, default_Y)
    #hole in pipe position
    Y1 = random.uniform(0, Y - 201)
    Y2 = Y1 + 200
    Obstacles=[[obstacle_pos, Y1, Y2]]
    #score and other variables
    score=0
    check=False
    font = pygame.font.Font('slkscr.ttf', 40)
    seconds1=0
    while running:
        screen.fill((0, 0, 0))
        #other screen settings
        keys=pygame.key.get_pressed()
        if keys[pygame.K_F12]:
            pygame.display.toggle_fullscreen()
        #time related things
        clock.tick(60)
        dt = clock.tick(60) / 1000
        seconds=pygame.time.get_ticks()/1000
        #leaving game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        #draw game
        if keys[pygame.K_p]:
            start=True
        if start:
            for XY in Obstacles:
                XY[0][0]-=700*dt
            if keys[pygame.K_SPACE] and seconds-seconds1>0.1 and push==False:
                seconds1=seconds
                player_pos.y-=5000*dt
            else:
                player_pos.y +=700 * dt
        pygame.draw.rect(screen, (255,255,255), (player_pos.x, player_pos.y, 30, 30), 0)
        #drawing multiple obstacles
        for XY in Obstacles:
            pygame.draw.lines(screen, (255, 255, 255), False, ((XY[0][0], XY[0][1]), (XY[0][0], XY[1])), X//10)
            pygame.draw.lines(screen, (255, 255, 255), False, ((XY[0][0], XY[2]),(XY[0][0], Y)), X//10)
        if Obstacles[0][0][0]<=X/2+50 and len(Obstacles)==1:
            Ytmp1 = random.uniform(0, Y - 201)
            Ytmp2 = Ytmp1 + 200
            Obstacles.append([pygame.Vector2(default_X, default_Y), Ytmp1,Ytmp2])
        if Obstacles[0][0][0]<=1:
            Obstacles.pop(0)
            check=False
        #death
        if player_pos.y>Y-30  or player_pos.y<30 :
            running=False
        if (Obstacles[0][0][0]-X//20 <=player_pos.x+30 and (Obstacles[0][0][1]+Obstacles[0][2]<=player_pos.y+30 or Obstacles[0][1]>=player_pos.y)) and Obstacles[0][0][0]+X//20 >= player_pos.x:
            running=False
        #score
        if int(Obstacles[0][0][0])<=int(player_pos.x) and check==False:
            score+=1
            check=True
        scoredisplay = font.render(str(score), True, (255, 255, 255), (0, 0, 0))
        rect = scoredisplay.get_rect()
        rect.center = (X // 2, Y // 10)
        screen.blit(scoredisplay, rect)
        pygame.display.flip()
        push=keys[pygame.K_SPACE]
if __name__ == '__main__':
    main()