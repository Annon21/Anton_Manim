from manim import *
import numpy as np
from scipy.optimize import minimize_scalar

class NormalDistro(Scene):
    def construct(self):
        # Create the axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"color": BLUE},
        )
        axes.add_coordinates()
        self.play(Create(axes))

        # Create the normal distribution
        normal_dist = self.get_normal_dist(0, 1)
        self.play(Create(normal_dist))

        # Create the shaded area
        shade = self.get_shaded_area(-1, 1)
        self.play(Create(shade))

        # Create the text
        text = MathTex(r"\text{Area} = 0.6827").scale(1.5)
        text.to_edge(UP)
        self.play(Create(text))
        self.wait(2)

    def get_normal_dist(self, mu, sigma):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"color": BLUE},
        )
        x = np.linspace(-4, 4, 100)
        y = np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))
        points = [axes.c2p(x_, y_) for x_, y_ in zip(x, y)]
        return VMobject().set_points_as_corners(points)

    def get_shaded_area(self, x1, x2):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"color": BLUE},
        )
        x = np.linspace(x1, x2, 100)
        y = np.exp(-0.5 * ((x - 0) / 1) ** 2) / (1 * np.sqrt(2 * np.pi))
        points = [axes.c2p(x_, y_) for x_, y_ in zip(x, y)]
        points.insert(0, axes.c2p(x1, 0))
        points.append(axes.c2p(x2, 0))
        return Polygon(*points, color=BLUE, fill_opacity=0.5)
    
class CircleVariation(Scene):
    def construct(self):
        # Creating the circle
        c = Circle(radius=2, color=GREEN).set_fill(color=GREEN, opacity=0.5).set_color(GREEN).to_edge(LEFT)

        # These updaters are so the radius line and text will update in real time
        def dot_on_center(obj):
            obj.become(Dot(c.get_center(), radius=0.05))
        def dot_on_top(obj):
            obj.become(Dot(c.get_right(), radius=0.05))
        def line_from_dots(obj):
            obj.become(Line(d0.get_center(), d1.get_center(), color=RED))
        def line_label_updater(obj):
            obj.become(Tex(f"Radie: {l.get_length():.3f} cm", color=RED).next_to(c, UP))

        # Creating the dots and the line and adding the updaters to them
        d0, d1 = Dot(c.get_center()), Dot(c.get_right())
        d0.add_updater(dot_on_center)
        d1.add_updater(dot_on_top)


        self.play(FadeIn(c, d0, d1))

        l = Line()
        l.add_updater(line_from_dots)
        self.play(Write(l))

        l_label = Tex('Radie: 2.000 cm', color=RED).next_to(c, UP)
        l_label.add_updater(line_label_updater)


        
        self.add(l_label)
        self.wait(1)

        radii = []
        scales = [1.5, 0.5, 1.5, 1.25, 0.6, 1.5, 0.75, 1.25, 0.5, 1.25, 1.25, 0.6] # The scales are chosen arbitratly

        # Creating the radius dependent on the above scaling
        radii = [0.2]  # Initial radius
        for scale in scales:
            new_radius = scale * radii[-1]
            radii.append(new_radius)


        previous_circle = None
        acc = 1 # This is the accelerator for the runtime, will make the animation faster and faster
        runtime = 1
        for radius, scale in zip(radii, scales):
            new_circle = c.copy()
            new_circle_t = Circle(radius=radius).set_fill(color=GREEN, opacity=0.5).set_color(GREEN)
            if previous_circle is not None:
                new_circle_t.next_to(previous_circle, DOWN)
            else:
                new_circle_t.to_edge(UR)
            self.add(new_circle)
            self.play(Transform(new_circle, new_circle_t), run_time=runtime)
            self.play(c.animate.scale(scale), run_time=runtime)
            runtime = np.exp(-acc*0.15) # this will make the animation faster and faster
            acc += 1
            previous_circle = new_circle
        self.wait(4)


