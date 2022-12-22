# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def mvmntobjbfld(self, field, axis_x, axis_y, direction, is_fly, is_creep, speed_factor=1):
        """Функция реализует перемещение юнита по полю."""
        if is_fly and is_creep:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed_factor *= 1.2
            if direction == 'UP':
                new_y = axis_y + speed_factor
                new_x = axis_x
            elif direction == 'DOWN':
                new_y = axis_y - speed_factor
                new_x = axis_x
            elif direction == 'LEFT':
                new_y = axis_y
                new_x = axis_x - speed_factor
            elif direction == 'RIGHT':
                new_y = axis_y
                new_x = axis_x + speed_factor
        if is_creep:
            speed_factor *= 0.5
            if direction == 'UP':
                new_y = axis_y + speed_factor
                new_x = axis_x
            elif direction == 'DOWN':
                new_y = axis_y - speed_factor
                new_x = axis_x
            elif direction == 'LEFT':
                new_y = axis_y
                new_x = axis_x - speed_factor
            elif direction == 'RIGHT':
                new_y = axis_y
                new_x = axis_x + speed_factor

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
