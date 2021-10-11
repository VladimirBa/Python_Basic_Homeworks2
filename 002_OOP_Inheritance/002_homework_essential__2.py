class GraphicObject:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Rectangle(GraphicObject):
    def draw(self):
        print("The button is OFF.")
        print('\n'.join(["- " * self.width] * self.height))


class Button(Rectangle):
    def __init__(self, width, height, push=''):
        super().__init__(width, height)
        self.push = push

    def push_on(self, push):
        if push == 'off':
            Rectangle.draw(self)
        elif push == 'on':
            print("The button is ON.")
            print('\n'.join(["* " * self.width] * self.height))


width = 6
height = 4


def main():

    push = input('To turn button on enter "on", to off - enter "off": ').lower()
    if push == "on" or push == 'off':
        button = Button(width, height, push)
        button.push_on(push)
    else:
        print("Enter correct action: 'on' or 'off'!")


if __name__ == '__main__':
    main()
