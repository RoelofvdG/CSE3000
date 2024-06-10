from jclass import JClass
from llmapi import LLMAPI
from runner import Runner
import time
import subprocess
import os
import re

if __name__ == '__main__':
    print("Mutation test")

    cs = JClass.get_classes()
    api = LLMAPI()
    print(cs)
    for c in cs:
    #     # c.disable()
    #     # print(c, c.is_disabled())
        c.enable()
    #     # print(c.is_disabled())
    start_t = time.perf_counter()
    c = cs[0]
    runner = Runner(c)
    runner.do_run(1)
    end_t = time.perf_counter()

    print("=====")
    print(str(end_t - start_t), "s elapsed")
