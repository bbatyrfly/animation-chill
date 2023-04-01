from manim import *
from pathlib import Path
import os

FLAGS = f"-pqm"
SCENE = 'Algo1EX1'

class Introduction(Scene):
    def construct(self):
        title1 = Text('Система счисления').scale(2)
        title2 = Text('''
        Система счисления  — символический метод записи чисел, 
           представление чисел с помощью письменных знаков.
        ''').scale(0.6)
        title3 = Text('Система счисления').move_to([0, 3.3, 0])
        ar1 = Arrow([0, 3, 0], [-4, 2, 0])
        ar2 = Arrow([0, 3, 0], [4, 2, 0])
        deli1 = Text('Позиционную').scale(0.7).move_to([-4, 1.5, 0])
        deli2 = Text('Непозиционную').scale(0.7).move_to([4, 1.5, 0])
        defi1 = Text('''
        система счисления, в которой значение
        каждого числового знака ( цифры ) в записи
        числа зависит от его позиции ( разрада )  
        относительно десятичного разделителя.
        ''').scale(0.4).move_to([-4, 0.5, 0])
        defi2 = Text('''
        система счисления в которой величина,
        которую обозначает цифра, не зависит 
        от положения в числе. При этом система 
        может накладывать ограничения на положение 
        цифр, например, чтобы они были расположены 
        в порядке убывания.
        ''').scale(0.4).move_to([4, 0.3, 0])

        exp1 = MathTex('1010011_{2}').scale(0.7).move_to([-5, -1, 0])
        exp2 = MathTex('1354_{8}').scale(0.7).move_to([-5, -1.5, 0])
        exp3 = MathTex('573_{10}').scale(0.7).move_to([-5, -2, 0])
        exp4 = MathTex('1AC3_{16}').scale(0.7).move_to([-5, -2.5, 0])
        exx = [exp1, exp2, exp3, exp4]

        exn1 = Text('VII - римские числа').scale(0.7).move_to([4, -1.3, 0])
        exn2 = Text('древнеегипетские числа').scale(0.7).move_to([4, -2.3, 0])
        exs = [exn1, exn2]

        delete = VGroup(title2, title3, ar1, ar2, deli1, deli2, defi1, defi2, exn1, exn2, exp1, exp2, exp3, exp4)

        wig = Text('Позиционная').move_to([-5, 3.5, 0])

        wig1 = Text('Двоичная СС').scale(0.7).next_to([-6, 3, 0], 2*DOWN, aligned_edge=LEFT)
        wig2 = Text('Восмеричная СС').scale(0.7).next_to([-6, 1.5, 0], 2 * DOWN, aligned_edge=LEFT)
        wig3 = Text('Десятичная СС').scale(0.7).next_to([-6, 0, 0], 2 * DOWN, aligned_edge=LEFT)
        wig4 = Text('Шестнадцатеричная СС').scale(0.7).next_to([-6, -1.5, 0], 2 * DOWN, aligned_edge=LEFT)
        wigg = [wig1, wig2, wig3, wig4]

        wig_1 = Text('-').next_to([0, 3, 0], 2.5*DOWN)
        wig_2 = Text('-').next_to([0, 1.5, 0], 2.5*DOWN)
        wig_3 = Text('-').next_to([0, 0, 0], 2.5*DOWN)
        wig_4 = Text('-').next_to([0, -1.5, 0], 2.5*DOWN)
        wig_g = [wig_1, wig_2, wig_3, wig_4]

        data1 = Text('0 1').next_to([1, 3, 0], 2*DOWN, aligned_edge=LEFT)
        data2 = Text('0 1 2 3 4 5 6 7').next_to([1, 1.5, 0], 2*DOWN, aligned_edge=LEFT)
        data3 = Text('0 1 2 3 4 5 6 7 8 9').next_to([1, 0, 0], 2*DOWN, aligned_edge=LEFT)
        data4 = Text('0 1 2 3 4 5 6 7 8 9').next_to([1, -1.5, 0], 2*DOWN, aligned_edge=LEFT)
        data41 = Text('A B C D E F').next_to(data4, 2*DOWN, aligned_edge=LEFT)
        date = [data1, data2, data3, data4, data41]


        self.play(Write(title1))
        self.wait(2)
        self.remove(title1)
        self.wait()
        self.play(Write(title2))
        self.wait()
        self.play(Transform(title2, title3))
        self.wait(2)
        self.play(Create(ar1), Create(ar2))
        self.wait()
        self.play(Write(deli1))
        self.wait()
        self.play(Write(deli2))
        self.wait()
        self.play(Write(defi1))
        self.wait(2)
        self.play(Write(defi2))
        self.wait(3)
        for i in range(4):
            self.play(Write(exx[i]))
            self.wait()
        for i in range(2):
            self.play(Write(exs[i]))
            self.wait()
        self.wait(2)
        self.play(Transform(delete, wig))
        self.wait(1)
        for i in range(4):
            self.play(Write(wigg[i]))
        for i in range(4):
            self.play(Create(wig_g[i]))
        for i in range(5):
            self.play(Write(date[i]))
            self.wait(i*0.5)


