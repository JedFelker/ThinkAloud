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

    again = input("Would you like to pick again? (y/enter) ")

    if (again == "y"):
        main()
    elif (again == ""):
        exit()


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
    elif (user == "4"):
        weirdScience()
    elif (user == "5"):
        theBatman()
    elif(user == "6"):
        avatar()
    else:
        print("Please choose a valid option")
        getMovie()
    
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
    console.print("Description: [bright_yellow]Slow-witted Forrest Gump (Tom Hanks) has never thought of himself as disadvantaged, and thanks to his supportive mother (Sally Field), he leads anything but a restricted life. Whether dominating on the gridiron as a college football star, fighting in Vietnam or captaining a shrimp boat, Forrest inspires people with his childlike optimism. But one person Forrest cares about most may be the most difficult to save -- his childhood love, the sweet but troubled Jenny (Robin Wright).[/bright_yellow]")

def weirdScience():
    console.print("\nTitle: [bright_blue]Weird Science[/bright_blue]")
    console.print("Director: [bright_blue]John Hughes[/bright_blue]")
    console.print("Release Date: [bright_blue]August 2, 1985[/bright_blue]")
    console.print("Streaming: [bright_blue]Philo[/bright_blue], [bright_blue]AppleTV[/bright_blue] ([dark_green]$3.99[/dark_green]), [bright_blue]Vudu[/bright_blue] ([dark_green]$3.99[/dark_green]), [bright_blue]Hulu[/bright_blue], [bright_blue]Google Play Movies[/bright_blue] ([dark_green]$3.99[/dark_green]), [bright_blue]Prime Video[/bright_blue], [bright_blue]Youtube[/bright_blue] ([dark_green]$3.99[/dark_green])")
    console.print("Description: [bright_blue]Teen misfits Gary (Anthony Michael Hall) and Wyatt (Ilan Mitchell-Smith) design their ideal woman on a computer, and a freak electrical accident brings her to life in the form of the lovely, superhuman Lisa (Kelly LeBrock). She outfits Gary and Wyatt in cool clothes, surprises them with a Porsche and helps them stand up to jerks Ian (Robert Downey Jr.) and Max (Robert Rusler). But, all the while, the boys must hide Lisa's existence from Chet (Bill Paxton), Wyatt's nightmare of a big brother.[/bright_blue]")

def theBatman():
    console.print("\nTitle: [bright_magenta]The Batman[/bright_magenta]")
    console.print("Director: [bright_magenta]Matt Reeves[/bright_magenta]")
    console.print("Release Date: [bright_magenta]March 4, 2022[/bright_magenta]")
    console.print("Streaming: [bright_magenta]HBO Max[/bright_magenta], [bright_magenta]AppleTV[/bright_magenta] ([dark_green]$3.99[/dark_green]), [bright_magenta]Vudu[/bright_magenta] ([dark_green]$3.99[/dark_green]), [bright_magenta]Hulu[/bright_magenta], [bright_magenta]Google Play Movies[/bright_magenta] ([dark_green]$3.99[/dark_green]), [bright_magenta]Prime Video[/bright_magenta] ([dark_green]$3.99[/dark_green]), [bright_magenta]Youtube[/bright_magenta] ([dark_green]$3.99[/dark_green]), [bright_magenta]Redbox[/bright_magenta] ([dark_green]$3.99[/dark_green]")
    console.print("Description: [bright_magenta]Batman ventures into Gotham City's underworld when a sadistic killer leaves behind a trail of cryptic clues. As the evidence begins to lead closer to home and the scale of the perpetrator's plans become clear, he must forge new relationships, unmask the culprit and bring justice to the abuse of power and corruption that has long plagued the metropolis.[/bright_magenta]")
 
def avatar():
    console.print("\nTitle: [bright_cyan]Avatar[/bright_cyan]")
    console.print("Director: [bright_cyan]James Cameron[/bright_cyan]")
    console.print("Release Date: [bright_cyan]December 18,2009[/bright_cyan]")
    console.print("Streaming: [bright_cyan]AppleTV[/bright_cyan] ([dark_green]$3.99[/dark_green]), [bright_cyan]Vudu[/bright_cyan] ([dark_green]$3.99[/dark_green]), [bright_cyan]Google Play Movies[/bright_cyan] ([dark_green]$3.99[/dark_green]), [bright_cyan]Prime Video[/bright_cyan] ([dark_green]$3.99[/dark_green]), [bright_cyan]Youtube[/bright_cyan] ([dark_green]$3.99[/dark_green]), [bright_cyan]Redbox[/bright_cyan] ([dark_green]$3.99[/dark_green]")
    console.print("Description: [bright_cyan]Batman ventures into Gotham City's underworld when a sadistic killer leaves behind a trail of cryptic clues. As the evidence begins to lead closer to home and the scale of the perpetrator's plans become clear, he must forge new relationships, unmask the culprit and bring justice to the abuse of power and corruption that has long plagued the metropolis.[/bright_cyan]")
   
main()