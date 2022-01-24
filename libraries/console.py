import colorama
from colorama import Fore, Style

class Console:
    console_prefix = None
    
    def __init__(self, prefix = "Sparky> "):
        colorama.init(autoreset = True)
        self.console_prefix = prefix
    
    def Message(self, text):
        print(f"{self.console_prefix}{text}")
    
    def Success(self, text):
        print(f"{self.console_prefix}{Fore.GREEN}{Style.BRIGHT}{text}")
    
    def Information(self, text):
        print(f"{self.console_prefix}{Fore.CYAN}{text}")
        
    def Warning(self, text):
        print(f"{self.console_prefix}{Fore.YELLOW}{text}")
        
    def Error(self, text):
        print(f"{self.console_prefix}{Fore.RED}{text}")
        
if __name__ == "__main__":
    C = Console("")
    
    C.Message("Message example")
    C.Success("Success example")
    C.Information("Information example")
    C.Warning("Warning example")
    C.Error("Error example")
        