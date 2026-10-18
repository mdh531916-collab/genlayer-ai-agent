# { "Depends": "py-genlayer:test" }
from genlayer import *

class AIAgentEvaluator(gl.Contract):
    """
    Intelligent Contract for AI Agent Evaluation on GenLayer Network.
    Implements non-deterministic AI evaluation with strict validator consensus.
    """
    owner: str
    submissions: dict

    def __init__(self):
        self.owner = gl.message.sender
        self.submissions = {}

    @gl.public.write
    def submit_and_evaluate_task(self, task_id: str, prompt: str) -> str:
        """
        Submits a task prompt and performs non-deterministic AI evaluation 
        ensuring consensus across validators.
        """
        def evaluate_task() -> str:
            return gl.nondet.exec_prompt(prompt)

        # Ensures validator agreement through non-deterministic consensus principle
        evaluation_result = gl.eq_principle.strict_eq(evaluate_task)

        self.submissions[task_id] = {
            "creator": gl.message.sender,
            "prompt": prompt,
            "evaluation": evaluation_result,
            "status": "Evaluated"
        }

        return evaluation_result

    @gl.public.view
    def get_task(self, task_id: str) -> dict:
        """
        Retrieves submission details for a given task ID.
        """
        return self.submissions.get(task_id, {})
        
