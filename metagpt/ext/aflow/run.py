import asyncio
import json
from pathlib import Path
from metagpt.benchmark.hotpotqa import HotpotQABenchmark
from .graph import Workflow

# LLM配置
llm_config = {
    "model": "gpt-4o-mini",  # 或其他模型名称
    "api_key": "sk-b6XnSDwGJCHHly3lC3B36cE3Ac014914AaD07b17Ca3e18F0",
    "base_url": "https://oneapi.deepwisdom.ai/v1"  # 如果需要的话
}

async def main():
    # 创建workflow实例
    workflow = Workflow(
        name="hotpotqa",
        llm_config=llm_config,
        dataset="HotpotQA"
    )
    
    # 初始化benchmark
    benchmark = HotpotQABenchmark(
        name="hotpotqa",
        file_path="data/hotpotqa_test.jsonl",  # 测试数据路径
        log_path="logs"  # 日志路径
    )
    
    # 运行benchmark
    results = await benchmark.run(workflow)
    
    # 输出结果
    print(f"Average Score: {results['average_score']}")
    print(f"Total Cost: ${results['total_cost']}")

if __name__ == "__main__":
    asyncio.run(main())