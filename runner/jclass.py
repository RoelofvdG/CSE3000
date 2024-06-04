import corpus
import os

IMPORTS_MARKER = "// INSERT IMPORTS HERE"
TESTS_MARKER = "// INSERT TESTS HERE"


class JClass:
    def __init__(self, abs_path: str):
        self.absolute_path = abs_path
        self.class_name = abs_path[abs_path.rfind("\\") + 1:-5]
        temp = abs_path.replace(corpus.MAIN_PATH, "")[1:abs_path.rfind("\\")]
        self.package_name = temp[:max(0, temp.rfind("\\"))].replace("\\", ".")

    def has_tests(self):
        test_path = os.path.join(os.path.dirname(self.absolute_path.replace("main", "test", 1)),
                                 self.class_name + "Test.java")
        return os.path.isfile(test_path)

    def get_code(self):
        with open(self.absolute_path, "r") as f:
            return f.read()

    def create_improved_tests_file(self, imports=None, tests=None):
        test_path = os.path.join(os.path.dirname(self.absolute_path.replace("main", "test", 1)),
                                 self.class_name + "Test")
        test_file = test_path + ".java"
        improved_file = test_path + "Improved.java"

        with open(test_file, "r") as f:
            test_code = f.read()
        improved_code = test_code.replace(self.class_name + "Test", self.class_name + "TestImproved", 1)
        if imports is not None:
            improved_code = improved_code.replace(IMPORTS_MARKER, "\n".join(imports))
        if tests is not None:
            improved_code = improved_code.replace(TESTS_MARKER, "\n".join(tests).lstrip())

        with open(improved_file, "w") as f:
            f.write(improved_code)

        return improved_file

    def delete_improved_tests_file(self):
        test_path = os.path.join(os.path.dirname(self.absolute_path.replace("main", "test", 1)),
                                 self.class_name + "Test")
        improved_file = test_path + "Improved.java"
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
                if abs_path.endswith(".java"):
                    class_files.append(JClass(abs_path))
        return class_files
