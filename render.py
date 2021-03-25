import pygame as pg
from object_3d import *
from camera import *
from projection import *


class Render:
    def __init__(self, coordinates):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.camera = Camera(self, [1, 1, -4])
        self.projection = Projection(self)
        self.square_objects = self.create_square_objects(coordinates)
        axes_cords = np.array([(0, 0, 0, 1), (1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])
        self.axes = Axes(self,axes_cords)
        self.axes.scale(3)

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        [obj.draw() for obj in self.square_objects]
        self.axes.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption("3D_view")
            pg.display.flip()
            self.clock.tick(self.FPS)

    def create_square_objects(self, vertexes) -> list:
        objects = list()
        for square in vertexes:
            new_object = Square(self,vertexes=square)
            objects.append(new_object)
        return objects