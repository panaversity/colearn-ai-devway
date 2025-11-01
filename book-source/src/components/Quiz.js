"use strict";
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", { value: true });
var react_1 = require("react");
var Quiz_module_css_1 = require("./Quiz.module.css");
var Quiz = function (_a) {
    var _b = _a.title, title = _b === void 0 ? "Quiz" : _b, questions = _a.questions, _c = _a.passingScore, passingScore = _c === void 0 ? 70 : _c;
    var _d = (0, react_1.useState)(0), currentQuestion = _d[0], setCurrentQuestion = _d[1];
    var _e = (0, react_1.useState)(new Array(questions.length).fill(null)), selectedAnswers = _e[0], setSelectedAnswers = _e[1];
    var _f = (0, react_1.useState)(false), showResults = _f[0], setShowResults = _f[1];
    var _g = (0, react_1.useState)(new Set()), answeredQuestions = _g[0], setAnsweredQuestions = _g[1];
    var handleAnswerSelect = function (optionIndex) {
        var newAnswers = __spreadArray([], selectedAnswers, true);
        newAnswers[currentQuestion] = optionIndex;
        setSelectedAnswers(newAnswers);
        var newAnswered = new Set(answeredQuestions);
        newAnswered.add(currentQuestion);
        setAnsweredQuestions(newAnswered);
    };
    var handleNext = function () {
        if (currentQuestion < questions.length - 1) {
            setCurrentQuestion(currentQuestion + 1);
        }
    };
    var handleBack = function () {
        if (currentQuestion > 0) {
            setCurrentQuestion(currentQuestion - 1);
        }
    };
    var handleSubmit = function () {
        setShowResults(true);
    };
    var handleReset = function () {
        setCurrentQuestion(0);
        setSelectedAnswers(new Array(questions.length).fill(null));
        setShowResults(false);
        setAnsweredQuestions(new Set());
    };
    var calculateScore = function () {
        var correct = 0;
        selectedAnswers.forEach(function (answer, index) {
            if (answer === questions[index].correctOption) {
                correct++;
            }
        });
        return {
            correct: correct,
            total: questions.length,
            percentage: Math.round((correct / questions.length) * 100)
        };
    };
    var score = calculateScore();
    var allAnswered = selectedAnswers.every(function (answer) { return answer !== null; });
    if (showResults) {
        var passed = score.percentage >= passingScore;
        return (<div className={Quiz_module_css_1.default.quizContainer}>
        <div className={Quiz_module_css_1.default.resultsCard}>
          <div className={Quiz_module_css_1.default.resultsHeader}>
            <h2 className={Quiz_module_css_1.default.resultsTitle}>Quiz Results</h2>
            <div className={"".concat(Quiz_module_css_1.default.scoreCircle, " ").concat(passed ? Quiz_module_css_1.default.passed : Quiz_module_css_1.default.failed)}>
              <div className={Quiz_module_css_1.default.scorePercentage}>{score.percentage}%</div>
              <div className={Quiz_module_css_1.default.scoreLabel}>Score</div>
            </div>
          </div>

          <div className={Quiz_module_css_1.default.resultsStats}>
            <div className={Quiz_module_css_1.default.statItem}>
              <span className={Quiz_module_css_1.default.statValue}>{score.correct}</span>
              <span className={Quiz_module_css_1.default.statLabel}>Correct</span>
            </div>
            <div className={Quiz_module_css_1.default.statItem}>
              <span className={Quiz_module_css_1.default.statValue}>{score.total - score.correct}</span>
              <span className={Quiz_module_css_1.default.statLabel}>Incorrect</span>
            </div>
            <div className={Quiz_module_css_1.default.statItem}>
              <span className={Quiz_module_css_1.default.statValue}>{score.total}</span>
              <span className={Quiz_module_css_1.default.statLabel}>Total</span>
            </div>
          </div>

          <div className={"".concat(Quiz_module_css_1.default.resultMessage, " ").concat(passed ? Quiz_module_css_1.default.passMessage : Quiz_module_css_1.default.failMessage)}>
            {passed ? (<>
                <span className={Quiz_module_css_1.default.resultIcon}>🎉</span>
                <strong>Congratulations!</strong> You passed the quiz!
              </>) : (<>
                <span className={Quiz_module_css_1.default.resultIcon}>📚</span>
                <strong>Keep Learning!</strong> Review the material and try again.
              </>)}
          </div>

          <div className={Quiz_module_css_1.default.detailedResults}>
            <h3 className={Quiz_module_css_1.default.detailedResultsTitle}>Question Review</h3>
            {questions.map(function (q, index) {
                var userAnswer = selectedAnswers[index];
                var isCorrect = userAnswer === q.correctOption;
                return (<div key={index} className={Quiz_module_css_1.default.reviewItem}>
                  <div className={Quiz_module_css_1.default.reviewHeader}>
                    <span className={Quiz_module_css_1.default.reviewQuestionNumber}>Question {index + 1}</span>
                    <span className={"".concat(Quiz_module_css_1.default.reviewBadge, " ").concat(isCorrect ? Quiz_module_css_1.default.correctBadge : Quiz_module_css_1.default.incorrectBadge)}>
                      {isCorrect ? '✓ Correct' : '✗ Incorrect'}
                    </span>
                  </div>
                  <p className={Quiz_module_css_1.default.reviewQuestion}>{q.question}</p>
                  <div className={Quiz_module_css_1.default.reviewAnswers}>
                    <div className={Quiz_module_css_1.default.reviewAnswer}>
                      <strong>Your answer:</strong>{' '}
                      <span className={isCorrect ? Quiz_module_css_1.default.correctText : Quiz_module_css_1.default.incorrectText}>
                        {userAnswer !== null ? q.options[userAnswer] : 'Not answered'}
                      </span>
                    </div>
                    {!isCorrect && (<div className={Quiz_module_css_1.default.reviewAnswer}>
                        <strong>Correct answer:</strong>{' '}
                        <span className={Quiz_module_css_1.default.correctText}>
                          {q.options[q.correctOption]}
                        </span>
                      </div>)}
                    {q.explanation && (<div className={Quiz_module_css_1.default.explanation}>
                        <strong>Explanation:</strong> {q.explanation}
                      </div>)}
                  </div>
                </div>);
            })}
          </div>

          <button onClick={handleReset} className={Quiz_module_css_1.default.resetButton}>
            Retake Quiz
          </button>
        </div>
      </div>);
    }
    var question = questions[currentQuestion];
    var selectedAnswer = selectedAnswers[currentQuestion];
    var progress = ((currentQuestion + 1) / questions.length) * 100;
    return (<div className={Quiz_module_css_1.default.quizContainer}>
      <div className={Quiz_module_css_1.default.quizCard}>
        <div className={Quiz_module_css_1.default.quizHeader}>
          <h2 className={Quiz_module_css_1.default.quizTitle}>{title}</h2>
          <div className={Quiz_module_css_1.default.questionCounter}>
            Question {currentQuestion + 1} of {questions.length}
          </div>
        </div>

        <div className={Quiz_module_css_1.default.progressBar}>
          <div className={Quiz_module_css_1.default.progressFill} style={{ width: "".concat(progress, "%") }}/>
        </div>

        <div className={Quiz_module_css_1.default.questionSection}>
          <h3 className={Quiz_module_css_1.default.questionText}>{question.question}</h3>

          <div className={Quiz_module_css_1.default.optionsGrid}>
            {question.options.map(function (option, index) { return (<button key={index} className={"".concat(Quiz_module_css_1.default.optionButton, " ").concat(selectedAnswer === index ? Quiz_module_css_1.default.selected : '')} onClick={function () { return handleAnswerSelect(index); }}>
                <span className={Quiz_module_css_1.default.optionLetter}>
                  {String.fromCharCode(65 + index)}
                </span>
                <span className={Quiz_module_css_1.default.optionText}>{option}</span>
                {selectedAnswer === index && (<span className={Quiz_module_css_1.default.checkmark}>✓</span>)}
              </button>); })}
          </div>
        </div>

        <div className={Quiz_module_css_1.default.navigationSection}>
          <div className={Quiz_module_css_1.default.answeredIndicator}>
            Answered: {answeredQuestions.size} / {questions.length}
          </div>

          <div className={Quiz_module_css_1.default.navigationButtons}>
            <button onClick={handleBack} disabled={currentQuestion === 0} className={"".concat(Quiz_module_css_1.default.navButton, " ").concat(Quiz_module_css_1.default.backButton)}>
              ← Back
            </button>

            {currentQuestion === questions.length - 1 ? (<button onClick={handleSubmit} disabled={!allAnswered} className={"".concat(Quiz_module_css_1.default.navButton, " ").concat(Quiz_module_css_1.default.submitButton)} title={!allAnswered ? 'Please answer all questions' : ''}>
                Submit Quiz
              </button>) : (<button onClick={handleNext} className={"".concat(Quiz_module_css_1.default.navButton, " ").concat(Quiz_module_css_1.default.nextButton)}>
                Next →
              </button>)}
          </div>
        </div>

        <div className={Quiz_module_css_1.default.questionDots}>
          {questions.map(function (_, index) { return (<button key={index} className={"".concat(Quiz_module_css_1.default.dot, " ").concat(index === currentQuestion ? Quiz_module_css_1.default.activeDot : '', " ").concat(answeredQuestions.has(index) ? Quiz_module_css_1.default.answeredDot : '')} onClick={function () { return setCurrentQuestion(index); }} title={"Question ".concat(index + 1)}/>); })}
        </div>
      </div>
    </div>);
};
exports.default = Quiz;
