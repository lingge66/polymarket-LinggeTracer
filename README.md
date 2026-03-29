# 🪐 polymarket-LinggeTracer (全领域预测市场大户雷达)1.1版本

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![OpenClaw Ready](https://img.shields.io/badge/OpenClaw-Ready-orange.svg)
![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-green.svg)

将 Polymarket 钱包的链上预测交易行为，一键转化为顶级量化分析研报的 OpenClaw 技能插件。由开发者领哥大虾（lingge66）设计构建。

## 🌟 核心能力
1. **无需读取海量 CSV**：底层算法自动计算绝对资金吞吐量、盈亏比偏好、最大单笔重仓。
2. **极速动态响应**：基于 `Cursor / Offset` 动态混合分页的极速 API 抓取器，防限流、防遗漏。
3. **完美适配 LLM**：将庞大的高频交易流水压缩为高密度的“特征摘要”，直接喂给大语言模型，一秒输出高维度人类可读研报。
## ❂ 最近更新内容
1. **上帝视角财务审计 (绝对 PnL 与胜率)：不再盲猜收益！深度接入隐藏排行榜与底层持仓 API，精确提取大户的 All-time 真实总盈亏、7天/30天资金趋势，以及基于真实结算开奖的绝对胜率。
2. **高阶量化流派解码：不仅统计单纯的 Buy/Sell，更深度解析盘口做市行为（SPLIT/MERGE）与到期兑付（REDEEM）。让 AI 瞬间识破伪装成大户的“无风险套利机器人”或“高频对冲脚本”。
3. **用户名免转换直通车 (智能寻址)：告别反人类的 0x... 十六进制长串！支持直接输入 Polymarket 玩家用户名（如 Theo4），底层雷达全自动在全网数据库中寻址对齐。
## 📞 技术支持与声明
**主架构师**：lingge66 & AI 团队
**Twitter**：[@shangdu2005](https://x.com/shangdu2005)
---

## 🚀 方式一：零代码一键魔法安装（推荐普通用户）

如果你使用的是 OpenClaw 或其他具备 Python 代码执行能力的 AI Agent，**完全不需要在本地安装任何东西**。

只需直接复制下方这段“魔法指令”，发送给你的 AI 助手即可完成技能注入：


> ```python
> 请帮我加载并安装外挂分析技能【polymarket-LinggeTracer】。
> 请利用你的 Python 运行环境，随时准备执行以下 Python 脚本获取数据。
> 当我对你说“帮我追踪 polymarket 钱包：[钱包地址]”时，请你：
> 1. 自动执行这段代码拉取该钱包的底层特征数据。
> 2. 读取代码返回的 JSON/文本摘要。
> 3. 以“LinggeTracer 量化分析师”的身份，结合你的金融知识，为我输出一份图文并茂的《大户猎杀行为研报》（包含资金体量、胜率偏好、赛道偏好和跟单建议）。
> 
> 这里是技能的核心驱动代码，请你理解并记忆：
> > import urllib.request
> > import json
> 
> # OpenClaw 动态加载 LinggeTracer 核心引擎
> def run_lingge_tracer(wallet_address):
>     url = "[https://raw.githubusercontent.com/lingge66/polymarket-LinggeTracer/main/core_radar.py](https://raw.githubusercontent.com/lingge66/polymarket-LinggeTracer/main/core_radar.py)"
>     try:
>         req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
>         code = urllib.request.urlopen(req).read().decode('utf-8')
>         namespace = {}
>         exec(code, namespace)
>         
>         # 调用下载下来的代码中的分析类
>         analyzer = namespace['PolymarketAnalyzer']()
>         return analyzer.generate_ai_summary(wallet_address)
>     except Exception as e:
>         return f"LinggeTracer 引擎拉取失败，请检查网络或代理: {str(e)}"
> ```

---

## 💻 方式二：开发者本地集成部署

如果你想将本工具集成到你自己的量化系统或独立 Agent 框架中，请按照以下步骤操作：

```bash
1. 克隆与安装依赖包
git clone [https://github.com/lingge66/polymarket-LinggeTracer.git](https://github.com/lingge66/polymarket-LinggeTracer.git)
cd polymarket-LinggeTracer

2. 安装依赖
pip install -r requirements.txt

3. 注册为 Agent Tool (以 OpenClaw 为例)
将项目中的 openclaw_plugin.py 里的 analyze_prediction_wallet_tool 函数，注册为你的 Bot 的 Function Calling / Tools。
(注：如遇网络阻断，请在 openclaw_plugin.py 内部配置你的本地代理端口。)
🎮 体验魔法
部署完成后，在对话框中直接向你的机器人下达指令：

“帮我分析一下这个 Polymarket 钱包：0xbddf623A2DE3b232677943fFf82e88a38Ff0eE4E”

🤖 Bot 将自动返回如下深度洞察：

该大户的真实注码管理偏好（Kelly Criterion 估算）

最爱重仓赛道（NBA、欧洲杯或政治大选）

赔率猎杀习惯（专挑下狗 Underdog 还是求稳 Favorite）

最终图文并茂的千字深度投资研报！



