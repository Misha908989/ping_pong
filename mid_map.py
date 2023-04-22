from pygame import*

tvick = (220, 255, 255)
widht = 600
height = 500
window = display.set_mode((widht, height))
window.fill(tvick)

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)