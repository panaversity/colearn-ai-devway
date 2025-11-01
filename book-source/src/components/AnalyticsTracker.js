"use strict";
/**
 * AnalyticsTracker Component
 *
 * A React component that automatically tracks user interactions:
 * - Page views and navigation
 * - Scroll depth (how far users read)
 * - External link clicks (GitHub, YouTube, etc.)
 * - Time spent on page
 *
 * Usage:
 * Wrap your app or page layout with this component:
 * <AnalyticsTracker>
 *   <YourPageContent />
 * </AnalyticsTracker>
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.AnalyticsTracker = void 0;
var react_1 = require("react");
var router_1 = require("@docusaurus/router");
var analytics_1 = require("@/utils/analytics");
var AnalyticsTracker = function (_a) {
    var children = _a.children, chapterTitle = _a.chapterTitle, part = _a.part, chapterNumber = _a.chapterNumber;
    var location = (0, router_1.useLocation)();
    var startTimeRef = (0, react_1.useRef)(Date.now());
    var _b = (0, react_1.useState)(0), lastScrollDepth = _b[0], setLastScrollDepth = _b[1];
    var _c = (0, react_1.useState)(new Set()), trackedScrollMilestones = _c[0], setTrackedScrollMilestones = _c[1];
    // Track page view and chapter view on mount/navigation
    (0, react_1.useEffect)(function () {
        startTimeRef.current = Date.now();
        setLastScrollDepth(0);
        setTrackedScrollMilestones(new Set());
        // Announce page view to GA4
        if (typeof window !== "undefined" && window.gtag) {
            window.gtag("event", "page_view", {
                page_path: location.pathname,
                page_title: document.title,
            });
        }
        // Track chapter view if metadata provided
        if (chapterTitle && part && chapterNumber !== undefined) {
            (0, analytics_1.trackChapterView)(chapterNumber, chapterTitle, part);
        }
        // Debug log only in development
        if (process.env.NODE_ENV === "development") {
            console.log("\uD83D\uDCCD Navigated to: ".concat(location.pathname));
        }
    }, [location, chapterTitle, part, chapterNumber]);
    // Handle scroll tracking
    (0, react_1.useEffect)(function () {
        var scrollTimeout;
        var handleScroll = function () {
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(function () {
                var scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
                var scrollPercentage = scrollHeight > 0 ? (window.scrollY / scrollHeight) * 100 : 0;
                var roundedPercentage = Math.round(scrollPercentage / 10) * 10; // Round to nearest 10%
                // Track at 25%, 50%, 75%, 100% milestones
                if (!trackedScrollMilestones.has(roundedPercentage) &&
                    roundedPercentage % 25 === 0) {
                    var newMilestones = new Set(trackedScrollMilestones);
                    newMilestones.add(roundedPercentage);
                    setTrackedScrollMilestones(newMilestones);
                    (0, analytics_1.trackScrollDepth)(Math.min(roundedPercentage, 100));
                }
                setLastScrollDepth(roundedPercentage);
            }, 300); // Debounce scroll tracking
        };
        window.addEventListener("scroll", handleScroll, { passive: true });
        return function () {
            window.removeEventListener("scroll", handleScroll);
            clearTimeout(scrollTimeout);
        };
    }, [trackedScrollMilestones]);
    // Handle outbound link tracking
    (0, react_1.useEffect)(function () {
        var handleClick = function (event) {
            var target = event.target;
            var link = target.closest("a");
            if (link && link.href) {
                var href_1 = link.href;
                var isExternal = !href_1.includes(window.location.hostname);
                if (isExternal) {
                    // Determine resource type
                    var resourceType = "external";
                    if (href_1.includes("github.com")) {
                        resourceType = "github";
                    }
                    else if (href_1.includes("youtube.com") ||
                        href_1.includes("youtu.be")) {
                        resourceType = "youtube";
                    }
                    (0, analytics_1.trackResourceClick)(resourceType, href_1, link.textContent || undefined);
                    // For outbound links, add a small delay to ensure GA tracks before navigation
                    if (!link.getAttribute("target")) {
                        event.preventDefault();
                        setTimeout(function () {
                            window.location.href = href_1;
                        }, 200);
                    }
                }
            }
        };
        document.addEventListener("click", handleClick);
        return function () { return document.removeEventListener("click", handleClick); };
    }, []);
    // Track time on page on component unmount
    (0, react_1.useEffect)(function () {
        return function () {
            var timeSpent = (Date.now() - startTimeRef.current) / 1000; // Convert to seconds
            if (timeSpent > 0) {
                (0, analytics_1.trackTimeOnPage)(document.title, timeSpent, chapterTitle);
            }
        };
    }, [chapterTitle]);
    // Render scroll depth indicator in development mode
    var isDevelopment = process.env.NODE_ENV === "development";
    return (<>
      {children}
      {isDevelopment && (<div style={{
                position: "fixed",
                bottom: "20px",
                right: "20px",
                backgroundColor: "rgba(0, 0, 0, 0.7)",
                color: "#fff",
                padding: "10px 15px",
                borderRadius: "5px",
                fontSize: "12px",
                zIndex: 9999,
                fontFamily: "monospace",
                pointerEvents: "none",
            }}>
          📊 Scroll: {Math.round(lastScrollDepth)}%
        </div>)}
    </>);
};
exports.AnalyticsTracker = AnalyticsTracker;
exports.default = exports.AnalyticsTracker;
