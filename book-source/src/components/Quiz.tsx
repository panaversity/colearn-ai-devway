import React, { useState } from 'react';
import styles from './Quiz.module.css';

export interface QuizQuestion {
  question: string;
  options: [string, string, string, string];
  correctOption: 0 | 1 | 2 | 3;
  explanation?: string;
}

export interface QuizProps {
  title?: string;
  questions: QuizQuestion[];
  passingScore?: number;
}

const Quiz: React.FC<QuizProps> = ({
  title = "Quiz",
  questions,
  passingScore = 70
}) => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState<(number | null)[]>(
    new Array(questions.length).fill(null)
  );
  const [showResults, setShowResults] = useState(false);
  const [answeredQuestions, setAnsweredQuestions] = useState<Set<number>>(new Set());

  const handleAnswerSelect = (optionIndex: number) => {
    const newAnswers = [...selectedAnswers];
    newAnswers[currentQuestion] = optionIndex;
    setSelectedAnswers(newAnswers);

    const newAnswered = new Set(answeredQuestions);
    newAnswered.add(currentQuestion);
    setAnsweredQuestions(newAnswered);
  };

  const handleNext = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    }
  };

  const handleBack = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  };

  const handleSubmit = () => {
    setShowResults(true);
  };

  const handleReset = () => {
    setCurrentQuestion(0);
    setSelectedAnswers(new Array(questions.length).fill(null));
    setShowResults(false);
    setAnsweredQuestions(new Set());
  };

  const calculateScore = () => {
    let correct = 0;
    selectedAnswers.forEach((answer, index) => {
      if (answer === questions[index].correctOption) {
        correct++;
      }
    });
    return {
      correct,
      total: questions.length,
      percentage: Math.round((correct / questions.length) * 100)
    };
  };

  const score = calculateScore();
  const allAnswered = selectedAnswers.every(answer => answer !== null);

  if (showResults) {
    const passed = score.percentage >= passingScore;

    return (
      <div className={styles.quizContainer}>
        <div className={styles.resultsCard}>
          <div className={styles.resultsHeader}>
            <h2 className={styles.resultsTitle}>Quiz Results</h2>
            <div className={`${styles.scoreCircle} ${passed ? styles.passed : styles.failed}`}>
              <div className={styles.scorePercentage}>{score.percentage}%</div>
              <div className={styles.scoreLabel}>Score</div>
            </div>
          </div>

          <div className={styles.resultsStats}>
            <div className={styles.statItem}>
              <span className={styles.statValue}>{score.correct}</span>
              <span className={styles.statLabel}>Correct</span>
            </div>
            <div className={styles.statItem}>
              <span className={styles.statValue}>{score.total - score.correct}</span>
              <span className={styles.statLabel}>Incorrect</span>
            </div>
            <div className={styles.statItem}>
              <span className={styles.statValue}>{score.total}</span>
              <span className={styles.statLabel}>Total</span>
            </div>
          </div>

          <div className={`${styles.resultMessage} ${passed ? styles.passMessage : styles.failMessage}`}>
            {passed ? (
              <>
                <span className={styles.resultIcon}>🎉</span>
                <strong>Congratulations!</strong> You passed the quiz!
              </>
            ) : (
              <>
                <span className={styles.resultIcon}>📚</span>
                <strong>Keep Learning!</strong> Review the material and try again.
              </>
            )}
          </div>

          <div className={styles.detailedResults}>
            <h3 className={styles.detailedResultsTitle}>Question Review</h3>
            {questions.map((q, index) => {
              const userAnswer = selectedAnswers[index];
              const isCorrect = userAnswer === q.correctOption;

              return (
                <div key={index} className={styles.reviewItem}>
                  <div className={styles.reviewHeader}>
                    <span className={styles.reviewQuestionNumber}>Question {index + 1}</span>
                    <span className={`${styles.reviewBadge} ${isCorrect ? styles.correctBadge : styles.incorrectBadge}`}>
                      {isCorrect ? '✓ Correct' : '✗ Incorrect'}
                    </span>
                  </div>
                  <p className={styles.reviewQuestion}>{q.question}</p>
                  <div className={styles.reviewAnswers}>
                    <div className={styles.reviewAnswer}>
                      <strong>Your answer:</strong>{' '}
                      <span className={isCorrect ? styles.correctText : styles.incorrectText}>
                        {userAnswer !== null ? q.options[userAnswer] : 'Not answered'}
                      </span>
                    </div>
                    {!isCorrect && (
                      <div className={styles.reviewAnswer}>
                        <strong>Correct answer:</strong>{' '}
                        <span className={styles.correctText}>
                          {q.options[q.correctOption]}
                        </span>
                      </div>
                    )}
                    {q.explanation && (
                      <div className={styles.explanation}>
                        <strong>Explanation:</strong> {q.explanation}
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>

          <button
            onClick={handleReset}
            className={styles.resetButton}
          >
            Retake Quiz
          </button>
        </div>
      </div>
    );
  }

  const question = questions[currentQuestion];
  const selectedAnswer = selectedAnswers[currentQuestion];
  const progress = ((currentQuestion + 1) / questions.length) * 100;

  return (
    <div className={styles.quizContainer}>
      <div className={styles.quizCard}>
        <div className={styles.quizHeader}>
          <h2 className={styles.quizTitle}>{title}</h2>
          <div className={styles.questionCounter}>
            Question {currentQuestion + 1} of {questions.length}
          </div>
        </div>

        <div className={styles.progressBar}>
          <div
            className={styles.progressFill}
            style={{ width: `${progress}%` }}
          />
        </div>

        <div className={styles.questionSection}>
          <h3 className={styles.questionText}>{question.question}</h3>

          <div className={styles.optionsGrid}>
            {question.options.map((option, index) => (
              <button
                key={index}
                className={`${styles.optionButton} ${
                  selectedAnswer === index ? styles.selected : ''
                }`}
                onClick={() => handleAnswerSelect(index)}
              >
                <span className={styles.optionLetter}>
                  {String.fromCharCode(65 + index)}
                </span>
                <span className={styles.optionText}>{option}</span>
                {selectedAnswer === index && (
                  <span className={styles.checkmark}>✓</span>
                )}
              </button>
            ))}
          </div>
        </div>

        <div className={styles.navigationSection}>
          <div className={styles.answeredIndicator}>
            Answered: {answeredQuestions.size} / {questions.length}
          </div>

          <div className={styles.navigationButtons}>
            <button
              onClick={handleBack}
              disabled={currentQuestion === 0}
              className={`${styles.navButton} ${styles.backButton}`}
            >
              ← Back
            </button>

            {currentQuestion === questions.length - 1 ? (
              <button
                onClick={handleSubmit}
                disabled={!allAnswered}
                className={`${styles.navButton} ${styles.submitButton}`}
                title={!allAnswered ? 'Please answer all questions' : ''}
              >
                Submit Quiz
              </button>
            ) : (
              <button
                onClick={handleNext}
                className={`${styles.navButton} ${styles.nextButton}`}
              >
                Next →
              </button>
            )}
          </div>
        </div>

        <div className={styles.questionDots}>
          {questions.map((_, index) => (
            <button
              key={index}
              className={`${styles.dot} ${
                index === currentQuestion ? styles.activeDot : ''
              } ${answeredQuestions.has(index) ? styles.answeredDot : ''}`}
              onClick={() => setCurrentQuestion(index)}
              title={`Question ${index + 1}`}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Quiz;
