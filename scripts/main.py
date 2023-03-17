import sys
import create_elastic_users


class Job:

    def __init__(self, command, description, func):
        self.command = command
        self.description = description
        self.func = func


JOBS = [
    Job("elastic_users",
        "Create the required Elastic users for CSL applictions",
        create_elastic_users.run)
]


def run():
    args = sys.argv[1:]
    allowed_args_map = {job.command: job for job in JOBS}
    for arg in args:
        job = allowed_args_map.get(arg)
        if job:
            job.func()
        else:
            print(f"ERROR: \"{arg}\" is not a valid script argument. Valid scripts are: {allowed_args_map.keys()}")


run()
