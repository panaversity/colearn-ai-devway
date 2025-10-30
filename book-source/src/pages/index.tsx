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
          <div className={styles.heroImageContainer}>
            <img 
              src="/img/book-cover.png" 
              alt="CoLearning Programming Book Cover" 
              className={styles.heroBookCover}
            />
          </div>
          <div className={styles.heroLabel}>Panaversity AI-Driven Way Book Series</div>
          <Heading as="h1" className={styles.heroTitle}>
            CoLearning Programming
            <br />
            <span className={styles.heroTitleAccent}>The AI Driven Way</span>
          </Heading>
          <p className={styles.heroSubtitle}>
            Master Python & TypeScript by building production-ready AI systems.
            <br />
            Transform how you learn with AI as your co-learner and collaborator.
          </p>
          <div className={styles.heroBadges}>
            <span className={styles.badge}>
              <span className={styles.badgeIcon}>✨</span>
              100% Free & Open Source
            </span>
            <span className={styles.badge}>
              <span className={styles.badgeIcon}>📚</span>
              46 Chapters
            </span>
            <span className={styles.badge}>
              <span className={styles.badgeIcon}>🎯</span>
              Beginner Friendly
            </span>
          </div>
          <div className={styles.heroButtons}>
            <Link
              className={clsx('button button--primary button--lg', styles.ctaButton)}
              to="/docs/Introducing-AI-Driven-Development/intro">
              <span className={styles.buttonContent}>
                <span className={styles.buttonText}>Start Learning Free</span>
                <span className={styles.buttonIcon}>→</span>
              </span>
            </Link>
            <Link
              className={clsx('button button--outline button--lg', styles.secondaryButton)}
              to="/docs/Introducing-AI-Driven-Development/intro">
              <span className={styles.buttonContent}>
                <span className={styles.buttonText}>View Book</span>
                <span className={styles.buttonIcon}>📖</span>
              </span>
            </Link>
            <Link
              className={clsx('button button--outline button--lg', styles.coursesButton)}
              href="https://panaversity.org/flagship-program/courses"
              target="_blank"
              rel="noopener noreferrer">
              <span className={styles.buttonContent}>
                <span className={styles.buttonText}>Take Panaversity Courses</span>
                <span className={styles.buttonIcon}>🎓</span>
              </span>
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}

function Feature({title, description, icon}: {title: string; description: string; icon: string}) {
  return (
    <div className={styles.feature}>
      <div className={styles.featureIcon}>{icon}</div>
      <h3 className={styles.featureTitle}>{title}</h3>
      <p className={styles.featureDescription}>{description}</p>
    </div>
  );
}

function FeaturesSection() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className={styles.featuresGrid}>
          <Feature
            icon="🤖"
            title="AI-First Learning"
            description="Master AI-driven development from day one. Build with Claude, Gemini, and OpenAI Agents SDK."
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
          />
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
          <Heading as="h2" className={styles.sectionTitle}>
            Challenging Traditional CS Education
          </Heading>
          <div className={styles.comparisonGrid}>
            <div className={styles.comparisonCard}>
              <div className={styles.comparisonLabel}>Traditional Approach</div>
              <ul className={styles.comparisonList}>
                <li>Learn syntax first, build later</li>
                <li>Memorize algorithms</li>
                <li>Solo problem-solving</li>
                <li>Toy projects and exercises</li>
                <li>Textbook-driven curriculum</li>
              </ul>
            </div>
            <div className={clsx(styles.comparisonCard, styles.comparisonCardHighlight)}>
              <div className={styles.comparisonLabel}>AI-Driven Way</div>
              <ul className={styles.comparisonList}>
                <li>Build production systems from day one</li>
                <li>Understand patterns through AI collaboration</li>
                <li>Pair programming with AI assistants</li>
                <li>Real-world architectures and deployments</li>
                <li>Specification-driven, tool-augmented learning</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function LearningPath() {
  return (
    <section className={styles.pathSection}>
      <div className="container">
        <Heading as="h2" className={styles.sectionTitle}>
          Your Learning Journey
        </Heading>
        <div className={styles.pathGrid}>
          <div className={styles.pathCard}>
            <div className={styles.pathNumber}>01</div>
            <h3>Foundations</h3>
            <p>AI tools, prompt engineering, and Python fundamentals</p>
          </div>
          <div className={styles.pathCard}>
            <div className={styles.pathNumber}>02</div>
            <h3>Agentic AI</h3>
            <p>OpenAI Agents SDK, MCP protocol, and agent orchestration</p>
          </div>
          <div className={styles.pathCard}>
            <div className={styles.pathNumber}>03</div>
            <h3>Cloud Systems</h3>
            <p>Docker, Kubernetes, event-driven architecture, and state management</p>
          </div>
          <div className={styles.pathCard}>
            <div className={styles.pathNumber}>04</div>
            <h3>Production</h3>
            <p>Realtime agents, voice AI, and enterprise deployments</p>
          </div>
        </div>
      </div>
    </section>
  );
}

function FinalCTA() {
  return (
    <section className={styles.ctaSection}>
      <div className="container">
        <div className={styles.ctaContent}>
          <Heading as="h2" className={styles.ctaTitle}>
            Ready to Start Your AI-Driven Learning Journey?
          </Heading>
          <p className={styles.ctaSubtitle}>
            Access the complete free book and explore our comprehensive courses
          </p>
          <div className={styles.ctaButtons}>
            <Link
              className={clsx('button button--primary button--lg', styles.ctaButtonLarge)}
              to="/docs/Introducing-AI-Driven-Development/intro">
              <span className={styles.buttonContent}>
                <span className={styles.buttonText}>Read the Book Free</span>
                <span className={styles.buttonIcon}>→</span>
              </span>
            </Link>
            <Link
              className={clsx('button button--outline button--lg', styles.ctaButtonSecondary)}
              href="https://panaversity.org/flagship-program/courses"
              target="_blank"
              rel="noopener noreferrer">
              <span className={styles.buttonContent}>
                <span className={styles.buttonText}>Explore Courses</span>
                <span className={styles.buttonIcon}>🎓</span>
              </span>
            </Link>
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
      description="Master Python & TypeScript by building production-ready AI systems. Free comprehensive guide with 46 chapters. AI as your co-learner and collaborator.">
      <HomepageHeader />
      <FeaturesSection />
      <ParadigmShift />
      <LearningPath />
      <FinalCTA />
    </Layout>
  );
}
