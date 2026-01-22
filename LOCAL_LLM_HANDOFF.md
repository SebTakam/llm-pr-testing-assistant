Local LLM / Human Completion (Final Step)
diff


At this stage:
- Test plan is approved
- Test structure is approved
- No test implementations exist

Next steps (choose one):

OPTION A — Human
- Pull branch
- Implement tests manually using structure as guide

OPTION B — Local LLM (recommended)
- Load repo into local LLM (Ollama / LM Studio / Continue)
- Provide:
  - artifacts/test_structure.json
  - repository source code
- Prompt:
  "Implement the tests described. Follow existing conventions.
   Ask before making assumptions."

DO NOT:
- Push generated code automatically
- Skip code review
