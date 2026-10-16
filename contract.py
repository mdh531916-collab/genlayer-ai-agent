from genlayer import *

@gl.contract
class AIAgentEvaluator:
    def __init__(self):
        self.owner = gl.message.sender
        self.submissions = {}

    @gl.public
    def submit_task(self, task_id: str, details: str):
        self.submissions[task_id] = {
            "creator": gl.message.sender,
            "details": details,
            "status": "Pending"
        }

    @gl.public
    def get_task(self, task_id: str) -> dict:
        return self.submissions.get(task_id, {})
      
