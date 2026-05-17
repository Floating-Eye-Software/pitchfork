# player.py

from contract import Contract
from token import Token

class Player:
    def __init__(self, name, tokens=None, progress=None, scores=None):
        if tokens is None:
            tokens = {color: 0 for color in Token.COLORS}
        tokens["gray"] = 0  # Add gray tokens
        self.tokens = tokens
        if progress is None:
            progress = {"skills": 0, "contracts": 0, "achievements": []}
        self.progress = progress
        if scores is None:
            scores = {
                "skill_enhancement": 0,
                "contract_completion": 0,
                "commodity_conversion": 0,
                "market_success": 0,
                "quester_score": 0,
                "questgiver_score": 0
            }
        self.scores = scores


    def collect_token(self, color):
        if color in self.tokens:
            self.tokens[color] += 1
            self.progress["skills"] += 1
            return True
        return False

    def get_tokens(self):
        return self.tokens

    def get_progress(self):
        return self.progress

    def create_contract(self, task_description, reward_token, reward_amount):
        contract = Contract(self.name, task_description, reward_token, reward_amount)
        # Store contract in a database or list
        return contract

    def complete_contract(self, contract):
        if contract.completed:
            return "Contract already completed"
        # Logic to reward player
        self.tokens[contract.reward_token] += contract.reward_amount
        contract.completed = True
        return f"Contract completed: {contract.task_description}"

    def earn_achievement(self, achievement_name):
        self.progress["achievements"].append(achievement_name)

    def update_score(self, score_type, amount):
        if score_type in self.scores:
            self.scores[score_type] += amount

    def convert_to_gray_tokens(self, color, amount):
        if color in self.tokens and self.tokens[color] >= amount:
            self.tokens[color] -= amount
            self.tokens["gray"] += amount
            return True
        return False

    def convert_commodities_to_tokens(self, commodity, amount):
        # Logic for converting commodity shares into colored tokens
        pass
