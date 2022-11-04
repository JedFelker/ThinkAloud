"""
    Name: movie_info.py
    Author: Jed Felker
    Created: 11/3/22
    Say the name of an available movie and recieve the info
"""

# pip install rich
# Import Console for console printing
from rich.console import Console
# Import Panel for title displays
from rich.panel import Panel

# Initialize rich.console
console = Console()

def main():
    programTitle()
    printMenu()
    getMovie()


def programTitle():
    console.print(
        Panel.fit(
            " Jed's Movie Center ",
            style="bright_green",
            subtitle="by Jed Felker"
        )
    )

def printMenu():
    console.print("\n[1] [bright_red]The Lord of the Rings: The Fellowship of the Ring[/bright_red]")
    console.print("[2] [bright_green]Avengers: Infinity War[/bright_green]")
    console.print("[3] [bright_yellow]Forrest Gump[/bright_yellow]")
    console.print("[4] [bright_blue]Weird Science[/bright_blue]")
    console.print("[5] [bright_magenta]The Batman[/bright_magenta]")
    console.print("[6] [bright_cyan]Avatar[/bright_cyan]")

def getMovie():
    user = input("\nWhich movie would you like to see information for: ")

    if (user == "1"):
        lotrFellowship()
    elif (user == "2"):
        avengersIW()
    elif (user == "3"):
        forrestGump()
    
def lotrFellowship():
    console.print("\nTitle: [bright_red]The Lord of the Rings: The Fellowship of the Rings[/bright_red]")
    console.print("Director: [bright_red]Peter Jackson[/bright_red]")
    console.print("Release Date: [bright_red]December 10, 2001[/bright_red]")
    console.print("Streaming: [bright_red]Prime Video[/bright_red], [bright_red]AppleTV[/bright_red] ([dark_green]$3.99[/dark_green]), [bright_red]Vudu[/bright_red] ([dark_green]$3.99[/dark_green]), [bright_red]HBO Max[/bright_red]")
    console.print("Description: [bright_red]The future of civilization rests in the fate of the One Ring, which has been lost for centuries. Powerful forces are unrelenting in their search for it. But fate has placed it in the hands of a young Hobbit named Frodo Baggins (Elijah Wood), who inherits the Ring and steps into legend. A daunting task lies ahead for Frodo when he becomes the Ringbearer - to destroy the One Ring in the fires of Mount Doom where it was forged.[/bright_red]")

def avengersIW():
    console.print("\nTitle: [bright_green]Avengers: Infinity War[/bright_green]")
    console.print("Director: [bright_green]Anthony Russo, Joe Russo[/bright_green]")
    console.print("Release Date: [bright_green]April 27, 2018[/bright_green]")
    console.print("Streaming: [bright_green]Disney+[/bright_green], [bright_green]AppleTV[/bright_green] ([dark_green]$3.99[/dark_green]), [bright_green]Vudu[/bright_green] ([dark_green]$3.99[/dark_green]), [bright_green]Redbox[/bright_green] ([dark_green]$3.99[/dark_green]), [bright_green]Google Play Movies[/bright_green] ([dark_green]$3.99[/dark_green]), [bright_green]Prime Video[/bright_green] ([dark_green]$3.99[/dark_green]), [bright_green]Youtube[/bright_green] ([dark_green]$3.99[/dark_green])")
    console.print("Description: [bright_green]Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality. The fate of the planet and existence itself has never been more uncertain as everything the Avengers have fought for has led up to this moment.[/bright_green]")

def forrestGump():
    console.print("\nTitle: [bright_yellow]Forrest Gump[/bright_yellow]")
    console.print("Director: [bright_yellow]Robert Zemeckis[/bright_yellow]")
    console.print("Release Date: [bright_yellow]July 6, 1994[/bright_yellow]")
    console.print("Streaming: [bright_yellow]Paramount+[/bright_yellow], [bright_yellow]AppleTV[/bright_yellow] ([dark_green]$3.99[/dark_green]), [bright_yellow]Vudu[/bright_yellow] ([dark_green]$2.99[/dark_green]), [bright_yellow]Redbox[/bright_yellow] ([dark_green]$2.99[/dark_green]), [bright_yellow]Google Play Movies[/bright_yellow] ([dark_green]$2.99[/dark_green]), [bright_yellow]Prime Video[/bright_yellow], [bright_yellow]Youtube[/bright_yellow] ([dark_green]$2.99[/dark_green]), [bright_yellow]Pluto TV[/bright_yellow]")
    console.print("Description: [bright_yellow]Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality. The fate of the planet and existence itself has never been more uncertain as everything the Avengers have fought for has led up to this moment.[/bright_green]")


main()