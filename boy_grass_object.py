from pico2d import *
import random
import os

# (선택) 리소스 경로를 확실히 하고 싶다면:
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# def res(path): return os.path.join(BASE_DIR, path)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')  # load_image(res('grass.png'))

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90
        self.frame = 0
        self.image = load_image('run_animation.png')  # load_image(res('run_animation.png'))

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
        if self.x > 800:  # (선택) 화면 밖으로 나가면 왼쪽에서 다시
            self.x = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')  # 10프레임짜리 시트 가정

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5
        if self.x > 800:
            self.x = 0

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h   # ✅ 여기
        # 원본 크기로 출력
        self.image.clip_draw(self.frame * frame_width, 0,
                             frame_width, frame_height,
                             self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.frame = 0
        self.image = load_image('ball21x21.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

def reset_world():
    global world
    global running
    running = True
    world = []
    global grass
    grass = Grass()
    world.append(grass)
    global team          # ✅ 전역으로 선언
    team = [Boy() for _ in range(10)]
    world += team
    global zombie
    zombie = Zombie()
    world.append(zombie)
    global ball
    ball = [Ball() for _ in range(10)]
    world += ball

reset_world()

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
