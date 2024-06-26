from cliapp import CliApp


app = CliApp()


@app.flag("name")    
def name(name: str) -> None:
    print(f"Hello {name}!")


app.run()
