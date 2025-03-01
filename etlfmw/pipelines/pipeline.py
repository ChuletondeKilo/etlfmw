from uuid import uuid4

class Pipeline:
    def __init__(self, steps):
        self.steps = steps
        self.pipeline_id: str = uuid4()

    def run(self, data):
        for step in self.steps:
            data = step(data)
        return data
