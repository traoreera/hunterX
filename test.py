from rich import print 
 
with open("readme.md","r") as file : file = file.read()
htmls = """
            [bold red]bienvenu sur local [bold green]server [/bold green][bold yellow]http fille[/bold yellow][[bold green]![/bold green]][/bold red]
"""

print(htmls)