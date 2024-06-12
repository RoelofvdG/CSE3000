from openai import OpenAI
from jclass import JClass


class LLMAPI:
    def __init__(self, url="https://llm.roelofvdg.nl/v1"):
        self.client = OpenAI(base_url=url, api_key="lm-studio")

        self.models = self.client.models.list()
        self.model_id = list(self.models)[0].id

    def prompt(self, message):
        completion = self.client.chat.completions.create(
            model=self.model_id,
            messages=[
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )
        return completion.choices[0].message.content

    def generate_tests(self, jclass: JClass):
        code = jclass.get_code()
        raw = self.prompt("Write junit 4 test for this Java class, give only the Java code:\n" + code)
        lines = raw.splitlines(keepends=True)
        imports = []
        tests = []
        extracting_test = None
        tab = None

        for i in range(len(lines)):
            l = lines[i]
            if l.strip().startswith("import"):
                imports.append(l)

            if l.strip().startswith("@") and extracting_test is None:
                extracting_test = l
                tab = l[:l.index("@")]
            elif extracting_test is not None:
                extracting_test += l
                if l.startswith(tab + "}"):
                    tests.append(extracting_test)
                    extracting_test = None

        res = {
            "raw": raw,
            "imports": imports,
            "tests": tests
        }
        return res
