import colorama
from colorama import Fore, Back, Style
from time import gmtime, strftime

class Console:
    console_prefix = None
    
    def __init__(self, prefix = "Sparky> "):
        colorama.init(autoreset = True)
        self.console_prefix = prefix
    
    def title(self):
        print()
        print("                                  ```......---.....``")                               
        print("                         `.-/+syhddmmmNNNNMMMNNNmmddhys+/-.`")                       
        print("                     `-+ydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdyo-`")                       
        print("                    /dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd/")                       
        print("                   sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs")                       
        print("                  +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+")                       
        print("                 `NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN`")                       
        print("                 +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMM+")                       
        print("                 dMMMMNho:-...:/oymMMMMMMMMMMMMMMMmy+:.```.:ohMMMMMh")                       
        print('                `MMMNsoshho/:--.  `-sNMMMMMMMMMms-`  .-::/ohhsoyMMMN`                .dP"Y8 88""Yb  db    88""Yb 88  dP Yb  dP')                       
        print('                :MMNhmMMMMdhy+:-//.  .yMMMMMMMs.  .:/.:+shmMMMMmhMMM.                `Ybo." 88__dP dPYb   88__dP 88odP   YbdP')                       
        print('                oMMMMMMMMMMMMMNy:.//. :MMMMMMM.`-/:.:hNMMMMMMMMMMMMM:                o.`Y8b 88""" dP__Yb  88"Yb  88"Yb    8P')                       
        print('                yMMMMMMMMMMMMMMMNh:.:smMMMMMMMmy:./dMMMMMMMMMMMMMMMM/                8bodP` 88   dP""""Yb 88  Yb 88  Yb  dP')                       
        print("                dMMMMMMMNNmmmmNMMMMs``yMMMMMMMh-+dMMMNNmmmmNMMMMMMMM+")                       
        print("                dMMMMNh+-..``.-:odNMs `dMMMMMMydMMNd+-.````.:+dMMMMMo")                       
        print("                mMMmh:            -om  :MMMMMMMMM+.            +dmNMo")                       
        print("                dMM+ ``````....--:/ym  .MMMMMMMMNs/:/++++/////+sysyho")                       
        print("                mMMyydmNNMMMMMMMMMMMm  `NMMMMMMMMMMMMMMMMMMMMMMMMMMMy")                       
        print("                hMMMMMMMMMMMMMMMMMMMy  :MMMMMMMMMMMMMMMMMMMMMMMMMMMMy")                       
        print("                .NMMMMMMMMMMMMMMMMMM/  :MMMMMMMMMMMMMMMMMMMMMMMMMMMMo")                       
        print("                 `hMMMMMMMMMMMMMMMMM`  -MMMMMMMMMMMMMMMMMMMMMMMMMMMN.")                       
        print("                `s:hMMMMMMMMMMMMMMN+   -MMMMMMMMMMMMMMMMMMMMMMMMMNy.")                       
        print(f"                 hd.:sdmmmmmdhhmd/.``  +MMMMMMMhshMMMMMMMMMMMMNdsos                  {Fore.BLACK}{Back.WHITE}NAME")                       
        print("                 .Ny /:`/hyhdmmN: `yo  hMMMMMMMMNhsMMNyosyy+--+`.N/                  Sparky")                       
        print("                  /No.d:`oNMMMMMh.sMo `NMMMMMMMMMMdMMMMMMMh``yh`hm`")                       
        print(f"                   oMs/d- :yNMMMMNNMy.-MMMMMMNMMMMMMMMMMNo``hN:sN:                   {Fore.BLACK}{Back.WHITE}VERSION")                       
        print('                    sMh/y:  ./sdmNMNd:`odmmdy:oNMMMMMNdo- .hm:sMo                    1.5.1')                       
        print("                     sMm/+s/`   .-:-`   `/:`   -oys+:-` `/ds.sMs")                       
        print(f"                      sMN+.ody+-``     .hMNy.       ``-odm:`hMs                      {Fore.BLACK}{Back.WHITE}DESCRIPTION")                       
        print("                       oMMs .oNMNdyso+oyyyyhs---:/oshNMMNy:mMo                       Sparky is a discord bot. It is made for help your server keep tidy. It is")                       
        print("                        +NMy` .omMMMMMMMMMNNNMMMMMMMMMMMy/NN/                        censure messages and notify the person whos send that message about what")                       
        print("                         :NMh` +mmmdhdmNNMMNNMMMMMMMMMMsyMm-                         he has done. It can ban and unban as well as kick people. It also helps")                       
        print("                          .mMh.sMMMMMMm- .   yNMMMMMMNodMh`                          setup your server as fast as you want. It has a custom help command that")                       
        print("                           `hMy/MMMMMMMm    sMMMMMMMNsNMs`                           will show every command for you. It also can play music from YouTube, just")                       
        print("                            `sNsmMMMMMMo    sMMMMMMMNMN+                             give a link to it and Sparky does everything instead of you.")                       
        print("                              -hMMMMMMh   - `mMMMMMMMm-")                       
        print(f"                               `sMMMMMh   /  dMMMMMMy.                               {Fore.BLACK}{Back.WHITE}AUTHOR")                       
        print("                                 +NMMMN`    -MMMMMm+`                                Andor Zoltán Fülöp")                       
        print("                                  -hMMMo    yMMMms.")                       
        print("                                   `:sdh    ddy/.")                       
        print("                                       `    `") 
        print()
        print("===============================================================================================================================================================================")     
        print()                
        pass
    
    def Message(self, text):
        print(f"[{strftime('%H:%M:%S', gmtime())}] {self.console_prefix}{text}")
    
    def Success(self, text):
        print(f"[{strftime('%H:%M:%S', gmtime())}] {self.console_prefix}{Fore.GREEN}{Style.BRIGHT}{text}")
    
    def Information(self, text):
        print(f"[{strftime('%H:%M:%S', gmtime())}] {self.console_prefix}{Fore.CYAN}{text}")
        
    def Warning(self, text):
        print(f"[{strftime('%H:%M:%S', gmtime())}] {self.console_prefix}{Fore.YELLOW}{text}")
        
    def Error(self, text):
        print(f"[{strftime('%H:%M:%S', gmtime())}] {self.console_prefix}{Fore.RED}{text}")
        
if __name__ == "__main__":
    C = Console("")
    
    C.title()
    C.Message("Message example")
    C.Success("Success example")
    C.Information("Information example")
    C.Warning("Warning example")
    C.Error("Error example")
        