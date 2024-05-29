import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

from langchain.schema import AgentFinish
from langchain.schema.output import LLMResult
from langchain_core.callbacks.base import BaseCallbackHandler


def _current_time() -> str:
    return datetime.now(UTC).isoformat()


def _format_log(agent_name: str, event: str, output) -> Dict[str, str]:
    return {
        "agent": agent_name,
        "event": event,
        "timestamp": _current_time(),
        "tool": getattr(output, "tool", "Unknown"),
        "tool_input": getattr(output, "tool_input", "Unknown").strip(),
        "log": getattr(output, "log", "Unknown").strip(),
    }


def step_callback(
    agent_output: Union[str, List[Tuple[Dict, str]], AgentFinish],
    agent_name,
    log_file_path: Path,
):
    if isinstance(agent_output, list) and all(
        isinstance(item, tuple) for item in agent_output
    ):
        for action, description in agent_output:
            with log_file_path.open("a", encoding="utf-8") as file:
                file.write(
                    json.dumps(_format_log(agent_name, "agent_step", action)) + "\n"
                )
    elif isinstance(agent_output, AgentFinish):
        with log_file_path.open("a", encoding="utf-8") as file:
            file.write(
                json.dumps(_format_log(agent_name, "agent_finish", agent_output)) + "\n"
            )


class LLMCallbackHandler(BaseCallbackHandler):
    def __init__(self, log_path: Path):
        self.log_path = log_path

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        """Run when LLM starts running."""
        assert len(prompts) == 1
        data = {"event": "llm_start", "timestamp": _current_time(), "text": prompts[0]}
        with self.log_path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(data) + "\n")

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        """Run when LLM ends running."""
        generation = response.generations[-1][-1].message.content
        data = {"event": "llm_end", "timestamp": _current_time(), "text": generation}
        with self.log_path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(data) + "\n")
