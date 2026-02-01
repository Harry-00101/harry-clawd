# 飞书 (Feishu) + Clawdbot 集成研究
**Date:** 2026-02-01 15:04 UTC
**Project:** feishu-openclaw, openclaw-feishu

---

## 🎯 概述

**Clawdbot 原生支持 Telegram、Discord、Signal 等渠道，但国内用户最常用的办公工具是飞书。这个桥接器补上了这块拼图。**

### 两种接入方式

| 方式 | 说明 | 推荐 |
|------|------|------|
| **插件模式** (openclaw-feishu) | 内置在 Gateway 中，1个进程 | 日常使用 |
| **桥接模式** (feishu-openclaw) | 独立进程，2个进程 | 生产环境/隔离部署 |

---

## 🏗️ 架构原理

```
飞书用户 ←→ 飞书云端 ←→ 桥接脚本（本地） ←→ Clawdbot Gateway ←→ AI 模型
                     ↓
              WebSocket 长连接
              (不需要公网IP/域名)
```

### 通俗解释

1. **飞书端**：创建"自建应用"机器人，获取 App ID + App Secret
2. **桥接脚本**：本地运行，用 WebSocket 长连接接收消息
3. **Clawdbot**：通过本地 WebSocket 转发消息，调用 AI 生成回复

### 优势

| ✅ 优点 | 说明 |
|--------|------|
| 不需要公网 IP | 直接连接飞书云端 |
| 不需要域名 | 无需 HTTPS 证书 |
| 不需要 ngrok/frp | 内网穿透不需要 |
| 像微信一样 | 客户端主动连接，消息推过来 |

---

## 📦 安装方式

### 方式一：一键安装插件
```bash
# 通过 Clawdbot 安装
openclaw-feishu
```

### 方式二：npm 命令
```bash
clawdbot plugins install feishu-openclaw
npm
```

### 方式三：独立桥接脚本
```bash
cd feishu-bridge
npm install
FEISHU_APP_ID=cli_xxxxx node bridge.mjs
```

---

## 🔧 配置步骤

### 第一步：创建飞书机器人

