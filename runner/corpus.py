import os

PROJECT_PATH = os.path.join(os.path.dirname(os.getcwd()), "corpus")
CORPUS_PATH = os.path.join(PROJECT_PATH, "src")
MAIN_PATH = os.path.join(CORPUS_PATH, "main", "java", "nl", "roelofvdg")
TEST_PATH = os.path.join(CORPUS_PATH, "test", "java", "nl", "roelofvdg")
REPORT_PATH = os.path.join(PROJECT_PATH, "build", "reports", "pitest")