class Mainalgo(Scene):
    def construct(self):

        from1 = Text('2 СС').scale(0.5).next_to([-4, 2, 0], aligned_edge=LEFT)
        from2 = Text('8 СС').scale(0.5).next_to([-4, 0, 0], aligned_edge=LEFT)
        from3 = Text('16 СС').scale(0.5).next_to([-4, -2, 0], aligned_edge=LEFT)
        fromm = [from1, from2, from3]

        to1 = Text('2 СС').scale(0.5).next_to([3, 2, 0], aligned_edge=LEFT)
        to2 = Text('8 СС').scale(0.5).next_to([3, 0, 0], aligned_edge=LEFT)
        to3 = Text('16 СС').scale(0.5).next_to([3, -2, 0], aligned_edge=LEFT)
        too = [to1, to2, to3]

        centr = Text('10 СС').scale(0.5).move_to([0, 0, 0])

        ar2_10 = Arrow([-3, 2, 0], [-0.5, 0, 0], max_tip_length_to_length_ratio=0.05, max_stroke_width_to_length_ratio=1)
        ar8_10 = Arrow([-3, 0, 0], [-0.5, 0, 0], max_tip_length_to_length_ratio=0.08, max_stroke_width_to_length_ratio=1)
        ar16_10 = Arrow([-3, -2, 0], [-0.5, 0, 0], max_tip_length_to_length_ratio=0.05, max_stroke_width_to_length_ratio=1)
        ar10_2 = Arrow([0.5, 0, 0], [3, 2, 0], max_tip_length_to_length_ratio=0.05, max_stroke_width_to_length_ratio=1)
        ar10_8 = Arrow([0.5, 0, 0], [3, 0, 0], max_tip_length_to_length_ratio=0.08, max_stroke_width_to_length_ratio=1)
        ar10_16 = Arrow([0.5, 0, 0], [3, -2, 0], max_tip_length_to_length_ratio=0.05, max_stroke_width_to_length_ratio=1)

        algo1 = Text('Алгоритм 1', color=BLUE).scale(0.5).move_to([-1.5, 3, 0])
        algo2 = Text('Алгоритм 2', color=BLUE).scale(0.5).move_to([1.5, 3, 0])


        for i in range(3):
            self.play(Write(fromm[i]))
        self.wait()
        for i in range(3):
            self.play(Write(too[i]))
        self.wait()
        self.play(GrowFromCenter(centr))
        self.wait(3)
        self.play(Write(algo1), Write(algo2))
        self.play(GrowFromCenter(ar2_10))
        self.play(GrowFromCenter(ar10_8))
        self.play(FadeToColor(ar2_10, color=RED), FadeToColor(algo1, color=RED))
        self.wait()
        self.play(FadeToColor(ar10_8, color=YELLOW), FadeToColor(algo2, color=YELLOW))
        self.wait(3)
        self.play(GrowArrow(ar8_10), GrowArrow(ar16_10))
        self.wait()
        self.play(FadeToColor(ar8_10, color=RED), FadeToColor(ar16_10, color=RED))
        self.wait()
        self.play(GrowArrow(ar10_2), GrowArrow(ar10_16))
        self.play(FadeToColor(ar10_2, color=YELLOW), FadeToColor(ar10_16, color=YELLOW))
        self.wait(3)

        #self.play(FadeToColor(Text("Hello World!"), color=RED))


