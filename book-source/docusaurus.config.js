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
var prism_react_renderer_1 = require("prism-react-renderer");
// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)
var config = {
    title: "AI Native Software Development",
    tagline: "Colearning Agentic AI with Python and TypeScript – The AI & Spec Driven Way",
    favicon: "img/favicon.ico",
    // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
    future: {
        v4: true, // Improve compatibility with the upcoming Docusaurus v4
    },
    // Set the production url of your site here
    url: "https://ai-native.panaversity.org",
    // Set the /<baseUrl>/ pathname under which your site is served
    // For GitHub pages deployment, it is often '/<projectName>/'
    baseUrl: "/",
    // GitHub pages deployment config.
    // If you aren't using GitHub pages, you don't need these.
    organizationName: "panaversity", // Usually your GitHub org/user name.
    projectName: "ai-native-software-development", // Usually your repo name.
    trailingSlash: false,
    onBrokenLinks: "warn",
    // Add Font Awesome for social media icons
    headTags: __spreadArray([
        {
            tagName: "link",
            attributes: {
                rel: "stylesheet",
                href: "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css",
                integrity: "sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==",
                crossorigin: "anonymous",
                referrerpolicy: "no-referrer",
            },
        }
    ], (process.env.GA4_MEASUREMENT_ID
        ? [
            {
                tagName: "script",
                attributes: {
                    async: "true",
                    src: "https://www.googletagmanager.com/gtag/js?id=".concat(process.env.GA4_MEASUREMENT_ID),
                },
            },
            {
                tagName: "script",
                attributes: {},
                innerHTML: "\n          window.dataLayer = window.dataLayer || [];\n          function gtag(){dataLayer.push(arguments);}\n          gtag('js', new Date());\n          gtag('config', '".concat(process.env.GA4_MEASUREMENT_ID, "', {\n            'anonymize_ip': true,\n            'allow_google_signals': false,\n            'allow_ad_personalization_signals': false\n          });\n        "),
            },
        ]
        : []), true),
    // Even if you don't use internationalization, you can use this field to set
    // useful metadata like html lang. For example, if your site is Chinese, you
    // may want to replace "en" with "zh-Hans".
    i18n: {
        defaultLocale: "en",
        locales: ["en"],
    },
    presets: [
        [
            "classic",
            {
                docs: {
                    sidebarPath: "./sidebars.ts",
                    // Please change this to your repo.
                    // Remove this to remove the "edit this page" links.
                    editUrl: "https://github.com/panaversity/ai-native-software-development/tree/main/website/",
                },
                blog: false,
                theme: {
                    customCss: "./src/css/custom.css",
                },
            },
        ],
    ],
    plugins: [
        function (context, options) {
            return {
                name: "custom-webpack-config",
                configureWebpack: function (config, isServer, utils) {
                    var path = require("path");
                    return {
                        resolve: {
                            alias: {
                                "@": path.resolve(__dirname, "src"),
                            },
                        },
                    };
                },
            };
        },
    ],
    themeConfig: {
        // Replace with your project's social card
        image: "img/book-cover-page.png",
        colorMode: {
            respectPrefersColorScheme: true,
        },
        docs: {
            sidebar: {
                hideable: true,
            },
        },
        navbar: {
            title: "AI Native Development",
            // logo: {
            //   alt: 'Panaversity Logo',
            //   src: 'img/book-cover.png',
            //   width: 32,
            //   height: 32,
            // },
            hideOnScroll: false,
            items: [
                {
                    type: "docSidebar",
                    sidebarId: "tutorialSidebar",
                    position: "left",
                    label: "Book",
                },
                {
                    href: "https://github.com/panaversity/ai-native-software-development",
                    label: "GitHub",
                    position: "right",
                },
            ],
        },
        footer: {
            style: "dark",
            links: [
                {
                    title: "Learn",
                    items: [
                        {
                            label: "Start Your Journey",
                            to: "/docs/preface-agent-native",
                        },
                        {
                            label: "Full Curriculum",
                            to: "/docs/preface-agent-native",
                        },
                        {
                            label: "Learning Path",
                            to: "/#learning-path",
                        },
                    ],
                },
                {
                    title: "Community",
                    items: [
                        {
                            label: "YouTube",
                            href: "https://youtube.com/@panaversity",
                        },
                        {
                            label: "LinkedIn",
                            href: "https://linkedin.com/company/panaversity",
                        },
                        {
                            label: "Instagram",
                            href: "https://instagram.com/panaversity",
                        },
                        {
                            label: "Facebook",
                            href: "https://facebook.com/panaversity",
                        },
                    ],
                },
                {
                    title: "Resources",
                    items: [
                        {
                            label: "GitHub Repository",
                            href: "https://github.com/panaversity/ai-native-software-development",
                        },
                        {
                            label: "AI Native Specification",
                            href: "https://github.com/panaversity/ai-native-software-development/tree/main/specs",
                        },
                        {
                            label: "Example Projects",
                            href: "https://github.com/panaversity",
                        },
                    ],
                },
                {
                    title: "About",
                    items: [
                        {
                            label: "Panaversity",
                            href: "https://panaversity.org/",
                        },
                        {
                            label: "Our Mission",
                            href: "https://panaversity.org/#about",
                        },
                    ],
                },
            ],
            copyright: "Copyright \u00A9 ".concat(new Date().getFullYear(), " <strong>Panaversity</strong> \u2022 AI Native Software Development \u2022 100% Free & Open Source"),
        },
        prism: {
            theme: prism_react_renderer_1.themes.github,
            darkTheme: prism_react_renderer_1.themes.dracula,
        },
    },
};
exports.default = config;
