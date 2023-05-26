from datetime import datetime
from typing import Any
from langchain.prompts.prompt import PromptTemplate
from llm4data.prompts.utils import get_prompt_manager


class DatedPrompt(PromptTemplate):
    task_label = "DatedPrompt"
    prompt_type = "zeros"

    def format(self, **kwargs: Any) -> str:
        if "now" not in kwargs:
            kwargs["now"] = datetime.now().date()

        return super().format(**kwargs)

    def send_prompt(self, prompt: str, api_kwargs: dict = None, send_prompt_kwargs: dict = None, **kwargs: Any):
        prompt_manager = get_prompt_manager(
            self.task_label,
            type=self.prompt_type,
        )

        if send_prompt_kwargs is None:
            # Default to returning data
            send_prompt_kwargs = dict(
                return_data=True,
            )

        return prompt_manager.send_prompt(
            user_content=prompt,
            user_template=self.format(**kwargs),
            api_kwargs=api_kwargs,
            **send_prompt_kwargs,
        )
