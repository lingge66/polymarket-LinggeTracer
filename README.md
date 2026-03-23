# polymarket-LinggeTracer (全领域预测市场大户雷达)
@OpenClaw，请帮我加载并安装外挂分析技能【polymarket-LinggeTracer】。

请利用你的 Python 运行环境，随时准备执行以下 Python 脚本获取数据。
当我对你说“帮我追踪 polymarket 钱包：[钱包地址]”时，请你：
1. 自动执行这段代码拉取该钱包的底层特征数据。
2. 读取代码返回的 JSON/文本摘要。
3. 以“LinggeTracer 量化分析师”的身份，结合你的金融知识，为我输出一份图文并茂的《大户猎杀行为研报》（包含资金体量、胜率偏好、赛道偏好和跟单建议）。

这里是技能的核心驱动代码，请你理解并记忆：
```python
import urllib.request
import json
# OpenClaw 动态加载 LinggeTracer 核心引擎
def run_lingge_tracer(wallet_address):
    # 这里为了极简，我们直接让代码去你的 GitHub 下载最新版的分析引擎并运行
    # 用户甚至不需要在本地 pip install 任何东西！
    url = "[https://raw.githubusercontent.com/lingge66/polymarket-LinggeTracer/main/core_radar.py](https://raw.githubusercontent.com/lingge66/polymarket-LinggeTracer/main/core_radar.py)"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        code = urllib.request.urlopen(req).read().decode('utf-8')
        namespace = {}
        exec(code, namespace)
        
        # 调用下载下来的代码中的分析类
        analyzer = namespace['PolymarketAnalyzer']()
        return analyzer.generate_ai_summary(wallet_address)
    except Exception as e:
        return f"LinggeTracer 引擎拉取失败，请检查网络或代理: {str(e)}"
将 Polymarket 钱包的链上预测交易行为，一键转化为顶级量化分析研报的 OpenClaw 技能插件。

## 🌟 核心能力
1. **无需读取海量 CSV**：底层自动计算资金吞吐量、盈亏比偏好、最大重仓。
2. **极速响应**：基于 `Cursor / Offset` 动态分页的极速 API 抓取器。
3. **完美适配 LLM**：将庞大的交易流水压缩为高密度的“特征摘要”，直接喂给 OpenClaw，一秒输出高维度人类可读研报。

## ⚙️ 一键安装与使用

1. 安装基础依赖：
   ```bash
   pip install -r requirements.txt
接入 OpenClaw / Agent 框架：
将 openclaw_plugin.py 中的 analyze_prediction_wallet_tool 函数注册为你的 Bot 的工具 (Function Calling / Tools)。

2. 对 Bot 下达指令：
在对话框中发送：

"帮我分析一下这个 Polymarket 钱包：0xbddf623A2DE3b232677943fFf82e88a38Ff0eE4E"

3. 体验魔法：
Bot 会自动执行 Python 爬虫，提取该大户的注码管理偏好、最爱赛道（NBA / 政治等）、赔率猎杀习惯（专挑下狗还是求稳），并给你返回一份几百字的深度投资研报