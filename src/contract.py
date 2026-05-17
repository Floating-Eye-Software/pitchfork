class Contract:
    def __init__(self, questgiver, task_description, reward_token, reward_amount):
        self.questgiver = questgiver
        self.task_description = task_description
        self.reward_token = reward_token
        self.reward_amount = reward_amount
        self.completed = False
