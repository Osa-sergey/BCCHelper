import pygame as pg
from moves_matrix import *


class Object3D:
    def __init__(self, render, vertexes):
        self.render = render
        self.vertexes = vertexes
        self.faces = np.array([(0, 1, 2)])
        self.translate([0.001, 0.001, 0.001])
        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.color_faces = [(pg.Color('orange'), face) for face in self.faces]
        self.draw_vertexes = True
        self.label = ''

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        vertexes = self.vertexes @ self.render.camera.camera_matrix()
        vertexes = vertexes @ self.render.projection.projection_matrix
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes[(vertexes > 2) | (vertexes < -2)] = 0
        vertexes = vertexes @ self.render.projection.to_screen_matrix
        vertexes = vertexes[:, :2]

        for index, color_face in enumerate(self.color_faces):
            color, face = color_face
            polygon = vertexes[face]
            if not np.any((polygon == self.render.H_WIDTH) | (polygon == self.render.H_HEIGHT)):
                pg.draw.polygon(self.render.screen, color, polygon, 3)
                if self.label:
                    text = self.font.render(self.label[index], True, pg.Color('white'))
                    self.render.screen.blit(text, polygon[-1])
        if self.draw_vertexes:
            for vertex in vertexes:
                if not np.any((vertex == self.render.H_WIDTH) | (vertex == self.render.H_HEIGHT)):
                    pg.draw.circle(self.render.screen, pg.Color("white"), vertex, 6)

    def translate(self, pos):
        self.vertexes = self.vertexes @ translation(pos)

    def scale(self, n):
        self.vertexes = self.vertexes @ scale(n)

    def rotation_x(self, angel):
        self.vertexes = self.vertexes @ rotation_x(angel)

    def rotation_y(self, angel):
        self.vertexes = self.vertexes @ rotation_y(angel)

    def rotation_z(self, angel):
        self.vertexes = self.vertexes @ rotation_z(angel)


class Axes(Object3D):
    def __init__(self, render, vertexes):
        super().__init__(render, vertexes=vertexes)
        self.faces = np.array([(0, 1), (0, 2), (0, 3)])
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.draw_vertexes = False
        self.label = 'XYZ'


class Square(Object3D):
    def __init__(self, render, vertexes):
        super().__init__(render, vertexes=vertexes)
        self.faces = np.array([(0, 1, 2, 3)])
        self.color_faces = [(pg.Color('yellow'), face) for face in self.faces]
