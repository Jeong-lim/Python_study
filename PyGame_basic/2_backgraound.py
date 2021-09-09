import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정

screen_width = 480 # 모니터의 해상도에 따라서 달라질 수도 있다. 가로크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Py Game") # 게임 이름

# 배경 이미지 불러오기
# background = pygame.image.load("C:/Users/JLLEE/Desktop/Study/Python/Python_study/PyGame_basic/background.png")


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가
            running = False # 게임이 진행중이 아님
    
    screen.fill((0, 0, 240)) # 배경 그리기

    pygame.display.update() # 게임화면을 다시 그리기
# 이벤트 루프라는 건 프로그램이 종료되지 않게
# 키보드나 마우스가들어오는지 확인하는 과정

# python 종료
pygame.quit()
