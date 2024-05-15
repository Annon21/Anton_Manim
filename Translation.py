from manim import *

class Background(Scene):
    def construct(self):
        plane = NumberPlane(axis_config={"include_numbers": True})
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")

        self.add(plane)
        self.wait(2)
        self.play(Write(x_label), Write(y_label))

class VectotConstruction(Scene):
    def construct(self):
        plane = NumberPlane(axis_config={"include_numbers": True})
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")

        vector = Vector([3, 2], color=GREEN)
        vector_x = Vector([3,0], color=LOGO_GREEN)
        vector_y = Vector([0,2], color=LOGO_RED)
        vector_y.shift(vector_x.get_end())
        v_label = Tex(r"$\vec{v}$").next_to(vector, UP).set_color(GREEN)
        vector_x_label = Tex(r"$\vec{v}_x$").next_to(vector_x, DOWN).set_color(LOGO_GREEN)
        vector_y_label = Tex(r"$\vec{v}_y$").next_to(vector_y, RIGHT).set_color(LOGO_RED)

        self.add(plane, x_label, y_label)
        self.wait(2)
        self.play(Create(vector))
        self.wait(2)
        self.play(Write(v_label))
        self.wait(2)
        self.play(FadeOut(vector), FadeOut(v_label))
        self.play(
            AnimationGroup(
                Create(vector_x),
                Create(vector_y),
                Write(vector_x_label),
                Write(vector_y_label),
                lag_ratio=1.5
            )
        )
        self.wait(4)
        self.play(FadeIn(vector), FadeIn(v_label))
        self.wait(4)
        self.play(FadeOut(vector_x), FadeOut(vector_y), FadeOut(vector_x_label), FadeOut(vector_y_label))
        self.wait(3)

class Translation(Scene):
    def construct(self):
        plane = NumberPlane(axis_config={"include_numbers": True})
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")

        vector = Vector([3, 2], color=GREEN)
        vector_shift_R = Arrow(np.array([2,0,0]), np.array([5,2,0]), buff=2, color=GREEN)
        vector_shift_RU = Arrow(np.array([2,1.5,0]), np.array([5,3.5,0]), buff=2, color=GREEN)
        vector_shift_U = Arrow(np.array([0,1,0]), np.array([3,3,0]), buff=2, color=GREEN)
        vector_shift_UU = Arrow(np.array([1,-3,0]), np.array([4,-1,0]), buff=2, color=GREEN)

        self.add(plane, x_label, y_label)
        self.add(vector)
        self.wait(2)    
        self.play(Transform(vector, vector_shift_R))
        self.wait(2)
        self.play(Transform(vector, vector_shift_RU))
        self.wait(2)
        self.play(Transform(vector, vector_shift_U))
        self.wait(2)
        self.play(Transform(vector, vector_shift_UU))
        self.wait(2)

class Slide(MovingCameraScene):
    def construct(self):
        plane = NumberPlane(axis_config={"include_numbers": True})
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")

        v_RU = Arrow(np.array([2,1.5,0]), np.array([5,3.5,0]), buff=2, color=GREEN)
        v_LD = Arrow(np.array([-5,-3,0]), np.array([-2,-1,0]), buff=2, color=GREEN)

        self.add(plane, x_label, y_label)
        self.wait(2)
        self.play(Create(v_RU))
        self.camera.frame.save_state()
        self.wait(2)
        self.play(self.camera.frame.animate.move_to(v_RU.get_center()))
        self.play(self.camera.frame.animate.set_height(v_RU.get_height()*2.5))
        self.play(
            AnimationGroup(
                Transform(v_RU, v_LD),
                self.camera.frame.animate.move_to(v_LD),
            ), run_time=7
        )
        self.wait(2)
        self.play(Restore(self.camera.frame))
        self.wait(2)

class RotationAndScale(Scene):
    def construct(self):
        plane = NumberPlane(axis_config={"include_numbers": True})
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")

        vector = Vector([2, 1], color=GREEN)
        vector_R = Arrow(np.array([0,0,0]), np.array([2,1,0]), buff=2, color=GREEN)
        vector_RU = Arrow(np.array([3,-1,0]), np.array([5,0,0]), buff=2, color=GREEN)
        vector_U = Arrow(np.array([3,-1,0]), np.array([5,-2,0]), buff=2, color=GREEN)
        vector_LD = Arrow(np.array([-1,1,0]), np.array([1,0,0]), buff=2, color=GREEN)
        vector_scale = Arrow(np.array([-1,1,0]), np.array([3,-1,0]), buff=4, color=GREEN)

        checkmark = Tex(r"$\checkmark$").scale(5).set_color(GREEN).move_to(LEFT*2+UP*2)
        cross = Tex(r"$\times$").scale(5).set_color(RED).move_to(LEFT*2+UP*2)

        self.add(plane, x_label, y_label)
        self.add(vector)
        self.play(Transform(vector, vector_R))
        self.wait(2)
        self.play(Transform(vector, vector_RU))
        self.play(Write(checkmark))
        self.play(Flash(checkmark, flash_radius=1.6, num_lines=42))
        self.wait(2)
        self.play(FadeOut(checkmark))
        self.wait(2)
        self.play(Transform(vector, vector_U))
        self.play(Write(cross))
        self.play(Flash(cross, flash_radius=1.6, num_lines=42))
        self.wait(2)
        self.play(FadeOut(cross))
        self.wait(2)
        self.play(Transform(vector, vector_LD))
        self.play(Write(checkmark))
        self.play(Flash(checkmark, flash_radius=1.6, num_lines=42))
        self.wait(2)
        self.play(FadeOut(checkmark))
        self.wait(2)
        self.play(Transform(vector, vector_scale))
        self.play(Write(cross))
        self.play(Flash(cross, flash_radius=1.6, num_lines=42))
        self.wait(2)
        self.play(FadeOut(cross))
        self.wait(2)