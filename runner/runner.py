import runresult
from llmapi import LLMAPI
from runresult import RunResult
from jclass import JClass
import subprocess
import re
import xmltodict
import corpus
import os
import time
import json


class Runner:
    def __init__(self, jclass):
        self.jclass = jclass

    def do_run(self, amount=1):
        self.jclass.enable()
        results = []
        for i in range(amount):
            run_prefix = "R" + str(i + 1) + "/" + str(amount)
            self.jclass.delete_improved_tests_file()
            self.jclass.disable_base_tests()
            llm = LLMAPI()
            print(run_prefix, "Generating tests for class", self.jclass.class_name)
            start_t = time.perf_counter()
            tests = llm.generate_tests(self.jclass)
            # print(tests["raw"])
            star_imports = ["import org.junit.*;\n", "import org.junit.Assert.*;\n"]
            self.jclass.create_improved_tests_file(imports=tests["imports"] + star_imports, tests=tests["tests"])
            print(run_prefix, "Running tests for class", self.jclass.class_name)
            result = self.run_tests()

            if result.has_error():
                try:
                    print(run_prefix, "Error in tests for " + self.jclass.class_name + ":", result.status_code, "at",
                          result.error_locations)
                    # print(tests["raw"])
                    # print(result.raw)
                    for location in result.error_locations:
                        self.jclass.disable_improved_test(location)
                    for i in range(len(tests["tests"])):
                        print(run_prefix, "Retrying after disabling tests (" + str(i + 1) + "/", str(len(tests["tests"])) + ")")
                        result = self.run_tests()
                        if result.has_error():
                            for location in result.error_locations:
                                self.jclass.disable_improved_test(location)
                        else:
                            break
                except IndexError as err:
                    print("Error occurred during removal of method:")
                    print(err)
                    continue
            if not result.has_error():
                self.jclass.enable_base_tests()

            end_t = time.perf_counter()
            result.duration = end_t - start_t
            result.llm_output = tests
            results.append(result)
            print(result.get_improved_mutation_score(), result.get_combined_mutation_score())
            print(run_prefix, "Finished running tests for", self.jclass.class_name)
        return results

    def run_tests(self):
        mutant_class = (corpus.PACKAGE_PREFIX + self.jclass.package_name + "." + self.jclass.class_name).replace("..", ".")
        try:
            self.jclass.disable_base_tests()
            run = subprocess.check_output("cd ../corpus && gradle pitest", shell=True, text=True,
                                          stderr=subprocess.STDOUT)
            with open(os.path.join(corpus.REPORT_PATH, "mutations.xml"), "r") as file:
                xml = file.read()
            xml_dict = xmltodict.parse(xml)
            improved_mutants = []
            for mutant in xml_dict["mutations"]["mutation"]:
                if mutant["mutatedClass"] == mutant_class:
                    improved_mutants.append(mutant)

            self.jclass.enable_base_tests()
            run = subprocess.check_output("cd ../corpus && gradle pitest", shell=True, text=True,
                                          stderr=subprocess.STDOUT)
            with open(os.path.join(corpus.REPORT_PATH, "mutations.xml"), "r") as file:
                xml = file.read()
            xml_dict = xmltodict.parse(xml)
            combined_mutants = []
            for mutant in xml_dict["mutations"]["mutation"]:
                if mutant["mutatedClass"] == mutant_class:
                    combined_mutants.append(mutant)
            return RunResult(raw=run, status_code=runresult.SUCCESS, combined_result=combined_mutants,
                             improved_result=improved_mutants)
        except subprocess.CalledProcessError as err:
            if "Mutation testing requires a green suite." in err.output:  # Failing tests
                failing_tests = list(set(re.findall("name=(.*)\(", err.output)))
                return RunResult(status_code=runresult.TEST_ERROR, raw=err.output, error_locations=failing_tests)
            elif "Compilation failed;" in err.output:  # Compilation error
                lines = list(map(int, list(set(re.findall('.java:([0-9]*):', err.output, )))))
                return RunResult(status_code=runresult.COMPILE_ERROR, raw=err.output, error_locations=lines)

    @staticmethod
    def run_entire_corpus(runs_amount=1, output_file=None):
        cs = JClass.get_classes()
        print(cs)
        for c in cs:
            c.enable()
            c.delete_improved_tests_file()

        baseline = []
        base_run = Runner(cs[0]).run_tests()
        if base_run.has_error():
            raise Exception("Baseline tests contained an error")

        for c in cs:
            for c2 in cs:
                if c.class_name != c2.class_name:
                    c2.disable()
            c.enable()
            r = Runner(c)
            print("Computing baseline for " + c.class_name)
            run = r.run_tests()
            baseline.append(run)
            print("Baseline for " + c.class_name + ":", run.get_combined_mutation_score())

        # for c in cs:
        #     c.disable()

        results = []
        for c in cs:
            if c.has_tests():
                for c2 in cs:
                    if c2.package_name == c.package_name:
                        c2.enable()
                    else:
                        c2.disable()
                r = Runner(c)
                result = r.do_run(runs_amount)
                results.append(result)
                c.delete_improved_tests_file()

        if output_file is not None:
            results_dict = {
                "baseline": [],
                "results": []
            }

            for i in results:
                a = []
                for j in i:
                    a.append(j.to_dict())
                results_dict["results"].append(a)

            results_dict = {
                "baseline": list(map(lambda m: m.to_dict(), baseline)),
                "results": list(map(lambda x: list(map(lambda m: m.to_dict(), x)), results))
            }

            # print(results_dict)

            with open(output_file, "w") as f:
                # dict_list = list(map(lambda m: m.to_dict(), results))
                json.dump(results_dict, f)

        for c in cs:
            c.enable()
