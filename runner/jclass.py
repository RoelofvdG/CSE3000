import corpus
import os

IMPORTS_MARKER = "// INSERT IMPORTS HERE"
TESTS_MARKER = "// INSERT TESTS HERE"
BLACKLIST = ["calculator", "namedstyle", "consoleexception", "filenamerequest"]


class JClass:
    def __init__(self, abs_path: str):
        self.absolute_path = abs_path
        self.class_name = abs_path[abs_path.rfind("\\") + 1:].removesuffix(".disabled").removesuffix(".java")
        temp = abs_path.replace(corpus.MAIN_PATH, "")[1:abs_path.rfind("\\")]
        self.package_name = temp[:max(0, temp.rfind("\\"))].replace("\\", ".")

    def disable(self):
        if not self.is_disabled():
            new_path = self.absolute_path + ".disabled"
            os.rename(self.absolute_path, new_path)
            self.absolute_path = new_path

        test_path = self.__get_test_path() + ".java"
        improved_test_path = self.__get_test_path() + "Improved.java"
        if os.path.isfile(test_path):
            os.rename(test_path, test_path + ".disabled")
        if os.path.isfile(improved_test_path):
            os.rename(improved_test_path, improved_test_path + ".disabled")

    def enable(self):
        if self.is_disabled():
            new_path = self.absolute_path.removesuffix(".disabled")
            os.rename(self.absolute_path, new_path)
            self.absolute_path = new_path

        test_path = self.__get_test_path() + ".java.disabled"
        improved_test_path = self.__get_test_path() + "Improved.java.disabled"
        if os.path.isfile(test_path):
            os.rename(test_path, test_path.removesuffix(".disabled"))
        if os.path.isfile(improved_test_path):
            os.rename(improved_test_path, improved_test_path.removesuffix(".disabled"))

    def enable_base_tests(self):
        test_file = self.__get_test_path() + ".java.disabled"
        if os.path.isfile(test_file):
            os.rename(test_file, test_file.removesuffix(".disabled"))

    def disable_base_tests(self):
        test_file = self.__get_test_path() + ".java"
        if os.path.isfile(test_file):
            os.rename(test_file, test_file + ".disabled")

    def is_disabled(self):
        return self.absolute_path.endswith(".java.disabled")

    def __get_test_path(self):
        return os.path.join(os.path.dirname(self.absolute_path.replace("main", "test", 1)), self.class_name + "Test")

    def disable_improved_test_by_line(self, line_number):
        print("Disable test on line", line_number + 1)
        improved_file = self.__get_test_path() + "Improved.java"
        with open(improved_file, "r") as f:
            f = f.read()
        lines = f.splitlines(keepends=True)
        start = end = line_number
        for i in reversed(range(line_number)):
            if lines[i].replace("/", "").strip().startswith("@"):
                start = i
                break
        for i in range(line_number, len(lines)):
            # print(lines[i].replace("/", "").strip())
            if lines[i].replace("/", "").strip() == "}" and lines[i+1].replace("/", "").strip() == "":
                end = i
                break
        for i in range(start, end + 1):
            if i < len(lines):
                lines[i] = "//" + lines[i]

        with open(improved_file, "w") as f:
            f.write("".join(lines))

    def disable_improved_test_by_name(self, test_name):
        print("Disable test", test_name)
        improved_file = self.__get_test_path() + "Improved.java"
        with open(improved_file, "r") as f:
            f = f.read()
        lines = f.splitlines()
        for i in range(len(lines)):
            if test_name in lines[i]:
                self.disable_improved_test_by_line(i)
                return

    def disable_improved_test(self, location):
        if isinstance(location, int):
            self.disable_improved_test_by_line(location)
        elif isinstance(location, str):
            self.disable_improved_test_by_name(location)

    def has_tests(self):
        test_path = self.__get_test_path() + ".java"
        disabled_test_path = test_path + ".disabled"
        return os.path.isfile(test_path) or os.path.isfile(disabled_test_path)

    def get_code(self):
        with open(self.absolute_path, "r") as f:
            return f.read()

    def create_improved_tests_file(self, imports=None, tests=None):
        test_path = self.__get_test_path()
        test_file = test_path + "Template.java"
        improved_file = test_path + "Improved.java"

        with open(test_file, "r") as f:
            test_code = f.read()
        improved_code = test_code.replace(self.class_name + "TestTemplate", self.class_name + "TestImproved", 1)
        if imports is not None:
            improved_code = improved_code.replace(IMPORTS_MARKER, IMPORTS_MARKER + "\n" + "\n".join(imports))
        if tests is not None:
            improved_code = improved_code.replace(TESTS_MARKER, TESTS_MARKER + "\n" + "\n".join(tests))

        with open(improved_file, "w") as f:
            f.write(improved_code)

        return improved_file

    def delete_improved_tests_file(self):
        improved_file = self.__get_test_path() + "Improved.java"
        if os.path.exists(improved_file):
            os.remove(improved_file)
        return True

    def __repr__(self):
        return "<JClass " + ".".join([self.package_name, self.class_name]).lstrip(".") + ">"

    @staticmethod
    def get_classes():
        class_files = []
        for root, dirs, files in os.walk(corpus.MAIN_PATH):
            for file in files:
                abs_path = os.path.join(root, file)
                if abs_path.endswith(".java") or abs_path.endswith(".java.disabled"):
                    jclass = JClass(abs_path)
                    if jclass.class_name.lower() not in BLACKLIST:
                        class_files.append(jclass)
        return class_files
