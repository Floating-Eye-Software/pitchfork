# pitchfork_cli.py

import argparse
from pitchfork import Pitchfork

class PitchforkCLI:
    def __init__(self):
        self.game = Pitchfork()
        self.parser = argparse.ArgumentParser(description="Pitchfork Game CLI")

        subparsers = self.parser.add_subparsers(title="Subcommands", dest="subcommand")

        # Create subparser for the 'collect' subcommand
        collect_parser = subparsers.add_parser("collect", help="Collect a token")
        collect_parser.add_argument("player", help="Player's name")
        collect_parser.add_argument("color", help="Token color")

        # Create subparser for the 'tokens' subcommand
        tokens_parser = subparsers.add_parser("tokens", help="Get player's tokens")
        tokens_parser.add_argument("player", help="Player's name")

        # Create subparser for the 'progress' subcommand
        progress_parser = subparsers.add_parser("progress", help="Get player's progress")
        progress_parser.add_argument("player", help="Player's name")

        # Create subparser for the 'create' subcommand
        create_parser = subparsers.add_parser("create", help="Create a new player")
        create_parser.add_argument("player", help="Player's name")

        # Create subparser for the 'list' subcommand
        list_parser = subparsers.add_parser("list", help="List all players")

        # Add new subcommand for contract creation
        contract_parser = subparsers.add_parser("contract", help="Create or complete a contract")
        contract_parser.add_argument("action", choices=["create", "complete"], help="Action: create or complete a contract")
        contract_parser.add_argument("player", help="Player's name")
        contract_parser.add_argument("task", help="Task description for contract (if creating)")
        contract_parser.add_argument("reward", help="Reward token type")
        contract_parser.add_argument("amount", help="Amount of reward tokens")

    def run(self):
        args = self.parser.parse_args()

        if args.subcommand == "collect":
            success = self.game.collect_player_token(args.player, args.color)
            if success:
                print(f"Token collected: {args.color}")
            else:
                print("Invalid player or token color")

        elif args.subcommand == "tokens":
            tokens = self.game.get_player_tokens(args.player)
            if tokens is not None:
                print(f"Tokens for {args.player}: {tokens}")
            else:
                print("Invalid player")

        elif args.subcommand == "progress":
            progress = self.game.get_player_progress(args.player)
            if progress is not None:
                print(f"Progress for {args.player}: {progress}")
            else:
                print("Invalid player")

        elif args.subcommand == "create":
            self.game.create_player(args.player)
            print(f"Player '{args.player}' created.")

        elif args.subcommand == "list":
            players = self.game.get_all_players()
            print("Players:")
            for player in players:
                print(player)

        elif args.subcommand == "contract":
            if args.action == "create":
                contract = self.game.create_contract(args.player, args.task, args.reward, int(args.amount))
                print(f"Contract created: {args.task} for {args.reward} ({args.amount}) tokens")
            elif args.action == "complete":
                success = self.game.complete_contract(args.player, args.task)
                if success:
                    print("Contract completed successfully.")
                else:
                    print("Failed to complete contract.")

        else:
            print("Invalid subcommand. Use -h for help.")

if __name__ == "__main__":
    cli = PitchforkCLI()
    cli.run()
