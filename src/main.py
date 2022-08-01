import os
import supervisely as sly
from dotenv import load_dotenv
from art import tprint

load_dotenv("local.env")


def main():
    name = os.environ["context.userLogin"]
    print("Hello World!")
    print("This app is run by user:")
    tprint(name)


if __name__ == "__main__":
    main()
