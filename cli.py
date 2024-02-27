import argparse
from jproperties import Properties
from handlers.config_handler import ConfigHandler

class Cli:
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog = "http-tm.py", 
            description = "Creates python-scripts, that execute http-requests after authenticating.")
        
        self.configs = Properties()
        self.configHandler = ConfigHandler(self.configs)
        
        parser.add_argument(
            "-y", "--assume-yes", 
            action="store_true", 
            help="USE WITH CAUTION: Assumes yes whenever a interactive yes/no question is asked. Is applied to subcommands.")

        subparsers = parser.add_subparsers(dest="command")

        config_parser = subparsers.add_parser("config", description="change the user's config of default values", help="change config, see %(prog)s config -h")
        config_parser.add_argument("-l", "--list", action="store_true", help="lists all current configs")
        config_parser.add_argument("--get-location", action="store_true", help="prints the location of the config file")
        config_parser.add_argument("-u", "--user", help="new default username")
        config_parser.add_argument("-p", "--pass", dest="password", metavar="pass", help="new default password")
        config_parser.add_argument("--recreate", help="creates a new config file", action="store_true")
        
        args = parser.parse_args()

        if args.command == "config":
            self.configHandler.handle(args)

        # MARK: this might be required to change when more arguments are added
        if not args.command:
            parser.print_help()