---
sidebar_position: 5
title: "Chapter 2 Exercises: Applying What You've Learned"
---

# Chapter 2 Exercises: Applying What You've Learned

These three optional exercises help you deepen your understanding of Chapter 2's concepts. Each takes 10-15 minutes and connects the chapter's ideas to your own situation.

**Note**: Exercises are optional. You don't need to complete them to move forward. But they're valuable if you want to think more deeply about inflection points, development patterns, and tool selection.

---

## Exercise 1: "What Vertical Could YOU Dominate?"

### The Challenge

In Lesson 1, we established that 2025 is a genuine inflection point in AI-assisted development. This matters not just for AI companies, but for *every* industry.

Consider the "Snakes and Ladders" pattern: industries where AI tools provide disproportionate leverage. A solo developer with Claude Code can now do what once required a team.

**Your task**: Identify a vertical (industry or domain) where you have domain expertise, and explore what becomes possible for a solo developer or small team now that AI assistants exist.

### Steps

1. **Pick a vertical** where you have context (your current industry, a side project domain, something you've always wanted to build)

2. **Identify the leverage point**: What's something that currently requires a dedicated engineer or team, but could be handled by one person + AI?
   - Example: A solo developer could build a specialized CRM for dental practices (domain expertise + AI pair programming)
   - Example: A freelancer could offer rapid prototyping for startups (AI-accelerated MVP building)

3. **Estimate the scope**: How much work would this be for a single developer in 2024 (pre-inflection)? How much now?
   - Feature set?
   - Timeline?
   - Required team size?

4. **Reflect**: Is this opportunity created because AI is smarter than humans, or because it multiplies human capability?

### Acceptance Criteria

Your answer should be:
- [ ] Specific to a real vertical you understand
- [ ] Concrete (not hypothetical; include actual features or scope)
- [ ] Realistic (not requiring custom training or deep research)
- [ ] Testable (you could actually attempt this in the next year)
- [ ] Connected to Chapter 1's theme (orchestrator mindset, not "AI will do everything")

### Example Response

**Vertical**: Medical billing for independent physical therapists

**Leverage point**: Custom billing software that integrates with insurance requirements for different states

**Timeline comparison**:
- 2024: Requires a full-stack developer (3-4 months) or licensing existing software ($200+/month)
- 2025: One developer + Claude Code could build domain-specific version in 4-6 weeks

**Reflection**: This isn't because AI understands insurance law. It's because Claude Code can accelerate the engineering work (database schema, API building, testing), freeing the solo developer to focus on domain logic and regulatory requirements.

---

## Exercise 2: "Match Tools to Use Cases"

### The Challenge

Lesson 4 introduced four AI coding agents. Choosing one means understanding your constraints and use case. This exercise builds that judgment.

### Your Task

Match the following five scenarios to one or more tools from Lesson 4:

- Claude Code (Anthropic)
- Gemini CLI (Google)
- OpenAI Codex (OpenAI)
- Qwen Code (Alibaba)

**Scenario A**: You're a student learning Python for the first time. You have a modest laptop and no budget for paid tools. You want to practice problem-solving without worrying about cost.

*Best fit*: ___________________

*Why*: _______________________

---

**Scenario B**: Your enterprise team of 50 developers uses Slack heavily. You need code assistance that integrates with your existing workflow and has admin controls for security compliance.

*Best fit*: ___________________

*Why*: _______________________

---

**Scenario C**: You're refactoring a legacy monolith with complex interdependencies. You need an AI that can understand multi-file context and suggest architectural improvements, not just line completions.

*Best fit*: ___________________

*Why*: _______________________

---

**Scenario D**: Your fintech company requires all tools to be deployed on-premise due to data privacy regulations. You need full transparency into model behavior for regulatory audits.

*Best fit*: ___________________

*Why*: _______________________

---

**Scenario E**: You're building a mobile app and want to explore rapid prototyping. You'd like AI that can research libraries and frameworks in real-time while generating code.

*Best fit*: ___________________

*Why*: _______________________

---

### Model Answers

**Scenario A**: Gemini CLI or Qwen Code

- Gemini: Free tier is generous (1,000 req/day, 1M context), easiest to get started
- Qwen: Also free to self-host, gives full transparency into the model
- Both are cost-effective for learning

**Scenario B**: OpenAI Codex (ChatGPT Business Plan)

- Native Slack integration is critical here
- Admin controls for enterprise security
- Team collaboration features built-in
- $30/user/month scales for teams

**Scenario C**: Claude Code (Claude Pro or Max)

- Deep contextual understanding across files is Claude's differentiator
- Subagents feature allows parallel analysis of complex systems
- Excellent at architectural reasoning and multi-file refactoring
- Best for complex, interconnected codebases

**Scenario D**: Qwen Code (self-hosted)

- Only open-source option; full transparency for audits
- On-premise deployment required for fintech data regulations
- Apache 2.0 license provides legal clarity
- Can audit and verify model behavior internally

**Scenario E**: Gemini CLI

- Web integration allows real-time library research
- 1M token context perfect for full-codebase understanding
- Can search Stack Overflow, GitHub, and official docs live
- Free tier sufficient for exploration and learning

---

## Exercise 3: "Explain to a Skeptical Colleague"

### The Challenge

You've read Chapter 2. You understand the evidence, the methodology distinction, and the tools. But your colleague is skeptical:

> "AI coding assistants are just hype. They can't really understand code. And if we use them, we'll end up with unmaintainable garbage. Isn't discipline supposed to matter?"

Your job: Construct a 2-minute pitch (150-300 words) that:

1. Acknowledges their skepticism as valid
2. Presents evidence from Chapter 2
3. Reframes the relationship between AI and discipline (not opposed; complementary)
4. Invites them to a low-risk experiment

### Your Task

Write your pitch below. It should feel conversational, grounded in Chapter 2 evidence, and address the skepticism directly.

---

### Template (optional)

**Opening**: Acknowledge the skepticism
- "You're right about X..."
- "That's a fair concern because..."

**Evidence**: Present 2-3 facts from Chapter 2
- DORA findings (high-performing orgs combine AI + discipline)
- Adoption metrics (84% of developers, 95% of orgs)
- Team A/B example (vibe coding risks; SDD benefits)

**Reframe**: Explain how AI and discipline work together
- "Discipline isn't the opposite of using AI..."
- "High-performing teams show that..."

**Experiment**: Propose a low-risk test
- "What if we tried..."
- "How would you measure success..."

**Closing**: Invite conversation
- "What's your biggest concern..."
- "Would you be willing to explore this if..."

---

### Example Response

---

**"AI and Discipline Aren't Opposed. They're Stronger Together"**

You're right that "AI writes perfect code" is hype. And you're also right that we've shipped unmaintainable code before. But here's what the data shows: it's not AI that's the problem. It's *discipline with AI*.

The DORA research found that high-performing organizations using AI get 10-20% velocity gains *without sacrificing quality*. How? They use AI within disciplined practices: test-driven development, code review, incremental deployment. Struggling organizations get faster shipping but worse quality—not because of AI, but because they shipped messy code faster.

Think about it this way: if you gave a developer with weak testing practices a faster IDE, they'd ship buggy code faster. That's not the IDE's fault. The same applies to AI—it's a force multiplier. It amplifies good practices and bad practices equally.

What if we ran a 2-week experiment? Pick one small feature, use Claude Code with spec + tests + review, and measure the outcome. I bet you'll see that discipline + AI beats both alone. And if I'm wrong, we're only out 2 weeks and a clear answer.

---

### Acceptance Criteria

Your pitch should:
- [ ] Be 150-300 words (approximately 2 minutes spoken aloud)
- [ ] Cite at least 2 specific facts from Chapter 2 (DORA, adoption rates, Team A/B, etc.)
- [ ] Acknowledge the skepticism directly (not dismissive)
- [ ] Reframe AI and discipline as complementary, not opposed
- [ ] Propose a specific, low-risk experiment
- [ ] Feel conversational (not a lecture)
- [ ] Be something you'd actually say to a colleague

---

## Reflection Questions (Optional)

If you want to go deeper on any exercise:

**After Exercise 1**:
- What skills or domain expertise do you have that could be a "lever" with AI?
- What would it take to test that hypothesis?

**After Exercise 2**:
- Which tool surprised you as a good fit for a scenario?
- What trade-off did you find most interesting (cost, reasoning, transparency, team features)?

**After Exercise 3**:
- Which part of your pitch felt most persuasive?
- What would a true skeptic challenge you on next?

---

## Sharing & Discussion (Optional)

These exercises are personal reflection tools. But if you're learning with others:

- **Discuss Exercise 1**: What verticals did others identify? Are there patterns across your group?
- **Compare Exercise 2**: Did you and a colleague match scenarios the same way? Why or why not?
- **Workshop Exercise 3**: Practice your pitch on a colleague. Ask: "What would convince you to try this?"

---

## Moving Forward

Completed these exercises? Great. You've deepened your understanding of Chapter 2's themes:

- Inflection points aren't abstract—they're visible in your industry
- Tool selection matters, but isn't permanent
- Communicating about AI to skeptics is a skill you'll need

**Next step**: Move to Chapter 3, where you'll install an AI agent and write your first prompt. The theoretical understanding from Chapter 2 becomes practical skill in Chapter 3.

**Not doing the exercises?** No problem. Move straight to Chapter 3 whenever you're ready. The exercises will be here if you circle back.

---

*Optional exercises created as deepening opportunities, not gatekeeping.*
