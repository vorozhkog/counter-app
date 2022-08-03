import os
from dotenv import load_dotenv
from art import tprint

# load ENV variables for debug
load_dotenv("local.env")


def main():
    name = os.environ["context.userLogin"]
    print("Hello World! This app is run by the user:")
    tprint(name)


if __name__ == "__main__":
    main()
