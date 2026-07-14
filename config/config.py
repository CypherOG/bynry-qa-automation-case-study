import os

class Config:
    BASE_URL = "https://app.workflowpro.com"

    USERNAME = os.getenv("USERNAME", "admin@company1.com")
    PASSWORD = os.getenv("PASSWORD", "password123")

    API_URL = "https://app.workflowpro.com/api/v1"

    TIMEOUT = 15000

    BROWSER = "chromium"

    HEADLESS = True