class Algo1Ex1(Scene):
    def construct(self):
        
        title = Text('Aлгоритм 2').move_to([0, 3.5, 0]).scale(0.5)
        x = 123
        y = 2
        x_m = MathTex(f'{x}').next_to([-5, 2.5, 0], RIGHT, aligned_edge=UR).scale(0.65)
        l1 = Line([-4.4, 2.5, 0], [-4.4, 1.5, 0])
        l2 = Line([-4.4, 2, 0], [-3.8, 2, 0])
        y1 = MathTex(f'{y}').next_to([-4.5, 2.5, 0], 1.2*RIGHT, aligned_edge=UR).scale(0.65)
        x2 = x // y
        x2_m = MathTex(f'{x2}').move_to([-4.1, 1.75, 0]).scale(0.65)
        vch1 = x2 * y
        vch1_m = MathTex(f'{vch1}').next_to(x_m, DOWN).scale(0.65)
        minus1 = MathTex('-').move_to([-5, 2, 0]).scale(0.65)
        ll1 = Line([-5, 1.5, 0], [-4.4, 1.5, 0])
        os1 = x % y
        os1_m = MathTex(f'{os1}').move_to([-4.7, 1.3, 0]).scale(0.65)
        c1 = Circle().scale(0.25).move_to([-4.7, 1.3, 0])
        vg1 = VGroup(y1, x2_m)


        l3 = Line([-3.8, 2, 0], [-3.8, 1, 0])
        l4 = Line([-3.8, 1.5, 0], [-3.2, 1.5, 0])
        y2 = MathTex(f'{y}').next_to(x2_m, 1.5*RIGHT).scale(0.65)
        x3 = x2 // y
        x3_m = MathTex(f'{x3}').move_to([-3.5, 1.27, 0]).scale(0.65)
        vch2 = x3 * y
        vch2_m = MathTex(f'{vch2}').next_to(x2_m, DOWN).scale(0.65)
        minus2 = MathTex('-').move_to([-4.2, 1.5, 0]).scale(0.65)
        ll2 = Line([-4.4, 1, 0], [-3.8, 1, 0])
        os2 = x2 % y
        os2_m = MathTex(f'{os2}').move_to([-4.1, 0.8, 0]).scale(0.65)
        c2 = Circle().scale(0.25).move_to([-4.1, 0.8, 0])
        vg2 = VGroup(x_m, minus1, vch1_m)
        vg3 = VGroup(y2, x3_m)
        vg4 = VGroup(x2_m, minus2, vch2_m)

        l5 = Line([-3.2, 1.5, 0], [-3.2, 0.5, 0])
        l6 = Line([-3.2, 1, 0], [-2.6, 1, 0])
        y3 = MathTex(f'{y}').next_to(x3_m, 1.5*RIGHT).scale(0.65)
        x4 = x3 // y
        x4_m = MathTex(f'{x4}').move_to([-2.9, 0.75, 0]).scale(0.65)
        vch3 = x4 * y
        vch3_m = MathTex(f'{vch3}').next_to(x3_m, DOWN).scale(0.65)
        minus3 = MathTex('-').move_to([-3.6, 1, 0]).scale(0.65)
        ll3 = Line([-3.8, 0.5, 0], [-3.2, 0.5, 0])
        os3 = x3 % y
        os3_m = MathTex(f'{os3}').move_to([-3.5, 0.3, 0]).scale(0.65)
        c3 = Circle().scale(0.25).move_to([-3.5, 0.3, 0])
        vg5 = VGroup(y3, x4_m)
        vg6 = VGroup(x3_m, minus3, vch3_m)

        l7 = Line([-2.6, 1, 0], [-2.6, 0, 0])
        l8 = Line([-2.6, 0.5, 0], [-2, 0.5, 0])
        y4 = MathTex(f'{y}').next_to(x4_m, 1.5*RIGHT).scale(0.65)
        x5 = x4 // y
        x5_m = MathTex(f'{x5}').move_to([-2.3, 0.25, 0]).scale(0.65)
        vch4 = x5 * y
        vch4_m = MathTex(f'{vch4}').next_to(x4_m, DOWN).scale(0.65)
        minus4 = MathTex('-').move_to([-3, 0.5, 0]).scale(0.65)
        ll4 = Line([-3.2, 0, 0], [-2.6, 0, 0])
        os4 = x4 % y
        os4_m = MathTex(f'{os4}').move_to([-2.9, -0.2, 0]).scale(0.65)
        c4 = Circle().scale(0.25).move_to([-2.9, -0.2, 0])
        vg7 = VGroup(y4, x5_m)
        vg8 = VGroup(x4_m, minus4, vch4_m)

        l9 = Line([-2, 0.5, 0], [-2, -0.5, 0])
        l10 = Line([-2, 0, 0], [-1.4, 0, 0])
        y5 = MathTex(f'{y}').next_to(x5_m, 1.5*RIGHT).scale(0.65)
        x6 = x5 // y
        x6_m = MathTex(f'{x6}').next_to(x5_m, DOWN + 1.5*RIGHT).scale(0.65)
        vch5 = x6 * y
        vch5_m = MathTex(f'{vch5}').next_to(x5_m, DOWN).scale(0.65)
        minus5 = MathTex('-').move_to([-2.5, 0, 0]).scale(0.65)
        ll5 = Line([-2.6, -0.5, 0], [-2, -0.5, 0])
        os5 = x5 % y
        os5_m = MathTex(f'{os5}').move_to([-2.3, -0.7, 0]).scale(0.65)
        c5 = Circle().scale(0.25).move_to([-2.3, -0.7, 0])
        vg9 = VGroup(y5, x6_m)
        vg10 = VGroup(x5_m, minus5, vch5_m)

        l11 = Line([-1.4, 0, 0], [-1.4, -1, 0])
        l12 = Line([-1.4, -0.5, 0], [-0.8, -0.5, 0])
        y6 = MathTex(f'{y}').next_to(x6_m, 1.5*RIGHT).scale(0.65)
        x7 = x6 // y
        x7_m = MathTex(f'{x7}').next_to(x6_m, DOWN + 1.5*RIGHT).scale(0.65)
        vch6 = x7 * y
        vch6_m = MathTex(f'{vch6}').next_to(x6_m, DOWN).scale(0.65)
        minus6 = MathTex('-').move_to([-1.8, -0.5, 0]).scale(0.65)
        ll6 = Line([-2, -1, 0], [-1.4, -1, 0])
        os6 = x6 % y
        os6_m = MathTex(f'{os6}').move_to([-1.7, -1.2, 0]).scale(0.65)
        c6 = Circle().scale(0.25).move_to([-1.7, -1.2, 0])
        vg11 = VGroup(y6, x7_m)
        vg12 = VGroup(x6_m, minus6, vch6_m)

        c7 = Circle().scale(0.25).move_to(x7_m)

        
        
        
        self.play(Write(title))
        self.wait()
        self.play(Write(x_m))
        self.play(Create(l1), Create(l2))
        self.play(Write(y1))
        self.wait()
        self.play(Write(x2_m))
        self.play(TransformFromCopy(vg1, vch1_m), run_time=2)
        self.wait()
        self.play(Create(minus1))
        self.play(Create(ll1))
        self.play(TransformFromCopy(vg2, os1_m), run_time=2)
        self.wait()
        self.play(Create(c1))
        self.wait()
        self.play(Create(l3), Create(l4))
        self.play(Write(y2))
        self.wait()
        self.play(Write(x3_m))
        self.play(TransformFromCopy(vg3, vch2_m), run_time=2)
        self.wait()
        self.play(Create(minus2))
        self.play(Create(ll2))
        self.play(TransformFromCopy(vg4, os2_m), run_time=2)
        self.wait()
        self.play(Create(c2))
        self.wait()
        self.play(Create(l5), Create(l6))
        self.play(Write(y3))
        self.wait()
        self.play(Write(x4_m))
        self.play(TransformFromCopy(vg5, vch3_m), run_time=2)
        self.wait()
        self.play(Create(minus3))
        self.play(Create(ll3))
        self.play(TransformFromCopy(vg6, os3_m), run_time=2)
        self.wait()
        self.play(Create(c3))
        self.wait()
        self.play(Create(l7), Create(l8))
        self.play(Write(y4))
        self.wait()
        self.play(Write(x5_m))
        self.play(TransformFromCopy(vg7, vch4_m), run_time=2)
        self.wait()
        self.play(Create(minus4))
        self.play(Create(ll4))
        self.play(TransformFromCopy(vg8, os4_m), run_time=2)
        self.wait()
        self.play(Create(c4))
        self.wait()
        self.play(Create(l9), Create(l10))
        self.play(Write(y5))
        self.wait()
        self.play(Write(x6_m))
        self.play(TransformFromCopy(vg9, vch5_m), run_time=2)
        self.wait()
        self.play(Create(minus5))
        self.play(Create(ll5))
        self.play(TransformFromCopy(vg10, os5_m), run_time=2)
        self.wait()
        self.play(Create(c5))
        self.wait()
        self.play(Create(l11), Create(l12))
        self.play(Write(y6))
        self.wait()
        self.play(Write(x7_m))
        self.play(TransformFromCopy(vg11, vch6_m), run_time=2)
        self.wait()
        self.play(Create(minus6))
        self.play(Create(ll6))
        self.play(TransformFromCopy(vg12, os6_m), run_time=2)
        self.wait()
        self.play(Create(c6))
        self.wait(2)
        self.play(Create(c7))
        self.wait()

