class Importer():
    @staticmethod
    def message(error: str, biblioteka: str, module: str = "", debug: bool = True):
        if debug:
            try:
                from colorama import Fore
            except ImportError:
                Fore = Importer.install("colorama", ("Fore", ))[0]

            values = {
                    "SUCCESSFUL": ("✓", Fore.GREEN + "[OK]" + Fore.RESET),
                    "ERROR": ("✗", Fore.RED + "[ERROR]" + Fore.RESET)
                }

            name = (biblioteka + " " * (100 // 2 - len(biblioteka) - 3) + " → "+ module) if module else biblioteka

            mark, color_answer = values.get(error.upper())

            return print(mark, name, " " * (100 - len(name)), color_answer)

    @staticmethod
    def install(biblioteka: str, modules: tuple = ()):
        from subprocess import run
        from sys import executable

        if biblioteka == "PyQt6.QtWebEngineWidgets":
            package_name = "PyQt6-WebEngine"
        else:
            package_name = biblioteka
        
        run([executable, "-m", "pip", "install", package_name])

        return Importer.startup(biblioteka, modules)

    @staticmethod
    def startup(biblioteka: str, modules: tuple = ()):
        short = False
        try:
            if biblioteka:
                parts = biblioteka.split('.')
                main_lib = parts[0]

                if len(parts) > 1:
                    bib = __import__(biblioteka, fromlist=[parts[-1]])
                else:
                    bib = __import__(main_lib)

                if len(parts) > 1:
                    current = bib
                    if main_lib == "PyQt6":
                        try:
                            for part in parts[1:]:
                                current = getattr(current, part)
                        except AttributeError:
                            current = __import__(biblioteka, fromlist=parts[1:])
                    else:
                        for part in parts[1:]:
                            current = getattr(current, part)
                else:
                    current = bib
                    globals()[main_lib] = bib
                
                Importer.message("successful", biblioteka)
                
                if not isinstance(modules, tuple):
                    short = True
                    modules = (modules, )

                imported = []
                for module in modules:
                    try:
                        if hasattr(current, module):
                            value = getattr(current, module)
                            globals()[module] = value
                            Importer.message("successful", biblioteka, module)
                            imported.append(value)
                        else:
                            Importer.message("error", biblioteka, module)
                    except Exception as e:
                        Importer.message("error", biblioteka, module)
                
                if modules:
                    return imported[0] if short else imported
                else:
                    return current
                
        except ImportError:
            Importer.message("error", biblioteka)
            return Importer.install(biblioteka, modules)
