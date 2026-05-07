#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROMPT_ROOTS = [ROOT / 'prompts', ROOT / 'prompts-en']
REQUIRED = ['title', 'category', 'subcategory', 'source_section', 'author', 'version', 'status', 'tags']
VALID_STATUS = {'active', 'draft', 'third-party-review'}


def parse_frontmatter(path: Path):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        return None, text
    end = text.find('\n---\n', 4)
    if end == -1:
        return None, text
    data = {}
    for line in text[4:end].splitlines():
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        data[key.strip()] = value.strip().strip('"')
    return data, text[end+5:]


def main():
    errors = []
    warnings = []
    files = []
    for prompt_root in PROMPT_ROOTS:
        if prompt_root.exists():
            files.extend(p for p in sorted(prompt_root.rglob('*.md')) if p.name != 'README.md')
    titles = {}
    for path in files:
        fm, body = parse_frontmatter(path)
        rel = path.relative_to(ROOT)
        if not fm:
            errors.append(f'{rel}: missing frontmatter')
            continue
        for key in REQUIRED:
            if not fm.get(key):
                errors.append(f'{rel}: missing {key}')
        if fm.get('status') not in VALID_STATUS:
            errors.append(f'{rel}: invalid status {fm.get("status")}')
        title = fm.get('title')
        if title in titles:
            warnings.append(f'duplicate title: {title} ({titles[title]}, {rel})')
        titles[title] = rel
        if '<span style=' in body or '</span>' in body:
            errors.append(f'{rel}: contains Feishu span style')
        if 'images/《姚金刚提示词合集》' in body or 'files/《姚金刚提示词合集》' in body:
            warnings.append(f'{rel}: contains original attachment reference')

    print(f'Checked {len(files)} prompt files.')
    if warnings:
        print('\nWarnings:')
        for item in warnings:
            print(f'- {item}')
    if errors:
        print('\nErrors:')
        for item in errors:
            print(f'- {item}')
        sys.exit(1)
    print('OK')


if __name__ == '__main__':
    main()
