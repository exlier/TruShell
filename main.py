from pyfunny import joke, joke_trex
from todocli import addtask, deletetask, updatetask, completetask, showtask

from chronoterm.shell import now, world, tz, alarm, sw, shell, run

import typer
import re


app = typer.Typer(help="Joke REPL: Type 'cow', 'trex', or 'exit'.")


# Interactive Shell
@app.command()
def atoffice():
    """Starts an interactive shell for jokes."""
    typer.secho("Entering AtOffice REPL. Type 'exit' to quit.", fg=typer.colors.CYAN)
    
    # The Loop
    while True:
        # Shell prompt
        command = typer.prompt("atoffice-shell").lower().strip()

        

        # PyJoke module
        if command in ["exit", "quit"]:
            break
        elif command == "joke":
            joke()
        elif command == "joke_trex":
            joke_trex()

      
        # ToDoCLI module
        elif match := re.match(r"deletetask\s(\d+)", command):
            position = int(match.group(1))
            deletetask(position)

        elif match := re.match(r'addtask\s+"([^"]+)"\s+"([^"]+)"', command):
            task_name = match.group(1)
            category_name = match.group(2)
            addtask(task_name, category_name)

        elif match := re.match(r'updatetask\s+(\d+)\s+"([^"]+)"\s+"([^"]+)"', command):
            position = int(match.group(1))
            task = match.group(2)
            category = match.group(3)
            updatetask(position, task, category)

        elif match := re.match(r'completetask\s+(\d+)', command):
            position = int(match.group(1))
            completetask(position)

        elif command == "showtasks":
            showtask()


        # Chronoterm module
        elif command == "now":
            now()
        
        elif command == "world":
            world()
        
        elif command.startswith("tz"):
            tz(command.replace("tz", "", 1).strip())
        
        elif match := re.match(r"^alarm(?:\s+(.*))?$", command):
            args = match.group(1) or ""
            alarm(args)

        elif match := re.match(r"^sw(?:\s+(.*))?$", command):
            args = match.group(1) or ""
            sw(args)


        # additionals...
        elif command == "help":
            print("Available commands: joke, joke_trex, \n addtask, deletetask, updatetask, completetask, showtask, \nnow, world, tz, alarm, sw, \nexit, help")
        else:
            typer.secho(f"Unknown command: {command}", fg=typer.colors.RED)


if __name__ == "__main__":
    app()