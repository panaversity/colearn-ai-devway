---
sidebar_position: 5
title: "Connecting MCP Servers and Common Workflows"
---

# Connecting MCP Servers and Common Workflows

## Breaking Free from the File System

You've mastered Claude Code's core features: installation, subagents for specialization, and skills for autonomous expertise. But there's a fundamental limitation we haven't addressed yet: **Claude Code can only see what's in your file system.**

What if you need Claude to:
- Check the status of GitHub issues and pull requests?
- Query your PostgreSQL database to understand data patterns?
- Read metrics from your monitoring dashboard?
- Access your company's internal API documentation?

All of this information lives **outside your local files**—in external services, databases, and APIs. Without a bridge to these systems, Claude Code operates in isolation.

**Model Context Protocol (MCP)** is that bridge. It's a standard way to connect Claude Code to external data sources, dramatically expanding what it can help you with.

In this lesson, you'll learn what MCP is, how to connect your first MCP server (GitHub), understand critical security considerations, and see four complete workflows that combine files, commands, and external integrations.

By the end, you'll understand how to integrate Claude Code into your full development ecosystem—not just your local code.

---

## What Is Model Context Protocol (MCP)?

**Definition**: Model Context Protocol (MCP) is an open standard that allows AI assistants like Claude Code to securely connect to external data sources and tools. MCP servers provide Claude Code with access to databases, APIs, monitoring systems, and third-party services.

### How MCP Works: The Architecture

**Without MCP**:
```
You ↔ Claude Code ↔ Local Files Only
```

**With MCP**:
```
You ↔ Claude Code ↔ MCP Servers ↔ External Systems
                        ↓
              [GitHub, PostgreSQL, Slack,
               Monitoring, Custom APIs, etc.]
```

**MCP Server**: A program that implements the MCP standard, providing Claude Code with specific capabilities (e.g., reading GitHub issues, querying databases, accessing Slack messages).

**MCP Connection**: A configured link between Claude Code and an MCP server, defined in your `.mcp.json` configuration file.

### MCP vs. Skills vs. Subagents

You've now learned three extension mechanisms. Here's how they differ:

| Feature | Subagent | Agent Skill | MCP Server |
|---------|----------|-------------|------------|
| **Purpose** | Specialized AI assistant | Autonomous expertise | External data access |
| **Data Source** | Local files only | Local files only | **External systems** |
| **Example** | Code reviewer with custom standards | Auto-generate docstrings | Query GitHub issues, access database |
| **Invocation** | Explicit: `claude agent run` | Autonomous discovery | Automatic when relevant |
| **Security Concern** | Low (local files) | Low (local files) | **High (external access)** |

**Key Distinction**: MCP servers give Claude Code access **beyond your local machine**, which is powerful but requires careful security evaluation.

---

## A Note on Security

**Use official Anthropic MCP servers** (GitHub, PostgreSQL, File System, Memory). They're maintained by Anthropic and safe to use.

