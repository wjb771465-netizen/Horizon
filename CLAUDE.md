# Horizon

AI 驱动的信息聚合系统——从多源抓取内容、AI 打分筛选、二次丰富背景知识，生成中英双语日报。当前在个人定制阶段：接入 SiliconFlow 的 DeepSeek V4 Flash，修 bug、调性能、本地化。

## Key Paths

| 路径 | 用途 |
|------|------|
| `src/main.py` | CLI 入口，argparse 参数解析 |
| `src/orchestrator.py` | 核心编排器，串联 fetch → dedup → score → enrich → summary 全流程 |
| `src/models.py` | Pydantic 数据模型：Config、ContentItem、AIConfig、各 source 配置 |
| `src/ai/` | AI 层：多 provider 客户端（OpenAI/Anthropic/Gemini/Azure）、内容分析、背景丰富、摘要生成 |
| `src/scrapers/` | 内容源抓取器：HackerNews、RSS、Reddit、Telegram、Twitter、GitHub、OpenBB、OSS Insight |
| `src/services/` | 输出服务：邮件投递、webhook 通知（飞书/Slack/Discord 等）、trending 子命令 |
| `src/storage/` | 文件持久化：配置加载/保存、日报存储、订阅者管理 |
| `src/mcp/` | MCP 服务器，将 pipeline 各阶段暴露为工具供 AI assistant 调用 |
| `src/setup/` | 交互式配置向导 |
| `scripts/` | 辅助脚本：daily-run.sh（cron）、github_trending.py（原型） |
| `data/` | 运行时数据：config.json、presets.json、summaries/ |
| `.github/workflows/` | GitHub Actions：每 3 天定时跑 horizon + trending，产物 commit 到 `data/summaries/` |
| `docs/` | Jekyll GitHub Pages 文档站点 |
| `tests/` | pytest 测试套件 |

## Rules

- 配置文件 `data/config.json` 中所有字符串值支持 `${VAR}` 环境变量展开
- AI 客户端有 fallback 机制：主 provider 超时/网络错误时自动切备用 provider
- `--quiet` 模式用于 cron 定时任务，抑制所有终端输出
- 日报输出默认按 `{output_dir}/YYYY/MM/` 日期子目录存放

## Tech Stack

- Python 3，asyncio 异步全链路
- httpx（HTTP）、feedparser（RSS）、ddgs（DuckDuckGo 搜索）
- OpenAI SDK（多 provider 兼容层）、Anthropic SDK、Google genai
- Pydantic（配置/数据模型）、Rich（终端 UI）、Tenacity（重试）
- Jekyll（GitHub Pages 文档站点）
- uv（包管理）
