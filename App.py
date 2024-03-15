from Controller import Controller


class App:
    def __init__(self):
        self.controller = Controller()
        self.controller.main()


if __name__ == "__main__":
    App()
