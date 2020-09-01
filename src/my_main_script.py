import os
import random
import string
import supervisely_lib as sly

my_app = sly.AppService()

LENGTH = int(os.environ['modal.state.length'])

@sly.timeit
@my_app.callback("generate")
def generate_random_string(api: sly.Api, task_id, context, state, app_logger):
    rand_string = ''.join((random.choice(string.ascii_letters + string.digits)) for _ in range(LENGTH))
    rand_string = state["prefix"] + rand_string
    api.task.set_field(task_id, "data.randomString", rand_string)


@sly.timeit
@my_app.callback("preprocessing")
def preprocessing(api: sly.Api, task_id, context, state, app_logger):
    sly.logger.info("do something here")


def main():
    sly.logger.info("Script arguments from modal dialog box",  extra={"length: ": LENGTH})

    api = sly.Api.from_env()

    data = {
        "randomString": "hello!"
    }

    state = {
        "prefix": "abc_"
    }

    initial_events = [
        {
            "state": None,
            "context": None,
            "command": "preprocessing",
        }
    ]

    # Run application service
    my_app.run(data=data, state=state, initial_events=initial_events)


if __name__ == "__main__":
    sly.main_wrapper("main", main)