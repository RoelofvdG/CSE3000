import corpus
from jclass import JClass
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import json
import vda


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


def load_stats_from_files(files):
    stats_dict = {}
    for fn in files:
        with open(fn, "r") as f:
            key = fn.split(".")[0].split("-")[1]
            stats_dict[key] = json.loads(f.read())
    return stats_dict


def convert_run_to_stats(in_file, outfile="savedata/stats.json"):
    with open(in_file, "r") as f:
        data = json.load(f)

    classes = JClass.get_classes()
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
        stats_dict[jclass.class_name] = {
            "class_name": jclass.class_name
        }

        base_mutation_score = combined_mutation_score_from_dict(baseline)
        stats_dict[jclass.class_name]["base_score"] = base_mutation_score
        stats_dict[jclass.class_name]["mutants"] = base_mutation_score[1]
        base_perc = 0 if base_mutation_score[1] == 0 else round(base_mutation_score[0] / base_mutation_score[1] * 100)
        stats_dict[jclass.class_name]["base_perc"] = base_perc
        # print("Base mutations score for", jclass.class_name, str(base_mutation_score))
        base_array = [base_mutation_score[0]] * 6

        improved_array = []
        combined_array = []
        stats_dict[jclass.class_name]["runs"] = []
        for (rdx, run) in enumerate(results):
            improved_score = improved_mutation_score_from_dict(run)
            combined_score = combined_mutation_score_from_dict(run)
            combined_perc = 0 if combined_score[1] == 0 else round(combined_score[0] / combined_score[1] * 100)
            improved_perc = 0 if improved_score[1] == 0 else round(improved_score[0] / improved_score[1] * 100)
            # print("Mutation score of run", rdx, combined_score, improved_score)
            improved_array.append(improved_score[0])
            combined_array.append(combined_score[0])
            stats_dict[jclass.class_name]["runs"].append({
                "improved_score": improved_score,
                "improved_perc": improved_perc,
                "combined_score": combined_score,
                "combined_perc": combined_perc,
                "duration": run["duration"]
            })
        t_test = stats.ttest_ind(base_array, combined_array, equal_var=False)
        base_percs = [base_perc] * len(base_array)
        combined_percs = list(map(lambda x: x["combined_perc"], stats_dict[jclass.class_name]["runs"]))
        # print(base_percs, combined_percs)
        a12 = vda.VD_A(combined_percs, base_percs)
        # print(("" + a12[1].upper()[0] + "(" + '{:.2f}'.format(round(a12[0], 2)) + ")").replace("N", "\\textbf{--}"))
        stats_dict[jclass.class_name]["t_test"] = {
            "statistic": t_test.statistic,
            "p_value": t_test.pvalue
        }
        stats_dict[jclass.class_name]["a12"] = a12
        # print("Welch T-test", t_test.statistic, t_test.pvalue)
        # print(combined_array)
    with open(outfile, "w") as f:
        f.write(json.dumps(stats_dict, indent=3))


def make_table_from_stats(stats_file):
    with open(stats_file, "r") as f:
        stats = json.loads(f.read())
    print(stats)


def title_map(name):
    if name == "codestral":
        return "Codestral 22B"
    elif name == "llama":
        return "Code Llama 13B"
    elif name == "deepseek":
        return "Deepseek Coder 6.7B"
    elif name == "gemma":
        return "CodeGemma 7B"
    else:
        return "UNKNOWN MODEL"


def make_bar_charts(files):
    # https://www.geeksforgeeks.org/create-a-grouped-bar-plot-in-matplotlib/
    stats_dict = load_stats_from_files(files)

    for model in stats_dict:
        model_data = stats_dict[model]
        x_labels = list(model_data)
        bars = [[]] * 7

        for c in x_labels:
            c_data = model_data[c]
            bars[0] = bars[0] + [c_data["base_perc"]]
            for run_idx in range(len(c_data["runs"])):
                run = c_data["runs"][run_idx]
                bars[run_idx + 1] = bars[run_idx + 1] + [run["combined_perc"]]
        total_width = 10
        x = np.arange(len(bars[0])) * total_width
        colours = ["#0288D1", "#FFCC80", "#FFB74D", "#FFA726", "#FF9800", "#FB8C00", "#F57C00"]
        labels = ["Baseline", "Run 1", "Run 2", "Run 3", "Run 4", "Run 5", "Run 6"]
        for (bar_idx, bar) in enumerate(bars):
            x_offset = x - (total_width / 2) + (bar_idx * total_width / len(bars))
            plt.bar(x_offset, bar, total_width / len(bars[0]), color=colours[bar_idx], label=labels[bar_idx])
        plt.xticks(x, x_labels, rotation=45, ha="right")
        plt.xlabel("Class")
        plt.ylabel("Mutation score (%)")
        plt.title("Combined mutation scores for " + title_map(model))
        plt.tight_layout()
        # plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc='lower left', ncol=7, mode="expand")
        # plt.subplots_adjust(top=0.7)
        plt.savefig("plots/bars-" + model + ".svg", format="svg", transparent=True, dpi=1200)
        plt.savefig("plots/bars-" + model + ".png", format="png", dpi=1200)
        plt.show(transparent=True, dpi=1200)


def make_box_plots(files):
    # https://datasciencepartners.nl/python-boxplot/
    stats_dict = load_stats_from_files(files)
    for model in stats_dict:
        model_data = stats_dict[model]
        x_labels = list(model_data)
        bars = []
        for cn in x_labels:
            runs = list(map(lambda x: x["combined_perc"], model_data[cn]["runs"]))
            bars.append(runs)
        for (cn_idx, cn) in enumerate(x_labels):
            base_score = model_data[cn]["base_perc"]
            plt.plot(cn_idx + 1, base_score, cn_idx + 1, base_score, marker="o", color="#0288D1",
                     linestyle="solid", linewidth=4)
        plt.boxplot(bars)
        plt.xlabel("Class")
        plt.ylabel("Mutation score (%)")
        plt.xticks(np.arange(len(bars)) + 1, x_labels, rotation=45, ha="right")
        plt.title("Combined mutation scores for " + title_map(model))
        plt.tight_layout()
        plt.savefig("plots/box-" + model + ".svg", format="svg", transparent=True, dpi=1200)
        plt.savefig("plots/box-" + model + ".png", format="png", dpi=1200)
        plt.show(transparent=True, dpi=1200)


def make_time_box_plots(files):
    stats_dict = load_stats_from_files(files)
    for model in stats_dict:
        model_data = stats_dict[model]
        x_labels = list(model_data)
        bars = []
        for cn in x_labels:
            runs = list(map(lambda x: x["duration"], model_data[cn]["runs"]))
            bars.append(runs)
        plt.boxplot(bars)
        plt.xlabel("Class")
        plt.ylabel("Duration (s)")
        plt.xticks(np.arange(len(bars)) + 1, x_labels, rotation=45, ha="right")
        plt.title("Test generation and removal runtime for " + title_map(model))
        plt.tight_layout()
        plt.savefig("plots/time-" + model + ".svg", format="svg", transparent=True, dpi=1200)
        plt.savefig("plots/time-" + model + ".png", format="png", dpi=1200)
        plt.show(transparent=True, dpi=1200)
