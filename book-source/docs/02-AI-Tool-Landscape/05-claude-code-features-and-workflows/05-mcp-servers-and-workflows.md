---
sidebar_position: 5
title: "Lesson 5: Connecting MCP Servers and Common Workflows"
duration: "32-39 min"
---

# Lesson 5: Connecting MCP Servers and Common Workflows

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

## 🔴 CRITICAL: MCP Server Security Considerations

**Before connecting any MCP server, read this section carefully.**

### The Security Risk

MCP servers have access to external systems—often with your credentials. A malicious or compromised MCP server could:

- ❌ Read sensitive data from your GitHub repos, databases, or APIs
- ❌ Modify or delete data (if granted write permissions)
- ❌ Exfiltrate credentials or API keys
- ❌ Execute commands on external systems with your privileges

**Unlike skills or subagents** (which only access local files you control), **MCP servers interact with external services using your authentication**.

### Evaluating MCP Server Trustworthiness

Before installing any MCP server, evaluate it systematically:

#### 1. Source and Maintainer Trust

**✅ High Trust**:
- Official Anthropic MCP servers (https://github.com/anthropics/mcp-servers)
- Major companies' official servers (GitHub, Stripe, PostgreSQL project)
- Well-known open-source projects with active maintenance

**⚠️ Medium Trust**:
- Community-maintained servers with public source code
- Servers from unknown individuals but with code review possible

**❌ Low Trust**:
- Closed-source MCP servers
- Servers from unknown sources with no code visibility
- Abandoned projects with no recent updates

#### 2. Code Review (If Open Source)

**Check the server's code**:
```bash
git clone https://github.com/[maintainer]/[mcp-server]
cd [mcp-server]
# Review what the server does
cat src/index.js  # or main.py, etc.
```

**Red flags**:
- ❌ Makes network requests to unexpected domains
- ❌ Writes files outside expected directories
- ❌ Executes system commands without clear purpose
- ❌ Obfuscated or minified code
- ❌ Requests excessive permissions

**Green flags**:
- ✅ Clear, readable code with comments
- ✅ Minimal dependencies
- ✅ Only accesses documented external services
- ✅ Active GitHub issues/PRs showing community engagement
- ✅ Security audit reports or vulnerability disclosure policy

#### 3. Permission Scoping

**Principle of Least Privilege**: Only grant the minimum permissions necessary.

**Examples**:
- ✅ GitHub MCP: Read-only access to public repos for learning (not private repos)
- ❌ Database MCP with admin credentials that can DROP tables
- ✅ Monitoring MCP with read-only API key
- ❌ API MCP with master key instead of scoped service key

**How to scope**:
1. Create limited-scope API tokens/keys for MCP servers
2. Use read-only credentials when write access isn't needed
3. Restrict access to specific repos, databases, or resources

#### 4. Environment Isolation

**Best practices**:
- ✅ Test new MCP servers in isolated development environments first
- ✅ Use separate credentials for MCP access (not your personal GitHub token)
- ✅ Monitor API usage for unexpected spikes
- ❌ Never use production database credentials in MCP configuration

### Official Trusted MCP Servers

These MCP servers are officially maintained by Anthropic and considered safe:

- **GitHub** (`@anthropic/mcp-server-github`) — Read GitHub repos, issues, PRs
- **PostgreSQL** (`@anthropic/mcp-server-postgres`) — Query PostgreSQL databases
- **File System** (`@anthropic/mcp-server-filesystem`) — Extended file operations
- **Memory** (`@anthropic/mcp-server-memory`) — Persistent knowledge graph storage

**Security Note**: Even official servers should be configured with scoped credentials (e.g., read-only GitHub tokens).

### When to Avoid MCP Servers

**Don't connect MCP servers if**:
- ❌ You can't review the source code
- ❌ The server requests permissions far beyond its stated purpose
- ❌ You're unsure what data it will access
- ❌ It's abandoned (no updates in 12+ months)
- ❌ Your company security policy prohibits external tool integrations

**Alternative**: For high-security environments, consider building internal MCP servers that you fully control and audit.

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

### Step 2: Install the GitHub MCP Server

Run:

```bash
claude mcp install @anthropic/mcp-server-github
```

**Expected output**:
```
Installing @anthropic/mcp-server-github...
✓ MCP server installed successfully
✓ Configuration file created: .mcp.json

Next step: Configure authentication
```

### Step 3: Configure Authentication

Claude Code will prompt you to add the GitHub token:

```bash
claude mcp config github
```

**Prompt**:
```
Enter your GitHub Personal Access Token:
```

Paste the token you created in Step 1 and press Enter.

**Expected output**:
```
✓ GitHub authentication configured
✓ Connection test successful
Ready to use GitHub MCP
```

**Security**: The token is stored securely in your system's credential manager (Keychain on macOS, Credential Manager on Windows, Secret Service on Linux).

### Step 4: Verify the Connection

Test the MCP connection:

```bash
claude "List the 5 most recent issues in the anthropics/anthropic-sdk-python repository"
```

**Expected behavior**:
- Claude Code recognizes you're asking about GitHub data
- Invokes the GitHub MCP server automatically
- Retrieves and displays the 5 most recent issues

**If you see GitHub data**: ✅ MCP connection successful!

**If you see an error**: Check:
- Is the token valid? Test at https://api.github.com/user (with `Authorization: token YOUR_TOKEN`)
- Did you grant the necessary scopes? Re-create the token if needed
- Run `claude mcp status` to see connection details

### Step 5: Explore GitHub MCP Capabilities

Try these commands to understand what the GitHub MCP can do:

```bash
# Search for issues by label
claude "Find open 'bug' issues in microsoft/vscode"

# Get pull request information
claude "Show details of PR #123 in facebook/react"

# Analyze repository structure
claude "What's the directory structure of pytorch/pytorch?"

# Check release information
claude "What's the latest release of rust-lang/rust?"
```

---

## Common Workflows: Putting It All Together

Now that you have Claude Code fully configured (subagents, skills, MCP), let's see four complete workflows that demonstrate real-world usage.

### Workflow 1: Systematic Codebase Exploration

**Scenario**: You're joining a new project and need to understand the codebase quickly.

**Workflow**:

```bash
# Step 1: Get repository structure
claude "Show me the main directories and their purposes in this project"

# Step 2: Identify entry points
claude "Find the main application entry point (main.py, index.js, etc.)"

# Step 3: Understand dependencies
claude "What are the key dependencies in package.json (or requirements.txt)?"

# Step 4: Check for tests
claude "Where are tests located, and what testing framework is used?"

# Step 5: Review recent changes
claude "Using GitHub MCP, what are the 10 most recent commits?"

# Step 6: Check open issues
claude "Using GitHub MCP, what critical bugs are currently open?"
```

**What this demonstrates**:
- Claude Code reads local files (Steps 1-4)
- Claude Code queries external data via MCP (Steps 5-6)
- You get a complete project overview in minutes

### Workflow 2: Issue-Driven Debugging with GitHub Integration

**Scenario**: A user reported a bug via GitHub issue. You need to understand the issue, locate relevant code, and fix it.

**Workflow**:

```bash
# Step 1: Get issue details
claude "Using GitHub MCP, show me details of issue #247 in myorg/myrepo"

# Step 2: Find related code
claude "Search the codebase for files related to [issue topic from step 1]"

# Step 3: Analyze the bug
claude "Read [relevant files] and explain what might cause [issue symptom]"

# Step 4: Create a fix with subagent
claude agent run code-reviewer "Review my proposed fix for issue #247"

# Step 5: Generate tests
claude "Create unit tests that verify issue #247 is fixed"

# Step 6: Verify fix
claude "Run the tests and confirm they pass"
```

**What this demonstrates**:
- External issue tracking integration (GitHub MCP)
- Code analysis (file reading)
- Specialized review (code-reviewer subagent)
- Test generation and execution
- Complete bug-fix workflow in one session

### Workflow 3: Database-Backed Feature Validation

**Scenario**: You're adding a new feature that queries a database. You need to understand existing data patterns and test your queries.

**Prerequisites**: PostgreSQL MCP server configured (install with `claude mcp install @anthropic/mcp-server-postgres`)

**Workflow**:

```bash
# Step 1: Understand schema
claude "Using Postgres MCP, show me the schema for the 'users' table"

# Step 2: Analyze data patterns
claude "Query the database: What's the distribution of user signups by month?"

# Step 3: Test your query
claude "I'm writing this SQL query: [paste query]. Run it against the database and show results"

# Step 4: Validate edge cases
claude "Check if there are any users with NULL email addresses"

# Step 5: Generate application code
claude "Write a Python function using SQLAlchemy to safely query users by email"

# Step 6: Security review with skill
claude "Use the sql-injection-checker skill to verify my query is safe"
```

**What this demonstrates**:
- Database integration via MCP
- Interactive query testing
- Code generation informed by real data
- Security validation via skills

### Workflow 4: Multi-System Debugging

**Scenario**: A production issue involves multiple systems—application logs, database state, and GitHub deployment history. You need to correlate information across all three.

**Prerequisites**: File system access, PostgreSQL MCP, GitHub MCP

**Workflow**:

```bash
# Step 1: Check application logs
claude "Read logs/production.log and find errors from the last hour"

# Step 2: Identify error pattern
claude "What's the most frequent error in the logs?"

# Step 3: Check database state
claude "Using Postgres MCP, query the database: Are there any locked transactions?"

# Step 4: Check recent deployments
claude "Using GitHub MCP, what commits were deployed to production today?"

# Step 5: Correlate timeline
claude "Did any of today's commits change code related to [error from step 2]?"

# Step 6: Root cause analysis
claude "Based on logs, database state, and recent commits, what's the likely root cause?"

# Step 7: Document findings
claude "Create an incident report summarizing the root cause and suggested fix"
```

**What this demonstrates**:
- Multi-source data correlation (logs, database, GitHub)
- Systematic debugging across systems
- Claude Code acts as incident investigator
- Produces actionable documentation

---

## Hands-On Exercise: Connect and Use MCP

**Exercise: Explore a Public Repository with GitHub MCP**

**Goal**: Use GitHub MCP to understand a popular open-source project.

**Steps**:

1. **Choose a repository** you're interested in (e.g., `microsoft/vscode`, `django/django`, `pytorch/pytorch`)

2. **Repository Overview**:
   ```bash
   claude "Using GitHub MCP, give me an overview of [repo-name]: description, stars, primary language, and license"
   ```

3. **Recent Activity**:
   ```bash
   claude "What are the 10 most recent commits in [repo-name]? Summarize what changed."
   ```

4. **Issue Analysis**:
   ```bash
   claude "What are the top 5 open issues by comment count in [repo-name]? What topics are most discussed?"
   ```

5. **Contributor Activity**:
   ```bash
   claude "Who are the top 5 contributors to [repo-name] by commit count?"
   ```

6. **Connect to Local Code**:
   - Clone the repository: `git clone https://github.com/[repo-name]`
   - Ask Claude to analyze it:
   ```bash
   claude "Based on the GitHub information and the local files, explain how to contribute to this project"
   ```

**💡 Learning with AI**:
- Ask Claude Code: *"What other GitHub MCP queries would help me understand this project?"*
- Experiment: *"Can you create a comparison table of issues labeled 'bug' vs 'feature'?"*
- Deepen understanding: *"Explain how the GitHub MCP works behind the scenes"*

Use Claude Code as a mentor to explore MCP capabilities, not just to complete the task.

---

## Managing MCP Connections

As you add more MCP servers, you'll need to manage them effectively.

### List Installed MCP Servers

```bash
claude mcp list
```

**Output**:
```
Installed MCP servers:
  - github (@anthropic/mcp-server-github) - Connected ✓
  - postgres (@anthropic/mcp-server-postgres) - Connected ✓
  - filesystem (@anthropic/mcp-server-filesystem) - Not configured
```

### Check MCP Status

```bash
claude mcp status github
```

**Output**:
```
GitHub MCP Server
Status: Connected
Scopes: public_repo, read:org, read:user
Last used: 5 minutes ago
Rate limit: 4,847 / 5,000 requests remaining
```

**Use case**: Monitor API rate limits to avoid throttling.

### Remove an MCP Server

```bash
claude mcp remove postgres
```

**Warning**: This removes the server configuration and stored credentials. You'll need to reconfigure if you add it again later.

### MCP Configuration File

MCP servers are configured in `.mcp.json` in your project directory:

```json
{
  "mcpServers": {
    "github": {
      "transport": "stdio",
      "command": "mcp-server-github",
      "env": {
        "GITHUB_TOKEN": "keychain:github-token"
      }
    },
    "postgres": {
      "transport": "stdio",
      "command": "mcp-server-postgres",
      "env": {
        "DATABASE_URL": "keychain:postgres-url"
      }
    }
  }
}
```

**Security Note**: Credentials are stored in your system keychain (not plain text), referenced as `keychain:[key-name]`.

---

## Troubleshooting MCP Connections

### Issue: MCP Server Not Connecting

**Symptoms**: Claude Code can't access external data; MCP commands timeout.

**Fixes**:

1. **Check credentials**: `claude mcp config [server-name]` to re-enter credentials
2. **Test manually**: Use the API directly (e.g., `curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user`)
3. **Check firewall**: Ensure your network allows connections to the external service
4. **Review logs**: `claude mcp logs [server-name]` to see error details

### Issue: Rate Limiting

**Symptoms**: MCP commands fail with "rate limit exceeded" errors.

**Fixes**:

1. **Check usage**: `claude mcp status [server-name]` to see remaining quota
2. **Wait**: Most APIs reset rate limits hourly or daily
3. **Upgrade**: Some services offer higher rate limits for paid accounts
4. **Cache**: Claude Code caches responses when possible to reduce API calls

### Issue: Unexpected Data Access

**Symptoms**: MCP server accesses data you didn't intend it to see.

**Fixes**:

1. **Review scopes**: Check what permissions your API token grants
2. **Revoke token**: Go to the service's settings and revoke the token immediately
3. **Create scoped token**: Generate a new token with narrower permissions
4. **Remove MCP server**: `claude mcp remove [server-name]` until you resolve the issue

**Security Principle**: If you're ever uncertain about what an MCP server is accessing, **remove it immediately and investigate**.

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
- Security evaluation is critical
- Complete workflows combining local and external data

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
- Can you explain the difference between subagents, skills, and MCP servers to a colleague?
- Why is MCP security evaluation critical compared to skills/subagents?

**Application**:
- Which workflows from this lesson would help your current projects?
- What domain-specific skills could your team build?

**Integration**:
- How would you combine subagents, skills, and MCP in a complete development workflow?
- What external systems would most benefit from MCP integration in your work?

**Strategic Thinking**:
- If you were leading a development team, how would you leverage Claude Code's features to create competitive advantage?
- What unique expertise could you encode as skills to scale across your organization?

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

## Supplementary Resources

For deeper exploration beyond this chapter:

- **Official Claude Code Documentation**: https://docs.claude.com/en/docs/claude-code
- **MCP Specification**: https://modelcontextprotocol.io
- **Community MCP Servers**: https://github.com/anthropics/mcp-servers
- **Claude Code Discord**: https://discord.gg/anthropic (#claude-code channel)

See the [Supplementary Resources](./supplementary-resources.md) page for a complete curated list of documentation, tutorials, community forums, and practice projects.

---

## Key Takeaways

- **MCP connects Claude Code to external systems** (GitHub, databases, APIs, monitoring)
- **Security evaluation is critical**: Review source code, scope permissions, use trusted servers
- **Official Anthropic MCP servers are trusted**: GitHub, PostgreSQL, File System, Memory
- **Four complete workflows** demonstrate combining files, commands, and external integrations
- **MCP complements skills/subagents**: Skills = internal expertise, MCP = external data
- **Configuration stored securely**: Credentials in system keychain, referenced in `.mcp.json`
- **Management commands**: List, status, config, remove MCP servers with `claude mcp`
- **You now have complete toolkit**: Main conversation, subagents, skills, MCP

---

**🎉 Congratulations!** You've completed Chapter 5 and mastered Claude Code's core features. You're ready to leverage AI as an integrated development partner, not just a question-answering tool.

**Continue your journey**: Explore the supplementary resources, apply these concepts to your own projects, and see how AI-driven development transforms your workflow.

**Up Next**: [Chapter 6 - AI-Driven Development Methodology](../../03-AIDD-in-Practice/06-aidd-methodology/README.md)
