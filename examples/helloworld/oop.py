from cliapptool import CliApp


class HelloWorld(CliApp):
    def __init__(self) -> None:
        super().__init__()
        self.add_flag("name", self.name)

    def name(self, name: str) -> None:
        print(f"Hello {name}!")


if __name__ == "__main__":
    app = HelloWorld()
    app.run()
