from os import getenv

class GolemLanguageWriter:
    def __init__(self):
        self.path = getenv("GOLENS_SCRIPTS_PATH")
        self.rows = []
        
    def create_golem_script(self, file_name):
        file = open(self.path + file_name + getenv("GOLENS_SCRIPTS_EXTENSIONS"), "x")
                       
    def golem_script_fill(self, file_name):
        file = open(self.path + file_name + getenv("GOLENS_SCRIPTS_EXTENSIONS"), "a")
        for row in self.rows:
            file.write(row)
                
    def add_command_row_click(self, x, y, time):
        self.rows.append(f"command:click/x:{x}/y:{y}/time:{time}\n")
        