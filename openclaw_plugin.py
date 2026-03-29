# ==============================================================================
# Copyright (C) 2026 领哥大虾 (lingge66). All Rights Reserved.
# Project: polymarket-LinggeTracer
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# 警告：本项目采用 GPLv3 传染性开源协议。任何企业或个人未经授权，
# 严禁将本核心逻辑（及其衍生算法）用于闭源商业化盈利项目。违者必究。
# ==============================================================================
# openclaw_plugin.py
import time
from core_radar import PolymarketAnalyzer

def analyze_prediction_wallet_tool(target_id: str, bot_send_message_func=None) -> str:
    """
    OpenClaw Skill/Tool: 分析 Polymarket 预测市场的大户档案。
    
    参数:
    - target_id (str): 支持直接输入 Polymarket 上的用户名（如 Theo4），或 0x 开头的钱包地址。
    - bot_send_message_func (callable): 可选。电报等客户端的实时进度播报回调。
    """
    # 实例化分析器，按需开启代理端口
    analyzer = PolymarketAnalyzer(proxy_port="7890")  
    
    def telegram_updater(msg_text):
        if bot_send_message_func:
            bot_send_message_func(msg_text)
        else:
            print(f"[系统播报] {msg_text}")

    # 获取数据浓缩摘要 (支持传名字了！)
    data_summary = analyzer.generate_ai_summary(target_id, progress_callback=telegram_updater)
    
    # 💡 提示词全面升级，加入对真实利润（PnL）的结合分析
    ai_instruction = f"""
你现在是顶级加密货币与预测市场量化分析师。我刚刚突破了 API 限制，抓取了该玩家全量、无死角的底层交易数据。
以下是该玩家的客观财务数据与高阶特征摘要：

{data_summary}

请根据以上数据摘要，输出一份极其专业、甚至带有压迫感的《大户资金猎杀与风险评估研报》。
研报需包含以下核心模块：
1. 【PnL与胜率审计】：结合总盈亏、30天/7天趋势、以及真实结算胜率，评价他的赚钱能力（是在稳步增长，还是在近期暴亏？）。分析他的“生涯最佳/最惨战役”，看看他靠什么发家，又在哪栽了跟头。
2. 【高阶策略模式判定】：这是最重要的部分！请根据他的“操作类型分布”判定他的流派：
   - 如果 SPLIT/MERGE 很多：判定为“套利/做市商机器人”。
   - 如果只有 BUY 和 REDEEM，几乎没有 SELL：判定为“死忠信仰者/基本面下注者”。
   - 如果独立市场数极多，单笔小：判定为“分散投资扫盘客”。
   - 结合他的资金吞吐量和独立市场数进行专业定性。
3. 【当前风险暴露】：分析他的“当前未平仓头寸”和占用资金。他是空仓观望，还是重兵压境？
4. 【跟单可行性与风控预警】：直接告诉用户，这个钱包到底值不值得做反指（Counter-Trade），或者值不值得设置巨鲸监控跟随？

请用清晰的排版（Markdown）和专业的加密量化行话输出报告。
"""
    return ai_instruction

# ================= 测试你的技能 =================
if __name__ == "__main__":
    # 测试时，你现在可以直接写名字了！底层会自动寻址转成 0x
    test_target = "0xfaa5f6821c549c6571980ccc3a86ad9e052eb8de" # 你也可以改回之前的 0xbddf623A2DE3b232677943fFf82e88a38Ff0eE4E
    
    print("🤖 正在模拟 OpenClaw BOT 触发技能...\n")
    
    def mock_telegram_send(msg):
        print(f"\r💬 [电报实时进度]: {msg.replace(chr(10), ' ')}", end="", flush=True)
        time.sleep(0.1)
        
    prompt_for_llm = analyze_prediction_wallet_tool(test_target, bot_send_message_func=mock_telegram_send)
    
    print("\n\n✅ 抓取与特征抽取完成！以下内容将自动喂给大模型进行研报生成：\n")
    print(prompt_for_llm)
