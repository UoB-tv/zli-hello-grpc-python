from pants.task.task import Task

class ProtocTask(Task):
    def execute(self):
        print("executing protoc...")
        