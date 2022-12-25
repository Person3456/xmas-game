import pygame
from random import randint

twentyGifts = []
giftNumber = 1
pos_W_list = []
pos_X_list = []

pos_Z_list = []
pos_Y_list = []


gameStarted = False

pygame.init()


x_size, y_size = 1200, 600
screen = pygame.display.set_mode((x_size, y_size))
screen = pygame.display.set_mode((x_size, y_size), pygame.RESIZABLE)

#Sprite starting position, needed so sprite can move without going off screen
spriteLeftSide = 550
spriteTopSide = 250
spriteRightSide = 600
spriteBottomSide = 340



#Creating image variables
present_image = pygame.image.load('namedSimple_present.png').convert_alpha()

santa_image = pygame.image.load('mediumSanta_sprite.png').convert_alpha()

class Sprite(pygame.sprite.Sprite):

    def __init__(self, start_x, start_y, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.update(start_x, start_y, self.rect.width, self.rect.height)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def playerControl(self, dx, dy):
        self.rect = self.rect.move(dx, dy)



class Player(pygame.sprite.Sprite):
    #Creating player sprite
    def __init__(self, width, height, pos_x, pos_y, colour):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load('mediumSanta_sprite.png').convert_alpha()
        self.rect = self.image.get_rect()
        #Allows sprite position to be updated

        self.rect.update(spriteLeftSide, spriteTopSide, spriteBottomSide, spriteRightSide) 
    #Draw function for player sprite
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    #Movement function for player sprite
    def playerControl(self, dx, dy):
        self.rect = self.rect.move(dx, dy)




#Button Class
class Button():
    def __init__(self, x, y, width, height, image):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def is_inside(self, x, y):
        if x < self.rect.x:
            return False

        if y < self.rect.y:
            return False

        if x > self.rect.x + self.rect.width:
            return False

        if y > self.rect.y + self.rect.height:
            return  False

        return True



class Gift(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_X, pos_Y, image):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image = (pos_X, pos_Y)
        self.image = pygame.image.load(giftImage).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.update(pos_X, pos_Y, pos_Z, pos_W)


    def draw(self):
            screen.blit(self.image, (self.rect.pos_X, self.rect.pos_Y))




#Allows constant movement when holding wasd
pygame.key.set_repeat(16, 16)

# #Player sprite size, position and colour
player = Sprite(x_size//2, y_size//2, 'mediumSanta_sprite.png')

#Mini game gift positions
minigameGift = "", giftNumber

gift_group = pygame.sprite.Group()
for i in range(20):
        pos_X = randint(50, x_size - 50)
        pos_W = pos_X + 50
        pos_Y = randint(50, y_size - 50)
        pos_Z = pos_Y + 50

        pos_X_list.append(pos_X)
        pos_W_list.append(pos_W)
        pos_Y_list.append(pos_Y)
        pos_Z_list.append(pos_Z)

        if giftNumber < 6:
            giftImage = "purpleMinigame_gift.png"

        elif 5 < giftNumber < 11:
            giftImage = "blueMinigame_gift.png"

        elif 10 < giftNumber < 16:
            giftImage = "yellowMinigame_gift.png"

        elif 15 < giftNumber < 21:
            giftImage = "greenMinigame_gift.png"

       
        giftPos = (pos_X, pos_Y)
        twentyGifts.append(giftPos)
        
        minigameGift = Sprite(pos_X, pos_Y, giftImage)
        gift_group.add(minigameGift)
        giftNumber = giftNumber + 1

# #Need so can draw player sprite
player_group = pygame.sprite.Group()
player_group.add(player)

#create button instances
present_button = Button((x_size//2)-142, (y_size//2)-101, 284, 202, present_image)
present_buttonY = (y_size//2)-150



if __name__ == "__main__":


    clock = pygame.time.Clock()
    done = False
    clickNum = 0


    while not done and not gameStarted:
        bg = pygame.image.load("merryChristmas_bg.png")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONUP:
                bgClick = True

                if bgClick and clickNum == 0:
                    pygame.mixer.music.load("merryChristmas_audio.mp3")
                    pygame.mixer.music.play()
                    clickNum = clickNum +1

                elif bgClick and clickNum == 1:
                    pygame.mixer.music.stop()
                    gameStarted = True

        screen.blit(bg, (0, 0))
        pygame.display.flip()
        clock.tick(60)

#*********************
    
    

    clock = pygame.time.Clock()
    done = False
    times = 0
    bgColour = [120, 68, 190]
    
    while not done and gameStarted:
        mx, my = pygame.mouse.get_pos()
        click = False
        keys = pygame.key.get_pressed()

    


        #Allows program to end
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONUP:
                click = True

            #Event for wasd sprite movement
            if event.type == pygame.KEYDOWN:

                #Incase of need for sudden shutdown
                if keys[pygame.K_p]:
                    done = True
            
                #Moves left if player presses a and is not about to go off screen
                if keys[pygame.K_a] and spriteLeftSide != 0:
                    player.playerControl(-1, 0)
                    spriteLeftSide = spriteLeftSide -1
                    spriteRightSide = spriteRightSide -1

                    print("spriteLeftSide", spriteLeftSide, "\n", "spriteRightSide", spriteRightSide, "\n", "spriteTopSide", spriteTopSide, "\n", "spriteBottomSide", spriteBottomSide)

      
                #Moves down if player presses s and is not about to go off screen
                if keys[pygame.K_s] and spriteBottomSide != y_size:
                    player.playerControl(0, 1)
                    spriteBottomSide = spriteBottomSide +1
                    spriteTopSide = spriteTopSide+1

                    print("spriteLeftSide", spriteLeftSide, "\n", "spriteRightSide", spriteRightSide, "\n", "spriteTopSide", spriteTopSide, "\n", "spriteBottomSide", spriteBottomSide)


                #Moves right if player presses d and is not about to go off screen
                if keys[pygame.K_d] and spriteRightSide != x_size:
                    player.playerControl(1, 0)
                    spriteRightSide = spriteRightSide +1
                    spriteLeftSide = spriteLeftSide +1

                    print("spriteLeftSide", spriteLeftSide, "\n", "spriteRightSide", spriteRightSide, "\n", "spriteTopSide", spriteTopSide, "\n", "spriteBottomSide", spriteBottomSide)


                #Moves upwards if player presses w and is not about to go off screen
                if keys[pygame.K_w] and spriteTopSide != 0:
                    player.playerControl(0, -1)
                    spriteTopSide = spriteTopSide -1
                    spriteBottomSide = spriteBottomSide -1

                    print("spriteLeftSide", spriteLeftSide, "\n", "spriteRightSide", spriteRightSide, "\n", "spriteTopSide", spriteTopSide, "\n", "spriteBottomSide", spriteBottomSide)\

        



        #Fills screen and draws the present button
        screen.fill(bgColour)

       
        present_button.draw()

        

        #If clicking the present button for the first time, the button image chsnges to a console, a jingle plays
        if click and times == 0 and present_button.is_inside(mx, my):
            pygame.time.delay(500)
            present_image = pygame.image.load('simple_console.png').convert_alpha()
            present_button = Button((x_size//2)-300, (y_size//2)-150, 600, 300, present_image)
            pygame.mixer.music.load('console_jingle.mp3')
            pygame.mixer.music.play()
            times = times +1


        #If clicking the present button (console) for the second time then moves present button to bottom of the screen and changes colour of background
        elif click and times == 1 and present_button.is_inside(mx, my):
            bg = pygame.image.load("giftCollectingInstructions_bg.png")
            screen.blit(bg, (0, 0))
            pygame.display.flip()
            pygame.time.delay(1000)
            present_buttonY += 150

            # if pygame.sprite.collide_rect(present_button, player):
            #     present_image.set_alpha(100)

            present_image.set_alpha(100)
            present_button = Button((x_size//2)-300, present_buttonY, 600, 300, present_image)
            bgColour = [0, 0, 0]
            pygame.mixer.music.load("presentCollecting_tune.mp3")
            pygame.mixer.music.play()
        
            print(gift_group)
            print(pos_W_list)
            print(pos_X_list)
            print(pos_Z_list)
            print(pos_Y_list)

            

            
            gift_group.draw(screen)

            times = times +1
           

        #If clicked the present button 2 or more times draw the player sprite and present button
        
        
        if times >= 2:
            player_group.draw(screen)
            present_button.draw()
            gift_group.draw(screen)
            present_image.set_alpha(100)


            
        
        pygame.sprite.groupcollide(player_group, gift_group, False, True, pygame.sprite.collide_rect_ratio(1.0))

        
        if not gift_group:
            pygame.sprite.Sprite.kill(player)
            present_buttonY += 1
            present_button = Button((x_size//2)-300, present_buttonY, 600, 300, present_image)
            present_button.draw()

        if present_buttonY > y_size:
           
            

            bg = pygame.image.load("finalMerryChristmas_bg.png")
            screen.blit(bg, (0, 0))
            
            

        

        pygame.display.flip()
        clock.tick(60)
        
        