**When creating credentials**:
- Create a read-only GitHub token (you don't need write access for learning)
- Credentials are stored securely in your system keychain, not in plain text
- You can revoke access anytime

That's it. This lesson is about learning to use MCP, not evaluating untrusted servers.

---

## Hands-On Tutorial: Connecting the GitHub MCP Server

Now that you understand the security considerations, let's connect the **official Anthropic GitHub MCP server**—a commonly useful integration for developers.

### Prerequisites

- GitHub account
- Personal Access Token (PAT) with appropriate scopes
- Claude Code installed and authenticated

### Step 1: Create a GitHub Personal Access Token

**Why**: The MCP server needs credentials to access GitHub on your behalf.

**Security**: Create a token with minimal required permissions.

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. **Token name**: "Claude Code MCP (Read-Only)"
4. **Scopes** (select only these for read-only access):
   - ✅ `repo` → `public_repo` (access public repositories)
   - ✅ `read:org` (read organization data)
   - ✅ `read:user` (read user profile)
5. Click "Generate token"
6. **Copy the token immediately**—you won't see it again

**Security Best Practice**: Do NOT select full `repo` scope (which grants write access) unless you specifically need Claude Code to create issues or PRs.

### Step 2: Add the GitHub MCP Server

Register the GitHub MCP server with Claude Code:

```bash
claude mcp add --transport http github https://api.github.com/graphql
```

**What this does**:
- Adds the official Anthropic GitHub MCP server to your Claude Code configuration
- Uses HTTP transport (the recommended, safe method)
- Names it "github" for easy reference
- Stores the configuration in your `.mcp.json` file

**Expected outcome**: MCP server registered successfully. Configuration saved to `.mcp.json`.

### Step 3: Configure Authentication with Your GitHub Token

Claude Code will automatically prompt you for the GitHub token when it first tries to use the MCP server. You can also set the token explicitly by adding an environment variable:

```bash
export GITHUB_TOKEN=your_token_here
```

Or, when Claude Code first connects, paste your token when prompted:

```
Enter your GitHub Personal Access Token:
```

**What happens**:
- Paste the token you created in Step 1
- Claude Code stores it securely in your system's credential manager:
  - **macOS**: Keychain
  - **Windows**: Credential Manager
  - **Linux**: Secret Service
- The token is never stored in plain text files

**Security**: Your token is stored securely and can be revoked anytime from GitHub's settings page.

### Step 4: Test the MCP Connection

Ask Claude Code about GitHub data. In your Claude Code session:

```
Tell me about the most recent issues in the anthropic-sdk-python repository on GitHub
```

**What happens**:
- Claude Code recognizes you're asking about GitHub data
- It invokes the GitHub MCP server automatically
- It retrieves real GitHub data and discusses it with you

**If you see GitHub data and discussion**: ✅ MCP connection successful!

**If you see an error**:
- Is your token valid? Check: https://github.com/settings/tokens
- Do you have the right scopes? Create a new read-only token if needed
- See the troubleshooting guide in the official docs

### Step 5: Explore GitHub with MCP

Now that MCP is working, try exploring other GitHub projects. Ask Claude naturally:

```
Show me the most active open-source Python projects right now
```

```
Tell me about recent activity in the pytorch repository
```

```
What are the most common issues in the React repository?
```

Claude Code will query GitHub in real-time and discuss what it finds with you. **This is the power of MCP**: you're no longer limited to local files—you're exploring the entire GitHub ecosystem through Claude Code.

---

## Your First MCP Workflow: Exploring GitHub

Now that GitHub MCP is connected, let's use it for something practical: exploring a project you're interested in.

**Try this**:

```
Ask Claude: "Using GitHub, tell me about the most active projects right now"
```

Claude will query GitHub and describe what's trending.

**Next, try this**:

```
Ask Claude: "Show me the 5 most recent commits in [a project you like]"
```

Claude will retrieve actual commit history from GitHub and summarize what changed.

**That's it.** You're now using Claude Code as a **collaborative explorer** that can see external systems in real-time. No complex workflows yet—just the ability to ask Claude questions about GitHub projects and get live answers.

---

## Comprehensive Reflection: Your Claude Code Journey

You've completed all five lessons. Take a moment to reflect on what you've learned and how it integrates into a complete mental model of Claude Code.

### Knowledge Integration

**Lesson 1: Paradigm Shift**
- Claude Code is an agentic assistant, not a passive chatbot
- Terminal integration enables direct file/command access

**Lesson 2: Installation**
- Platform-specific installation (NPM or native)
- Dual authentication paths (Claude.ai or Console API)
- Troubleshooting covers 90% of issues

**Lesson 3: Subagents**
- Specialized AI assistants with isolated context
- Explicit invocation for focused, repeatable tasks
- Consistency through custom system prompts

**Lesson 4: Agent Skills**
- Autonomous discovery and invocation
- Scales expertise across teams and projects
- Competitive advantage through domain-specific skill libraries

**Lesson 5: MCP Servers**
- External data access (GitHub, databases, APIs)
- Use official Anthropic MCP servers for safe integration
- Simple workflows connecting local work with external systems

### The Complete Claude Code Toolkit

You now have four extension mechanisms:

1. **Main Conversation**: Exploratory, flexible, one-off tasks
2. **Subagents**: Specialized, repeatable, context-isolated tasks
3. **Skills**: Autonomous expertise automatically applied
4. **MCP Servers**: External data and service integration

**Strategic Decision Framework**:

```
Need external data (GitHub, database)?
  → Use MCP Server

Have repetitive task with clear rules?
  ├─ Want automatic application → Create Agent Skill
  └─ Want explicit control → Create Subagent

Exploratory or one-off task?
  → Use main conversation
```

### Reflection Questions

**Understanding**:
- Can you explain the difference between subagents (explicit), skills (autonomous), and MCP (external data) to a colleague?
- How does MCP extend Claude Code's capabilities beyond just reading local files?

**Application**:
- What GitHub repositories would be interesting to explore using MCP?
- How could accessing external data (like GitHub) improve your development workflow?

**Integration**:
- How would you combine a subagent, a skill, and MCP in a single project?
- If your subagent needed external data, how could you use MCP to provide it?

**Practical Experience**:
- What was the difference between explicitly invoking a subagent vs. having a skill automatically discover when to help?
- How did using MCP feel different from just asking Claude Code about local files?

---

## What's Next: Beyond Claude Code

You've mastered Claude Code—a powerful terminal-based AI assistant. But the AI tool landscape is vast, and Claude Code is one of many options.

**In Chapter 6**, you'll explore **other AI development tools**:
- **Gemini CLI**: Google's terminal-based AI assistant
- **GitHub Copilot**: IDE-integrated pair programming
- **Cursor and Windsurf**: AI-first code editors

Each tool has different strengths, and choosing the right tool for your workflow matters.

**Your foundation is solid**: The concepts you've learned—agentic AI, specialization, security evaluation, workflow integration—apply across all AI development tools. You're not just learning Claude Code; you're learning **how to work effectively with AI in software development.**

---

## Resources for Learning More

For deeper exploration beyond this chapter:

- **Official Claude Code Documentation**: https://docs.claude.com/en/docs/claude-code
- **MCP Specification**: https://modelcontextprotocol.io
- **Community MCP Servers**: https://github.com/anthropics/mcp-servers
- **Claude Code Discord**: https://discord.gg/anthropic (#claude-code channel)
- **Anthropic Blog**: https://www.anthropic.com/blog (announcements and case studies)

---

## Key Takeaways

- **MCP connects Claude Code to external systems** like GitHub, enabling real-time data access beyond local files
- **Use official Anthropic MCP servers**: GitHub, PostgreSQL, File System, and Memory are maintained and trusted
- **Simple GitHub integration**: Ask Claude naturally about GitHub repositories, issues, and activity
- **MCP complements subagents and skills**: Subagents for explicit tasks, skills for autonomous expertise, MCP for external data
- **Credentials stored securely**: Your tokens are managed by your system's credential store (Keychain, Credential Manager, Secret Service)
- **Real-time exploration**: Query live GitHub data, trending projects, repository activity, all through natural language prompts
- **You now have complete toolkit**: Main conversation (exploratory), subagents (explicit tasks), skills (autonomous expertise), MCP (external data)

---

**🎉 Congratulations!** You've completed Chapter 5 and mastered Claude Code's core features. You're ready to leverage AI as an integrated development partner, not just a question-answering tool.

**Continue your journey**: Explore the supplementary resources, apply these concepts to your own projects, and see how AI-driven development transforms your workflow.