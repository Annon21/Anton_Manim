from manim import *

class Addition(Scene):
    def construct(self):
        plane = NumberPlane(axis_config={"include_numbers": True})
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")

        vector = Vector([3, 2], color=GREEN)
        label_vector = Tex(r"$\vec{a}$").next_to(vector, UP).set_color(GREEN)
        vector_2 = Vector([2, -3], color=BLUE)
        label_vector_2 = Tex(r"$\vec{b}$").next_to(vector_2, RIGHT).set_color(BLUE)
        group_v2 = VGroup(vector_2, label_vector_2)
        
        vector_2_shift = Arrow(np.array([3,2,0]), np.array([5,-1,0]), buff=2, color=BLUE)
        vector_add = Vector([5, -1], color=ORANGE)
        label_vector_add = Tex(r"$\vec{a} + \vec{b}$").next_to(vector_add, DOWN).set_color(ORANGE)

        self.add(plane, x_label, y_label)
        self.wait(2)
        self.play(Create(vector))
        self.play(Write(label_vector))
        self.wait(2)
        self.play(Create(group_v2))
        self.wait(2)
        self.play(
            AnimationGroup(
                Transform(vector_2, vector_2_shift),
                label_vector_2.animate.next_to(vector_2_shift, RIGHT),
                lag_ratio=0
            )
        )
        self.wait(2)
        self.play(Create(vector_add))
        self.play(Write(label_vector_add))
        self.wait(2)

class AdditionCommutative(Scene):
    def construct(self):
        plane = NumberPlane(axis_config={"include_numbers": True})
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")

        vector = Vector([3, 2], color=GREEN)
        label_vector = Tex(r"$\vec{a}$").next_to(vector, UP).set_color(GREEN)
        vector_2 = Vector([2, -3], color=BLUE)
        label_vector_2 = Tex(r"$\vec{b}$").next_to(vector_2, LEFT).set_color(BLUE)
        group_v2 = VGroup(vector_2, label_vector_2)
        
        vector_1_shift = Arrow(np.array([2,-3,0]), np.array([5,-1,0]), buff=2, color=GREEN)
        vector_add = Vector([5, -1], color=ORANGE)
        label_vector_add = Tex(r"$\vec{b} + \vec{a}$").next_to(vector_add, UP).set_color(ORANGE)

        self.add(plane, x_label, y_label)
        self.wait(2)
        self.play(Create(vector))
        self.play(Write(label_vector))
        self.wait(2) 
        self.play(Create(group_v2))
        self.wait(2)
        self.play(
            AnimationGroup(
                Transform(vector, vector_1_shift),
                label_vector.animate.next_to(vector_1_shift, RIGHT),
                lag_ratio=0
            )
        )
        self.wait(2)
        self.play(Create(vector_add))
        self.play(Write(label_vector_add))
        self.wait(2)

class AdditionSameDirection(Scene):
    def construct(self):
        plane = NumberPlane(axis_config={"include_numbers": True})
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")

        vector_1 = Arrow(np.array([0,0,0]), np.array([2,1,0]), buff=2, color=GREEN)
        label_vector_1 = Tex(r"$\vec{a}$").next_to(vector_1, UP).set_color(GREEN)
        vector_2 = Arrow(np.array([-3,1,0]), np.array([-1,2,0]), buff=2, color=BLUE)
        label_vector_2 = Tex(r"$\vec{b}$").next_to(vector_2, UP).set_color(BLUE)
        vector_2_shift = Arrow(np.array([2,1,0]), np.array([4,2,0]), buff=2, color=BLUE)
        vector_add = Vector([4, 2], color=ORANGE)
        label_vector_add = Tex(r"$\vec{a} + \vec{b}$").next_to(vector_add, RIGHT).set_color(ORANGE)

        self.add(plane, x_label, y_label)
        self.wait(2)
        self.play(Create(vector_1))
        self.play(Write(label_vector_1))
        self.wait(2)
        self.play(Create(vector_2))
        self.play(Write(label_vector_2))
        self.wait(2)
        self.play(
            AnimationGroup(
                Transform(vector_2, vector_2_shift),
                label_vector_2.animate.next_to(vector_2_shift, UP),
                lag_ratio=0
            )
        )
        self.wait(2)
        self.play(
            vector_1.animate.set_fill(GREEN, opacity=0.5),
            vector_2.animate.set_fill(BLUE, opacity=0.5),
        )
        self.play(Create(vector_add))
        self.play(Write(label_vector_add))
        self.wait(2)
        self.play(
            FadeOut(vector_add),
            vector_1.animate.set_fill(GREEN, opacity=1),
            vector_2.animate.set_fill(BLUE, opacity=1),
        )
        self.wait(2)
        self.play(
            FadeIn(vector_add),
            vector_1.animate.set_fill(GREEN, opacity=0.5),
            vector_2.animate.set_fill(BLUE, opacity=0.5),
        )
        self.play(FadeOut(label_vector_1), FadeOut(label_vector_2))
        self.wait(2)

