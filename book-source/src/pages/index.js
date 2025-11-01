"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = Home;
var clsx_1 = require("clsx");
var Link_1 = require("@docusaurus/Link");
var useDocusaurusContext_1 = require("@docusaurus/useDocusaurusContext");
var Layout_1 = require("@theme/Layout");
var Heading_1 = require("@theme/Heading");
var index_module_css_1 = require("./index.module.css");
function HomepageHeader() {
    var siteConfig = (0, useDocusaurusContext_1.default)().siteConfig;
    return (<header className={index_module_css_1.default.heroBanner}>
      <div className={index_module_css_1.default.heroGradient}/>
      <div className="container">
        <div className={index_module_css_1.default.heroContent}>
          {/* Left side - Book Cover */}
          <div className={index_module_css_1.default.heroImageContainer}>
            <img src="/img/book-cover-page.png" alt="CoLearning Programming: The AI-Driven Way Book Cover" className={index_module_css_1.default.heroBookCover}/>
          </div>
          
          {/* Right side - Content */}
          <div className={index_module_css_1.default.heroTextContent}>
            <div className={index_module_css_1.default.heroLabel}>Panaversity AI-Native Book Series</div>
            <Heading_1.default as="h1" className={index_module_css_1.default.heroTitle}>
              AI Native Software Development
              <br />
              <span className={index_module_css_1.default.heroTitleAccent}>Colearning Agentic AI with Python and TypeScript – <strong>The AI & Spec Driven Way</strong></span>
            </Heading_1.default>
            
            <div className={index_module_css_1.default.heroBadges}>
              <span className={index_module_css_1.default.badge}>
                <span className={index_module_css_1.default.badgeIcon}>✨</span>
                100% Free & Open Source
              </span>
              <span className={index_module_css_1.default.badge}>
                <span className={index_module_css_1.default.badgeIcon}>🤝</span>
                Co-Learning with AI
              </span>
              <span className={index_module_css_1.default.badge}>
                <span className={index_module_css_1.default.badgeIcon}>🎯</span>
                Spec-Driven Development
              </span>
            </div>
            
            <div className={index_module_css_1.default.heroButtons}>
              <Link_1.default className={(0, clsx_1.default)('button button--primary button--lg', index_module_css_1.default.ctaButton)} to="/docs/preface-agent-native">
                <span className={index_module_css_1.default.buttonContent}>
                  <span className={index_module_css_1.default.buttonText}>Start Reading Free</span>
                  <span className={index_module_css_1.default.buttonIcon}>→</span>
                </span>
              </Link_1.default>
              <Link_1.default className={(0, clsx_1.default)('button button--outline button--lg', index_module_css_1.default.secondaryButton)} href="https://panaversity.org/flagship-program/courses" target="_blank" rel="noopener noreferrer">
                <span className={index_module_css_1.default.buttonContent}>
                  <span className={index_module_css_1.default.buttonText}>Explore Panaversity</span>
                  <span className={index_module_css_1.default.buttonIcon}>🎓</span>
                </span>
              </Link_1.default>
            </div>
          </div>
        </div>
      </div>
    </header>);
}
function Feature(_a) {
    var title = _a.title, description = _a.description, icon = _a.icon, featured = _a.featured;
    return (<div className={(0, clsx_1.default)(index_module_css_1.default.feature, featured && index_module_css_1.default.featureFeatured)}>
      {featured && <div className={index_module_css_1.default.featureBadge}>Most Popular</div>}
      <div className={index_module_css_1.default.featureIconWrapper}>
        <div className={index_module_css_1.default.featureIcon}>{icon}</div>
      </div>
      <h3 className={index_module_css_1.default.featureTitle}>{title}</h3>
      <p className={index_module_css_1.default.featureDescription}>{description}</p>
      <div className={index_module_css_1.default.featureAccent}/>
    </div>);
}
function AISpectrumSection() {
    return (<section className={index_module_css_1.default.spectrumSection}>
      <div className="container">
        <div className={index_module_css_1.default.spectrumHeader}>
          <div className={index_module_css_1.default.spectrumLabel}>Understanding AI Development</div>
          <Heading_1.default as="h2" className={index_module_css_1.default.spectrumTitle}>
            The AI Development Spectrum
          </Heading_1.default>
          <p className={index_module_css_1.default.spectrumSubtitle}>
            Three distinct approaches to AI in software development. This book teaches you both AI-Driven and AI-Native development.
          </p>
        </div>

        <div className={index_module_css_1.default.spectrumCards}>
          {/* AI Assisted */}
          <div className={index_module_css_1.default.spectrumCard}>
            <div className={index_module_css_1.default.spectrumCardHeader}>
              <div className={index_module_css_1.default.spectrumIcon}>🛠️</div>
              <h3 className={index_module_css_1.default.spectrumCardTitle}>AI Assisted</h3>
              <div className={index_module_css_1.default.spectrumCardSubtitle}>AI as Helper</div>
            </div>
            <p className={index_module_css_1.default.spectrumCardDescription}>
              AI enhances your productivity with code completion, debugging assistance, and documentation generation.
            </p>
            <ul className={index_module_css_1.default.spectrumCardList}>
              <li>Code completion & suggestions</li>
              <li>Bug detection & debugging</li>
              <li>Documentation generation</li>
            </ul>
            <div className={index_module_css_1.default.spectrumCardExample}>
              <strong>Example:</strong> Using Copilot to build a React website faster
            </div>
          </div>

          {/* AI Driven */}
          <div className={(0, clsx_1.default)(index_module_css_1.default.spectrumCard, index_module_css_1.default.spectrumCardHighlight)}>
            <div className={index_module_css_1.default.spectrumBadge}>Focus of This Book</div>
            <div className={index_module_css_1.default.spectrumCardHeader}>
              <div className={index_module_css_1.default.spectrumIcon}>🚀</div>
              <h3 className={index_module_css_1.default.spectrumCardTitle}>AI Driven</h3>
              <div className={index_module_css_1.default.spectrumCardSubtitle}>AI as Co-Creator</div>
            </div>
            <p className={index_module_css_1.default.spectrumCardDescription}>
              AI generates significant code from specifications. You act as architect, director, and reviewer.
            </p>
            <ul className={index_module_css_1.default.spectrumCardList}>
              <li>Code generation from specs</li>
              <li>Automated testing & optimization</li>
              <li>Architecture from requirements</li>
            </ul>
            <div className={index_module_css_1.default.spectrumCardExample}>
              <strong>Example:</strong> Writing a spec for a REST API, AI generates complete FastAPI backend
            </div>
          </div>

          {/* AI Native */}
          <div className={(0, clsx_1.default)(index_module_css_1.default.spectrumCard, index_module_css_1.default.spectrumCardHighlight)}>
            <div className={index_module_css_1.default.spectrumBadge}>Focus of This Book</div>
            <div className={index_module_css_1.default.spectrumCardHeader}>
              <div className={index_module_css_1.default.spectrumIcon}>🧠</div>
              <h3 className={index_module_css_1.default.spectrumCardTitle}>AI Native</h3>
              <div className={index_module_css_1.default.spectrumCardSubtitle}>AI IS the Software</div>
            </div>
            <p className={index_module_css_1.default.spectrumCardDescription}>
              Applications architected around AI capabilities. LLMs and agents are core functional components.
            </p>
            <ul className={index_module_css_1.default.spectrumCardList}>
              <li>Natural language interfaces</li>
              <li>Intelligent automation & reasoning</li>
              <li>Agent orchestration systems</li>
            </ul>
            <div className={index_module_css_1.default.spectrumCardExample}>
              <strong>Example:</strong> Building a customer support agent that autonomously resolves tickets
            </div>
          </div>
        </div>

        {/* Redesigned progression visualization */}
        <div className={index_module_css_1.default.spectrumFlow}>
          <div className={index_module_css_1.default.spectrumFlowTrack}>
            
            <div className={index_module_css_1.default.spectrumFlowStep}>
              <div className={index_module_css_1.default.flowStepCircle}>
                <span className={index_module_css_1.default.flowStepNumber}>1</span>
              </div>
              <div className={index_module_css_1.default.flowStepContent}>
                <div className={index_module_css_1.default.flowStepTitle}>AI Assisted</div>
                <div className={index_module_css_1.default.flowStepSubtitle}>Helper</div>
              </div>
            </div>

            <div className={index_module_css_1.default.spectrumFlowLine}>
              <div className={index_module_css_1.default.flowLineProgress}></div>
            </div>

            <div className={(0, clsx_1.default)(index_module_css_1.default.spectrumFlowStep, index_module_css_1.default.flowStepActive)}>
              <div className={index_module_css_1.default.flowStepCircle}>
                <span className={index_module_css_1.default.flowStepNumber}>2</span>
              </div>
              <div className={index_module_css_1.default.flowStepContent}>
                <div className={index_module_css_1.default.flowStepTitle}>AI Driven</div>
                <div className={index_module_css_1.default.flowStepSubtitle}>Co-Creator</div>
              </div>
            </div>

            <div className={index_module_css_1.default.spectrumFlowLine}>
              <div className={index_module_css_1.default.flowLineProgress}></div>
            </div>

            <div className={(0, clsx_1.default)(index_module_css_1.default.spectrumFlowStep, index_module_css_1.default.flowStepActive)}>
              <div className={index_module_css_1.default.flowStepCircle}>
                <span className={index_module_css_1.default.flowStepNumber}>3</span>
              </div>
              <div className={index_module_css_1.default.flowStepContent}>
                <div className={index_module_css_1.default.flowStepTitle}>AI Native</div>
                <div className={index_module_css_1.default.flowStepSubtitle}>Core System</div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>);
}
function FeaturesSection() {
    return (<section className={index_module_css_1.default.features}>
      <div className="container">
        {/* Section Header */}
        <div className={index_module_css_1.default.featuresHeader}>
          <div className={index_module_css_1.default.featuresLabel}>Core Pillars</div>
          <Heading_1.default as="h2" className={index_module_css_1.default.featuresHeading}>
            What Makes This Book Different
          </Heading_1.default>
          <p className={index_module_css_1.default.featuresSubheading}>
            A comprehensive, production-focused approach to co-learning with AI in the spec-driven way
          </p>
        </div>

        {/* Features Grid */}
        <div className={index_module_css_1.default.featuresGrid}>
          <Feature icon="�" title="Co-Learning Philosophy" description="Learn alongside AI agents. Not just using AI as a tool, but co-creating where both human and AI learn together." featured={true}/>
          <Feature icon="🐍" title="Dual Language Mastery" description="Python for reasoning & intelligence, TypeScript for interaction & UI. Master the bilingual AI-native stack."/>
          <Feature icon="📋" title="Spec-Driven Development" description="Write specifications that both humans and AI understand. Specs become executable blueprints for intelligent systems."/>
          <Feature icon="🤖" title="Agentic AI Systems" description="Build with OpenAI Agents SDK and Google ADK. Create agents that reason, act, and collaborate autonomously."/>
          <Feature icon="🏗️" title="Production-Ready Architecture" description="Cloud-native deployment with Docker, Kubernetes, Dapr, and Ray. Scalable, secure, fault-tolerant systems."/>
          <Feature icon="🚀" title="Complete Learning Journey" description="46 comprehensive chapters from programming basics to deploying enterprise agentic AI systems in production." featured={true}/>
        </div>
      </div>
    </section>);
}
function MaturityLevelsSection() {
    return (<section className={index_module_css_1.default.maturitySection}>
      <div className="container">
        <div className={index_module_css_1.default.maturityHeader}>
          <div className={index_module_css_1.default.maturityLabel}>Your AI Journey</div>
          <Heading_1.default as="h2" className={index_module_css_1.default.maturityTitle}>
            Organizational AI Maturity Levels
          </Heading_1.default>
          <p className={index_module_css_1.default.maturitySubtitle}>
            Where does your organization stand? Understanding these levels helps you chart your path forward.
          </p>
        </div>

        <div className={index_module_css_1.default.maturityLevels}>
          {/* Level 1 */}
          <div className={index_module_css_1.default.maturityLevel}>
            <div className={index_module_css_1.default.maturityLevelNumber}>1</div>
            <div className={index_module_css_1.default.maturityLevelHeader}>
              <div>
                <h3 className={index_module_css_1.default.maturityLevelTitle}>AI Awareness</h3>
                <div className={index_module_css_1.default.maturityLevelSubtitle}>Experimenting</div>
              </div>
              <div className={index_module_css_1.default.maturityLevelImpact}>10-20% productivity gains</div>
            </div>
            <p className={index_module_css_1.default.maturityLevelDescription}>
              Individual developers experimenting with AI coding tools. Early AI Assisted Development.
            </p>
            <div className={index_module_css_1.default.maturityLevelApproach}>
              <strong>Approach:</strong> AI Assisted (Individual)
            </div>
          </div>

          {/* Level 2 */}
          <div className={index_module_css_1.default.maturityLevel}>
            <div className={index_module_css_1.default.maturityLevelNumber}>2</div>
            <div className={index_module_css_1.default.maturityLevelHeader}>
              <div>
                <h3 className={index_module_css_1.default.maturityLevelTitle}>AI Adoption</h3>
                <div className={index_module_css_1.default.maturityLevelSubtitle}>Standardizing</div>
              </div>
              <div className={index_module_css_1.default.maturityLevelImpact}>30-40% productivity boost</div>
            </div>
            <p className={index_module_css_1.default.maturityLevelDescription}>
              Organization-wide adoption with governance. Established guidelines and security policies.
            </p>
            <div className={index_module_css_1.default.maturityLevelApproach}>
              <strong>Approach:</strong> AI Assisted (Team)
            </div>
          </div>

          {/* Level 3 */}
          <div className={(0, clsx_1.default)(index_module_css_1.default.maturityLevel, index_module_css_1.default.maturityLevelHighlight)}>
            <div className={index_module_css_1.default.maturityBadge}>BOOK FOCUS</div>
            <div className={index_module_css_1.default.maturityLevelNumber}>3</div>
            <div className={index_module_css_1.default.maturityLevelHeader}>
              <div>
                <h3 className={index_module_css_1.default.maturityLevelTitle}>AI Integration</h3>
                <div className={index_module_css_1.default.maturityLevelSubtitle}>Transforming Workflows</div>
              </div>
              <div className={index_module_css_1.default.maturityLevelImpact}>2-3x faster development</div>
            </div>
            <p className={index_module_css_1.default.maturityLevelDescription}>
              AI-Driven Development practices. Specs become living documentation. Workflows redesigned around AI collaboration.
            </p>
            <div className={index_module_css_1.default.maturityLevelApproach}>
              <strong>Approach:</strong> AI Driven (Workflow)
            </div>
          </div>

          {/* Level 4 */}
          <div className={(0, clsx_1.default)(index_module_css_1.default.maturityLevel, index_module_css_1.default.maturityLevelHighlight)}>
            <div className={index_module_css_1.default.maturityBadge}>BOOK FOCUS</div>
            <div className={index_module_css_1.default.maturityLevelNumber}>4</div>
            <div className={index_module_css_1.default.maturityLevelHeader}>
              <div>
                <h3 className={index_module_css_1.default.maturityLevelTitle}>AI-Native Products</h3>
                <div className={index_module_css_1.default.maturityLevelSubtitle}>Building Intelligence</div>
              </div>
              <div className={index_module_css_1.default.maturityLevelImpact}>New capabilities unlocked</div>
            </div>
            <p className={index_module_css_1.default.maturityLevelDescription}>
              Products where AI/LLMs are core components. Agent orchestration, natural language interfaces, intelligent systems.
            </p>
            <div className={index_module_css_1.default.maturityLevelApproach}>
              <strong>Approach:</strong> AI Native (Product)
            </div>
          </div>

          {/* Level 5 */}
          <div className={index_module_css_1.default.maturityLevel}>
            <div className={index_module_css_1.default.maturityLevelNumber}>5</div>
            <div className={index_module_css_1.default.maturityLevelHeader}>
              <div>
                <h3 className={index_module_css_1.default.maturityLevelTitle}>AI-First Enterprise</h3>
                <div className={index_module_css_1.default.maturityLevelSubtitle}>Living in the Future</div>
              </div>
              <div className={index_module_css_1.default.maturityLevelImpact}>10x productivity</div>
            </div>
            <p className={index_module_css_1.default.maturityLevelDescription}>
              Entire organization AI-native. Custom models, self-improving systems, AI embedded in every aspect.
            </p>
            <div className={index_module_css_1.default.maturityLevelApproach}>
              <strong>Approach:</strong> AI Native (Enterprise)
            </div>
          </div>
        </div>

        <div className={index_module_css_1.default.maturityCTA}>
          <p className={index_module_css_1.default.maturityCTAText}>
            <strong>This book prepares you for Levels 3-4:</strong> Master AI-Driven workflows and build AI-Native products
          </p>
        </div>
      </div>
    </section>);
}
function ParadigmShift() {
    return (<section className={index_module_css_1.default.paradigmSection}>
      <div className="container">
        <div className={index_module_css_1.default.paradigmContent}>
          {/* Section Header */}
          <div className={index_module_css_1.default.paradigmHeader}>
            <div className={index_module_css_1.default.paradigmLabel}>The Great Shift</div>
            <Heading_1.default as="h2" className={index_module_css_1.default.paradigmTitle}>
              From Automation to Intelligence<br />
              <span className={index_module_css_1.default.paradigmTitleAccent}>From Coding to Co-Creating</span>
            </Heading_1.default>
            <p className={index_module_css_1.default.paradigmSubtitle}>
              AI-native development is not about replacing developers—it's about amplifying intelligence.
              Learn to collaborate with reasoning entities that learn with you.
            </p>
          </div>

          {/* Comparison Grid */}
          <div className={index_module_css_1.default.comparisonGrid}>
            {/* Traditional Card */}
            <div className={index_module_css_1.default.comparisonCard}>
              <div className={index_module_css_1.default.comparisonIconWrapper}>
                <div className={index_module_css_1.default.comparisonIcon}>📚</div>
              </div>
              <div className={index_module_css_1.default.comparisonLabel}>Traditional Development</div>
              <div className={index_module_css_1.default.comparisonDescription}>
                The automation era
              </div>
              <ul className={index_module_css_1.default.comparisonList}>
                <li>
                  <span className={index_module_css_1.default.comparisonItemTitle}>Instruction-Based</span>
                  Tell computers exactly what to do with precise syntax
                </li>
                <li>
                  <span className={index_module_css_1.default.comparisonItemTitle}>Solo Coding</span>
                  Developer writes every line manually
                </li>
                <li>
                  <span className={index_module_css_1.default.comparisonItemTitle}>Documentation as Afterthought</span>
                  Specs are static contracts written post-facto
                </li>
                <li>
                  <span className={index_module_css_1.default.comparisonItemTitle}>Linear Learning</span>
                  Learn syntax → Build simple projects → Slowly scale
                </li>
                <li>
                  <span className={index_module_css_1.default.comparisonItemTitle}>Code-First</span>
                  Focus on implementation details from day one
                </li>
              </ul>
            </div>

            {/* VS Divider */}
            <div className={index_module_css_1.default.comparisonDivider}>
              <div className={index_module_css_1.default.comparisonVS}>VS</div>
              <div className={index_module_css_1.default.comparisonArrow}>→</div>
            </div>

            {/* AI-Native Card */}
            <div className={(0, clsx_1.default)(index_module_css_1.default.comparisonCard, index_module_css_1.default.comparisonCardHighlight)}>
              <div className={index_module_css_1.default.comparisonIconWrapper}>
                <div className={index_module_css_1.default.comparisonIcon}>🤖</div>
              </div>
              <div className={index_module_css_1.default.comparisonLabel}>AI-Native Way</div>
              <div className={index_module_css_1.default.comparisonDescription}>
                The intelligence era
              </div>
              <ul className={index_module_css_1.default.comparisonList}>
                <li>
                  <span className={index_module_css_1.default.comparisonItemTitle}>Intent-Based</span>
                  Describe what you want; AI reasons how to build it
                </li>
                <li>
                  <span className={index_module_css_1.default.comparisonItemTitle}>Co-Learning Partnership</span>
                  You and AI teach each other through iteration
                </li>
                <li>
                  <span className={index_module_css_1.default.comparisonItemTitle}>Specs as Living Blueprints</span>
                  Specifications drive code, tests, and documentation
                </li>
                <li>
                  <span className={index_module_css_1.default.comparisonItemTitle}>Production-First Learning</span>
                  Build real agentic systems from day one
                </li>
                <li>
                  <span className={index_module_css_1.default.comparisonItemTitle}>Architecture-First</span>
                  Design intelligent collaborations, not just code
                </li>
              </ul>
            </div>
          </div>

          {/* Bottom CTA */}
          <div className={index_module_css_1.default.paradigmCTA}>
            <div className={index_module_css_1.default.paradigmCTAContent}>
              <div className={index_module_css_1.default.paradigmCTAIcon}>🌱</div>
              <div className={index_module_css_1.default.paradigmCTAText}>
                <h3 className={index_module_css_1.default.paradigmCTATitle}>Ready to Co-Learn with AI?</h3>
                <p className={index_module_css_1.default.paradigmCTADescription}>
                  Join the revolution where coding becomes conversation and software becomes alive
                </p>
              </div>
              <Link_1.default className={(0, clsx_1.default)('button button--primary button--lg', index_module_css_1.default.paradigmCTAButton)} to="/docs/preface-agent-native">
                Begin Your Journey
              </Link_1.default>
            </div>
          </div>
        </div>
      </div>
    </section>);
}
function Home() {
    var siteConfig = (0, useDocusaurusContext_1.default)().siteConfig;
    return (<Layout_1.default title="AI Native Software Development | Free Book" description="Colearning Agentic AI with Python and TypeScript – The AI & Spec Driven Way. Build production-ready intelligent systems.">
      <HomepageHeader />
      <AISpectrumSection />
      <FeaturesSection />
      <MaturityLevelsSection />
      <ParadigmShift />
    </Layout_1.default>);
}
