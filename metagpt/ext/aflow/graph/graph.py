# -*- coding: utf-8 -*-
# @Date    : 6/27/2024 22:07 PM
# @Author  : didi
# @Desc    : Basic Graph Class

from typing import Literal
import metagpt.ext.aflow.scripts.optimized.AMC.workflows.template.operator as operator
import metagpt.ext.aflow.scripts.optimized.AMC.workflows.round_1.prompt as prompt_custom
from metagpt.provider.llm_provider_registry import create_llm_instance
from metagpt.utils.cost_manager import CostManager
import re

DatasetType = Literal["HumanEval", "MBPP", "GSM8K", "MATH", "HotpotQA", "DROP"]

def extract_content(xml_string, tag):
    # 构建正则表达式，匹配指定的标签内容
    pattern = rf'<{tag}>(.*?)</{tag}>'
    match = re.search(pattern, xml_string, re.DOTALL)  # 使用 re.DOTALL 以匹配换行符
    return match.group(1).strip() if match else None

class Workflow:
    def __init__(
        self,
        name: str,
        llm_config,
        dataset: DatasetType,
    ) -> None:
        self.name = name
        self.dataset = dataset
        self.llm = create_llm_instance(llm_config)
        self.llm.cost_manager = CostManager()
        self.custom = operator.Custom(self.llm)

    async def __call__(self, problem: str):
        """
        Implementation of the workflow
        """
        solution = await self.custom(input=problem, instruction=prompt_custom.PROMPT)
        return solution['response'], self.llm.cost_manager.total_cost
