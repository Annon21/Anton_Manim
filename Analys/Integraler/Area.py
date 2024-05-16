from manim import *
import numpy as np

def f1(x):   # Funktion f(x)
    return 0.5*((0.5*x-2)-1)*((0.5*x-2)**2-2)+3

class Function(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 10],
            y_range=[-1, 6],
            axis_config={"color": BLUE},
        ).add_coordinates()
        labels = axes.get_axis_labels(x_label="t [s]", y_label="v [m/s]")
        graph = axes.plot(f1, x_range=[-1, 12], color=GREEN_C, stroke_width=2)
        area = axes.get_area(graph, x_range=[1, 7], color=BLUE, opacity=0.4)

        self.play(Create(axes), Create(labels))
        self.play(Create(graph))
        self.wait(1)
        self.play(FadeIn(area))
        self.wait(2)

class SimpleArea(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10],
            y_range=[-1, 6],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(0, 10, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 6, 1)},
        )
        labels = axes.get_axis_labels(x_label="t [s]", y_label="v [m/s]")

        graph = axes.plot(lambda x: 4, x_range=[0, 7], color=RED, stroke_width=6) # Function: straight line y=4
        area = axes.get_area(graph, x_range=[0, 7], color=BLUE, opacity=0.3)
        upper_brace = BraceLabel(graph, text="7 s", brace_direction=UP, label_constructor=Tex)
        right_brace = BraceLabel(area, text="4 m/s", brace_direction=RIGHT, label_constructor=Tex)
        area_text = Tex("A = 28 m").move_to(area)

        self.play(Create(axes), Create(labels))
        self.play(Create(graph), run_time=6)
        self.wait(1)
        self.play(GrowFromCenter(upper_brace))
        self.wait(1)
        self.play(GrowFromCenter(right_brace))
        self.wait(1)
        self.play(FadeIn(area), run_time=2)
        self.play(Write(area_text))
        self.wait(2)

