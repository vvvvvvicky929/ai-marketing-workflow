# Yao Open Prompts

[English Content Prompts](prompts-en/06-ai-content/README.md) · [Web Navigation](https://yaojingang.github.io/yao-open-prompts/) · [GitHub Repository](https://github.com/yaojingang/yao-open-prompts)

Yao Open Prompts is an open-source prompt library for practical AI work, learning, content creation, marketing, and everyday scenarios.

The main repository is organized around the Chinese prompt library. This English README is a focused entry point for the English prompt versions currently available in the repository.

## English Prompt Set

**[36 Content and Operations Prompts](prompts-en/06-ai-content/README.md)**: English versions of the content creation, persona style, content tooling, platform operations, industry content, livestream, private-domain sales, AI image, comment operations, interview planning, data review, and viral remix prompts.

Each English prompt is stored as an independent Markdown file and points back to its matching Chinese source file through the `source_section` frontmatter field.

## Directory

```text
prompts-en/
  README.md
  06-ai-content/
    README.md
    hook-opening-copy.md
    spoken-viral-script.md
    topic-planner.md
    ...
```

## How To Use

1. Open [English Content Prompts](prompts-en/06-ai-content/README.md).
2. Choose the prompt that matches your task.
3. Copy the `Prompt` section.
4. Replace `{{user_information}}` with your task details.
5. Run it in your preferred AI model and iterate for your platform, audience, and tone.

## Maintenance

English prompts are kept in `prompts-en/` so they do not mix with the Chinese source library. To regenerate the current English content set, run:

```bash
python3 scripts/generate_english_content_prompts.py
```
