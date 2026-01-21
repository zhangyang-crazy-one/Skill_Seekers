# Skill Seeker（技能搜索器）

[![版本](https://img.shields.io/badge/version-2.8.0-blue.svg)](https://github.com/zhangyang-crazy-one/Skill_Seekers)
[![许可证: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MCP 集成](https://img.shields.io/badge/MCP-集成-blue.svg)](https://modelcontextprotocol.io)
[![测试](https://img.shields.io/badge/测试-1200+%20通过-brightgreen.svg)](tests/)
[![PaddleOCR](https://img.shields.io/badge/PaddleOCR-支持-blue.svg)](#paddleocr-支持)

**中文文档生成 Claude AI 技能的自动化工具。支持文档网站、GitHub 仓库和 PDF 文件的一键转换。**

---

## 🎯 项目简介

Skill Seeker 是一个自动化工具，可将文档网站、GitHub 仓库和 PDF 文件快速转换为 Claude AI 可用的技能格式。

**核心功能：**
- 🤖 自动抓取文档内容（支持任何文档网站）
- 📊 深度分析代码仓库（AST 解析）
- 🔍 检测文档与代码实现之间的冲突
- ✨ AI 增强（提取最佳示例和关键概念）
- 📦 一键打包为 Claude 可用的 `.zip` 文件

**效率提升：** 原本需要数小时的手动工作，现在只需 20-40 分钟即可完成！

---

## ✨ 核心特性

### 📄 PDF 解析（新增 PaddleOCR 支持 ⭐）

**2025年重大更新：**

现在支持 **PaddleOCR** 进行中文文档的 OCR 识别！

| 特性 | 详情 |
|------|------|
| **OCR 引擎** | PaddleOCR（推荐）或 Tesseract（备用） |
| **中文识别率** | 86.05%（印刷中文） |
| **模型大小** | 仅 16 MB（识别）+ 4.7 MB（检测） |
| **处理速度** | 21ms/图，370+ 字符/秒 |

**PaddleOCR vs Tesseract 对比：**

| 指标 | PaddleOCR | Tesseract |
|------|-----------|-----------|
| **中文印刷识别率** | ✅ 86.05% | ~85% |
| **中文手写识别率** | ✅ 41.66% | ~20% |
| **模型大小** | 16 MB | 20 MB |
| **处理速度** | 21ms/图 | 50-100ms/图 |
| **安装复杂度** | ⭐⭐ 简单 | ⭐⭐⭐⭐⭐ 复杂 |

**使用方法：**

```bash
# 使用 PaddleOCR（推荐，中文效果更好）
skill-seekers pdf --pdf docs.pdf --ocr --ocr-engine paddle --paddle-lang ch

# 自动选择引擎（默认）
skill-seekers pdf --pdf docs.pdf --ocr --ocr-engine auto

# 使用 Tesseract（备用）
skill-seekers pdf --pdf docs.pdf --ocr --ocr-engine tesseract
```

**支持的语言：**
- `ch` - 简体中文（默认）
- `en` - 英文
- `chinese_cht` - 繁体中文
- `korean` - 韩文
- `japan` - 日文
- `latin` - 拉丁语系

### 🌍 MiniMax 兼容支持 ⭐

**2025年新增：**

现在支持使用 **MiniMax** 作为 Anthropic 兼容的后端！

**MiniMax API 特性：**
- ✅ 完全兼容 Anthropic API 格式
- ✅ 支持 Claude SDK
- ✅ 中文识别率 97-98%
- ✅ 成本仅为 Claude 的 1/10

**配置方法：**

```bash
# 设置 MiniMax 环境变量
export ANTHROPIC_BASE_URL="https://api.minimax.chat/v1/chat/completions"
export ANTHROPIC_AUTH_TOKEN="your-minimax-api-key"
export ANTHROPIC_MODEL="MiniMax-M2.1"

# 使用 Skill Seeker 的 AI 增强功能
skill-seekers enhance output/react/ --ai-mode api
```

**获取 MiniMax API Key：**

1. 访问 [MiniMax 开放平台](https://platform.minimaxi.com/)
2. 注册账号并获取 API Key
3. 推荐使用 **Coding Plan** 套餐（专为 AI 编程优化）

### 📚 文档抓取

- ✅ **llms.txt 支持** - 自动检测 LLM 优化文档（提速 10 倍）
- ✅ **通用抓取器** - 支持任何文档网站
- ✅ **智能分类** - 自动按主题组织内容
- ✅ **代码语言检测** - 支持 Python、JavaScript、C++、GDScript 等
- ✅ **8 个预设配置** - Godot、React、Vue、Django、FastAPI 等

### 🐙 GitHub 仓库分析

- ✅ **深度代码分析** - 支持 Python、JavaScript、TypeScript、Java、C++、Go 的 AST 解析
- ✅ **API 提取** - 函数、类、方法的参数和类型
- ✅ **仓库元数据** - README、文件树、语言分布、Star/Fork 数
- ✅ **Issues 和 PR** - 提取标签和里程碑信息
- ✅ **冲突检测** - 对比文档 API 与实际代码实现

### 🤖 多 LLM 平台支持

| 平台 | 格式 | 上传 | AI 增强 | API 密钥 |
|------|------|------|---------|---------|
| **Claude AI** | ZIP + YAML | ✅ 自动 | ✅ 是 | `ANTHROPIC_API_KEY` |
| **MiniMax** | 兼容 Claude | ✅ 自动 | ✅ 是 | `ANTHROPIC_AUTH_TOKEN` |
| **Google Gemini** | tar.gz | ✅ 自动 | ✅ 是 | `GOOGLE_API_KEY` |
| **OpenAI ChatGPT** | ZIP + Vector Store | ✅ 自动 | ✅ 是 | `OPENAI_API_KEY` |
| **通用 Markdown** | ZIP | ❌ 手动 | ❌ 否 | 无 |

---

## 🚀 快速开始

### 1. 安装

```bash
# 使用 uv 安装（推荐）
cd Skill_Seekers
uv sync

# 激活虚拟环境
source .venv/bin/activate

# 或使用 pip
pip install -e .
```

### 2. 基本用法

```bash
# 抓取文档网站
skill-seekers scrape --config configs/react.json

# PDF 提取（使用 PaddleOCR）
skill-seekers pdf --pdf docs/manual.pdf --name myskill --ocr --ocr-engine paddle

# GitHub 仓库分析
skill-seekers github --repo facebook/react

# AI 增强
skill-seekers enhance output/react/

# 打包技能
skill-seekers package output/react/
```

### 3. 一键安装工作流

```bash
# 设置 API key
export ANTHROPIC_API_KEY=sk-ant-your-key

# 一键完成所有步骤
skill-seekers install --config react
```

---

## 📖 使用示例

### 示例 1：中文 PDF 文档 OCR

```bash
# 扫描版中文 PDF 使用 PaddleOCR
skill-seekers pdf --pdf 中文技术文档.pdf \
  --name tech_docs \
  --ocr \
  --ocr-engine paddle \
  --paddle-lang ch
```

### 示例 2：MiniMax 作为后端

```bash
# 配置 MiniMax
export ANTHROPIC_BASE_URL="https://api.minimax.chat/v1/chat/completions"
export ANTHROPIC_AUTH_TOKEN="sb-your-minimax-key"
export ANTHROPIC_MODEL="MiniMax-M2.1"

# 使用 MiniMax 进行 AI 增强
skill-seekers enhance output/react/ --ai-mode api
```

### 示例 3：统一多源抓取

```bash
# 抓取文档 + GitHub + PDF
skill-seekers unified --config configs/react_unified.json
```

---

## 📦 依赖管理

使用 `uv` 管理 Python 依赖：

```bash
# 添加新依赖
uv add paddleocr

# 开发依赖
uv add --dev pytest

# 同步依赖
uv sync

# 导出 requirements.txt
uv export -o requirements.txt
```

**核心依赖：**
- `paddleocr>=2.7.0` - 中文 OCR 引擎
- `paddlepaddle>=3.2.0` - PaddlePaddle 后端
- `PyMuPDF>=1.24.14` - PDF 处理
- `anthropic>=0.76.0` - Claude API
- `pytesseract>=0.3.13` - Tesseract OCR（备用）

---

## 🛠️ 开发指南

### 本地开发

```bash
# 克隆项目
git clone https://github.com/zhangyang-crazy-one/Skill_Seekers.git
cd Skill_Seekers

# 创建虚拟环境
uv venv .venv
source .venv/bin/activate

# 安装依赖
uv sync

# 运行测试
pytest tests/

# 开发模式运行
python -m src.skill_seekers.cli.main scrape --config configs/react.json
```

### 添加新功能

1. Fork 项目
2. 创建功能分支：`git checkout -b feature/your-feature`
3. 提交更改：`git commit -m "feat: 添加新功能"`
4. 推送到分支：`git push origin feature/your-feature`
5. 创建 Pull Request

---

## 📊 性能对比

### OCR 引擎对比

| 引擎 | 中文识别率 | 英文识别率 | 模型大小 | 处理速度 |
|------|-----------|-----------|----------|----------|
| **PaddleOCR Mobile** | 86.05% | 优秀 | 16 MB | 21ms/图 |
| **PaddleOCR Server** | 90.13% | 优秀 | 81 MB | 31ms/图 |
| **Tesseract** | ~85% | 优秀 | 20 MB | 50-100ms/图 |

### LLM 成本对比

| 模型 | 输入价格 | 输出价格 | 相对成本 |
|------|----------|----------|----------|
| Claude Sonnet 4 | $3.00/百万 token | $15.00/百万 token | 100% |
| **MiniMax-M2.1** | **$0.30/百万 token** | **$1.20/百万 token** | **10%** |

---

## 📝 更新日志

### v2.8.0（2025年1月）

**✨ 新增功能：**
- ✅ PaddleOCR 支持，中文 OCR 识别率提升至 86.05%
- ✅ MiniMax Anthropic 兼容支持
- ✅ 新增 `--ocr-engine` 和 `--paddle-lang` 命令行参数
- ✅ 支持 6 种语言：简体中文、英文、繁体中文、韩文、日文、拉丁语系

**🔧 优化：**
- 使用 uv 管理依赖
- PDF 解析性能优化
- 统一的 OCR 引擎接口

---

## 🤝 贡献指南

欢迎贡献代码！请查看：

- [贡献指南](CONTRIBUTING.md)
- [开发路线图](ROADMAP.md)
- [项目看板](https://github.com/users/yusufkaraaslan/projects/2)

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

- [PaddlePaddle](https://github.com/PaddlePaddle/PaddleOCR) - 强大的 OCR 引擎
- [MiniMax](https://platform.minimaxi.com/) - Anthropic 兼容 API
- [Anthropic](https://www.anthropic.com/) - Claude AI
- [原项目作者](https://github.com/yusufkaraaslan/Skill_Seekers) - 优秀的开源项目

---

**⭐ 如果这个项目对你有帮助，请给个 Star 支持一下！**

---

## 📞 联系方式

- **GitHub**: https://github.com/zhangyang-crazy-one/Skill_Seekers
- **原项目**: https://github.com/yusufkaraaslan/Skill_Seekers
- **官网**: https://skillseekersweb.com/

---

**Happy Coding! 🚀**