class Algo2Ex3(Scene):
    def construct(self):
        
        x = 2398
        y = 16
        x_m = MathTex(f'{x}').move_to([-5, 2.5, 0]).scale(1.3)
        l1 = Line([-4, 3, 0], [-4, 1, 0])
        l2 = Line([-4, 2, 0], [-2, 2, 0])
        y1 = MathTex(f'{y}').move_to([-3, 2.5, 0]).scale(1.3)
        title = MathTex(f'{x}','_{10}', '=?', '_{16}').scale(3)
        

        x2 = x // y
        x2_m = MathTex(f'{x2}').move_to([-3, 1.5, 0]).scale(1.3)
        vg1 = VGroup(y1, x2_m)
        vch1 = x2 * y
        vch1_m = MathTex(f'{vch1}').move_to([-5, 1.5, 0]).scale(1.3)
        ll1 = Line([-6, 1, 0], [-4, 1, 0])
        os1 = x % y
        os1_m = MathTex(f'{os1}').move_to([-5, 0.5, 0]).scale(1.3)
        c1 = Circle().scale(0.5).move_to([-5, 0.5, 0])
        minus1 = MathTex('-').move_to([-6, 2, 0]).scale(1.3)
        vg2 = VGroup(x_m, minus1, vch1_m)


        l3 = Line([-2, 2, 0], [-2, 0, 0])
        l4 = Line([-2, 1, 0], [0, 1, 0])
        grp2 = VGroup(l3, l4)
        y2 = MathTex(f'{y}').move_to([-1, 1.5, 0]).scale(1.3)
        x3 = x2 // y
        x3_m = MathTex(f'{x3}').move_to([-1, 0.5, 0]).scale(1.3)
        vch2 = x3 * y
        vch2_m = MathTex(f'{vch2}').move_to([-3, 0.5, 0]).scale(1.3)
        ll2 = Line([-4, 0, 0], [-2, 0, 0])
        os2 = x2 % y
        os2_m = MathTex(f'{os2}').move_to([-3, -0.5, 0]).scale(1.3)
        c2 = Circle().scale(0.5).move_to([-3, -0.5, 0])
        minus2 = MathTex('-').move_to([-3.6, 1, 0]).scale(1.3)
        vg3 = VGroup(y2, x3_m)
        vg4 = VGroup(x2_m, minus2, vch2_m)


        
        c3 = Circle().scale(0.5).move_to([-1, 0.5, 0])


        
        self.play(Write(title))
        self.wait()
        self.remove(title)
        self.wait()
        self.play(Write(x_m))
        self.play(Create(l1), Create(l2))
        self.play(Write(y1))
        self.wait()
        self.play(Write(x2_m))
        self.play(TransformFromCopy(vg1, vch1_m), run_time=2)
        self.wait()
        self.play(Create(minus1))
        self.play(Create(ll1))
        self.play(TransformFromCopy(vg2, os1_m), run_time=2)
        self.wait()
        self.play(Create(c1))
        self.play(Create(grp2))
        self.play(Write(y2))
        self.play(Write(x3_m))
        self.play(TransformFromCopy(vg3, vch2_m), run_time=2)
        self.wait()
        self.play(Create(minus2))
        self.play(Create(ll2))
        self.play(TransformFromCopy(vg4, os2_m), run_time=2)
        self.wait()
        self.play(Create(c2))
        self.wait()
        self.play(Create(c3))
        self.wait()

