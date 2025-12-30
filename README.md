# Sett Assignment

## How to follow history

The project was developed to use python to trigger and generate ChatGPT responses.

Using prompts defined in files at `prompts/`, the script generates the desired plan
and then generates the implementation.

Each generation attempts was commited with prefix `gpt:`
The generation attemps follows a:
- Edit to the input prompts
- The generation result from ChatGPT

The results are stored in `results/`

So, you can follow the generation history by following commit history.

## Best results and Final Result

The best results were saved under `best_results/` for keeping track of what
worked.

The result chosen to be worked upon is `best_results/2025_12_30__07_51`

The final result was selected and placed under `final_result/`.
This was the implementation that were manually edited and improved.

## Final Result

You can check the final implementation on:
`final_result/implementation.html`

## GPT Logs

The logs from AI usage, other than generating the plan and implementation, can be found here:
[chatgpt.com/share/6953c73b-6f04-8002-a9f5-a0bf0b305a28](https://chatgpt.com/share/6953c73b-6f04-8002-a9f5-a0bf0b305a28)

## Question Answers

#### How did you pick and evaluate the plan to use for the implementation generation?

  A: I evaluate how well the prompt translated the PDV requirements into planned actions/code, and also evaluated the prepared code on the plan. I found out that focusing on code specifics
  generate better results.

#### How did you pick the initial implementation version you modified to create the final playable?

  A: I selected the most complete version generated, that had all the groundings to work only on details. Taking into account: the general visual aspect, the buttons and interactions funcionality and gameplay flow and requirement satisfaction.

#### Describe the process you followed for this task.

  A: I decided to start by automating the prompt requesting to GPT using a file structure, the goal was that I needed only to edit the input prompt files and run the code to generate and test results, while also using git to register each step.

  Then I started to verify the plan output from GPT and try to correct and steer it to guide the
  implementation to use a structured code. The plan containing code definitions and patterns worked better.

### Describe how much time approximately you spend on planning generation, implementation generation and on the fixes to get the final playable version.

A: I spent 80-90% of the time on planning generation and testing plan output and implementation output. The last 10% was used on the fixes to the final version, as it was already very satisfactory.

