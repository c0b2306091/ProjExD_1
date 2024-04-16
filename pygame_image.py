import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    Fscreen = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img = pg.transform.rotozoom(kk_img,10,1.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200

    tmr = 0
    while True:
        tmr += 1
        kk_rct.move_ip(-1,0)
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kk_rct.move_ip(0,-1)
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip(0,+1)
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip(+2,0)
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip(-1,0)


        screen.blit(bg_img, [-(tmr%3200), 0])
        screen.blit(Fscreen, [-(tmr%3200)+1600, 0])
        screen.blit(bg_img, [-(tmr%3200)+3200, 0])
        screen.blit(Fscreen, [-(tmr%3200)+4800, 0])
        screen.blit(kk_img,[-(tmr),0])
        screen.blit(kk_img,kk_rct)
        pg.display.update()        
        clock.tick(200)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()