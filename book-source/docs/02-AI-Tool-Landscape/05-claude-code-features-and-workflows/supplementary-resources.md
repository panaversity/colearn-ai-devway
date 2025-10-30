---
sidebar_position: 6
title: "Supplementary Resources"
---

# Supplementary Resources for Claude Code

This page provides curated resources for deepening your understanding of Claude Code, MCP servers, and AI-assisted development workflows.

## Official Documentation

### Claude Code Documentation
- **Quick Start Guide**: [https://docs.claude.com/en/docs/claude-code/quick-start](https://docs.claude.com/en/docs/claude-code/quick-start)
  - Installation instructions (all platforms)
  - Authentication setup
  - First-run verification

- **Subagents Documentation**: [https://docs.claude.com/en/docs/claude-code/subagents](https://docs.claude.com/en/docs/claude-code/subagents)
  - Creating custom subagents
  - System prompt best practices
  - Subagent management

- **Agent Skills Documentation**: [https://docs.claude.com/en/docs/claude-code/skills](https://docs.claude.com/en/docs/claude-code/skills)
  - SKILL.md structure and format
  - Writing discoverable descriptions
  - Skill library organization

- **MCP Integration**: [https://docs.claude.com/en/docs/claude-code/mcp](https://docs.claude.com/en/docs/claude-code/mcp)
  - Connecting MCP servers
  - Security best practices
  - Troubleshooting MCP connections

### Model Context Protocol (MCP)
- **Official MCP Website**: [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)
  - Protocol specification
  - Available MCP servers registry
  - Developer guides for building custom MCPs

- **MCP GitHub Repository**: [https://github.com/anthropics/mcp](https://github.com/anthropics/mcp)
  - Source code and examples
  - Community-contributed servers
  - Issues and discussions

## Community Resources

### GitHub Repositories
- **Claude Code Examples**: [https://github.com/anthropics/claude-code-examples](https://github.com/anthropics/claude-code-examples)
  - Subagent templates
  - Skill examples
  - Workflow demos

- **MCP Server Collection**: [https://github.com/anthropics/mcp-servers](https://github.com/anthropics/mcp-servers)
  - Official MCP servers (GitHub, PostgreSQL, File System, etc.)
  - Installation guides
  - Security audit reports

### Community Forums and Support
- **Claude Code Discord**: [https://discord.gg/anthropic](https://discord.gg/anthropic)
  - `#claude-code` channel for questions and discussions
  - Community-shared subagents and skills
  - Troubleshooting help from experienced users

- **GitHub Discussions**: [https://github.com/anthropics/claude-code/discussions](https://github.com/anthropics/claude-code/discussions)
  - Feature requests
  - Best practices discussions
  - Workflow sharing

## Related Reading

### AI-Assisted Development
- **"The AI-First Developer"** by Anthropic Engineering Team
  - Available at: https://www.anthropic.com/research/ai-first-development
  - Explores paradigm shifts in software development with AI
  - Case studies from teams using Claude Code

- **"Prompt Engineering for Developers"** by OpenAI
  - Available at: https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/
  - While focused on ChatGPT, principles apply to Claude Code
  - Free course with practical exercises

### Security and Best Practices
- **"Securing AI Assistants in Development Environments"**
  - Published by OWASP (Open Web Application Security Project)
  - Available at: https://owasp.org/www-project-ai-security/
  - Security considerations for AI tools with code access

- **"API Key Management Best Practices"** by Anthropic Security Team
  - Available at: https://docs.anthropic.com/en/docs/security/api-key-management
  - How to safely store and rotate API keys
  - Scope limiting strategies

## Video Tutorials (When Available)

**Note**: As of January 2025, official video tutorials for Claude Code are limited. Check the official documentation for updates.

### Recommended YouTube Channels (General AI Coding Assistance)
- **Anthropic Official Channel**: [https://www.youtube.com/@anthropic-ai](https://www.youtube.com/@anthropic-ai)
  - Product announcements
  - Feature deep-dives
  - Developer interviews

- **AI-Driven Development Tutorials**: Search for "Claude Code tutorial" on YouTube
  - Community-created walkthroughs
  - Workflow demonstrations
  - Troubleshooting guides

## Hands-On Practice Projects

### Beginner Projects (After Completing Chapter 5)
1. **Personal Code Reviewer**
   - Create a subagent that reviews your code for common issues
   - Practice: Customize system prompt for your preferred language/framework

2. **Documentation Generator Skill**
   - Build an Agent Skill that generates API documentation
   - Practice: Write discoverable descriptions for autonomous invocation

3. **GitHub Issue Tracker**
   - Connect GitHub MCP and create a workflow for issue management
   - Practice: Query issues, filter by labels, create issue summaries

### Intermediate Projects (After Mastery)
1. **Multi-MCP Debugging Workflow**
   - Combine GitHub, File System, and Database MCPs
   - Practice: Systematic root cause analysis using multiple data sources

2. **Team Skill Library**
   - Create 5-10 domain-specific skills for your team
   - Practice: Version control, skill sharing, discovery optimization

3. **Custom Subagent Ecosystem**
   - Build specialized subagents for common tasks (reviews, testing, refactoring)
   - Practice: Context management, subagent orchestration

## Staying Updated

### Official Channels
- **Anthropic Blog**: [https://www.anthropic.com/blog](https://www.anthropic.com/blog)
  - Product announcements
  - Feature releases
  - Case studies

- **Claude Code Release Notes**: [https://docs.claude.com/en/docs/claude-code/release-notes](https://docs.claude.com/en/docs/claude-code/release-notes)
  - Version updates
  - New features
  - Breaking changes

### Twitter/X Accounts to Follow
- **@AnthropicAI**: Official Anthropic account
- **@ClaudeAI**: Claude-specific updates
- Search hashtag: `#ClaudeCode` for community discussions

## Troubleshooting Resources

### Common Issues Database
- **Claude Code GitHub Issues**: [https://github.com/anthropics/claude-code/issues](https://github.com/anthropics/claude-code/issues)
  - Search existing issues before opening new ones
  - Community solutions and workarounds
  - Official team responses

### Platform-Specific Guides
- **Windows WSL Guide**: [https://docs.claude.com/en/docs/claude-code/platforms/windows-wsl](https://docs.claude.com/en/docs/claude-code/platforms/windows-wsl)
  - WSL-specific installation
  - Common WSL issues

- **macOS M1/M2/M3 Guide**: [https://docs.claude.com/en/docs/claude-code/platforms/macos-apple-silicon](https://docs.claude.com/en/docs/claude-code/platforms/macos-apple-silicon)
  - Apple Silicon-specific installation
  - Rosetta 2 considerations

## Advanced Topics (Beyond This Chapter)

For readers who want to go deeper:

### MCP Server Development
- **Building Custom MCP Servers**: [https://docs.claude.com/en/docs/mcp/building-servers](https://docs.claude.com/en/docs/mcp/building-servers)
  - MCP protocol implementation
  - Server registration
  - Security considerations

### Claude Code API Integration
- **Programmatic Claude Code Usage**: [https://docs.claude.com/en/docs/claude-code/api](https://docs.claude.com/en/docs/claude-code/api)
  - Using Claude Code in CI/CD pipelines
  - Automated code reviews
  - Batch processing

### Enterprise Deployment
- **Claude Code for Teams**: [https://www.anthropic.com/claude-code-enterprise](https://www.anthropic.com/claude-code-enterprise)
  - Team license management
  - Centralized skill libraries
  - Usage analytics

---

## How to Use These Resources

**If you're just starting**: Focus on the **Official Documentation** section and complete the **Beginner Projects**.

**If you're stuck on something specific**: Check **Troubleshooting Resources** and **Community Forums**.

**If you want to go deeper**: Explore **Advanced Topics** and **Intermediate Projects**.

**If you want to stay current**: Bookmark **Staying Updated** channels and check monthly.

---

**Contribution**: Found a great resource not listed here? Submit a pull request to add it! All resources should be:
- Publicly accessible (no paywalls)
- Relevant to Claude Code specifically
- Maintained and current (updated within 6 months)

---

**Next Steps**: Return to [Chapter 5 Overview](./README.md) or proceed to **Chapter 6: AI-Driven Development Methodology** to learn systematic AI collaboration patterns.
