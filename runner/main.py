import corpus
from jclass import JClass
from runner import Runner
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import json
import stats
import vda


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

    # file_name = "savedata/data-codestral.json"
    #
    # # Runner.run_entire_corpus(6, output_file=file_name)
    #
    # with open(file_name, "r") as f:
    #     data = json.load(f)
    #
    # classes = JClass.get_classes()
    # print(classes)
    #
    # table = "\\begin{tabular}{l|l|l|l|l|l}\n"
    # table += tab(1) + "Classname & Mutants & Baseline & Run & Combined score & Generated only \\\\\n"
    # stats_dict = {}
    # for (idx, jclass) in enumerate(classes):
    #
    #     if not jclass.has_tests():
    #         continue
    #
    #     baseline, results = None, None
    #     mutated_class = (corpus.PACKAGE_PREFIX + jclass.package_name + "." + jclass.class_name).replace("..", ".")
    #     print("Finding results for", jclass.class_name)
    #     for (bix, b) in enumerate(data["baseline"]):
    #         if b["combined_result"][0]["mutatedClass"] == mutated_class:
    #             baseline = b
    #             results = data["results"][bix]
    #
    #     if baseline is None or results is None:
    #         print("No results found for", jclass.class_name)
    #         continue
    #     table += tab(1) + "\\hline\n" + tab(1) + "\\hline\n"
    #     stats_dict[jclass.class_name] = {
    #         "class_name": jclass.class_name
    #     }
    #     # baseline = data["baseline"][idx]
    #     # results = data["results"][i]
    #
    #     base_mutation_score = combined_mutation_score_from_dict(baseline)
    #     stats_dict[jclass.class_name]["base_score"] = base_mutation_score
    #     stats_dict[jclass.class_name]["mutants"] = base_mutation_score[1]
    #     base_perc = 0 if base_mutation_score[1] == 0 else round(base_mutation_score[0] / base_mutation_score[1] * 100)
    #     stats_dict[jclass.class_name]["base_perc"] = base_perc
    #     # print("Base mutations score for", jclass.class_name, str(base_mutation_score))
    #     base_array = [base_mutation_score[0]]*6
    #     # print(base_array)
    #
    #     improved_array = []
    #     combined_array = []
    #     stats_dict[jclass.class_name]["runs"] = []
    #     for (rdx, run) in enumerate(results):
    #         improved_score = improved_mutation_score_from_dict(run)
    #         combined_score = combined_mutation_score_from_dict(run)
    #         combined_perc = 0 if combined_score[1] == 0 else round(combined_score[0]/combined_score[1] * 100)
    #         improved_perc = 0 if improved_score[1] == 0 else round(improved_score[0] / improved_score[1] * 100)
    #         # print("Mutation score of run", rdx, combined_score, improved_score)
    #         improved_array.append(improved_score[0])
    #         combined_array.append(combined_score[0])
    #         if rdx == 0:
    #             table += tab(1) + "\\multirow{6}{*}{"+ jclass.class_name + "} & \\multirow{6}{*}{" + str(base_mutation_score[1]) + "} & \\multirow{6}{*}{" + str(base_perc) + "\\%} & 1 &  " + str(combined_perc) + "\\% & " + str(improved_perc) + "\\%\\\\\\cline{4-6}\n"
    #         else:
    #             table += tab(1) + "& & & " + str(rdx + 1) + " & " + str(combined_perc) + "\\% & " + str(improved_perc) + "\\%\\\\\\cline{4-6}\n"
    #         stats_dict[jclass.class_name]["runs"].append({
    #             "improved_score": improved_score,
    #             "improved_perc": improved_perc,
    #             "combined_score": combined_score,
    #             "combined_perc": combined_perc,
    #         })
    #     t_test = stats.ttest_ind(base_array, combined_array, equal_var = False)
    #     stats_dict[jclass.class_name]["t_test"] = {
    #         "statistic": t_test.statistic,
    #         "p_value": t_test.pvalue
    #     }
    #     # print("Welch T-test", t_test.statistic, t_test.pvalue)
    #     # print(combined_array)
    # table += "\\end{tabular}"
    # print(table)
    # with open("savedata/stats.json", "w") as f:
    #     f.write(json.dumps(stats_dict, indent=3))

    files = ["savedata/stats-deepseek.json", "savedata/stats-llama.json", "savedata/stats-codestral.json"]
    titles = []
    stats.make_box_plots(files)
    stats.make_bar_charts(files)
    stats.make_time_box_plots(files)
    for jclass in JClass.get_classes():
        print(jclass.package_name, jclass.class_name)

    package_map = {
        "Util": "org.apache.commons.cli",
        "ArrayFill": "org.apache.commons.lang3",
        "Distance": "org.jcvi.jillion.assembly.ca.frg",
        "IlluminaUtil": "org.jcvi.jillion.trace.fastq",
        "Vector": "jigl.math",
        "AbstractNFeAdaptadorBean": "br.com.jnfe.base.adapter",
        "StringUtils": "org.jsecurity.util",
        "UnsyncBufferedInputStream": "com.liferay.portal.kernel.io.unsync",
        "PrefixParser": "it.pdfsam.console.tools",
        "DateTime": "dk.statsbiblioteket.summa.plugins",
        "StringMap": "dk.statsbiblioteket.summa.common.util",
        "OpMatcher": "org.templateit"
    }

    # stats.convert_run_to_stats("savedata/data-deepseek.json", "savedata/stats-deepseek.json")


    print("=====")
