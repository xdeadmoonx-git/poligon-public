#Переделанная функция генерации частиц с "Связанные лагерем" так, чтобы можно было добавлять больше частиц без указания точного кол-ва
init python:

    # Простое представление векторов
    class ShortVector(renpy.object.Object):
       
        def __init__(self, *data):
            self.data = data

        def __repr__(self):
            return repr(self.data)

        def __add__(self, other):
            return tuple(a + b for a, b in zip(self.data, other.data))

        def __sub__(self, other):
            return tuple(a - b for a, b in zip(self.data, other.data))

    
    # Описание состояния одной частицы
    class ShortParticleData(renpy.object.Object):
        def __init__(self, sp, fp, t, rt, ft, zoom, alpha, st):
            self.start_pos = sp
            self.finish_pos = fp

            self.part_time = t
            self.rise_time = rt
            self.fall_time = ft

            self.max_zoom = zoom
            self.max_alpha = alpha

            self.oldst = st
            self.pos = self.start_pos
            self.zoom = .0
            self.alpha = .0
            
            self.img = None

    # Здесь образуем множество частиц на экране
    class ShortParticles(renpy.Displayable):
        from random import randint, uniform, choice
        from math import sqrt, pow

        def __init__(self, *args, **kwargs):
            #parts_count указывает, какое кол-во частиц будет на экране (рекомендуется 125-200, дальше фпс просто просядет)
            parts_count = kwargs.pop('parts_count', 200)
            super(ShortParticles, self).__init__()

            #Т.к сука тут старый Python, то пришлось разделять с помощью отрезания
            part_imgs = args[:-2]
            vin_img   = args[-2]
            vin_alpha = args[-1]

            self.part_imgs = [renpy.displayable(img) for img in part_imgs]
            self.vingette = renpy.displayable(vin_img)
            self.vin_alpha = vin_alpha

            self.w, self.h = (config.screen_width, config.screen_height)

            self.particles = [self.make_particle() for _ in xrange(parts_count)]

        def get_rand_cord(self, w, h):
            """
            Возвращает случайную пару координат (x, y) внутри экрана
            """
            return self.randint(0, w), self.randint(0, h)

        def progress_calc(self, oldst, t, st):
            """
            Рассчитывает относительный прогресс анимации:
            oldst — время старта сегмента,
            t — длительность сегмента,
            st — текущее время.
            Возвращает значение в диапазоне [0.0, 1.0].
            """
            target = oldst + t
            anim_time = target - st
            res = 1.0 - anim_time / t

            if res < .0:
                return .0
            elif .0 <= res <= 1.0:
                return res
            else:
                return 1.0

        def make_particle(self, st=float()):
            """
            Создаёт новый объект ShortParticleData с случайными параметрами:
            позиции, время жизни, скорости, масштаб и прозрачность.
            """
            w, h = self.w, self.h

            start_pos = self.get_rand_cord(w, h)
            finish_pos = self.get_rand_cord(w, h)
            xdist, ydist = ShortVector(*finish_pos) - ShortVector(*start_pos)

            speed = self.uniform(90, 110)

            part_time = self.sqrt(self.pow(xdist, 2) + self.pow(ydist, 2)) / speed
            rise_time = part_time * self.uniform(.1, .25)
            fall_time = part_time * self.uniform(.1, .25)

            max_alpha = self.uniform(.25, .75)
            max_zoom = self.uniform(.25, .75)

            part = ShortParticleData(
                start_pos,
                finish_pos,
                part_time,
                rise_time,
                fall_time,
                max_zoom,
                max_alpha,
                st
            )
            
            # Берем рандом частицу.
            part.img = self.choice(self.part_imgs)
            return part

        def update_particle(self, part_idx, st):
            """
            Обновляет состояние частицы:
            вычисляет прогресс анимации, позицию, прозрачность и масштаб,
            перерождает частицу по окончании её жизни.
            """
            part = self.particles[part_idx]

            t = part.part_time
            rt = part.rise_time
            ft = part.fall_time

            start_time = part.oldst
            rise_time = start_time + rt
            fall_time = start_time + t - ft

            anim_progress = self.progress_calc(start_time, t, st)
            rise_progress = self.progress_calc(rise_time, rt, st)
            fall_progress = self.progress_calc(fall_time, ft, st)

            rise_vs_fall = rise_progress - fall_progress

            part.pos = renpy.atl.interpolate(
                anim_progress,
                part.start_pos,
                part.finish_pos,
                (int, int)
            )

            part.alpha = part.max_alpha * rise_vs_fall
            part.zoom = part.max_zoom * rise_vs_fall

            if anim_progress >= 1.0:

                self.particles.pop(part_idx)
                self.particles.append(self.make_particle(st))

        def visit(self):
            """
            Возвращает список текущих изображений для отрисовки —
            Ren’Py вызывает этот метод для построения списка children.
            """
            return [part.img for part in self.particles]

        def render(self, w, h, st, at):
            """
            Основной метод отрисовки. Создаёт Render-объект, обновляет все частицы,
            рендерит каждую с учётом alpha и zoom, затем накладывает виньетку.
            """
            rv = renpy.Render(w, h)

            for idx, part in enumerate(self.particles):
                self.update_particle(idx, st)
                xpos, ypos = part.pos

                t = Transform(
                    child=part.img,
                    alpha=part.alpha,
                    zoom=part.zoom
                )

                tr = t.render(w, h, st, at)
                rv.blit(tr, (xpos, ypos))


            vt = Transform(self.vingette, alpha=self.vin_alpha)
            v_rend = renpy.render(vt, w, h, st, at)
            rv.blit(v_rend, (0, 0))

            renpy.redraw(self, 0.0)
            return rv
