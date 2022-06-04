import pygame
pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Turtle Code")

x = 50
y = 50
width = 40
height = 60
mov = 5

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > mov:
        x -= mov
    if keys[pygame.K_RIGHT] and x < 500 - mov - width:
        x +=mov

    if not(isJump):
        if keys[pygame.K_UP] and y > mov:
            y -= mov
        if keys[pygame.K_DOWN] and y < 500 - height - mov:
            y += mov
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    window.fill((0,0,0))

    pygame.draw.rect(window, (0,255,0), (x,y,width,height))
    pygame.display.update()

pygame.quit()