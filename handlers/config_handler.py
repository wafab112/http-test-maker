import consts
import argparse
import pathlib
from jproperties import Properties

class ConfigHandler:

    def __init__(self, parser: argparse.ArgumentParser, configs: Properties):
        self.parser = parser
        self.configs = configs

        if not pathlib.Path.exists(consts.CONFIG_PATH):
            self.create_config_file()
        
        self.load_config_file()

    def load_config_file(self):
        with open(consts.CONFIG_PATH, "rb") as configFile:
            self.configs.load(configFile)

    def handle(self, args: argparse.Namespace):
        hadArgument = False

        if args.get_location:
            print(str(consts.CONFIG_PATH))
            hadArgument = True

        if args.list:
            print("Listing current config.")
            self.list_config()
            hadArgument = True

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
            hadArgument = True

        if args.password:
            old = self.configs["default.password"]
            self.configs["default.password"] = args.password
            self.safe_config()
            print(f"set old default password ({old[0]}) to '{args.password}'")
            hadArgument = True

        if args.user:
            old = self.configs["default.user"]
            self.configs["default.user"] = args.user
            self.safe_config()
            print(f"set old default user ({old[0]}) to '{args.user}'")
            hadArgument = True

        if not hadArgument:
            print("No argmuents given")
            self.parser.print_help()


    def delete_config_file(self):
        if consts.CONFIG_PATH.exists():
            consts.CONFIG_PATH.unlink()
        print("Old config file deleted.")

    def safe_config(self):
        with open(consts.CONFIG_PATH, "r+b") as configFile:
            self.configs.store(configFile)

    def create_config_file(self):
        consts.CONFIG_PATH.touch()

        with open(consts.CONFIG_PATH, "r+b") as configFile:
            self.configs.clear()
            self.configs["default.user"] = "test"
            self.configs["default.password"] = "pass"
            self.configs.store(configFile)

        with open(consts.CONFIG_PATH, "rb") as configFile:
            self.configs.load(configFile)
        print(f"New config file {str(consts.CONFIG_PATH)} created.")

    def list_config(self):
        for item in self.configs.items():
            print("\t" + item[0] + "=" + item[1][0])