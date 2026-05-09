# git 在LLM 中配置的最佳实践指南

## Coplilot

### 规范 Git Commit Message

Copilot 可以自动生成 Git Commit Message。建议在 VS Code 配置中写入团队的 Commit Message 规范，使生成的内容符合团队标准。

```json
"github.copilot.chat.commitMessageGeneration.instructions": [
    {
        "text": "1. Use conventional commit message format(such: feat:xxxxx,docs:xxxx,chors:xxxx); 2. Be concise and clear; 3. Summarize changes made in the commit; 4.Limit to 50 characters; 5. only english is allowed"
    }
]
```
