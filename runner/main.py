from jclass import JClass
from llmapi import LLMAPI
import os

if __name__ == '__main__':
    print("Mutation test")

    c = JClass.get_classes()[0]
    c.create_improved_tests_file()
    api = LLMAPI()
    tests = api.generate_tests(c)
    c.create_improved_tests_file(imports=tests["imports"], tests=tests["tests"])
    os.system("cd ../corpus && gradle pitest --rerun-tasks")
    # print(tests)
    # for l in tests["tests"]:
    #     print(l)
