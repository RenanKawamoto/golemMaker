from os import getenv

class GolemLanguageTranslator:
    def __init__(self, file_name):
        self.path = getenv("GOLENS_SCRIPTS_PATH")   
        self.file_name = file_name
        self.file_name_with_extension = file_name + getenv("GOLENS_SCRIPTS_EXTENSIONS")
        
    def _split_in_bar(array):
        return array.split("/")
        
    def golem_script_to_dict(self):
        with open(self.path + self.file_name_with_extension, "r") as file:       
            raw_lines = file.readlines()
            split_lines = list(map(_split_in_bar, raw_lines))
            result = []
            for row in split_lines:
                current_row = {}
                for column in row:
                    key, value = column.split(":")
                    current_row[key] = value
                result.append(current_row)
            file.close()
        return result
    
    def dict_to_script(self, dict):        
        script_file = open(self.path + self.file_name + ".py", "a")
        script_file.write("import pyautogui\n")
        for row in dict:
            if row["command"] == "click":
                script_file.write("pyautogui.click(100, 100)\n")
        script_file.close()