import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={styles.heroBanner}>
      <div className={styles.heroGradient} />
      <div className="container">
        <div className={styles.heroContent}>
          {/* Left side - Book Cover */}
          <div className={styles.heroImageContainer}>
            <img 
              src="/img/book-cover.png" 
              alt="CoLearning Programming: The AI-Driven Way Book Cover" 
              className={styles.heroBookCover}
            />
          </div>
          
          {/* Right side - Content */}
          <div className={styles.heroTextContent}>
            <div className={styles.heroLabel}>Panaversity AI-Driven Way Book Series</div>
            <Heading as="h1" className={styles.heroTitle}>
              CoLearning Programming
              <br />
              <span className={styles.heroTitleAccent}>The AI-Driven Way</span>
            </Heading>
            <p className={styles.heroSubtitle}>
              Master Python & TypeScript by building production-ready AI systems. Transform how you learn with AI as your co-learner and collaborator.
            </p>
            
            <div className={styles.heroBadges}>
              <span className={styles.badge}>
                <span className={styles.badgeIcon}>✨</span>
                100% Free & Open Source
              </span>
              <span className={styles.badge}>
                <span className={styles.badgeIcon}>📚</span>
                AI Driven Learning
              </span>
              <span className={styles.badge}>
                <span className={styles.badgeIcon}>🎯</span>
                Production Ready
              </span>
            </div>
            
            <div className={styles.heroButtons}>
              <Link
                className={clsx('button button--primary button--lg', styles.ctaButton)}
                to="/docs/Introducing-AI-Driven-Development">
                <span className={styles.buttonContent}>
                  <span className={styles.buttonText}>Start Reading Free</span>
                  <span className={styles.buttonIcon}>→</span>
                </span>
              </Link>
              <Link
                className={clsx('button button--outline button--lg', styles.secondaryButton)}
                href="https://panaversity.org/flagship-program/courses"
                target="_blank"
                rel="noopener noreferrer">
                <span className={styles.buttonContent}>
                  <span className={styles.buttonText}>Explore Panaversity Courses</span>
                  <span className={styles.buttonIcon}>🎓</span>
                </span>
              </Link>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

function Feature({title, description, icon, featured}: {title: string; description: string; icon: string; featured?: boolean}) {
  return (
    <div className={clsx(styles.feature, featured && styles.featureFeatured)}>
      {featured && <div className={styles.featureBadge}>Most Popular</div>}
      <div className={styles.featureIconWrapper}>
        <div className={styles.featureIcon}>{icon}</div>
      </div>
      <h3 className={styles.featureTitle}>{title}</h3>
      <p className={styles.featureDescription}>{description}</p>
      <div className={styles.featureAccent} />
    </div>
  );
}

function FeaturesSection() {
  return (
    <section className={styles.features}>
      <div className="container">
        {/* Section Header */}
        <div className={styles.featuresHeader}>
          <div className={styles.featuresLabel}>Core Pillars</div>
          <Heading as="h2" className={styles.featuresHeading}>
            What Makes This Book Different
          </Heading>
          <p className={styles.featuresSubheading}>
            A comprehensive, production-focused approach to learning programming in the age of AI
          </p>
        </div>

        {/* Features Grid */}
        <div className={styles.featuresGrid}>
          <Feature
            icon="🤖"
            title="AI-First Learning"
            description="Master AI-driven development from day one. Build with Claude, Gemini, and OpenAI Agents SDK."
            featured={true}
          />
          <Feature
            icon="🏗️"
            title="Production Systems"
            description="Learn through real-world architectures: MCP, containers, Dapr, event-driven patterns, and Kubernetes."
          />
          <Feature
            icon="🧠"
            title="Spec-Kit Plus Methodology"
            description="Specification-driven development designed for AI collaboration. Plan, iterate, and scale systematically."
          />
          <Feature
            icon="🌐"
            title="Cloud-Native Stack"
            description="Stateless, containerized applications. Deploy anywhere with Docker, Kubernetes, and modern DevOps."
          />
          <Feature
            icon="💬"
            title="Voice & Realtime Agents"
            description="Build cutting-edge realtime and voice-interactive AI agents that respond to natural language."
          />
          <Feature
            icon="🚀"
            title="Zero to Production"
            description="46 comprehensive chapters taking you from programming basics to deploying enterprise AI systems."
            featured={true}
          />
        </div>

        {/* Bottom Stats Bar */}
        <div className={styles.featuresStats}>
          <div className={styles.featureStat}>
            <div className={styles.featureStatNumber}>46</div>
            <div className={styles.featureStatLabel}>Chapters</div>
          </div>
          <div className={styles.featureStatDivider} />
          <div className={styles.featureStat}>
            <div className={styles.featureStatNumber}>15+</div>
            <div className={styles.featureStatLabel}>Real Projects</div>
          </div>
          <div className={styles.featureStatDivider} />
          <div className={styles.featureStat}>
            <div className={styles.featureStatNumber}>100%</div>
            <div className={styles.featureStatLabel}>Free & Open</div>
          </div>
          <div className={styles.featureStatDivider} />
          <div className={styles.featureStat}>
            <div className={styles.featureStatNumber}>∞</div>
            <div className={styles.featureStatLabel}>Production Ready</div>
          </div>
        </div>
      </div>
    </section>
  );
}

