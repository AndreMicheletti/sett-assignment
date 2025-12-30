# Sett — AI Playables Engineer Candidate Task

## 🎯 Objective

Create, iterate, and fix a small HTML5 playable called **Fishing-In-The-Deep** using a combination of **AI tools** and **your own reasoning**.

We want to see:

* How you think through the **generative process**.
* How you **iterate between planning and implementation**.
* How you **balance AI automation with manual problem-solving**.
* The focus is on the creation process more **than** on the playable result at the end (you will not necessarily finish with a great playable because of the time limit and we are aware of that, also there is no need to integrate assets and code genereted primitives are completly fine).

🕒 Estimated total time: **~3 hours** (you may complete it over the next day).

---

## 📂 Folder Structure

```text
Sett_AI_Playables_Engineer_Test/
│
├── 0_README_Task_Instructions.md     ← (You’re here)
├── 1_PRD_Fishing_In_The_Deep.md       ← Full game specification (must be followed)
├── 2_Planning_Prompt_Template.txt     ← Base planning prompt (you may modify it)
├── 3_Submission_checklist.txt         ← Final checks before submission
├── example_playable.html              ← Visual reference for the expected behavior
└── assets/                            ← Game assets you should use
```

---

## 🧠 Inputs

### 1. `1_PRD_Fishing_In_The_Deep.md`

This is the **authoritative Product Requirements Document**.
Your playable must align closely with this document’s gameplay flow, mechanics, and rules.
**Do not edit or change the PRD file.**

### 2. `example_playable.html`

This is an example playable showing how a similar game looks and feels.
Your result should be similar to this playable but with primitives.

### 3. `2_Prompts_Template.txt`

A baseline planning prompt designed to help you generate your initial implementation plan.
A baseline of the prompt to trigger the implementation.

You are **free—and encouraged—to modify, expand, or replace** those **prompts** to get better outputs.

You may regenerate the outputs **via ChatGPT** as many times as you like.
However, do not manually edit the plan you got as output, the idea is to head towards an automated process.

---

## 🔁 Process

You can move freely between:

1. **Planning** – use GPT-5.1 with the planning prompt to create an implementation plan.
2. **Implementation** – use GPT-5.1 to generate code for the initial implementation.
3. **Fixing & Iteration** – run the game, find issues, and:

   * Adjust your prompts to improve the **plan**.
   * Adjust your prompt that triggers the initial implementation.
   * Do **manual code fixes** or use GPT with vibe-coding where needed.

**Rules:**

* You must use **the company ChatGPT environment (GPT-5.1 via api key)** for generations.
* The playable will be implemented as a **single HTML5 file**.
* Commit your changes so we will have visibility on the complete process together with the GPT logs.
* **Up to one third of your total work time may be dedicated to improving the chosen implementation output.**
* Check the `3_Submission_checklist.txt` before final submission.

---

## 🔍 Evaluation Focus

| Dimension                           | What We Observe                                                                       |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| **Systemic Thinking**               | How planning, code, and feedback connect.                                             |
| **Prompt Literacy**                 | How precisely you steer the AI and refine prompts.                                    |
| **Technical Depth**                 | HTML5/TypeScript/JS understanding, ability to reason about code and browser behavior. |
| **Documentation & Decision Making** | The process is clear, transparent, and reasonable. Your thought process is visible.   |

---

## 💡 Tip

Think of this task as a **mini case study** of how you interact with AI and playables.

* The main thing we care about here is your **process**.
* It’s **not critical** if the game isn’t 100% complete or perfectly polished.
* Try to make us understand easily what you have done, when, and why through organized commits and full logs.
