const { test, expect } = require("@playwright/test");

test("shows core v1 flow", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByText("Job Application Agent")).toBeVisible();
  await expect(page.getByText("Simple v1: one resume, one JD, one focused analysis.")).toBeVisible();
  await page.locator('input[type="file"]').setInputFiles("tests/resume.txt");
  await page.getByLabel("Paste job description").fill("Need FastAPI and Streamlit skills.");
  await expect(page.getByRole("button", { name: "Analyze" })).toBeEnabled();
});
