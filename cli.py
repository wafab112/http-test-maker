import argparse
from jproperties import Properties
from handlers.config_handler import ConfigHandler

class Cli:
    """
    Creates the cli arguments and parses them.
    Takes the arguments and notifies the specific handlers to handle the arguments.
    """

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog = "http-tm.py", 
            description = "Creates python-scripts, that execute http-requests after authenticating.")
        
        self.configs = Properties()
        
        parser.add_argument(
            "-y", "--assume-yes", 
            action="store_true", 
            help="USE WITH CAUTION: Assumes yes whenever a interactive yes/no question is asked. Is applied to subcommands.")

        commandParsers = parser.add_subparsers(dest="command")

        configParser = self.__init_config_parser(commandParsers)
        self.configHandler = ConfigHandler(configParser, self.configs)
        
        args = parser.parse_args()

        if args.command == "config":
            self.configHandler.handle(args)

        # MARK: this might be required to change when more arguments are added
        if not args.command:
            print("No arguments given.")
            parser.print_help()

    def __init_config_parser(self, commandParsers):
        configParser = commandParsers.add_parser("config", description="change the user's config of default values", help="change config, see %(prog)s config -h")
        configParser.add_argument("-l", "--list", action="store_true", help="lists all current configs")
        configParser.add_argument("--get-location", action="store_true", help="prints the location of the config file")
        configParser.add_argument("-u", "--user", help="new default username")
        configParser.add_argument("-p", "--pass", dest="password", metavar="pass", help="new default password")
        configParser.add_argument("--recreate", help="creates a new config file", action="store_true")
        return configParser
