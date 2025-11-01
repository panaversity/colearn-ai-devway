"use strict";
/**
 * Analytics Utility Module
 *
 * Custom event tracking for GA4
 * Track chapter views, external resource clicks, scroll depth, and engagement
 *
 * Usage:
 * import { trackChapterView, trackResourceClick, trackScrollDepth } from '@/utils/analytics';
 * trackChapterView(1, 'Introducing AI-Driven Development', 'Part 1');
 */
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.trackCustomEvent = exports.trackLearnerSegment = exports.trackDownload = exports.trackQuizInteraction = exports.trackCodeInteraction = exports.trackTimeOnPage = exports.trackScrollDepth = exports.trackResourceClick = exports.trackChapterView = void 0;
// Helper to check if we're in development mode
var isDevelopment = function () { return process.env.NODE_ENV === "development"; };
// Helper for debug logging (only in development)
var debugLog = function (message) {
    if (isDevelopment()) {
        console.log(message);
    }
};
/**
 * Track when a chapter/lesson is viewed
 * @param chapterNumber - The chapter number (1, 2, 3, etc.)
 * @param chapterTitle - The title of the chapter
 * @param part - The part number or name (e.g., "Part 1", "Preface")
 */
var trackChapterView = function (chapterNumber, chapterTitle, part) {
    if (typeof window !== "undefined" && window.gtag) {
        window.gtag("event", "chapter_view", {
            chapter_number: chapterNumber,
            chapter_title: chapterTitle,
            part: part,
            timestamp: new Date().toISOString(),
        });
        debugLog("\uD83D\uDCCA Analytics: Chapter viewed - ".concat(part, ": ").concat(chapterTitle));
    }
};
exports.trackChapterView = trackChapterView;
/**
 * Track when external resources are clicked
 * @param resourceType - Type of resource ('github', 'youtube', 'docs', 'external')
 * @param url - The URL of the resource
 * @param label - Optional label for the resource
 */
var trackResourceClick = function (resourceType, url, label) {
    if (typeof window !== "undefined" && window.gtag) {
        window.gtag("event", "resource_click", {
            resource_type: resourceType,
            url: url,
            label: label || url,
            timestamp: new Date().toISOString(),
        });
        debugLog("\uD83D\uDCCA Analytics: ".concat(resourceType, " clicked - ").concat(label || url));
    }
};
exports.trackResourceClick = trackResourceClick;
/**
 * Track scroll depth as percentage of page scrolled
 * @param depthPercentage - Percentage of page scrolled (0-100)
 */
var trackScrollDepth = function (depthPercentage) {
    if (typeof window !== "undefined" && window.gtag) {
        // Only log significant scroll milestones to reduce noise
        var milestone = Math.floor(depthPercentage / 25) * 25;
        if (depthPercentage >= milestone) {
            window.gtag("event", "scroll_depth", {
                scroll_percentage: Math.min(depthPercentage, 100),
                page_title: document.title,
                timestamp: new Date().toISOString(),
            });
            debugLog("\uD83D\uDCCA Analytics: Scroll depth - ".concat(Math.min(depthPercentage, 100), "%"));
        }
    }
};
exports.trackScrollDepth = trackScrollDepth;
/**
 * Track time spent on a specific page
 * @param pageTitle - Title of the page
 * @param secondsSpent - Number of seconds spent on the page
 * @param chapter - Optional chapter identifier
 */
var trackTimeOnPage = function (pageTitle, secondsSpent, chapter) {
    if (typeof window !== "undefined" && window.gtag) {
        // Only track if user spent meaningful time (>5 seconds)
        if (secondsSpent > 5) {
            window.gtag("event", "page_engagement", {
                page_title: pageTitle,
                seconds_spent: Math.round(secondsSpent),
                chapter: chapter,
                timestamp: new Date().toISOString(),
            });
            debugLog("\uD83D\uDCCA Analytics: Page engagement - ".concat(pageTitle, " (").concat(Math.round(secondsSpent), "s)"));
        }
    }
};
exports.trackTimeOnPage = trackTimeOnPage;
/**
 * Track code block interactions (copy, view, etc.)
 * @param action - Action taken ('copy', 'expand', 'view')
 * @param codeLanguage - Programming language of the code block
 * @param chapter - Chapter where code block is located
 */
var trackCodeInteraction = function (action, codeLanguage, chapter) {
    if (typeof window !== "undefined" && window.gtag) {
        window.gtag("event", "code_interaction", {
            action: action,
            language: codeLanguage,
            chapter: chapter,
            timestamp: new Date().toISOString(),
        });
        debugLog("\uD83D\uDCCA Analytics: Code ".concat(action, " - ").concat(codeLanguage));
    }
};
exports.trackCodeInteraction = trackCodeInteraction;
/**
 * Track quiz or assessment interactions
 * @param action - Action taken ('start', 'complete', 'answer')
 * @param quizTitle - Title of the quiz
 * @param score - Optional score achieved
 * @param chapter - Chapter containing the quiz
 */
var trackQuizInteraction = function (action, quizTitle, score, chapter) {
    if (typeof window !== "undefined" && window.gtag) {
        window.gtag("event", "quiz_interaction", {
            action: action,
            quiz_title: quizTitle,
            score: score,
            chapter: chapter,
            timestamp: new Date().toISOString(),
        });
        debugLog("\uD83D\uDCCA Analytics: Quiz ".concat(action, " - ").concat(quizTitle));
    }
};
exports.trackQuizInteraction = trackQuizInteraction;
/**
 * Track file or resource downloads
 * @param fileName - Name of the file downloaded
 * @param fileType - Type of file (pdf, code, notebook, etc.)
 * @param chapter - Chapter where download was initiated
 */
var trackDownload = function (fileName, fileType, chapter) {
    if (typeof window !== "undefined" && window.gtag) {
        window.gtag("event", "file_download", {
            file_name: fileName,
            file_type: fileType,
            chapter: chapter,
            timestamp: new Date().toISOString(),
        });
        debugLog("\uD83D\uDCCA Analytics: Downloaded - ".concat(fileName));
    }
};
exports.trackDownload = trackDownload;
/**
 * Track learner segment/cohort
 * Helps segment users (e.g., 'beginner', 'experienced', 'educator')
 * @param segment - Learner segment identifier
 */
var trackLearnerSegment = function (segment) {
    if (typeof window !== "undefined" && window.gtag) {
        window.gtag("set", { user_segment: segment });
        window.gtag("event", "learner_segment", {
            segment: segment,
            timestamp: new Date().toISOString(),
        });
        debugLog("\uD83D\uDCCA Analytics: Learner segment - ".concat(segment));
    }
};
exports.trackLearnerSegment = trackLearnerSegment;
/**
 * Track custom event with flexible properties
 * Use this for tracking events not covered by other functions
 * @param eventName - Name of the custom event
 * @param eventData - Object containing event properties
 */
var trackCustomEvent = function (eventName, eventData) {
    if (typeof window !== "undefined" && window.gtag) {
        window.gtag("event", eventName, __assign(__assign({}, eventData), { timestamp: new Date().toISOString() }));
        debugLog("\uD83D\uDCCA Analytics: ".concat(eventName, " - ").concat(JSON.stringify(eventData)));
    }
};
exports.trackCustomEvent = trackCustomEvent;