class Integral(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10],
            y_range=[-1, 6], # Need some space under the x-axis to write stuff
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(0, 10, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 6, 1)},
        )
        labels = axes.get_axis_labels(x_label="t [s]", y_label="v [m/s]")
        graph = axes.plot(f1, x_range=[-1, 12], color=GREEN_C, stroke_width=2)
        area = axes.get_area(graph, x_range=[1, 7], color=BLUE, opacity=0.4)
        tx_areaTrue = Tex("Sanna Sträcka = 21.75 m", font_size=35).move_to(area)

        self.play(Create(axes), Create(labels))
        self.play(Create(graph))
        self.wait(1)
        self.play(FadeIn(area))
        self.wait(2)
        self.play(Write(tx_areaTrue))
        self.wait(2)
        self.play(tx_areaTrue.animate.to_edge(UR))

        self.play(FadeOut(area))
        riemann_1 = axes.get_riemann_rectangles(
            graph, x_range=[1, 7],
            dx=6,
            input_sample_type='left',
            stroke_width=1,
            fill_opacity=0.5
        )

        h_1 = f1(1)
        ub_riemann1 = BraceLabel(riemann_1, text="6 s", brace_direction=UP, label_constructor=Tex)
        lb_riemann1 = BraceLabel(riemann_1, text=f"{h_1:.1f} m/s", brace_direction=LEFT, label_constructor=Tex)
        tx_area1 = Tex("Sträcka = 16.2 m").move_to(riemann_1) # area calculated by hand
        line_dotted_1 = axes.get_horizontal_line(axes.i2gp(1, graph), color=RED, stroke_width=8)
        
        self.play(Create(riemann_1))
        self.wait(1)
        self.play(GrowFromCenter(ub_riemann1))
        self.wait(1)
        self.play(GrowFromCenter(lb_riemann1))
        self.play(Write(line_dotted_1))
        self.wait(1)
        self.play(Indicate(line_dotted_1))
        self.wait(2)
        self.play(Write(tx_area1))
        self.wait(2)
        self.play(FadeOut(riemann_1), FadeOut(ub_riemann1), FadeOut(lb_riemann1), FadeOut(tx_area1), FadeOut(line_dotted_1))

        riemann_2 = axes.get_riemann_rectangles(
            graph, x_range=[1, 7],
            dx=3,
            input_sample_type='left',
            stroke_width=1,
            fill_opacity=0.5
        )

        h_2 = [f1(1), f1(4)]
        ub_riemann2_1 = BraceLabel(riemann_2[0], text="3 s", brace_direction=UP, label_constructor=Tex)
        ub_riemann2_2 = BraceLabel(riemann_2[1], text="3 s", brace_direction=UP, label_constructor=Tex)
        rb_riemann2 = BraceLabel(riemann_2[1], text=f"{h_2[1]:.1f} m/s", brace_direction=RIGHT, label_constructor=Tex)
        lb_riemann2 = BraceLabel(riemann_2[0], text=f"{h_2[0]:.1f} m/s", brace_direction=LEFT, label_constructor=Tex)
        tx_area2 = MathTex("2.7" r"\times" "3 + 4" r"\times" "3 = 20.1 m").move_to(riemann_2)

        self.play(Write(riemann_2), run_time=4)
        self.wait(2)
        self.play(GrowFromCenter(ub_riemann2_1), GrowFromCenter(ub_riemann2_2))
        self.wait(1)
        self.play(GrowFromCenter(rb_riemann2))
        self.wait(1)
        self.play(GrowFromCenter(lb_riemann2))
        self.wait(2)
        self.play(Write(tx_area2))
        self.wait(2)
        self.play(FadeOut(ub_riemann2_1), FadeOut(ub_riemann2_2), FadeOut(rb_riemann2), FadeOut(lb_riemann2), FadeOut(tx_area2))

        invis_line_1 = axes.plot(lambda x: h_2[0], x_range=[1, 4]) # Need these lines so the area can be between the function and these lines
        invis_line_2 = axes.plot(lambda x: h_2[1], x_range=[4, 7])
        error_area1 = axes.get_area(invis_line_1, x_range=[1, 4], bounded_graph=graph, color=PURE_RED, opacity=0.8)
        error_area2 = axes.get_area(graph, x_range=[4, 7], bounded_graph=invis_line_2, color=PURE_BLUE, opacity=0.8)
        tx_error_area1 = Tex("3.76 m för lite", color=YELLOW, font_size = 36).move_to(error_area1) # Calculated by hand
        tx_error_area2 = Tex("2.11 m för mycket", color=YELLOW, font_size = 36).move_to(error_area2) 

        self.play(Write(error_area1), run_time=2)
        self.wait(1)
        self.play(Write(error_area2), run_time=2)
        self.wait(1)
        self.play(Write(tx_error_area1), Write(tx_error_area2), run_time=2)
        self.wait(4)
        self.play(FadeOut(tx_error_area1), FadeOut(tx_error_area2))
        self.wait(1)
        self.play(FadeOut(error_area1), FadeOut(error_area2), FadeOut(riemann_2))

        riemann_3 = axes.get_riemann_rectangles(
            graph, x_range=[1, 7],
            dx=1,
            input_sample_type='left',
            stroke_width=1,
            fill_opacity=0.5
        )

        h_3 = [f1(1), f1(2), f1(3), f1(4), f1(5), f1(6)] # using this to later caluclate the area

        db_riemann3_1 = BraceLabel(riemann_3[0], text=r"$\Delta x = 1 s$", brace_direction=DOWN, label_constructor=Tex).shift(0.5*DOWN)
        lb_riemann3_1 = BraceLabel(riemann_3[0], text=r"$\Delta y$", brace_direction=LEFT, label_constructor=Tex)

        self.play(Write(riemann_3), run_time=6)
        self.wait(2)
        self.play(GrowFromCenter(db_riemann3_1))
        self.wait(1)
        self.play(GrowFromCenter(lb_riemann3_1))
        self.wait(2)
        riemann_3_copy = riemann_3[0].copy() # Makes a copy of the first rectangle so i can change it later
        self.add(riemann_3_copy)
        self.play(FadeOut(riemann_3),
                  FadeOut(db_riemann3_1), FadeOut(lb_riemann3_1), FadeOut(graph), FadeOut(axes), FadeOut(labels), FadeOut(tx_areaTrue))
        self.wait(1)

        riemann_3_L = riemann_3_copy.move_to(ORIGIN+LEFT*2).scale(1.5)
        tx_y2 = MathTex("y_2").move_to(riemann_3_L.get_corner(UL)).shift(0.5*LEFT)
        tx_y1 = MathTex("y_1").move_to(riemann_3_L.get_corner(DL)).shift(0.5*LEFT)
        tx_x1 = MathTex("x_1").move_to(riemann_3_L.get_corner(DL)).shift(0.5*DOWN)
        tx_x2 = MathTex("x_2").move_to(riemann_3_L.get_corner(DR)).shift(0.5*DOWN)

        self.play(Transform(riemann_3_copy, riemann_3_L)) # Why is the so jaring?
        self.wait(1)
        self.play(Write(tx_y2), Write(tx_y1), Write(tx_x1), Write(tx_x2))
        self.wait(2)

        indicate_y_box = SurroundingRectangle(VGroup(tx_y2, tx_y1), color=RED, buff=0.1)
        indicate_x_box = SurroundingRectangle(VGroup(tx_x1, tx_x2), color=RED, buff=0.1)
        tx_01 = Tex(r"$\Delta y = y_2 - y_1$").next_to(tx_areaTrue, DOWN, buff=0.5)
        self.play(Write(tx_01))
        indicate_01_box = SurroundingRectangle(tx_01, color=RED, buff=0.1)
        self.play(Create(indicate_y_box), Create(indicate_01_box))
        self.wait(1)
        self.play(Circumscribe(indicate_y_box), Circumscribe(indicate_01_box))
        self.wait(2)
        self.play(FadeOut(indicate_y_box), FadeOut(indicate_01_box))
        tx_02 = Tex(r"$\Delta x = x_2 - x_1$").next_to(tx_01, DOWN, buff=0.5)
        self.play(Write(tx_02))
        indicate_02_box = SurroundingRectangle(tx_02, color=RED, buff=0.1)
        self.play(Create(indicate_x_box), Create(indicate_02_box))
        self.wait(1)
        self.play(Circumscribe(indicate_x_box), Circumscribe(indicate_02_box))
        self.wait(2)
        self.play(FadeOut(indicate_x_box), FadeOut(indicate_02_box))
        self.wait(1)
        tx_03 = Tex(r"$y_1 = 0$").next_to(tx_02, DOWN, buff=0.5)
        self.play(Write(tx_03))
        indicate_y1_box = SurroundingRectangle(tx_y1, color=RED, buff=0.1)
        indicate_03_box = SurroundingRectangle(tx_03, color=RED, buff=0.1)
        self.play(Create(indicate_y1_box), Create(indicate_03_box))
        self.wait(1)
        self.play(Circumscribe(indicate_y1_box), Circumscribe(indicate_03_box))
        self.wait(2)
        self.play(FadeOut(indicate_y1_box), FadeOut(indicate_03_box))
        self.wait(1)
        tx_04 = Tex(r"$y_2=f(x_1)$").next_to(tx_03, DOWN, buff=0.5)
        self.play(Write(tx_04))
        indicate_y2_box = SurroundingRectangle(tx_y2, color=RED, buff=0.1)
        indicate_04_box = SurroundingRectangle(tx_04, color=RED, buff=0.1)
        self.play(Create(indicate_y2_box), Create(indicate_04_box))
        self.wait(1)
        self.play(Circumscribe(indicate_y2_box), Circumscribe(indicate_04_box))
        self.wait(2)
        self.play(FadeOut(indicate_y2_box), FadeOut(indicate_04_box))
        self.wait(1)
        tx_05 = Tex(r"$\Delta y = f(x_1) - 0 = f(x_1)$").next_to(tx_04, DOWN, buff=0.5).shift(LEFT)
        self.play(Write(tx_05))
        
        self.wait(5)

        self.play(FadeOut(tx_05), FadeOut(tx_04), FadeOut(tx_03), FadeOut(tx_02), FadeOut(tx_01))
        self.play(FadeOut(tx_y2), FadeOut(tx_y1), FadeOut(tx_x1), FadeOut(tx_x2), FadeOut(riemann_3_copy))
        self.play(FadeIn(axes), FadeIn(labels), FadeIn(graph), FadeIn(tx_areaTrue), FadeIn(riemann_3))

        area_3 = np.sum(h_3)
        tx_area3 = Tex(f"Sträcka = {area_3:.2f} m").move_to(riemann_3)
        self.play(Write(tx_area3))
        self.wait(4)
        self.play(FadeOut(riemann_3), FadeOut(tx_area3))

        riemann_4 = axes.get_riemann_rectangles(
            graph, x_range=[1, 7],
            dx=0.5,
            input_sample_type='left',
            stroke_width=1,
            fill_opacity=0.5
        )

        h_4 = [f1(1), f1(1.5), f1(2), f1(2.5), f1(3), f1(3.5), f1(4), f1(4.5), f1(5), f1(5.5), f1(6), f1(6.5)]

        db_riemann4_1 = BraceLabel(riemann_4[0], text=r"$\Delta x = 0.5 s$", brace_direction=DOWN, label_constructor=Tex).shift(0.5*DOWN)
        self.play(Write(riemann_4), run_time=6)
        self.wait(2)
        self.play(GrowFromCenter(db_riemann4_1))
        self.wait(1)
        area_4 = 0
        for i in range(len(h_4)): # Calculating the area, multiplying the height with the width
            area_4 += h_4[i]*0.5

        tx_area4 = Tex(f"Sträcka = {area_4:.2f} m").move_to(riemann_4)
        self.play(Write(tx_area4))
        self.wait(4)
        self.play(FadeOut(riemann_4), FadeOut(tx_area4), FadeOut(db_riemann4_1))

        riemann_5 = axes.get_riemann_rectangles(
            graph, x_range=[1, 7],
            dx=0.25,
            input_sample_type='left',
            stroke_width=1,
            fill_opacity=0.5
        )

        h_5 = [f1(1), f1(1.25), f1(1.5), f1(1.75), f1(2), f1(2.25), f1(2.5), f1(2.75), f1(3), f1(3.25), f1(3.5), f1(3.75), f1(4), f1(4.25), f1(4.5), f1(4.75), f1(5), f1(5.25), f1(5.5), f1(5.75), f1(6), f1(6.25), f1(6.5), f1(6.75)]

        db_riemann5_1 = BraceLabel(riemann_5[0], text=r"$\Delta x = 0.25 s$", brace_direction=DOWN, label_constructor=Tex).shift(0.5*DOWN)

        self.play(Write(riemann_5), run_time=6)
        self.wait(2)
        self.play(GrowFromCenter(db_riemann5_1))
        self.wait(1)
        area_5 = 0
        for i in range(len(h_5)): # Calculating the area, multiplying the height with the width
            area_5 += h_5[i]*0.25

        tx_area5 = Tex(f"Sträcka = {area_5:.2f} m").move_to(riemann_5)
        self.play(Write(tx_area5))
        self.wait(4)
        self.play(FadeOut(riemann_5), FadeOut(tx_area5), FadeOut(db_riemann5_1))
        self.wait(2)

        db_riemann_int = BraceLabel(riemann_5[0], text=r"$\Delta x \to 0$ kallas dx", brace_direction=DOWN, label_constructor=Tex).shift(0.5*DOWN)
        self.play(Write(db_riemann_int), run_time=3)
        indicate_int_box = SurroundingRectangle(db_riemann_int, color=RED, buff=0.1)
        self.play(Write(indicate_int_box))
        self.play(Circumscribe(indicate_int_box))
        self.wait(2)
        self.play(FadeIn(area))

        tx_int = Tex(r"$\int_{1}^{7} f(x) dx$", font_size=90).move_to(area)
        self.play(Write(tx_int))
        self.play(tx_areaTrue.animate.next_to(tx_int, DOWN, buff=0.5))
        self.wait(4)











        