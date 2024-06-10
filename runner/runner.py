import runresult
from llmapi import LLMAPI
from runresult import RunResult
import subprocess
import re
import xmltodict
import corpus
import os


class Runner:
    def __init__(self, jclass):
        self.jclass = jclass

    def do_run(self, amount=1):
        self.jclass.enable()
        for i in range(amount):
            self.jclass.delete_improved_tests_file()
            self.jclass.disable_base_tests()
            llm = LLMAPI()
            print("Generating tests for class", self.jclass.class_name)
            tests = llm.generate_tests(self.jclass)
            # print(tests["raw"])
            star_imports = ["import org.junit.*;\n", "import org.junit.Assert.*;\n"]
            self.jclass.create_improved_tests_file(imports=tests["imports"] + star_imports, tests=tests["tests"])
            print("Running tests for class", self.jclass.class_name)
            result = self.run_tests()
            if result.has_error():
                print(tests["raw"])
                print(result.raw)
                for location in result.error_locations:
                    self.jclass.disable_improved_test(location)
                for i in range(len(tests["tests"])):
                    result = self.run_tests()
                    if result.has_error():
                        for location in result.error_locations:
                            self.jclass.disable_improved_test(location)
                    else:
                        break



    def run_tests(self):
        try:
            run = subprocess.check_output("cd ../corpus && gradle pitest", shell=True, text=True,
                                          stderr=subprocess.STDOUT)
            with open(os.path.join(corpus.REPORT_PATH, "mutations.xml"), "r") as file:
                xml = file.read()
            dict = xmltodict.parse(xml)
            print(dict["mutations"]["mutation"])
            mutant_class = ("nl.roelofvdg." + self.jclass.package_name + "." + self.jclass.class_name).replace("..", ".")
            print(mutant_class)
            mutants = []
            for mutant in dict["mutations"]["mutation"]:
                if mutant["mutatedClass"] == mutant_class:
                    mutants.append(mutant)
            for m in mutants:
                print(m)
            return RunResult(raw=run)
        except subprocess.CalledProcessError as err:
            if "Mutation testing requires a green suite." in err.output:  # Failing tests
                failing_tests = list(set(re.findall("name=(.*)\(", err.output)))
                return RunResult(status_code=runresult.TEST_ERROR, raw=err.output, error_locations=failing_tests)
            elif "Compilation failed;" in err.output:  # Compilation error
                lines = list(map(int, list(set(re.findall('.java:([0-9]*):', err.output, )))))
                return RunResult(status_code=runresult.COMPILE_ERROR, raw=err.output, error_locations=lines)

