if __name__ == "__main__":
    from Views.MenuView import MenuView
else:
    from ..Views.MenuView import MenuView

class App:

    def __init__(self):
        pass

    def run(self):
        start_menu = MenuView()
        start_menu.run()