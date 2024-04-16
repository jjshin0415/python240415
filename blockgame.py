import pygame
import random

pygame.init()

# 게임 화면 설정
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 설정
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 패들 설정
paddle_width = 500  #  게임시간 연장 
paddle_height = 10
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - 20, paddle_width, paddle_height)

# 볼 설정
ball = pygame.Rect(screen_width // 2 - 15, screen_height // 2 - 15, 30, 30)
ball_speed_x = 4 * random.choice([-1, 1])
ball_speed_y = 4 * random.choice([-1, 1])

# 블록 설정
block_list = [pygame.Rect(50 + 110 * i, 30 + 50 * j, 100, 30) for i in range(5) for j in range(3)]

# 게임 실행
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= 5
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += 5

    # 볼 움직임
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # 볼이 벽에 닿으면 튕기기
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # 볼이 패들에 닿으면 튕기기
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y

    # 볼이 화면 아래로 떨어지면 게임 오버
    if ball.bottom >= screen_height:
        running = False

    # 볼이 블록에 닿으면 블록 제거
    block_hit_list = [block for block in block_list if ball.colliderect(block)]
    for block in block_hit_list:
        ball_speed_y = -ball_speed_y
        block_list.remove(block)

    # 화면 그리기
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle)
    pygame.draw.ellipse(screen, red, ball)
    for block in block_list:
        pygame.draw.rect(screen, green, block)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
