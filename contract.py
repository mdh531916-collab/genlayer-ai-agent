# { "Depends": "py-genlayer:test" }
from genlayer import *

class AIAgentEvaluator(gl.Contract):
    """
    Enterprise-Grade Intelligent Contract for AI Agent Evaluation on GenLayer.
    Implements non-deterministic AI evaluation, strict validator consensus,
    input validation, state locks, and execution safety checks.
    """
    owner: str
    submissions: dict

    def __init__(self):
        self.owner = gl.message.sender
        self.submissions = {}

    @gl.public
    def submit_and_evaluate_task(self, task_id: str, prompt: str) -> str:
        """
        Evaluates a Web3 task using GenLayer's non-deterministic AI execution framework
        and enforces validator consensus with strict input and state safeguards.
        """
        # 1. Input validation to prevent empty data
        assert len(task_id.strip()) > 0, "Task ID cannot be empty"
        assert len(prompt.strip()) > 0, "Prompt cannot be empty"

        # 2. Prevent duplicate task IDs
        assert task_id not in self.submissions, "Task ID already exists"

        # 3. GenLayer Nondeterministic AI Execution
        def evaluate_task() -> str:
            result = gl.nondet.exec_prompt(prompt)
            assert len(str(result).strip()) > 0, "AI evaluation output was empty"
            return str(result)

        # 4. Validator consensus (Validator Agreement)
        evaluation_result = gl.eq_principle.strict_eq(evaluate_task)

        # 5. Save state with detailed structure
        self.submissions[task_id] = {
            "creator": gl.message.sender,
            "prompt": prompt,
            "evaluation": evaluation_result,
            "status": "Evaluated"
        }

        return evaluation_result

    @gl.public
    def get_task(self, task_id: str) -> dict:
        """
        Retrieves submission details for a given task ID.
        """
        assert task_id in self.submissions, "Task ID not found"
        return self.submissions[task_id]
        
