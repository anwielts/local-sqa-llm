# local-sqa-llm
Pre commit hook leveraging local LLMs for software quality assurance.

## Requirements

- [pre-commit](https://pre-commit.com/) for setting up the hook
- [ollama](https://ollama.com/) as the local LLM model registry
- [ollama python client](https://github.com/ollama/ollama-python) to interact from within the hook with a LLM

## Getting started

Add this to your .pre-commit-config.yaml file
```
repos:
  - repo: https://github.com/anwielts/local-sqa-llm
    rev: v0.0.1-alpha
    hooks:
      - id: local-sqa-llm
        args: [TBD]
```

Per default the LLM output will be printed to the console.

### Possible arguments

TBD

## Credits

Structure heavily inspired by [version-checker](https://github.com/jalvaradosegura/version-checker/tree/main) and his [post](https://dev.to/jalvaradosegura/create-your-own-pre-commit-hook-3kh) about creating one's own pre-commit hook