class Algo1Ex2(Scene):
    def construct(self):


        x = 1390
        y = 8
        x_m = MathTex(f'{x}').move_to([-5, 2.5, 0]).scale(1.3)
        l1 = Line([-4, 3, 0], [-4, 1, 0])
        l2 = Line([-4, 2, 0], [-2, 2, 0])
        y1 = MathTex('8').move_to([-3, 2.5, 0]).scale(1.3)
        title = MathTex(f'{x}','_{10}', '=?').scale(3)
        

        x2 = x // y
        x2_m = MathTex(f'{x2}').move_to([-3, 1.5, 0]).scale(1.3)
        vg1 = VGroup(y1, x2_m)
        vch1 = x2 * y
        vch1_m = MathTex(f'{vch1}').move_to([-5, 1.5, 0]).scale(1.3)
        ll1 = Line([-6, 1, 0], [-4, 1, 0])
        os1 = x % y
        os1_m = MathTex(f'{os1}').move_to([-5, 0.5, 0]).scale(1.3)
        c1 = Circle().scale(0.5).move_to([-5, 0.5, 0])
        minus1 = MathTex('-').move_to([-6, 2, 0]).scale(1.3)
        vg2 = VGroup(x_m, minus1, vch1_m)


        l3 = Line([-2, 2, 0], [-2, 0, 0])
        l4 = Line([-2, 1, 0], [0, 1, 0])
        grp2 = VGroup(l3, l4)
        y2 = MathTex('8').move_to([-1, 1.5, 0]).scale(1.3)
        x3 = x2 // y
        x3_m = MathTex(f'{x3}').move_to([-1, 0.5, 0]).scale(1.3)
        vch2 = x3 * y
        vch2_m = MathTex(f'{vch2}').move_to([-3, 0.5, 0]).scale(1.3)
        ll2 = Line([-4, 0, 0], [-2, 0, 0])
        os2 = x2 % y
        os2_m = MathTex(f'{os2}').move_to([-3, -0.5, 0]).scale(1.3)
        c2 = Circle().scale(0.5).move_to([-3, -0.5, 0])
        minus2 = MathTex('-').move_to([-3.6, 1, 0]).scale(1.3)
        vg3 = VGroup(y2, x3_m)
        vg4 = VGroup(x2_m, minus2, vch2_m)


        l5 = Line([0, 1, 0], [0, -1, 0])
        l6 = Line([0, 0, 0], [2, 0, 0])
        grp3 = VGroup(l5, l6)
        y3 = MathTex('8').move_to([1, 0.5, 0]).scale(1.3)
        x4 = x3 // y
        x4_m = MathTex(f'{x4}').move_to([1, -0.5, 0]).scale(1.3)
        vch3 = x4 * y
        vch3_m = MathTex(f'{vch3}').move_to([-1, -0.5, 0]).scale(1.3)
        ll3 = Line([-2, -1, 0], [0, -1, 0])
        os3 = x3 % y
        os3_m = MathTex(f'{os3}').move_to([-1, -1.5, 0]).scale(1.3)
        c3 = Circle().scale(0.5).move_to([-1, -1.5, 0])
        minus3 = MathTex('-').move_to([-1.6, 0, 0]).scale(1.3)
        c4 = Circle().scale(0.5).move_to([1, -0.5, 0])
        vg5 = VGroup(y3, x4_m)
        vg6 = VGroup(x3_m, minus3, vch3_m)

        vg7 = VGroup(x4_m, os3_m, os2_m, os1_m)
        ques = MathTex(f'{x}','_{10}').scale(1.3).move_to([-5.2, -3, 0])
        rav = MathTex('=').scale(1.3).move_to([-4, -3, 0])
        res = MathTex(f'{str(x4)+str(os3)+str(os2)+str(os1)}', '_{8}').scale(1.3).move_to([-2.9, -3, 0])




        self.play(Write(title))
        self.wait()
        self.remove(title)
        self.wait()
        self.play(Write(x_m))
        self.play(Create(l1), Create(l2))
        self.play(Write(y1))
        self.wait()
        self.play(Write(x2_m))
        self.play(TransformFromCopy(vg1, vch1_m), run_time=2)
        self.wait()
        self.play(Create(minus1))
        self.play(Create(ll1))
        self.play(TransformFromCopy(vg2, os1_m), run_time=2)
        self.wait()
        self.play(Create(c1))
        self.play(Create(grp2))
        self.play(Write(y2))
        self.play(Write(x3_m))
        self.play(TransformFromCopy(vg3, vch2_m), run_time=2)
        self.wait()
        self.play(Create(minus2))
        self.play(Create(ll2))
        self.play(TransformFromCopy(vg4, os2_m), run_time=2)
        self.wait()
        self.play(Create(c2))
        self.play(Create(grp3))
        self.play(Write(y3))
        self.play(Write(x4_m))
        self.play(TransformFromCopy(vg5, vch3_m), run_time=2)
        self.wait()
        self.play(Create(minus3))
        self.play(Create(ll3))
        self.play(TransformFromCopy(vg6, os3_m), run_time=2)
        self.wait()
        self.play(Create(c3))
        self.play(Create(c4))
        self.wait()
        self.play(Write(ques), Create(rav))
        self.wait()
        self.play(TransformFromCopy(vg7, res), run_time=2)
        self.wait(2)

