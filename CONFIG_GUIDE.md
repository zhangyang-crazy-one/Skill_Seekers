# PaddleOCR 和 MiniMax 配置指南

本文档介绍如何在 Skill Seeker 中配置和使用 PaddleOCR 和 MiniMax。

## 目录

- [PaddleOCR 配置](#paddleocr-配置)
- [MiniMax 配置](#minimax-配置)
- [OCR 引擎对比](#ocr-引擎对比)
- [成本对比](#成本对比)

---

## PaddleOCR 配置

### 1. 安装依赖

```bash
uv add paddleocr paddlepaddle
```

或使用 pip：

```bash
pip install paddleocr paddlepaddle
```

### 2. 使用方法

#### 命令行

```bash
# 使用 PaddleOCR（推荐，中文效果更好）
skill-seekers pdf --pdf docs.pdf --ocr --ocr-engine paddle --paddle-lang ch

# 自动选择引擎（默认）
skill-seekers pdf --pdf docs.pdf --ocr --ocr-engine auto

# 使用 Tesseract（备用）
skill-seekers pdf --pdf docs.pdf --ocr --ocr-engine tesseract
```

#### 支持的语言

| 参数 | 语言 | 识别率 |
|------|------|--------|
| `ch` | 简体中文 | 86.05% |
| `en` | 英文 | 优秀 |
| `chinese_cht` | 繁体中文 | 优秀 |
| `korean` | 韩文 | 优秀 |
| `japan` | 日文 | 优秀 |
| `latin` | 拉丁语系 | 优秀 |

### 3. Python API

```python
from src.skill_seekers.cli.pdf_extractor_poc import PDFExtractor

# 创建提取器，使用 PaddleOCR
extractor = PDFExtractor(
    pdf_path='document.pdf',
    use_ocr=True,
    ocr_engine='paddle',  # 或 'auto', 'tesseract'
    paddle_lang='ch',      # 语言选择
    verbose=True
)

# 开始提取
result = extractor.extract_all()
```

---

## MiniMax 配置

### 1. 什么是 MiniMax？

MiniMax 是一个提供 Anthropic 兼容 API 的服务，可以使用 Claude SDK 调用 MiniMax 的模型。

**优势：**
- ✅ 完全兼容 Anthropic API 格式
- ✅ 支持 Claude SDK
- ✅ 中文识别率 97-98%
- ✅ 成本仅为 Claude 的 1/10

### 2. 获取 API Key

1. 访问 [MiniMax 开放平台](https://platform.minimaxi.com/)
2. 注册账号
3. 创建 API Key（推荐使用 Coding Plan 套餐）

### 3. 配置环境变量

#### Linux/macOS

```bash
# 临时设置（当前终端）
export ANTHROPIC_BASE_URL="https://api.minimax.chat/v1/chat/completions"
export ANTHROPIC_AUTH_TOKEN="your-minimax-api-key"
export ANTHROPIC_MODEL="MiniMax-M2.1"
```

#### 永久设置

```bash
# 添加到 ~/.bashrc 或 ~/.zshrc
echo 'export ANTHROPIC_BASE_URL="https://api.minimax.chat/v1/chat/completions"' >> ~/.bashrc
echo 'export ANTHROPIC_AUTH_TOKEN="your-minimax-api-key"' >> ~/.bashrc
echo 'export ANTHROPIC_MODEL="MiniMax-M2.1"' >> ~/.bashrc

# 生效
source ~/.bashrc
```

#### Windows

```cmd
# CMD
set ANTHROPIC_BASE_URL=https://api.minimax.chat/v1/chat/completions
set ANTHROPIC_AUTH_TOKEN=your-minimax-api-key
set ANTHROPIC_MODEL=MiniMax-M2.1

# PowerShell
$env:ANTHROPIC_BASE_URL="https://api.minimax.chat/v1/chat/completions"
$env:ANTHROPIC_AUTH_TOKEN="your-minimax-api-key"
$env:ANTHROPIC_MODEL="MiniMax-M2.1"
```

### 4. 在 Skill Seeker 中使用

```bash
# 使用 MiniMax 进行 AI 增强
skill-seekers enhance output/react/ --ai-mode api

# 或使用 Claude Code 本地模式
skill-seekers enhance output/react/ --ai-mode local
```

### 5. Python 示例

```python
import anthropic

# 配置 MiniMax
client = anthropic.Anthropic(
    api_key="your-minimax-api-key",
    base_url="https://api.minimax.chat/v1/chat/completions"
)

# 调用 API（与 Anthropic 完全一致）
message = client.messages.create(
    model="MiniMax-M2.1",
    max_tokens=4096,
    temperature=0.3,
    messages=[
        {
            "role": "user",
            "content": "请帮我增强这段文档..."
        }
    ]
)

print(message.content)
```

---

## OCR 引擎对比

### 性能对比

| 指标 | PaddleOCR Mobile | PaddleOCR Server | Tesseract |
|------|-----------------|-----------------|-----------|
| **中文印刷识别率** | 86.05% | 90.13% | ~85% |
| **中文手写识别率** | 41.66% | 58.07% | ~20% |
| **模型大小** | 16 MB | 81 MB | 20 MB |
| **处理速度** | 21ms/图 | 31ms/图 | 50-100ms/图 |
| **安装复杂度** | 简单 | 简单 | 复杂 |

### 推荐场景

| 场景 | 推荐引擎 | 原因 |
|------|----------|------|
| **中文扫描文档** | PaddleOCR | 识别率最高 |
| **英文扫描文档** | PaddleOCR 或 Tesseract | 效果相近 |
| **轻量级部署** | PaddleOCR Mobile | 模型最小 |
| **高精度需求** | PaddleOCR Server | 识别率最高 |
| **无网络环境** | Tesseract | 无需下载模型 |

---

## 成本对比

### LLM API 成本

| 模型 | 输入价格 | 输出价格 | 相对成本 |
|------|----------|----------|----------|
| Claude Sonnet 4 | $3.00/百万 token | $15.00/百万 token | 100% |
| Claude Haiku 3.5 | $0.25/百万 token | $1.25/百万 token | 8% |
| **MiniMax-M2.1** | **$0.30/百万 token** | **$1.20/百万 token** | **10%** |

### 成本节省示例

假设每月处理 1000 万 token：

| 后端 | 月成本 | 年成本 | 节省 |
|------|--------|--------|------|
| Claude | $1,500 | $18,000 | - |
| **MiniMax** | **$150** | **$1,800** | **90%** |

---

## 故障排除

### PaddleOCR 问题

**问题：模型下载失败**

```bash
# 设置代理
export HTTPS_PROXY="http://your-proxy:port"

# 或使用国内镜像
pip install paddlepaddle -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install paddleocr -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**问题：内存不足**

```bash
# 使用轻量级模型
skill-seekers pdf --pdf doc.pdf --ocr --ocr-engine paddle
```

### MiniMax 问题

**问题：认证失败**

```bash
# 检查 API Key
echo $ANTHROPIC_AUTH_TOKEN

# 重新设置
export ANTHROPIC_AUTH_TOKEN="your-correct-api-key"
```

**问题：速率限制**

```bash
# 检查限流
curl -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
  https://api.minimax.chat/v1/chat/completions \
  -d '{"model":"MiniMax-M2.1","messages":[{"role":"user","content":"test"}]}'
```

---

## 相关链接

- [PaddleOCR 官方文档](https://paddlepaddle.github.io/PaddleOCR/main/en/)
- [MiniMax 开放平台](https://platform.minimaxi.com/)
- [Skill Seeker GitHub](https://github.com/zhangyang-crazy-one/Skill_Seekers)
- [原项目 GitHub](https://github.com/yusufkaraaslan/Skill_Seekers)

---

**最后更新：2025年1月21日**