function ParadigmShift() {
  return (
    <section className={styles.paradigmSection}>
      <div className="container">
        <div className={styles.paradigmContent}>
          {/* Section Header */}
          <div className={styles.paradigmHeader}>
            <div className={styles.paradigmLabel}>The Revolution</div>
            <Heading as="h2" className={styles.paradigmTitle}>
              Why Traditional CS Education <br />
              <span className={styles.paradigmTitleAccent}>Needs a Rethink</span>
            </Heading>
            <p className={styles.paradigmSubtitle}>
              The world has changed. AI has fundamentally transformed how we build software.
              Your education should reflect this reality.
            </p>
          </div>

          {/* Comparison Grid */}
          <div className={styles.comparisonGrid}>
            {/* Traditional Card */}
            <div className={styles.comparisonCard}>
              <div className={styles.comparisonIconWrapper}>
                <div className={styles.comparisonIcon}>📚</div>
              </div>
              <div className={styles.comparisonLabel}>Traditional Approach</div>
              <div className={styles.comparisonDescription}>
                The old way of learning programming
              </div>
              <ul className={styles.comparisonList}>
                <li>
                  <span className={styles.comparisonItemTitle}>Syntax First</span>
                  Learn language basics before building anything meaningful
                </li>
                <li>
                  <span className={styles.comparisonItemTitle}>Memorize Algorithms</span>
                  Focus on rote learning of data structures
                </li>
                <li>
                  <span className={styles.comparisonItemTitle}>Solo Problem-Solving</span>
                  Work alone without modern collaborative tools
                </li>
                <li>
                  <span className={styles.comparisonItemTitle}>Toy Projects</span>
                  Build calculator apps and to-do lists
                </li>
                <li>
                  <span className={styles.comparisonItemTitle}>Textbook-Driven</span>
                  Theory-heavy with outdated examples
                </li>
              </ul>
            </div>

            {/* VS Divider */}
            <div className={styles.comparisonDivider}>
              <div className={styles.comparisonVS}>VS</div>
              <div className={styles.comparisonArrow}>→</div>
            </div>

            {/* AI-Driven Card */}
            <div className={clsx(styles.comparisonCard, styles.comparisonCardHighlight)}>
              <div className={styles.comparisonIconWrapper}>
                <div className={styles.comparisonIcon}>🚀</div>
              </div>
              <div className={styles.comparisonLabel}>AI-Driven Way</div>
              <div className={styles.comparisonDescription}>
                The future of programming education
              </div>
              <ul className={styles.comparisonList}>
                <li>
                  <span className={styles.comparisonItemTitle}>Production First</span>
                  Build real systems from day one with AI guidance
                </li>
                <li>
                  <span className={styles.comparisonItemTitle}>Pattern Understanding</span>
                  Learn through doing with AI as your guide
                </li>
                <li>
                  <span className={styles.comparisonItemTitle}>AI Pair Programming</span>
                  Collaborate with Claude, GPT, and Gemini
                </li>
                <li>
                  <span className={styles.comparisonItemTitle}>Real Architectures</span>
                  Deploy cloud-native, production-ready systems
                </li>
                <li>
                  <span className={styles.comparisonItemTitle}>Spec-Driven Learning</span>
                  Systematic, tool-augmented development
                </li>
              </ul>
            </div>
          </div>

          {/* Bottom CTA */}
          <div className={styles.paradigmCTA}>
            <div className={styles.paradigmCTAContent}>
              <div className={styles.paradigmCTAIcon}>💡</div>
              <div className={styles.paradigmCTAText}>
                <h3 className={styles.paradigmCTATitle}>Ready for the New Way?</h3>
                <p className={styles.paradigmCTADescription}>
                  Join thousands of learners who are mastering programming with AI as their co-learner
                </p>
              </div>
              <Link
                className={clsx('button button--primary button--lg', styles.paradigmCTAButton)}
                to="/docs/Introducing-AI-Driven-Development">
                Start Learning Now
              </Link>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title="CoLearning Programming: The AI-Driven Way | Free Book"
      description="Master Python & TypeScript by building production-ready AI systems. AI as your co-learner and collaborator.">
      <HomepageHeader />
      <FeaturesSection />
      <ParadigmShift />
    </Layout>
  );
}