class NormalCircles(Scene):
    def construct(self):
        np.random.seed(8)
        # Create the axes
        axes = Axes(
            x_range=[0.078, 0.309, 0.019],
            y_range=[0, 20, 2],
            axis_config={"color": BLUE},
        )
        axes.add_coordinates()

        axis_labels = axes.get_axis_labels(x_label="Radie (dm)", y_label="Frekvens")


        n = 81  # Number of circles
        std = 1.0  # Standard deviation   
        arr = 0.2 * np.random.normal(0, std, n)

        # Create the circles
        cir = VGroup(
            *[Circle(radius=0.2*(1+u))
              .shift(UP * np.random.uniform(-3, 3) + RIGHT * np.random.uniform(-5, 5))
              .set_fill(color=GREEN, opacity=0.5).set_color(GREEN)
              for u in arr]
        )

        # sorting
        sor_arr = np.sort(arr)
        sor_cir = VGroup(
            *[Circle(radius=0.2*(1+u))
              .shift(UP * np.random.uniform(-3, 3) + RIGHT * np.random.uniform(-5, 5))
              .set_fill(color=GREEN, opacity=0.5).set_color(GREEN)
              for u in sor_arr]
        )
        sor_cir.arrange_in_grid(buff=0.1)
        
        # Create the scene
        self.play(Create(cir))
        self.wait()
        self.play(ReplacementTransform(cir, sor_cir), run_time=3)
        self.wait()

        median_radius = sor_cir[n//2].radius # Median radius
        smallest_radius = sor_cir[0].radius # Smallest radius
        largest_radius = sor_cir[-1].radius # Largest radius
        tex_median = Text(f"Medianradie:\n {median_radius*10:.3f} cm", color=MAROON, font_size=30).to_edge(LEFT)
        tex_small = Text(f"Minsta radie: {smallest_radius*10:.3f} cm", color=ORANGE).to_edge(UP)
        tex_large = Text(f"Största radie: {largest_radius*10:.3f} cm", color=TEAL).to_edge(DOWN)
        

        # Median radius
        self.play(Write(tex_median))
        sor_cir[n//2].set_color(MAROON)
        #smalles radius in cir
        self.play(Write(tex_small))
        sor_cir[0].set_color(ORANGE)
        #largest radius in cir
        self.play(Write(tex_large))
        sor_cir[-1].set_color(TEAL)
        self.wait(3)
        self.play(FadeOut(tex_large), FadeOut(tex_small), FadeOut(tex_median))

        # sort into bins
        self.play(sor_cir.animate.shift(UP*1.5).scale(0.7))
        self.play(Create(axes))
        self.play(Create(axis_labels))
        hist_arr = np.array(0.2*(1+sor_arr))

        hist, bins = np.histogram(hist_arr, 10)

        buckets = VGroup()
        for i, (h, b) in enumerate(zip(hist, bins)):
            bar = Rectangle(width=std-0.1, height=(axes.get_vertical_line(axes.c2p(0,h)).get_length()), color=BLUE, fill_opacity=0.5)
            bar.move_to(axes.c2p(b, 0), aligned_edge=DOWN)
            buckets.add(bar)

        # colors for every bucket
        color_gradient = [BLUE_A, BLUE_B, TEAL_B, TEAL_C, GREEN_C,
                           GREEN_D, YELLOW_D, GOLD_E, RED_E, MAROON_E]
        for i, bar in enumerate(buckets):
            bar.set_fill(color_gradient[i], 0.5)

        

        # Calculate the cumulative sum of the histogram
        cum_hist = np.cumsum(hist)

        # Initialize the start index
        start = 0

        # Loop over the cumulative histogram
        for i, end in enumerate(cum_hist):
            # Set the color for the current section of the circle array
            sor_cir[start:end+1].set_color(color_gradient[i])
            # Update the start index for the next iteration
            self.play(sor_cir[start:end+1].animate.move_to(buckets[i].get_center()).scale(0.5))
            self.play(Create(buckets[i]), FadeOut(sor_cir[start:end+1]))
            self.wait(0.5)
            start = end + 1

        self.wait(2)
        # Adding normal distribution to the scene

        def normal(x, mean, std_dev):
            return 1/(std_dev * np.sqrt(2 * np.pi)) * np.exp(-0.5*((x - mean)/std_dev)**2)
        

        mean = np.mean(hist_arr)
        std_hist = np.std(hist_arr) # Creating a new std for the current dataset
        normal_distro = axes.plot(lambda x: normal(x, mean, std_hist), color=RED)
        result = minimize_scalar(lambda x: -normal(x, mean, std_hist)) # This neat trick will find the maximum value of the normal distribution so the mean_line will be the corrrect length
        max_value = -result.fun # The minimizer finds the min value, but by inverting it you get the max value
        mean_line = axes.get_vertical_line(axes.c2p(mean, max_value)).set_color(WHITE)
        variation_width = sor_cir[-1].radius - sor_cir[0].radius
        self.play(Create(normal_distro))
        self.play(Create(mean_line))
        self.wait(2)

        # Crateing some text for the normal
        #tx_meanline = Tex('Medellinje: ' , r"$\mu$ = " , f"{mean:.3f}", color=WHITE).next_to(mean_line, UP*2)
        tx_std = Tex('Standardavvikelse: ' , r"$\sigma$ = " , f"{std_hist*10:.3f} cm").to_edge(UL).shift(RIGHT)
        tx_mean = Tex('Medelvärde: ' , r"$\mu$ = " , f"{mean*10:.3f} cm").next_to(tx_std, DOWN)
        tx_population = Tex('Population: ' , f"{n}").to_edge(UR).shift(LEFT)
        tx_width = Tex('Variationsbredd: ' , f"{variation_width*10:.3f} cm").next_to(tx_population, DOWN)

        self.play(FadeOut(axis_labels))
        self.play(Write(tx_std))
        self.play(Write(tx_mean))
        self.play(Write(tx_population))
        self.play(Write(tx_width))
        self.wait(4)

        print(f"The maximum value of the function is: {max_value}")



    






class Histogram(Scene):
    def construct(self):
        # Create the axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"color": BLUE},
        )
        axes.add_coordinates()

        # Create the histogram
        hist = self.get_histogram([1, 2, 3, 4, 5, 6, 7, 8, 9], [0.1, 0.2, 0.3, 1.4, 0.3, 0.2, 0.1, 0.2, 0.3])
        self.play(Create(axes))
        self.play(Create(hist))
        self.wait(2)

    def get_histogram(self, x, y):
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"color": BLUE},
        )
        bars = VGroup()
        for i, (x_, y_) in enumerate(zip(x, y)):
            bar = Rectangle(width=0.5, height=y_, color=BLUE, fill_opacity=0.5)
            bar.move_to(axes.c2p(x_, 0), aligned_edge=DOWN)
            bars.add(bar)
        return bars 
