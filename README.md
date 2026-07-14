# Bynry QA Automation Engineering Internship Case Study

## Candidate

**Name:** Sarvesh Sonawane

**Role Applied:** QA Automation Engineering Intern

---

# Project Overview

This repository contains my solution for the Bynry QA Automation Engineering Internship Case Study.

The objective of this project is to demonstrate my understanding of modern QA Automation practices by designing a scalable automation testing framework for a multi-tenant B2B SaaS application.

The solution focuses on improving flaky tests, designing a maintainable automation framework, implementing API and UI integration testing concepts, and following industry-standard software testing practices.

---

# Technology Stack

- Python
- Pytest
- Playwright
- REST API Testing (Requests)
- BrowserStack (Conceptual Integration)
- Git & GitHub

---

# Repository Structure

```
bynry-qa-automation-case-study/

├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
│
├── api/
│   ├── api_client.py
│   └── project_api.py
│
├── config/
│   └── config.py
│
├── docs/
│   └── Case_Study_Solution.md
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
│
├── test_data/
│   └── users.json
│
├── tests/
│   ├── test_login.py
│   └── test_project_creation.py
│
├── utils/
│   ├── helper.py
│   └── logger.py
│
└── screenshots/
```

---

# Framework Design

The framework follows the **Page Object Model (POM)** architecture to improve code readability, maintainability, and reusability.

The project is divided into multiple modules:

- **Pages** – Contains page classes and UI interactions.
- **Tests** – Contains automated Playwright test cases.
- **API** – Contains reusable API helper methods.
- **Config** – Stores application configuration.
- **Utils** – Contains logging and helper functions.
- **Test Data** – Stores reusable test data.
- **Docs** – Contains the complete case study solution.

---

# Test Automation Strategy

The automation strategy focuses on:

- UI Automation using Playwright
- API Testing using Requests
- Page Object Model (POM)
- Reusable utility methods
- Configuration management
- Scalable folder structure
- Maintainable test scripts

---

# Assumptions

The following assumptions were made while designing the framework:

- Test environment is stable.
- API authentication tokens are available.
- BrowserStack devices are configured separately.
- Test users already exist.
- Test data can be created and cleaned up.
- Login authentication is accessible for automation.

---

# Future Improvements

Given additional time, the framework can be enhanced by implementing:

- Parallel Test Execution
- Docker Support
- GitHub Actions CI/CD
- Allure Reporting
- Cross-Browser Execution
- Mobile Automation
- Accessibility Testing
- Performance Testing
- Visual Regression Testing
- Database Validation

---

# How to Run

## Install dependencies

```bash
pip install -r requirements.txt
```

## Install Playwright browsers

```bash
playwright install
```

## Execute all tests

```bash
pytest
```

---

# Key Learning Outcomes

Through this assessment I learned:

- Designing a scalable QA automation framework.
- Debugging flaky UI tests.
- API and UI integration testing concepts.
- Multi-tenant application testing.
- Automation framework organization.
- Configuration management.
- Page Object Model implementation.
- Importance of reusable and maintainable test automation.

---

# Conclusion

This repository demonstrates my understanding of QA Automation fundamentals and my approach toward building a scalable, maintainable, and reusable automation framework suitable for a multi-tenant SaaS application.

Although this is an internship assessment, I have focused on following industry best practices and writing structured, readable, and maintainable automation code.
