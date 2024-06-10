SUCCESS = 0
COMPILE_ERROR = 1
TEST_ERROR = 2


class RunResult:
    def __init__(self, status_code=SUCCESS, raw="", error_locations=None):
        if error_locations is None:
            error_locations = []
        self.status_code = status_code
        self.raw = raw
        self.error_locations = error_locations

    def has_error(self):
        return self.status_code is not SUCCESS
