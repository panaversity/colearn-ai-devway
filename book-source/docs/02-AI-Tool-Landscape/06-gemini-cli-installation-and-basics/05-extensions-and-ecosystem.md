---
title: "When Your AI Needs More: Extensions for Real Business Tasks"
chapter: 2
lesson: 5
estimated_time: "25 minutes"
learning_objectives:
  - "Recognize when built-in tools aren't enough for your business task"
  - "Install and use MCP servers to extend AI capabilities (web research, live documentation)"
  - "Apply extensions to real business workflows (competitive research, staying current)"
  - "Understand security considerations when giving AI access to external systems"
  - "Consolidate your learning and identify next steps in your AI journey"
sidebar_position: 5
---

## The Moment You Hit a Wall

You've been using Gemini CLI for your business tasks. It's helped you analyze sales reports, research competitors, review customer feedback. But now you need something it can't do out of the box.

**Example scenarios:**
- You want your AI to browse live competitor websites and extract current pricing (not just fetch a single page)
- You need to stay current with constantly changing business tools (Stripe API updates, Shopify features, industry regulations)
- You want to monitor real-time data (stock prices, social media trends, breaking news in your industry)
- You need to connect to your business systems (CRM, project management, databases)

This is when **extensions** become essential.

But here's the key: **You don't learn to build extensions. You learn to use pre-built ones.**

This lesson shows you how to extend Gemini CLI with two powerful capabilities:
1. **Playwright MCP**: Your AI can browse websites like a human (for competitive research)
2. **Context7 MCP**: Your AI accesses the latest documentation (for staying current)

By the end, you'll understand when you need extensions, how to install them safely, and how to use them for real business value.

---

## What Are Extensions? (The Business Explanation)

An **extension** is a capability you add to Gemini CLI that lets your AI do things it couldn't before.

Think of it like apps on your phone:
- **Built-in apps** (camera, messages): Work out of the box
- **Downloaded apps** (Uber, Slack): You install them when you need specific features

**Gemini CLI works the same way:**
- **Built-in tools** (file reading, web fetching, search): Already covered in Lesson 3
- **Extensions** (web browsing, live docs, database connectors): You add them when needed

### What Is MCP? (Model Context Protocol)

**MCP** is the technology that lets your AI safely connect to external systems.

**Simple explanation:**
- Your AI lives on your computer (local)
- The data you need lives elsewhere (external): websites, databases, APIs, documentation sites
- **MCP servers** are bridges that safely connect your AI to that external data

**Without MCP:**
```
You → Gemini CLI → Your local files only
```

**With MCP:**
```
You → Gemini CLI → MCP Servers → External systems
                         ↓
              [Websites, Live Docs, Databases, APIs]
```

**Key insight**: MCP servers give your AI access **beyond your computer**, which is powerful but requires careful security evaluation.

---

## Security First: What You Must Know

Before we install anything, understand the risks and how to stay safe.

### The Risk

When you install an MCP server, you're giving your AI permission to access external systems. This means:
- ⚠️ Your AI can browse websites (could visit malicious sites if prompted carelessly)
- ⚠️ Your AI can query databases (could expose sensitive data)
- ⚠️ Your AI can access APIs (could rack up costs or leak credentials)

### How to Stay Safe

**1. Only install trusted MCP servers**

In this lesson, we use two widely trusted servers:
- ✅ **Playwright MCP**: Official, maintained by Microsoft/Playwright team
- ✅ **Context7 MCP**: Maintained by Upstash (reputable company)

**2. Understand what you're installing**

Before installing any MCP server, ask:
- Who built this? (Individual developer? Reputable company? Open source community?)
- What access does it need? (Read-only web access? Database write access?)
- Is it actively maintained? (Recent updates? Active community?)

**3. Test with non-sensitive data first**

