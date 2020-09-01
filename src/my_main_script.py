import os
import random
import string
import supervisely_lib as sly

my_app = sly.AppService()

LENGTH = int(os.environ['modal.state.length'])


@my_app.callback("generate")
@sly.timeit
def generate_random_string(api: sly.Api, task_id, context, state):
    rand_string = ''.join((random.choice(string.ascii_letters + string.digits)) for _ in range(LENGTH))
    api.task.set_field(task_id, "data.randomString", rand_string)


def main():
    sly.logger.info("Script arguments from modal dialog box",  extra={"length: ": LENGTH})

    api = sly.Api.from_env()

    data = {
        "randomString": "hello!"
    }

    state = {
    }

    initial_events = [
        {
            "state": None,
            "context": None,
            "command": "calc",
        }
    ]

    # Run application service
    my_app.run(data=data, state=state, initial_events=initial_events)


if __name__ == "__main__":
    sly.main_wrapper("main", main)