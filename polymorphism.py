############# ducktyping #########
class Vscode:

    def execute(self):
        print("shell prompt")

class Editor:
    def execute(self):
        print("spell check, intelisense,ide")

class Run:
    def programing(self,ide):
        ide.execute()

ide = Vscode()

exe = Run()

exe.programing(ide)