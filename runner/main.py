import json

from jclass import JClass
from runner import Runner
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

    file_name = "data.json"

    # Runner.run_entire_corpus(6, output_file=file_name)

    with open(file_name, "r") as f:
        data = json.load(f)

    classes = JClass.get_classes()
    print(classes)

    i = 0
    for (idx, jclass) in enumerate(classes):
        if not jclass.has_tests():
            continue
        baseline = data["baseline"][idx]
        results = data["results"][i]
        # print(baseline)

        base_mutation_score = combined_mutation_score_from_dict(baseline)
        print("Base mutations score for", jclass.class_name, str(base_mutation_score))

        for (rdx, run) in enumerate(results):
            print("Mutation score of run", rdx, combined_mutation_score_from_dict(run),
                  improved_mutation_score_from_dict(run))

        i += 1

    # print(baseline["combined_result"])
    # for r in results:
    #     print(r)
    # print(results[5]["combined_result"])
    # print(len(data["results"]))
    #
    # for d in data["baseline"]:
    #     print(d["combined_result"])

    print("=====")
