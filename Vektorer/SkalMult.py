from manim import *

class Smulti_excludeCoord(Scene):
    def construct(self):
        plane = Axes(
            x_range=[-1, 13],
            y_range=[-1, 9],
        ).add_coordinates()
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")

        vector = Arrow(plane.coords_to_point(0, 0), plane.coords_to_point(3, 2), buff=2.0, color=GREEN)
        label_vector = Tex(r"$\vec{a}$").next_to(vector, UP).set_color(GREEN)
        vector_copy = vector.copy().set_color(BLUE)
        unit_vector1 = Arrow(plane.coords_to_point(0, -1), plane.coords_to_point(3, 1), buff=2.0, color=BLUE).set_opacity(0.5)

        vector_multi_2 = Arrow(plane.coords_to_point(0, 0), plane.coords_to_point(6, 4), buff=4.0, color=ORANGE)
        label_vector_multi_2 = Tex(r"$2\vec{a}$").next_to(vector_multi_2, UP).set_color(ORANGE)
        unit_vector2 = Arrow(plane.coords_to_point(3, 1), plane.coords_to_point(6, 3), buff=2.0, color=BLUE).set_opacity(0.5)

        vector_multi_3 = Arrow(plane.coords_to_point(0, 0), plane.coords_to_point(9, 6), buff=6.0, color=RED)
        label_vector_multi_3 = Tex(r"$3\vec{a}$").next_to(vector_multi_3, UP).set_color(RED)
        unit_vector3 = Arrow(plane.coords_to_point(6, 3), plane.coords_to_point(9, 5), buff=2.0, color=BLUE).set_opacity(0.5)


        self.add(plane, x_label, y_label)
        self.wait(2)
        self.play(Create(vector))
        self.play(Write(label_vector))
        self.wait(2)
        self.add(vector_copy)
        self.play(Transform(vector_copy, unit_vector1))
        self.remove(vector_copy)
        self.add(unit_vector1)
        self.play(Transform(vector, vector_multi_2), Transform(label_vector, label_vector_multi_2))
        self.play(Write(unit_vector2))
        self.wait(2)
        self.play(Transform(vector, vector_multi_3), Transform(label_vector, label_vector_multi_3))
        self.play(Write(unit_vector3))
        self.wait(2)

class Smulti_includeCoord(Scene):
    def construct(self):
        plane = Axes(
            x_range=[-1, 13],
            y_range=[-1, 9],
        ).add_coordinates()
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")

        vector = Arrow(plane.coords_to_point(0, 0), plane.coords_to_point(3, 2), buff=2.0, color=GREEN)
        label_vector = Tex(r"$\vec{a} = (3,2)$").next_to(vector, UP).set_color(GREEN)
        vector_copy = vector.copy().set_color(BLUE)
        unit_vector1 = Arrow(plane.coords_to_point(0, -1), plane.coords_to_point(3, 1), buff=2.0, color=BLUE).set_opacity(0.5)

        vector_multi_2 = Arrow(plane.coords_to_point(0, 0), plane.coords_to_point(6, 4), buff=4.0, color=ORANGE)
        label_vector_multi_2 = Tex(r"$2\vec{a} = (6,4)$").next_to(vector_multi_2, UP).set_color(ORANGE)
        unit_vector2 = Arrow(plane.coords_to_point(3, 1), plane.coords_to_point(6, 3), buff=2.0, color=BLUE).set_opacity(0.5)

        vector_multi_3 = Arrow(plane.coords_to_point(0, 0), plane.coords_to_point(9, 6), buff=6.0, color=RED)
        label_vector_multi_3 = Tex(r"$3\vec{a} = (9,6)$").next_to(vector_multi_3, UP).set_color(RED)
        unit_vector3 = Arrow(plane.coords_to_point(6, 3), plane.coords_to_point(9, 5), buff=2.0, color=BLUE).set_opacity(0.5)


        self.add(plane, x_label, y_label)
        self.wait(2)
        self.play(Create(vector))
        self.play(Write(label_vector))
        self.wait(2)
        self.add(vector_copy)
        self.play(Transform(vector_copy, unit_vector1))
        self.remove(vector_copy)
        self.add(unit_vector1)
        self.play(Transform(vector, vector_multi_2), Transform(label_vector, label_vector_multi_2))
        self.play(Write(unit_vector2))
        self.wait(2)
        self.play(Transform(vector, vector_multi_3), Transform(label_vector, label_vector_multi_3))
        self.play(Write(unit_vector3))
        self.wait(2)
