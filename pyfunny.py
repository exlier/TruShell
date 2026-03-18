import cowsay
import pyjokes

import typer

from playsound import playsound
import random

app = typer.Typer(help="Joke REPL: Type 'cow', 'trex', or 'exit'.")

# Individual Commands

@app.command()
def joke():
    joke = pyjokes.get_joke()
    
    # Play sound, and show joke
    playsound(r'chronoterm/sounds/faaah-sound.mp3')
    return cowsay.cow(joke)
    
    

# Use an absolute path for reliability (e.g., 'C:\\Users\\YourUser\\Music\\song.mp3')
# Place an 'r' before the string to handle backslashes correctly in Windows paths

    playsound(audio_file_path)

@app.command()
def joke_trex():
    joke = pyjokes.get_joke()

    
    playsound(r'chronoterm/sounds/bruh-sound.mp3')
    return cowsay.trex(joke)

# # Interactive Shell
# @app.command()
# def repl():
#     """Starts an interactive shell for jokes."""
#     typer.secho("Entering Joke REPL. Type 'exit' to quit.", fg=typer.colors.CYAN)
    
#     # The Loop
#     while True:
#         # Read
#         command = typer.prompt("joke-shell").lower().strip()

#         # Evaluate & Print
#         if command in ["exit", "quit"]:
#             break
#         elif command == "cow":
#             cow()
#         elif command == "trex":
#             trex()
#         elif command == "help":
#             print("Available commands: cow, trex, exit, help")
#         else:
#             typer.secho(f"Unknown command: {command}", fg=typer.colors.RED)


if __name__ == "__main__":
    app()