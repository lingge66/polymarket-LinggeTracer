# openclaw_plugin.py
from core_radar import PolymarketAnalyzer

def analyze_prediction_wallet_tool(wallet_address: str) -> str:
    """
    OpenClaw Skill/Tool: 分析 Polymarket 预测市场的大户钱包交易模式。
    
    参数:
    - wallet_address (str): 以 0x 开头的以太坊/Polygon钱包地址。
    
    返回:
    - 给 AI 阅读的交易统计摘要与研报生成指令。
    """
    analyzer = PolymarketAnalyzer()  # 如果需要代理，在此处传入 proxy_port="10808"
    
    # 1. 抓取并获取数据浓缩摘要
    data_summary = analyzer.generate_ai_summary(wallet_address)
    
    # 2. 组装终极 System Prompt 给 OpenClaw 大脑
    ai_instruction = f"""
你现在是顶级加密货币与预测市场量化分析师。我刚刚通过底层程序抓取了目标钱包的交易数据，并进行了预处理。
以下是该钱包的交易特征客观数据摘要：

{data_summary}

请根据以上数据摘要，直接向用户输出一份专业、生动、具有洞察力的《大户钱包链上行为研报》。
研报需包含以下模块：
1. 【资金体量与身份画像】：通过总资金、平均单笔和最大单笔，判断他是巨鲸、量化机构还是散户？
2. 【交易流派分析】：通过“买卖行为分布”和“赔率偏好”，判断他是“稳健套利流”、“高赔率摸奖流”还是“绝对信仰持有者(纯买无卖)”？
3. 【赛道偏好】：分析他重仓的三大市场，他更关注体育、政治还是其他方向？
4. 【跟单建议】：如果普通用户想跟单他，你有什么风险提示或策略建议？

请用清晰的排版（Markdown）和专业的金融/加密行业术语输出报告。
"""
    return ai_instruction

# ================= 测试你的技能 =================
if __name__ == "__main__":
    test_wallet = "0xbddf623A2DE3b232677943fFf82e88a38Ff0eE4E"
    print("正在模拟 OpenClaw BOT 触发技能...")
    
    # BOT 调用你的函数
    prompt_for_llm = analyze_prediction_wallet_tool(test_wallet)
    
    print("\n✅ 抓取完成！以下内容将自动喂给 OpenClaw 的 LLM 大脑进行最终研报生成：\n")
    print(prompt_for_llm)