1. 开放平台](https打开 [飞书://open.feishu.cn/)
2. 创建自建应用（如 "My AI Assistant"）
3. 添加机器人能力
4. 开通权限：
   - `im:message` - 获取与发送单聊、群聊消息
   - `im:message.group_at_msg` - 接收群聊中 @ 机器人的消息
   - `im:message.p2p_msg` - 接收机器人单聊消息
5. 配置事件回调：
   - 添加事件：`im.message.receive_v1`
   - 使用长连接接收事件 ✅ 关键！

### 第二步：配置凭证

```bash
# 创建 secrets 目录
mkdir -p ~/.clawdbot/secrets

# 保存 App Secret
echo "你的AppSecret" > ~/.clawdbot/secrets/feishu_app_secret
chmod 600 ~/.clawdbot/secrets/feishu_app_secret
```

### 第三步：测试运行

```bash
FEISHU_APP_ID=cli_xxxxx node bridge.mjs
```

### 第四步：设置开机自启（macOS）

```bash
node setup-service.mjs
launchctl load ~/Library/LaunchAgents/com.clawdbot.feishu-bridge.plist
```

---

## ⚙️ 配置参数

### 桥接器配置

```yaml
channels:
  feishu:
    enabled: true
    appId: "cli_xxxxx"
    appSecret: "secret"
    
    # 域名: "feishu" (国内) 或 "lark" (国际)
    domain: "feishu"
    
    # 连接模式: "websocket" (推荐) 或 "webhook"
    connectionMode: "websocket"
    
    # 私聊策略: "pairing" | "open" | "allowlist"
    dmPolicy: "pairing"
    
    # 群聊策略: "open" | "allowlist" | "disabled"
    groupPolicy: "allowlist"
    
    # 群聊是否需要 @机器人
    requireMention: true
    
    # 媒体文件最大大小 (MB)
    mediaMaxMb: 30
    
    # 回复渲染模式: "auto" | "raw" | "card"
    renderMode: "auto"
```

### 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `FEISHU_APP_ID` | 飞书应用 ID | 必填 |
| `FEISHU_APP_SECRET` | 飞书应用密钥 | 必填 |
| `FEISHU_APP_SECRET_PATH` | Secret 文件路径 | `~/.clawdbot/secrets/feishu_app_secret` |
| `CLAWDBOT_CONFIG_PATH` | Clawdbot 配置文件 | `~/.clawdbot/clawdbot.json` |
| `CLAWDBOT_AGENT_ID` | 使用的 Agent ID | `main` |

---

## 💬 群聊行为

### 智能回复策略

默认"低打扰"模式，只在以下情况回复：

| 触发条件 | 示例 |
|----------|------|
| 被 @ | `@机器人` |
| 问号结尾 | `？` 或 `?` |
| 请求类动词 | 帮、请、分析、总结、写 |
| 名字呼唤 | `bot`、`助手` |

### "正在思考..." 提示

- AI 回复超过 2.5 秒时自动发送
- 回复生成后自动替换成完整内容

---

## 🔄 插件 vs 桥接对比

| | 插件 | 桥接 |
|--|------|------|
| **进程数** | 1 个（内置 Gateway） | 2 个（独立） |
| **崩溃影响** | 影响 Gateway | 互不影响 |
| **适合** | 日常使用 | 生产环境/隔离部署 |
| **推荐** | 日常用插件 | 生产用桥接 |

---

## 🛡️ 保活机制 (macOS)

通过 `launchd` 系统服务管理器：

```bash
# 开机自动启动
# 崩溃自动重启
# 日志自动写入文件
```

### 查看状态

```bash
launchctl list | grep feishu
```

### 停止服务

```bash
launchctl unload ~/Library/LaunchAgents/com.clawdbot.feishu-bridge.plist
```

---

## 📁 文件结构

```
feishu-bridge/
├── bridge.mjs           # 核心桥接脚本 (~200行)
├── setup-service.mjs    # 自动生成 launchd 保活配置
├── package.json         # 依赖声明
└── README.md            # 文档
```

### 日志位置

```
~/.clawdbot/logs/feishu-bridge.out.log  # 正常输出
~/.clawdbot/logs/feishu-bridge.err.log  # 错误日志
```

---

## 🆚 Harry-001 集成方案

### 当前状态

| 渠道 | 状态 |
|------|------|
| Telegram | ✅ 已集成 |
| Discord | ✅ 已集成 |
| 飞书 (Feishu) | ❌ 未集成 |

### 集成方案

#### 方案一：使用插件（推荐日常）

```bash
# 安装插件
clawdbot plugins install openclaw-feishu

# 重启 Gateway
clawdbot gateway restart
```

#### 方案二：使用桥接脚本（生产环境）

```bash
# 下载桥接脚本
git clone https://github.com/AlexAnys/feishu-openclaw.git
cd feishu-openclaw

# 配置凭证
export FEISHU_APP_ID=cli_xxxxx

# 运行
node bridge.mjs
```

---

## 🎯 集成优势

| 优势 | 说明 |
|------|------|
| **国内办公生态** | 飞书是主流办公工具 |
| **团队协作** | 群聊中 @机器人使用 |
| **无需公网** | WebSocket 长连接 |
| **低打扰模式** | 智能回复，不刷屏 |
| **保活机制** | 崩溃自动重启 |

---

## 📚 资源链接

| 资源 | 链接 |
|------|------|
| **桥接脚本** | https://github.com/AlexAnys/feishu-openclaw |
| **插件** | openclaw-feishu |
| **飞书开放平台** | https://open.feishu.cn/ |
| **教程** | https://cloud.tencent.com/developer/article/2625073 |
| **讨论** | https://github.com/moltbot/moltbot/discussions/2632 |

---

## 🎯 下一步

1. [ ] 创建飞书应用
2. [ ] 获取 App ID + App Secret
3. [ ] 安装 feishu-openclaw 插件/桥接
4. [ ] 配置群聊策略
5. [ ] 测试群聊互动
6. [ ] 设置开机自启

---

*研究完成！飞书集成让 Harry-001 进入国内办公生态！*
