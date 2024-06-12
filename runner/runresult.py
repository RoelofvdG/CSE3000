SUCCESS = 0
COMPILE_ERROR = "COMPILE ERROR"
TEST_ERROR = "TEST ERROR"

import json


class RunResult:
    def __init__(self, status_code=SUCCESS, raw="", error_locations=None, improved_result=None, combined_result=None,
                 llm_output=None, duration=0):
        if llm_output is None:
            llm_output = {}
        if combined_result is None:
            combined_result = []
        if improved_result is None:
            improved_result = []
        if error_locations is None:
            error_locations = []
        self.status_code = status_code
        self.raw = raw
        self.error_locations = error_locations
        self.improved_result = improved_result
        self.combined_result = combined_result
        self.duration = duration
        self.llm_output = llm_output

    def has_error(self):
        return self.status_code is not SUCCESS

    def __calculate_mutation_score(self, result):
        total = 0
        for mutant in result:
            if mutant["@detected"] == "true":
                total += 1
        return total, len(result)

    def get_improved_mutation_score(self):
        return self.__calculate_mutation_score(self.improved_result)

    def get_combined_mutation_score(self):
        return self.__calculate_mutation_score(self.combined_result)

    def to_dict(self):
        return {
            "status_code": self.status_code,
            "raw": self.raw,
            "error_locations": self.error_locations,
            "improved_result": self.improved_result,
            "combined_result": self.combined_result,
            "duration": self.duration,
            "llm_output": self.llm_output
        }
