"use strict";
/**
 * Docusaurus Root Component
 *
 * This component wraps the entire site with the AnalyticsTracker,
 * enabling automatic tracking of user interactions (page views, scroll depth, etc.)
 *
 * GA4 is configured via the GA4_MEASUREMENT_ID environment variable.
 * If not set, analytics will not load.
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = Root;
var react_1 = require("react");
var AnalyticsTracker_1 = require("@/components/AnalyticsTracker");
function Root(_a) {
    var children = _a.children;
    return (<AnalyticsTracker_1.AnalyticsTracker>
      {children}
    </AnalyticsTracker_1.AnalyticsTracker>);
}
