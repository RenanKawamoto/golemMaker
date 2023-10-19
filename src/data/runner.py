from os import getenv

class Runner:    
    @staticmethod
    def run_code_in_file(file_name):
        exec(open(getenv("GOLENS_SCRIPTS_PATH") + file_name + ".py").read())