import json

import corpus
from jclass import JClass
from runner import Runner
import scipy.stats as stats
import json


def combined_mutation_score_from_dict(run_dict):
    return mutation_score_from_result(run_dict["combined_result"])


def improved_mutation_score_from_dict(run_dict):
    return mutation_score_from_result(run_dict["improved_result"])


def mutation_score_from_result(run_dict):
    killed = 0
    for m in run_dict:
        if m["@detected"] == "true":
            killed += 1
    return killed, len(run_dict)

def tab(number):
    return " " * number * 4


if __name__ == '__main__':
    print("Mutation test")

    # classes = JClass.get_classes()
    # print(classes)
    # jclass = classes[0]
    # print(jclass)
    # runner = Runner(jclass)
    # # result = runner.do_run(1)
    # res = runner.run_tests()
    # print(res.error_locations)
    # for l in res.error_locations:
    #     jclass.disable_improved_test(l)

    file_name = "data-deepseek.json"

    # Runner.run_entire_corpus(6, output_file=file_name)

    with open(file_name, "r") as f:
        data = json.load(f)

    classes = JClass.get_classes()
    print(classes)

    table = "\\begin{tabular}{l|l|l|l|l|l}\n"
    table += tab(1) + "Classname & Mutants & Baseline & Run & Combined score & Generated only \\\\\n"
    stats_dict = {}
    for (idx, jclass) in enumerate(classes):

        if not jclass.has_tests():
            continue

        baseline, results = None, None
        mutated_class = (corpus.PACKAGE_PREFIX + jclass.package_name + "." + jclass.class_name).replace("..", ".")
        print("Finding results for", jclass.class_name)
        for (bix, b) in enumerate(data["baseline"]):
            if b["combined_result"][0]["mutatedClass"] == mutated_class:
                baseline = b
                results = data["results"][bix]

        if baseline is None or results is None:
            print("No results found for", jclass.class_name)
            continue
        table += tab(1) + "\\hline\n" + tab(1) + "\\hline\n"
        stats_dict[jclass.class_name] = {
            "class_name": jclass.class_name
        }
        # baseline = data["baseline"][idx]
        # results = data["results"][i]

        base_mutation_score = combined_mutation_score_from_dict(baseline)
        base_perc = 0 if base_mutation_score[1] == 0 else round(base_mutation_score[0] / base_mutation_score[1] * 100)
        # print("Base mutations score for", jclass.class_name, str(base_mutation_score))
        base_array = [base_mutation_score[0]]*6
        # print(base_array)

        improved_array = []
        combined_array = []
        for (rdx, run) in enumerate(results):
            improved_score = improved_mutation_score_from_dict(run)
            combined_score = combined_mutation_score_from_dict(run)
            combined_perc = 0 if combined_score[1] == 0 else round(combined_score[0]/combined_score[1] * 100)
            improved_perc = 0 if improved_score[1] == 0 else round(improved_score[0] / improved_score[1] * 100)
            # print("Mutation score of run", rdx, combined_score, improved_score)
            improved_array.append(improved_score[0])
            combined_array.append(combined_score[0])
            if rdx == 0:
                table += tab(1) + "\\multirow{6}{*}{"+ jclass.class_name + "} & \\multirow{6}{*}{" + str(base_mutation_score[1]) + "} & \\multirow{6}{*}{" + str(base_perc) + "\\%} & 1 &  " + str(combined_perc) + "\\% & " + str(improved_perc) + "\\%\\\\\\cline{4-6}\n"
            else:
                table += tab(1) + "& & & " + str(rdx + 1) + " & " + str(combined_perc) + "\\% & " + str(improved_perc) + "\\%\\\\\\cline{4-6}\n"
        t_test = stats.ttest_ind(base_array, combined_array, equal_var = False)
        print("Welch T-test", t_test.statistic, t_test.pvalue)
        # print(combined_array)
    table += "\\end{tabular}"
    # print(table)
    # print(baseline["combined_result"])
    # for r in results:
    #     print(r)
    # print(results[5]["combined_result"])
    # print(len(data["results"]))
    #
    # for d in data["baseline"]:
    #     print(d["combined_result"])

    print("=====")
