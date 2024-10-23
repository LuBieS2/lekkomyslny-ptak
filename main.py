import pygame
import random
def draw_text(text, color, background_color, x, y, screen, font, size):
    if font != "":
        font = pygame.font.Font(font, size)
    name = font.render(text, True, color, background_color)
    rect = name.get_rect()
    rect.center = (x, y)
    screen.blit(name, rect)
def main():
    #screen settings and basic commands
    pygame.display.set_caption("jakies gowno")
    pygame.init()
    clock = pygame.time.Clock()
    X=800
    Y=600
    screen = pygame.display.set_mode((X, Y)  )
    running=False
    start_screen=True
    restart_screen=False
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
    push=False
    #variables related to menu buttons
    color1 = "white"
    bcolor1 = "black"
    color2 = "white"
    bcolor2 = "black"
    first_button=False
    second_button=False

    while start_screen:
        screen.fill((0, 0, 0))
        keys=pygame.key.get_pressed()
        if keys[pygame.K_F12]:
            pygame.display.toggle_fullscreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_screen=False
        #drawing text and buttons
        draw_text("LEKKO MYSLNY PTAK", "white", "black", X//2, Y//4, screen, "slkscr.ttf", 60)
        draw_text("by mammon industries", "white", "black", X//10, Y*19//20, screen, "slkscr.ttf", 10)
        pygame.draw.rect(screen, (255, 255, 255), (X/2-110, Y/2, 220, 80))
        draw_text("Start", color1, bcolor1, X//2, Y//2+40, screen, "slkscr.ttf", 60)
        pygame.draw.rect(screen, (255, 255, 255), (X/2-110, Y/2+100, 220, 80), 0)
        draw_text("Quit", color2, bcolor2, X//2, Y//2+140, screen, "slkscr.ttf", 60)
        if keys[pygame.K_UP]:
            first_button=True
            second_button=False
        elif keys[pygame.K_DOWN]:
            first_button=False
            second_button=True
        if first_button:
            color1="black"
            bcolor1="white"
            color2 = "white"
            bcolor2 = "black"
            if keys[pygame.K_SPACE]:
                start_screen=False
                running=True
        if second_button:
            color2="black"
            bcolor2="white"
            color1 = "white"
            bcolor1 = "black"
            if keys[pygame.K_SPACE]:
                start_screen=False
        pygame.display.flip()
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
        speed=0
        max_speed=1500
        for XY in Obstacles:
            XY[0][0]-=700*dt
        if keys[pygame.K_SPACE] and seconds-seconds1>0.1 and push==False:
            seconds1=seconds
            player_pos.y-=3350*dt
            speed=0
        else:
            if speed<max_speed:
                speed=1050*(seconds-seconds1)
            else:
                speed=max_speed
            player_pos.y+=speed*dt

        pygame.draw.rect(screen, (255,255,255), (player_pos.x, player_pos.y, 30, 30), 0)
        #drawing multiple obstacles
        for XY in Obstacles:
            pygame.draw.lines(screen, (255, 255, 255), False, ((XY[0][0], XY[0][1]), (XY[0][0], XY[1])), X//10)
            pygame.draw.lines(screen, (255, 255, 255), False, ((XY[0][0], XY[2]),(XY[0][0], Y)), X//10)
        if Obstacles[0][0][0]<=X/2+50 and len(Obstacles)==1:
            Ytmp1 = random.uniform(0, Y - 151)
            Ytmp2 = Ytmp1 + 150
            Obstacles.append([pygame.Vector2(default_X, default_Y), Ytmp1,Ytmp2])
        if Obstacles[0][0][0]<=1:
            Obstacles.pop(0)
            check=False
        #death
        if player_pos.y>Y-30  or player_pos.y<30 :
            running=False
            restart_screen=True
        if (Obstacles[0][0][0]-X//20 <=player_pos.x+30 and (Obstacles[0][0][1]+Obstacles[0][2]<=player_pos.y+30 or Obstacles[0][1]>=player_pos.y)) and Obstacles[0][0][0]+X//20 >= player_pos.x:
            running=False
            restart_screen=True
        #score
        if int(Obstacles[0][0][0])<=int(player_pos.x) and check==False:
            score+=1
            check=True
        draw_text(str(score), "white", "black", X//2, Y//10, screen, "slkscr.ttf",50)
        pygame.display.flip()
        push=keys[pygame.K_SPACE]
        while restart_screen:
            screen.fill((0, 0, 0))
            keys=pygame.key.get_pressed()
            if keys[pygame.K_F12]:
                pygame.display.toggle_fullscreen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart_screen=False
            #drawing text and buttons
            draw_text("YOU LOSE", "white", "black", X//2, Y//4, screen, "slkscr.ttf", 60)
            draw_text("score "+str(score), "white", "black", X//2, Y//4+50, screen, "slkscr.ttf", 20)
            pygame.draw.rect(screen, (255, 255, 255), (X/2-110, Y/2, 220, 80))
            draw_text("Reset", color1, bcolor1, X//2, Y//2+40, screen, "slkscr.ttf", 60)
            pygame.draw.rect(screen, (255, 255, 255), (X/2-110, Y/2+100, 220, 80), 0)
            draw_text("Quit", color2, bcolor2, X//2, Y//2+140, screen, "slkscr.ttf", 60)
            if keys[pygame.K_UP]:
                first_button=True
                second_button=False
            elif keys[pygame.K_DOWN]:
                first_button=False
                second_button=True
            if first_button:
                color1="black"
                bcolor1="white"
                color2 = "white"
                bcolor2 = "black"
                if keys[pygame.K_SPACE]:
                    check=False
                    player_pos.y=Y/2
                    seconds1=seconds
                    score=0
                    default_X = X
                    default_Y = 0
                    obstacle_pos = pygame.Vector2(default_X, default_Y)
                    Y1 = random.uniform(0, Y - 201)
                    Y2 = Y1 + 200
                    Obstacles = [[obstacle_pos, Y1, Y2]]
                    start_screen=False
                    restart_screen=False
                    running=True
            if second_button:
                color2="black"
                bcolor2="white"
                color1 = "white"
                bcolor1 = "black"
                if keys[pygame.K_SPACE]:
                    start_screen=False
                    restart_screen=False
            pygame.display.flip()
if __name__ == '__main__':
    main()