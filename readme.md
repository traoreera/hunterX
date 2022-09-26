debut project :                       ||         fin project :
information :
                auteur:

                email:

                github:

                whatapp:

                instagram:
______________________________________________________________________________________________
dernier modification en date : 26 Septembre 2002
                                version : beta ==> test:
                                                            2.2.8 last-test
fichier main :
                class : srv-host 

                fonction : server
                           run_server
                           path_dir 
                           configurate
                
                composition fonction :
                                        
                                run_server : Server.running.default_running()

                                contigurate : server.running.configurate()
                arborisation:
                                                            |---> run_server |===> server.running.default_running()

                                                       _____|---> server
                                main => |===> srv_host|
                                                      |_____|---> path_dir

                                                            |---> configurate ===> server.running.configurate()
fichier Server : 
                    class : running

                    fonction : default_running
                               configurate


                    composition:
                                neams

                    arborisation :                          |---> default_running()
                                    Server => | ===>running |---> configurate()
_____________________________________________________________________________________________________________"#traoreera" 