class MyScene1(Scene):
    def construct(self):

        x = '10101001'
        y = 2
        


        title = MathTex(f'{x}','_{2}', '=?', '_{10}').scale(3)
        mobs = []
        pow = []
        pows = []
        for i in range(len(str(x))):
            mobs.append(MathTex(f'{x[i]}'))
            pow.append(MathTex(f'2'))
            pows.append(MathTex(f'^{i}'))
        
        pows.reverse()

        mobs[0].move_to([-1.5, 3, 0])
        pow[0].move_to([-1.5, 2, 0])
        pows[0].move_to([-1.35, 2.26, 0])

        for i in range(len(mobs)-1):
            mobs[i+1].next_to(mobs[i], RIGHT, aligned_edge=UP)
            pow[i+1].next_to(pow[i], RIGHT, aligned_edge=UP).scale(0.95)
            pows[i+1].next_to(pow[i], 1.6*RIGHT+0.9*UP, aligned_edge=UP)

        #self.add(*pow)
        #self.add(*mobs)
        #self.add(*pows)


        d0 = Dot([-1.5, 2.5, 0]).scale(0.5)
        d1 = Dot([-1, 2.5, 0]).scale(0.5)
        d2 = Dot([-0.6, 2.5, 0]).scale(0.5)
        d3 = Dot([-0.1, 2.5, 0]).scale(0.5)
        d4 = Dot([0.2, 2.5, 0]).scale(0.5)
        d5 = Dot([0.8, 2.5, 0]).scale(0.5)
        d6 = Dot([1.2, 2.5, 0]).scale(0.5)
        d7 = Dot([1.6, 2.5, 0]).scale(0.5)

        dd = [d0, d1, d2, d3, d4, d5, d6, d7]

        vg0 = VGroup(mobs[0], pow[0], pows[0], d0)
        vg1 = VGroup(mobs[1], pow[1], pows[1], d1)
        vg2 = VGroup(mobs[2], pow[2], pows[2], d2)
        vg3 = VGroup(mobs[3], pow[3], pows[3], d3)
        vg4 = VGroup(mobs[4], pow[4], pows[4], d4)
        vg5 = VGroup(mobs[5], pow[5], pows[5], d5)
        vg6 = VGroup(mobs[6], pow[6], pows[6], d6)
        vg7 = VGroup(mobs[7], pow[7], pows[7], d7)


        box0 = SurroundingRectangle(vg0, color=YELLOW)
        box1 = SurroundingRectangle(vg1, color=YELLOW)
        box2 = SurroundingRectangle(vg2, color=YELLOW)
        box3 = SurroundingRectangle(vg3, color=YELLOW)
        box4 = SurroundingRectangle(vg4, color=YELLOW)
        box5 = SurroundingRectangle(vg5, color=YELLOW)
        box6 = SurroundingRectangle(vg6, color=YELLOW)
        box7 = SurroundingRectangle(vg7, color=YELLOW)

        boxx = [box0, box1, box2, box3, box4, box5, box6, box7]

        l1 = Line([-2, 1.5, 0], [2, 1.5, 0])
        r = MathTex(f'{128}+{32}+{8}+{1}').move_to([0, 0.8, 0])

        sum = MathTex(f'{128+32+8+1}').move_to([0, -0.2, 0])

        ques = MathTex(f'{x}','_{2}').scale(1.3).move_to([-5.2, -3, 0])
        rav = MathTex('=').scale(1.3).move_to([-3.4, -3, 0])
        res = MathTex(f'{169}', '_{10}').scale(1.3).move_to([-2.2, -3, 0])

        #zz = [(vg0, r[0]), (vg1, r[1]), (vg2, r[2]), (vg3, r[3]), (vg4, r[4]), (vg5, r[5]), (vg6, r[5]), (vg7, r[6])]


        self.play(Write(title))
        self.wait(1.5)
        self.remove(title)
        self.play(Write(mobs[0]), Write(mobs[1]), Write(mobs[2]), Write(mobs[3]), Write(mobs[4]), Write(mobs[5]), Write(mobs[6]), Write(mobs[7]), run_time=2)
        self.wait()
        for i in range(8):
            self.play(Write(pow[i]), run_time=0.5)
        self.wait()
        for i in range(8):
            self.play(Write(pows[7-i]), run_time=0.5)
        self.wait(2)
        for i in range(8):
            self.play(Create(dd[i]), run_time=0.5)
        for i in range(8):
            self.play(Create(boxx[i]), run_time=0.5)
        self.wait()
        self.play(Create(l1))
        self.wait()
        self.play(FadeIn(r))
        self.wait(2)
        self.play(TransformFromCopy(r, sum))
        self.wait()
        self.play(Write(ques), Write(rav))
        self.play(TransformFromCopy(sum, res))
        self.wait(2)


class per_to_10(Scene):
    def construct(self):

        x = '5 1 1 4'
        x.split()
        y = 8
        the_length = len(x)
        
        def perevod_to_10(x, y):
            s = 0
            p = 0
            for i in x:
                i = int(i)
                s +=  i * y**p
                p += 1
            return s



        origins = [-the_length//2, 2.5, 0]
        
        for i in x:
            
            c = MathTex(f'{i}')
            
            


 
        self.number_plane = NumberPlane()
        self.add(self.number_plane)



if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
    
    