When trying a new MCP server:
- ✅ Test on public websites first (not your company's internal systems)
- ✅ Use test credentials (not your production API keys)
- ✅ Start with read-only tasks (not data modification)

**4. Know what NOT to share**

Never give MCP servers access to:
- 🚫 Bank accounts or financial credentials
- 🚫 Company databases with customer data (unless explicitly authorized)
- 🚫 Private emails or internal communications
- 🚫 Production API keys or passwords

**Rule of thumb**: If you wouldn't share it with a contractor, don't give an MCP server access to it.

---

## Extension 1: Playwright MCP — Browse the Web Like a Human

### What It Does

**Playwright MCP** lets your AI actively browse websites, click links, fill forms, and extract information—just like you would in a web browser.

**Business use cases:**
- Competitive research: Browse competitor websites to compare features, pricing, offerings
- Market research: Extract product details from e-commerce sites
- Price monitoring: Check competitor pricing across multiple pages
- Job research: Browse job boards to understand market salary ranges

### The Difference from Web Fetching (Lesson 3)

**Web Fetching** (built-in tool from Lesson 3):
- Reads one specific page
- Gets HTML content
- Like taking a snapshot

**Playwright MCP** (extension):
- Browses multiple pages
- Clicks buttons, follows links
- Fills out forms
- Like having a human browse for you

**Example:**
- Web Fetching: "Read the Stripe pricing page"
- Playwright: "Browse Stripe's website, click through all pricing tiers, and create a comparison table"

### How to Install Playwright MCP

**Step 1: Install the extension**

Open your terminal and run:

```bash
gemini extensions install https://github.com/gemini-cli-extensions/playwright-mcp
```

**What happens:**
- Gemini downloads the Playwright extension
- Installs necessary dependencies
- Makes it available for your conversations

**Step 2: Verify installation**

```bash
gemini extensions list
```

You should see `playwright-mcp` in the list.

### Business Workflow 1: Competitive Pricing Research

**Your goal**: You're launching a new product. You need to understand how 3 competitors price similar offerings.

**Traditional approach:**
1. Visit competitor A website
2. Navigate to pricing page
3. Take notes
4. Repeat for competitors B and C
5. Manually create comparison
6. Time: 1-2 hours

**With Playwright MCP:**

Open Gemini CLI and say:

```
Use Playwright to browse these three competitor websites:
1. [Competitor A URL]
2. [Competitor B URL]
3. [Competitor C URL]

For each, find their pricing page, extract:
- Pricing tiers (Basic, Pro, Enterprise, etc.)
- Monthly cost for each tier
- Key features included
- Any discounts or special offers

Create a comparison table showing all three side-by-side.
```

**What Gemini does:**
1. Launches Playwright browser
2. Visits first competitor site
3. Navigates to pricing page
4. Extracts relevant information
5. Repeats for other competitors
6. Creates comparison table

**Time: 5-10 minutes**

**Example output:**
```
Competitor Pricing Comparison

| Feature          | Competitor A | Competitor B | Competitor C |
|------------------|--------------|--------------|--------------|
| Basic Tier       | $29/month    | $25/month    | Free         |
| Pro Tier         | $99/month    | $89/month    | $79/month    |
| Enterprise       | Custom       | $299/month   | Custom       |
| Key Differentiator | Analytics | Support     | Integrations |
```

### Business Workflow 2: Product Research

**Your goal**: You're considering adding a new feature. You want to see how competitors implement it.

**Prompt:**
```
Use Playwright to visit [Competitor Website]. Browse their product features page,
click on [Specific Feature], and summarize:
- How they describe this feature
- What benefits they highlight
- What use cases they show
- How prominently they feature it (main page vs. buried?)
```

**What you learn:**
- How competitors position the feature
- What language resonates with customers
- How to differentiate your offering

### When Playwright MCP Is Useful

**✅ Use Playwright when:**
- You need to browse multiple pages on a site
- Information requires clicking/navigating (pricing calculators, feature pages)
- You're doing ongoing competitor monitoring (monthly pricing checks)
- You need to extract data from multiple similar pages

**❌ Don't use Playwright when:**
- Simple one-page fetch works (use built-in web fetching instead)
- Site blocks automated browsing (some sites detect bots)
- You're accessing sensitive/private data (security risk)

---

## Extension 2: Context7 MCP — Stay Current with Latest Documentation

### What It Does

**Context7 MCP** gives your AI access to constantly updated documentation for popular tools, libraries, and platforms.

**Business use cases:**
- Learning new tools: Get latest docs for Stripe, Shopify, QuickBooks APIs
- Staying current: Understand recent changes to platforms you use
- Quick reference: Get answers without hunting through documentation
- Onboarding: Help new team members understand your tech stack

### The Difference from Web Fetching

**Web Fetching** (built-in):
- You need to know the documentation URL
- Fetches what's on the page right now
- Manual process each time

**Context7 MCP** (extension):
- Knows where to find docs automatically
- Indexes documentation for fast searches
- Stays updated with latest changes
- One command gets you current information

### How to Install Context7 MCP

**Step 1: Install the extension**

```bash
gemini extensions install https://github.com/gemini-cli-extensions/context7-mcp
```

**Step 2: Verify installation**

```bash
gemini extensions list
```

You should see `context7-mcp` in the list.

### Business Workflow 3: Understanding API Changes

**Your goal**: Your team uses Stripe for payments. They announced API changes. You need to understand what changed and if it affects you.

**Prompt:**
```
Use Context7 to fetch the latest Stripe API documentation.
Specifically, I need to know:
1. What changed in the most recent API version?
2. Are there any breaking changes that would affect payment processing?
3. What new features were added?
4. Do we need to update our integration?

Provide a summary with links to relevant documentation sections.
```

**What Gemini does:**
1. Queries Context7 for latest Stripe docs
2. Identifies recent changes
3. Summarizes breaking changes
4. Provides links for details

**Example output:**
```
Stripe API Updates (v2024-10-15):

Breaking Changes:
- Payment Intents now require explicit confirmation (affects checkout flow)
- Legacy charge API deprecated (sunset date: 2025-06-01)

New Features:
- Multi-currency support for subscriptions
- Enhanced fraud detection (Radar v3)

Impact Assessment:
- Your integration uses Payment Intents: UPDATE REQUIRED
- Timeline: 2 weeks before legacy API sunset
- Recommended action: Review new confirmation flow

Documentation:
- Migration guide: https://stripe.com/docs/upgrades
- Payment Intents changes: https://stripe.com/docs/payments/intents
```

### Business Workflow 4: Quick Tool Learning

**Your goal**: Your team is considering Airtable for project management. You need a quick overview of its API capabilities.

**Prompt:**
```
Use Context7 to fetch Airtable API documentation and explain:
1. What can you do with the Airtable API?
2. How do you authenticate?
3. Can you read and write records?
4. What are the rate limits?
5. Is there a free tier for API access?

Give me a 3-minute summary suitable for a non-technical team.
```

**What you get:**
- Quick understanding of capabilities
- Technical requirements
- Cost implications
- Decision-making information

### When Context7 MCP Is Useful

**✅ Use Context7 when:**
- Learning a new tool or platform
- Checking if something changed recently
- Quick reference during conversation
- Comparing multiple tools' capabilities

**❌ Don't use Context7 when:**
- Documentation is offline/proprietary (Context7 needs public docs)
- You need older/archived versions
- Custom internal documentation (not indexed by Context7)

---

## Combining Extensions: A Powerful Business Workflow

Now let's see how to use both extensions together for maximum impact.

### Scenario: Market Research for New Product Launch

**Your goal**: You're launching a SaaS product. You need to:
1. Understand competitor offerings
2. Learn how to integrate with Stripe for billing
3. Research pricing models in your industry

**Workflow using both extensions:**

**Step 1: Competitive Research (Playwright)**

```
Use Playwright to browse these 5 SaaS competitor websites:
[List competitor URLs]

For each, extract:
- Pricing model (monthly, annual, usage-based?)
- Free trial offerings
- Payment methods accepted
- Refund policies

Create a comparison table.
```

**Step 2: Integration Research (Context7)**

```
Use Context7 to fetch Stripe subscription API documentation.
Explain:
- How to set up recurring billing
- How to implement free trials
- How to handle refunds programmatically

Provide code examples for a non-technical founder to share with developers.
```

**Step 3: Synthesis**

```
Based on the competitor research (from Playwright) and Stripe capabilities
(from Context7), recommend:
1. What pricing model should we use?
2. What free trial length is competitive?
3. What Stripe features do we need?
4. What can we offer that competitors don't?
```

**Result:**
- Comprehensive market understanding
- Technical implementation clarity
- Strategic differentiation
- Total time: 20-30 minutes (vs. 4-6 hours manually)

---

## Understanding Your Complete Toolkit

You now have access to powerful AI capabilities. Let's consolidate what you've learned across all 5 lessons.

### Your AI Capabilities (Chapter 6 Summary)

**Lesson 1: Why Gemini CLI?**
- Understanding AI companions as business tools
- When terminal AI makes sense

**Lesson 2: Installation & First Steps**
- Setting up Gemini CLI
- Running first commands
- Authentication and quotas

**Lesson 3: Built-In Tools**
- File operations (analyze reports, contracts)
- Web fetching (read competitor pages)
- Search grounding (current information with citations)
- Shell integration (file management tasks)

**Lesson 4: Context Windows**
- When to use which AI tool
- Multi-document analysis
- Asking AI to recommend tools

**Lesson 5 (This Lesson): Extensions**
- Playwright MCP (active web browsing)
- Context7 MCP (live documentation)
- Security considerations
- Real business workflows

### Strategic Decision Framework

When facing a business task, ask yourself:

```
1. Can built-in tools handle this?
   ├─ Yes → Use file operations, web fetch, or search (Lesson 3)
   └─ No → Need extensions...

2. Do I need active web browsing?
   ├─ Yes → Use Playwright MCP
   └─ No → Continue...

3. Do I need current technical documentation?
   ├─ Yes → Use Context7 MCP
   └─ No → Continue...

4. Do I need something else? (Database, CRM, custom integration)
   → Ask Gemini: "What extension exists for [my need]?"
   → Research available MCP servers
   → Evaluate security before installing
```

---

## What You're Ready For Now

After completing this chapter, you can:

✅ **Use AI companions for real business tasks**
- Competitive research
- Document analysis
- Market intelligence
- Strategic decision-making

✅ **Extend AI capabilities safely**
- Install trusted extensions
- Evaluate security risks
- Use MCP servers effectively

✅ **Ask AI for tool guidance**
- Don't memorize features
- Consult AI about what's possible
- Get personalized recommendations

✅ **Choose the right tool for each task**
- Built-in tools vs. extensions
- One AI tool vs. another
- When to combine multiple capabilities

---

## Looking Ahead: Your Next Steps

You've completed the Gemini CLI chapter. But this is a foundation, not the end.

### Immediate Next Actions

**1. Apply what you learned this week**

Choose one real business task and complete it using Gemini CLI:
- Competitive pricing research (use Playwright)
- Learn a new tool (use Context7)
- Analyze business data (use file operations)
- Multi-document synthesis (use large context)

**2. Explore additional extensions**

Ask Gemini:
```
What other MCP servers or extensions exist for Gemini CLI?
I'm interested in [your business area]. What extensions would help me?
```

**3. Identify your next learning priority**

Ask Gemini:
```
I've completed the Gemini CLI chapter. Based on my work in [your industry]
doing [your role], what should I learn next to get the most business value from AI?

Should I:
- Explore other AI tools (Claude, ChatGPT)?
- Learn prompt engineering techniques?
- Understand automation workflows?
- Something else?
```

### What Comes Next in This Book

The following chapters introduce:
- Other AI companions (Claude Code, ChatGPT, open-source models)
- Choosing between tools based on your specific needs
- Combining multiple AI tools in workflows
- Building AI-augmented business processes

**The core skill you've developed** — asking AI for guidance on tools and capabilities — transfers directly to all future chapters.

---

## Try With AI: Design Your Custom Business Workflow

### Setup

Open Gemini CLI (your AI companion from this chapter). You'll now design a real workflow for your business using everything you've learned.

---

### Prompt 1: Identify Your Need

```
I want to improve my business workflow in this area: [DESCRIBE YOUR SITUATION]

Examples:
- "I spend 3 hours weekly researching competitor pricing and features"
- "I need to stay current with Shopify API changes for our e-commerce site"
- "I analyze customer feedback emails manually each month"

What AI capabilities (built-in tools + extensions) would save me the most time?
Create a priority list: highest impact first.
```

**Expected Outcome**: Gemini identifies which tools and extensions address your specific pain points.

---

### Prompt 2: Design the Workflow

```
For my top priority task from the previous answer, design a complete workflow:

1. What tools/extensions do I need? (Be specific: Playwright? Context7? Built-in tools?)
2. What's the step-by-step process?
3. What information do I prepare beforehand?
4. What does the AI output look like?
5. How much time does this save vs. manual process?

Give me a workflow I can execute today.
```

**Expected Outcome**: A concrete, actionable workflow plan with commands and expected results.

---

### Prompt 3: Security Check

```
Before I implement this workflow, help me evaluate security:

1. What data am I giving the AI access to?
2. What are the privacy risks?
3. What credentials or sensitive information might be exposed?
4. How do I test this safely before using real data?
5. What's my "rollback plan" if something goes wrong?

Create a safety checklist for this workflow.
```

**Expected Outcome**: Clear security boundaries and a safe testing plan.

---

### Prompt 4: Implementation Guidance

```
I'm ready to implement the workflow you designed. Walk me through:

1. Exact commands to install any needed extensions
2. The first prompt I should give you to start the workflow
3. What to watch for (errors, unexpected behavior)
4. How to verify the results are correct
5. What to do if it doesn't work as expected

Assume I'm a beginner—be specific and clear.
```

**Expected Outcome**: Step-by-step implementation guide you can follow immediately.

---

### What Success Looks Like

✅ **You successfully completed this if:**
- You designed a workflow for YOUR actual business need (not a textbook example)
- You understand which tools/extensions solve your specific problem
- You have a security checklist before running it
- You have implementation steps you can execute today
- You know how to troubleshoot if something fails

---

### Safety & Ethics Note

**Before running your workflow on real business data:**

1. **Test with sample data first**
   - Use fake competitor URLs (or public sites)
   - Use test documentation (public APIs)
   - Don't use customer data until validated

2. **Verify outputs manually**
   - Spot-check AI-generated research
   - Confirm extracted data is accurate
   - Don't rely solely on AI for critical decisions

3. **Respect privacy and terms of service**
   - Don't scrape sites that prohibit automated access
   - Don't violate competitors' terms of service
   - Don't access private data without authorization

4. **Understand cost implications**
   - Some MCP servers may have usage limits
   - Monitor your Gemini API quota
   - Test incrementally before large-scale use

**Rule: If you wouldn't do it manually, don't ask AI to do it automatically.**

---

### Reflection Questions

Before moving to the next chapter, reflect:

**Understanding:**
- What's the difference between built-in tools and extensions?
- Why does MCP exist, and what problem does it solve?
- How do Playwright and Context7 differ from web fetching and search?

**Application:**
- What business task will you automate first with these new capabilities?
- How much time would this save you weekly or monthly?
- What other extensions would solve problems you currently face?

**Strategic Thinking:**
- How does AI change the way you approach competitive research?
- What business insights can you now access that were too time-consuming before?
- How will staying current with documentation (via Context7) change your decision-making?

**Your AI Journey:**
You started this chapter as a beginner. You now understand how to use AI as a business research partner, extend its capabilities safely, and design custom workflows for your specific needs.

**The meta-skill**: You don't memorize tools. You ask AI what's possible, evaluate options, and implement solutions iteratively.

This skill scales to every AI tool you'll encounter. When new extensions emerge, when tools evolve, when your needs change—you'll know how to adapt.

**Welcome to AI-augmented business workflows.** The next chapters build on this foundation.
