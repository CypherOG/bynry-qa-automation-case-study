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
- 

A maintainable automation framework reduces future maintenance effort while increasing test stability.
---

# Part 2 – Designing a Scalable Automation Framework

## Objective

The primary goal of the automation framework is to provide a reusable, maintainable, and scalable solution for testing a multi-tenant SaaS application.

Instead of writing independent scripts for every feature, the framework separates responsibilities into different modules. This makes the code easier to understand, maintain, and extend.

---

## Proposed Folder Structure

```
bynry-qa-automation-case-study/

├── api/
├── config/
├── docs/
├── pages/
├── test_data/
├── tests/
├── utils/
├── README.md
├── requirements.txt
└── pytest.ini
```

---

## Framework Components

### 1. Pages

The **pages** folder follows the **Page Object Model (POM)** design pattern.

Each page stores:

- UI locators
- User actions
- Page validations

This keeps test scripts clean and reduces duplicate code.

Example:

- Login Page
- Dashboard Page

---

### 2. Tests

The **tests** folder contains the actual test cases.

Examples:

- Login Test
- Project Creation Test

Each test focuses only on validating application behaviour.

---

### 3. API

The **api** folder contains reusable API helper methods.

Examples include:

- Authentication
- Project Creation
- Project Deletion
- User Management

This allows API calls to be reused across multiple tests.

---

### 4. Config

The **config** folder stores application configuration.

Examples:

- Base URL
- Environment
- Browser
- Timeouts

This avoids hardcoding values inside tests.

---

### 5. Utils

The **utils** folder contains reusable helper functions.

Examples:

- Logging
- Random Test Data Generation
- Screenshot Utilities

These utilities can be used across the entire project.

---

### 6. Test Data

The **test_data** folder stores reusable data such as:

- Test users
- Credentials
- Sample projects

Keeping test data separate improves maintainability.

---

## Configuration Management

Rather than hardcoding information, configuration should be stored centrally.

Examples include:

- Base URL
- Username
- Password
- Browser
- Timeout
- Environment

This makes switching between Development, QA, and Production environments much easier.

---

## Logging

Logging should capture:

- Test execution
- API requests
- Failures
- Exceptions

Good logging helps developers quickly identify the root cause of failures.

---

## Reporting

The framework should generate reports after every execution.

Recommended reports include:

- Pytest HTML Report
- Allure Report

Reports should include:

- Passed Tests
- Failed Tests
- Execution Time
- Screenshots for failed tests

---

## BrowserStack Integration

BrowserStack can be used to validate the application on multiple browsers and devices.

Benefits include:

- Cross-browser testing
- Mobile testing
- Parallel execution
- Cloud-based infrastructure

---

## CI/CD Integration

The framework can be integrated with GitHub Actions or Jenkins.

Typical pipeline:

Developer Commit

↓

GitHub

↓

Run Automation Tests

↓

Generate Report

↓

Notify Team

---

## Questions I Would Clarify Before Implementation

Before implementing automation in a real project, I would ask:

- Which environments are available for testing?
- Is database access allowed?
- How are authentication tokens generated?
- Is two-factor authentication enabled?
- How should failed tests be retried?
- What reporting format is preferred?
- What browsers should be supported?
- How should test data be cleaned after execution?

Clarifying these requirements helps avoid incorrect assumptions and ensures the framework meets project needs.

---

## Why This Design?

This framework emphasizes:

- Maintainability
- Reusability
- Scalability
- Readability
- Separation of responsibilities

Following these principles makes the automation suite easier to maintain as the application grows.
