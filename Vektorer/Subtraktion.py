from manim import *

class Subtraction(Scene):
    def construct(self):
        plane = NumberPlane(axis_config={"include_numbers": True})
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")

        vector = Vector([3, 1], color=GREEN)
        label_vector = Tex(r"$\vec{a}$").next_to(vector, UP).set_color(GREEN)
        group_a = VGroup(vector, label_vector)

        vector_2 = Vector([2, -2], color=BLUE)
        label_vector_2 = Tex(r"$\vec{b}$").next_to(vector_2, RIGHT).set_color(BLUE)
        group_b = VGroup(vector_2, label_vector_2)

        vector_2_shift_1 = Arrow(np.array([3,1,0]), np.array([5,-1,0]), buff=2, color=BLUE)
        vector_2_shift_2 = Arrow(np.array([5,-1,0]), np.array([3,1,0]), buff=2, color=RED)
        vector_2_shift_3 = Arrow(np.array([3,1,0]), np.array([1,3,0]), buff=2, color=RED)
        label_vector_2_neg = Tex(r"$\vec{-b}$").next_to(vector_2_shift_2, RIGHT).set_color(RED)

        vector_sub = Vector([1, 3], color=ORANGE)
        label_vector_sub = Tex(r"$\vec{a} - \vec{b}$").next_to(vector_sub, LEFT).set_color(ORANGE)
        group_sub = VGroup(vector_sub, label_vector_sub)

        self.add(plane, x_label, y_label)
        self.wait(2)
        self.play(Write(group_a))
        self.wait(2)
        self.play(Write(group_b))
        self.wait(2)
        self.play(
            AnimationGroup(
                Transform(vector_2, vector_2_shift_1),
                label_vector_2.animate.next_to(vector_2_shift_1, RIGHT),
                lag_ratio=0
            ))
        self.wait(1)
        self.play(
            AnimationGroup(
                Transform(vector_2, vector_2_shift_2),
                FadeOut(label_vector_2),
                FadeIn(label_vector_2_neg),
                lag_ratio=0
            )
        )
        self.wait(1)
        self.play(
            AnimationGroup(
                Transform(vector_2, vector_2_shift_3),
                label_vector_2_neg.animate.next_to(vector_2_shift_3, RIGHT),
                lag_ratio=0
            )
        )
        self.wait(2)
        self.play(Write(group_sub))
        self.wait(2)

class SubtractionNotCummutative(Scene):
    def construct(self):
        plane = NumberPlane(axis_config={"include_numbers": True})
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")

        vector_1 = Vector([3, 1], color=GREEN)
        label_vector_1 = Tex(r"$\vec{a}$").next_to(vector_1, UP).set_color(GREEN)
        group_a = VGroup(vector_1, label_vector_1)

        vector_2 = Vector([2, -2], color=BLUE)
        label_vector_2 = Tex(r"$\vec{b}$").next_to(vector_2, RIGHT).set_color(BLUE)
        group_b = VGroup(vector_2, label_vector_2)

        vector_1_shift_1 = Arrow(np.array([2,-2,0]), np.array([5,-1,0]), buff=2, color=GREEN)
        vector_1_shift_2 = Arrow(np.array([5,-1,0]), np.array([2,-2,0]), buff=2, color=RED)
        vector_1_shift_3 = Arrow(np.array([2,-2,0]), np.array([-1,-3,0]), buff=2, color=RED)
        label_vector_1_neg = Tex(r"$\vec{-a}$").next_to(vector_1_shift_2, DOWN).set_color(RED)

        vector_sub = Vector([-1, -3], color=ORANGE)
        label_vector_sub = Tex(r"$\vec{b} - \vec{a}$").next_to(vector_sub, LEFT).set_color(ORANGE)
        group_sub = VGroup(vector_sub, label_vector_sub)

        self.add(plane, x_label, y_label)
        self.wait(2)
        self.play(Write(group_a))
        self.wait(2)
        self.play(Write(group_b))
        self.wait(2)
        self.play(
            AnimationGroup(
                Transform(vector_1, vector_1_shift_1),
                label_vector_1.animate.next_to(vector_1_shift_1, DOWN),
                lag_ratio=0
            ))
        self.wait(1)
        self.play(
            AnimationGroup(
                Transform(vector_1, vector_1_shift_2),
                FadeOut(label_vector_1),
                FadeIn(label_vector_1_neg),
                lag_ratio=0
            )
        )
        self.wait(1)
        self.play(
            AnimationGroup(
                Transform(vector_1, vector_1_shift_3),
                label_vector_1_neg.animate.next_to(vector_1_shift_3, DOWN),
                lag_ratio=0
            )
        )
        self.wait(2)
        self.play(Write(group_sub))
        self.wait(2)