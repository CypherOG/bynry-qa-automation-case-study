# Bynry QA Automation Engineering Internship Case Study

**Candidate:** Sarvesh Sonawane

---

# Executive Summary

This document presents my approach to solving the QA Automation Engineering Internship Case Study.

The objective was not only to write automation scripts but also to design a maintainable, scalable, and reliable automation framework suitable for a multi-tenant SaaS application.

The proposed solution focuses on improving flaky UI tests, designing a reusable automation architecture, and validating application behavior across API and UI layers.

---

# Part 1 – Debugging Flaky Playwright Tests

## Problems Identified

The provided Playwright test contains several issues that can make automated tests unreliable.

### 1. Missing Explicit Waits

The script immediately interacts with UI elements without waiting for them to become visible.

This can cause failures when the application loads slowly.

---

### 2. Hardcoded Credentials

Usernames and passwords are directly written inside the test.

This is not secure and makes maintenance difficult.

Instead, credentials should come from configuration files or environment variables.

---

### 3. Hardcoded URLs

Application URLs are directly embedded inside the test.

Changing environments (Development, QA, Staging, Production) would require editing multiple files.

---

### 4. No Error Handling

If login fails, the script simply stops.

Proper logging and screenshots should be captured whenever a test fails.

---

### 5. Weak Assertions

The original script only checks the final URL.

A stronger validation would confirm that dashboard elements are actually visible.

---

### 6. No Retry Strategy

Temporary network delays may cause false failures.

A retry mechanism improves overall reliability.

---

### 7. Poor Maintainability

The automation directly interacts with locators inside test files.

This violates the Page Object Model design principle.

---

## Proposed Improvements

To improve reliability, I would:

- Implement explicit waits.
- Move locators into Page Object classes.
- Store configuration separately.
- Replace hardcoded credentials.
- Add structured logging.
- Capture screenshots for failed tests.
- Improve assertions.
- Organize reusable utilities.
- Support execution across multiple environments.

---

## Why These Changes?

These improvements make the framework:

- Easier to maintain
- Easier to debug
- More reliable
- Easier to scale as the application grows

A maintainable automation framework reduces future maintenance effort while increasing test stability.
