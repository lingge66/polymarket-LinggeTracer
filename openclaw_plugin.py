# openclaw_plugin.py
import time
from core_radar import PolymarketAnalyzer

def analyze_prediction_wallet_tool(wallet_address: str, bot_send_message_func=None) -> str:
    """
    OpenClaw Skill/Tool: 分析 Polymarket 预测市场的大户钱包交易模式。
    
    参数:
    - wallet_address (str): 以 0x 开头的以太坊/Polygon钱包地址。
    - bot_send_message_func (callable): 可选参数。传入机器人的发消息函数，实现电报等客户端的实时进度播报。
    
    返回:
    - 给 AI 阅读的交易统计摘要与研报生成指令。
    """
    # 实例化分析器，如果你的服务跑在东京 VPS 或者本地，按需开启代理端口
    analyzer = PolymarketAnalyzer(proxy_port="10808")  
    
    # 💡 核心新增：定义一个内部回调函数，专门用来向电报/终端更新状态
    def telegram_updater(msg_text):
        if bot_send_message_func:
            # 如果 OpenClaw 传入了发消息的接口，就调用它实时发给用户
            bot_send_message_func(msg_text)
        else:
            # 否则回退为本地打印
            print(f"[系统播报] {msg_text}")

    # 1. 抓取并获取数据浓缩摘要 (把回调函数传给底层引擎)
    data_summary = analyzer.generate_ai_summary(wallet_address, progress_callback=telegram_updater)
    
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
    print("🤖 正在模拟 OpenClaw BOT 触发技能...\n")
    
    # 模拟电报机器人的消息发送函数 (用来测试动态进度效果)
    def mock_telegram_send(msg):
        # 使用 \r 覆盖上一行，模拟电报消息被 "edit" 更新的视觉效果
        # 当你在本地 VSCode 的终端运行它时，你会看到进度条在同一行刷新！
        print(f"\r💬 [电报实时消息推送]: {msg.replace(chr(10), ' ')}", end="", flush=True)
        time.sleep(0.1)
        
    # BOT 调用你的函数，并将发消息的能力传进去
    prompt_for_llm = analyze_prediction_wallet_tool(test_wallet, bot_send_message_func=mock_telegram_send)
    
    print("\n\n✅ 抓取完成！以下内容将自动喂给 OpenClaw 的 LLM 大脑进行最终研报生成：\n")
    print(prompt_for_llm)
