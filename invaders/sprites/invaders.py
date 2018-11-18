import cocos
import cocos.collision_model as cm
import cocos.euclid as eu


class Invaders(object):
    def __init__(self, layer, resources):
        self.sprites = self.init_sprites(layer, resources)
        self.sprite_width = 32
        self.sprite_spacing = 5
        self.max_left = 0 + (self.sprite_width / 2)
        self.max_right = layer.width + (self.sprite_width / 2) + self.sprite_spacing

    def move_sprites(self, dt, missile):
        next_sprite_dist = self.sprite_width + self.sprite_spacing

        for y in range(5):
            left_limit = self.max_left
            right_x_offset = self.get_right_x_offset() + 1
            right_limit = self.max_right - (right_x_offset * next_sprite_dist)
            for x in range(11):
                self.sprites[y][x].move(dt, right_limit, left_limit)

                if missile is not None and \
                   missile.visible and \
                   self.sprites[y][x].visible:
                    self.sprites[y][x].set_cshape()
                    if missile.cshape.overlaps(self.sprites[y][x].cshape):
                        self.sprites[y][x].visible = False
                        missile.visible = False
                        missile.parent.remove("missile")

                left_x_offset = self.get_left_x_offset()
                left_limit = self.max_left + ((x-left_x_offset) * next_sprite_dist)

                right_x_offset = self.get_right_x_offset()
                right_limit = self.max_right - ((right_x_offset-x) * next_sprite_dist)

    def get_right_x_offset(self):
        result = 10
        for x in range(10, -1, -1):
            if self.sprites[0][x].visible == False and \
               self.sprites[1][x].visible == False and \
               self.sprites[2][x].visible == False and \
               self.sprites[3][x].visible == False and \
               self.sprites[4][x].visible == False:
                result = x - 1
            else:
                break
        return result

    def get_left_x_offset(self):
        result = -1
        for x in range(11):
            if self.sprites[0][x].visible == False and \
               self.sprites[1][x].visible == False and \
               self.sprites[2][x].visible == False and \
               self.sprites[3][x].visible == False and \
               self.sprites[4][x].visible == False:
                result = x
            else:
                break
        return result

    def init_sprites(self, layer, resources):
        result = [ [], [], [], [], [] ]
        start_position = (50, layer.height-100)
        width_inc = 32 + 5
        height_inc = 32 + 5

        for y in range(5):
            for x in range(11):
                invader = Invader(resources, start_position)
                result[y].append(invader)
                layer.add(invader)
                start_position = (start_position[0]+width_inc, start_position[1])
            start_position = (50, start_position[1]-height_inc)

        return result


class Invader(cocos.sprite.Sprite):
    def __init__(self, resources, start_position):
        super(Invader, self).__init__(resources.animated_invader)
        self.x = self.width / 2 + start_position[0]
        self.y = self.height / 2 + start_position[1]
        self.direction = "RIGHT"
        self.cshape = None
        self.set_cshape()

    def set_cshape(self):
        self.cshape = cm.CircleShape(eu.Vector2(self.x, self.y), 10)

    def move(self, dt, right_limit, left_limit):
        if self.direction == "RIGHT":
                self.move_right(dt*30, right_limit)
        elif self.direction == "LEFT":
                self.move_left(dt*30, left_limit)

    def move_down(self, distance, next_direction):
        new_y = self.y - distance
        bottom = 0 + self.height / 2
        if new_y > bottom:
            self.y = new_y
            self.direction = next_direction

    def move_right(self, distance, right_limit):
        new_x = self.x + distance
        if new_x < right_limit:
            self.x = new_x
        else:
            self.move_down(self.height / 2, "LEFT")

    def move_left(self, distance, left_limit):
        new_x = self.x - distance
        if new_x > left_limit:
            self.x = new_x
        else:
            self.move_down(self.height / 2, "RIGHT")
