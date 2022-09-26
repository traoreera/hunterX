import typer
from rich import print
import json
from rich.console import Console
from server.Server import running


console = Console()

app = typer.Typer()

# reduction du lien de sauvegarde des configuration json
js_path =  "server\http\conf\\"


class srv_host:

                    ######################################################################################
                    #                                    Commande server debut                           #
                    ######################################################################################
    @app.command()
    def server(host: str, port: int): 
        """
                        Configuration le plus bad posible sans login root ni password 
                        imposible de sauvegarde ce que l'utilisateur interreagie avec le server
                        chaque lensement de la commande sever en presisen le port et le host lencienne conf 
                        sera totalement ecrase ...


        """

            # configuration basique du server port + host 
        try:
            hosts = host.split(".")

            if len(hosts) == 4 and port:
                print(
                    f"tou ussing host : {host} you ussing port number {port}", end="\n")

            elif len(host) == 9:
                print(f"[bold green] you using {host}[/bold green]")
            with open(f"{js_path}config.json", 'w+') as file:
                srv = {
                    "host": f"{host}",
                    "port": port,
                }
                json.dump(srv, file)

        except Exception as e: 
            print(f"{e}")
            


        return 0
                    ######################################################################################
                    #                                    Commande server fin                             #
                    ######################################################################################




                    ######################################################################################
                    #                                    Commande runserver debut                        #
                    ######################################################################################
    @app.command()
    def run_server():
        """
            lense la config bassic du server 
        """
        from server.Server import running
        running.default_running()

                    ######################################################################################
                    #                                    Commande runserver fin                          #
                    ######################################################################################

                    

    @app.command()
    def paht_dir(path: str):

        dossier = {"dossier": f"{path}"}
        with open(f"{js_path}file.json", 'w+') as file:
            json.dump(dossier, file)
                    ######################################################################################
                    #                                    Commande runserver fin                        #
                    ######################################################################################


    @app.command()
    def configurate_server(): 

        try: running.configurate()
        except Exception as e : print(f"{e}")

                    

                    




if __name__ == "__main__":

    app()
