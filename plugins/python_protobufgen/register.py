from pants.goal.goal import Goal
from pants.goal.task_registrar import TaskRegistrar as task
from python_protobufgen.tasks.protoc_task import ProtocTask

def register_goals():
    Goal.register(
        name="python-protobufgen",
        description="Generate python stubs from proto files"
    )
    task(name="python-protoc", action=ProtocTask).install("python-protobufgen")