from os import getenv

class GolemLanguageWriter:
    def __init__(self, file_name):
        self.path = getenv("GOLENS_SCRIPTS_PATH")
        self.rows = []
        self.file_name_with_extension = file_name + getenv("GOLENS_SCRIPTS_EXTENSIONS")
        self.file_name = file_name
        
    def create_golem_script(self):
        try:
            with open(self.path + self.file_name_with_extension , "x") as file:
                return True
        except IOError:
            return False

    def golem_script_fill(self):
        with open(self.path + self.file_name_with_extension, "a") as file:
            for row in self.rows:
                file.write(row)
                
    def add_command_row_click(self, x, y, time):
        self.rows.append(f"command:click/x:{x}/y:{y}/time:{time}\n")
        