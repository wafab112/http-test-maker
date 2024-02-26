#!/usr/local/opt/python@3.11/bin/python3

import argparse
import sys
import pathlib
from jproperties import Properties

CONFIG_NAME = ".http-tm"
CONFIG_PATH = pathlib.Path.home() / CONFIG_NAME

class Cli:
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog = "http-tm.py", 
            description = "Creates python-scripts, that execute http-requests after authenticating.")
        
        self.configs = Properties()
        
        # TODO: load config file
        if not pathlib.Path.exists(CONFIG_PATH):
            self.create_config_file()

        self.load_config_file()
        
        parser.add_argument(
            "-y", "--assume-yes", 
            action="store_true", 
            help="USE WITH CAUTION: Assumes yes whenever a interactive yes/no question is asked. Is applied to subcommands.")

        subparsers = parser.add_subparsers(dest="command")

        config_parser = subparsers.add_parser("config", description="change the user's config of default values", help="change config, see %(prog)s config -h")
        config_parser.add_argument("-u", "--user", help="new default username")
        config_parser.add_argument("-p", "--pass", help="new default password")
        config_parser.add_argument("--get-location", action="store_true", help="prints the location of the config file")
        config_parser.add_argument(
            "--recreate",
            help="creates a new config file at specified path or default ~/.http-tm",
            action="store_true")
        
        args = parser.parse_args()

        if args.command == "config":
            self.handle_config(args)

    def load_config_file(self):
        with open(CONFIG_PATH, "rb") as configFile:
            self.configs.load(configFile)

    def handle_config(self, args: argparse.Namespace):
        if args.get_location:
            # TODO
            print("get-location")

        if args.recreate:
            if args.assume_yes:
                print("Are you sure you want to delete the old config and create a new one? (y/N): ")
                print("-y flag set. Assumed yes.")
                self.delete_config_file()
                self.create_config_file()

            else:
                confirmation = input("Are you sure you want to delete the old config and create a new one? (y/N): ")
                if not confirmation:
                    print("Left empty. Assumed no. Nothing changes.")

                if confirmation.lower() == "n":
                    print("Nothing changes.")

                if confirmation.lower() == "y":
                    self.delete_config_file()
                    self.create_config_file()

        if args.user:
            # TODO
            print(f"set old default user to '{args.user}'")

    def delete_config_file(self):
        if CONFIG_PATH.exists():
            CONFIG_PATH.unlink()
        print("Old config file deleted.")

    def create_config_file(self):
        CONFIG_PATH.touch()
        with open(CONFIG_PATH, "rb") as configFile:
            self.configs.load(configFile)
        print(f"New config file ${str(CONFIG_PATH)} created.")


if __name__ == "__main__":
    cli = Cli()
