# Contributing to Python Docs Tamil (ta)

First of all, thank you for your interest in contributing to the **Tamil (\*\***`ta`\***\*) translation of the Python documentation**.

The goal of this project is to make Python documentation accessible to the Tamil-speaking community by providing translations that are technically accurate, easy to understand, and consistent with the official Python documentation.

This repository follows the **Python Documentation Translation Project**, **PEP 545**, and the general contribution practices of the Python Software Foundation (PSF).

---

# Documentation Contribution Agreement

Python's documentation is maintained by contributors from around the world.

By contributing translations or improvements to this repository, you agree that your contributions may be distributed under the same licensing terms used by the official Python Documentation Translation Project.

Contributors retain credit for their work, and accepted contributions may become part of the official Tamil translation of the Python documentation.

By opening a Pull Request, you acknowledge and accept these contribution terms.

---

# Who Can Contribute?

Everyone is welcome.

You can contribute by:

- Translating documentation
- Reviewing translations
- Fixing grammar and readability
- Improving terminology consistency
- Reporting issues
- Improving project documentation
- Improving automation workflows
- Helping new contributors

No contribution is too small.

---

# Before You Start

Basic knowledge of the following is recommended:

- Git
- GitHub
- Python
- Markdown
- reStructuredText (RST)
- gettext (.po) files

Recommended tools:

- Git
- Poedit (or any PO editor)
- VS Code
- GNU gettext utilities (`msgfmt`, `msgattrib`, `msginit`)

---

# Repository Structure

The repository follows the structure of the official Python documentation translation project. The exact directory layout may evolve as new sections are added.

```text
python-docs-ta/
│
├── .github/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
│
├── tutorial/
├── library/
├── reference/
├── using/
├── whatsnew/
│
├── bugs.po
├── glossary.po
│
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
└── ...
```

---

# Getting Started

## 1. Fork the Repository

Fork this repository to your GitHub account.

---

## 2. Clone your Fork

```bash
git clone https://github.com/<your-username>/python-docs-ta.git
cd python-docs-ta
```

---

## 3. Add the Upstream Repository

```bash
git remote add upstream https://github.com/Terminal-Joint/python-docs-ta.git
```

Verify:

```bash
git remote -v
```

---

## 4. Create a Feature Branch

Always create a new branch from the latest translation branch.

```bash
git fetch upstream

git checkout -b tutorial-introduction upstream/3.15
```

Use a descriptive branch name.

Examples:

- tutorial-introduction
- library-functions
- glossary-update
- review-reference
- fix-typos

---

# Translation Workflow

```text
Choose a .po file
        │
        ▼
Translate
        │
        ▼
Self Review
        │
        ▼
Validate
        │
        ▼
Commit
        │
        ▼
Push
        │
        ▼
Open Pull Request
        │
        ▼
Maintainer Review
        │
        ▼
Merge
```

---

# Working with Translation Files

Most contributors will work with existing `.po` files already present in this repository.

Simply choose an untranslated or partially translated file, make your changes, validate them, and open a Pull Request.

Creating new `.po` files is typically handled by project maintainers when new documentation templates become available from the upstream Python documentation project.
Please ensure there are no validation errors before opening a Pull Request.

---

# Translation Guidelines

Our objective is **accuracy first, readability second, and consistency always**.

## Translate

- Titles
- Headings
- Paragraphs
- Notes
- Warnings
- User-facing descriptions
- Comments inside examples
- Table descriptions

---

## Never Translate

### Python Keywords

```
if
else
elif
for
while
class
def
return
import
from
try
except
finally
raise
pass
with
yield
lambda
```

---

### Python Identifiers

Do not translate:

- Function names
- Class names
- Module names
- Package names
- Variable names
- Exception names

Examples

```
print
len
range
list
dict
tuple
set
ValueError
TypeError
os
sys
json
pathlib
```

---

### Documentation Markup

Never modify Sphinx roles.

```
:func:
:class:
:mod:
:meth:
:attr:
:exc:
:term:
:ref:
```

---

### Preserve

- URLs
- File names
- Package names
- Version numbers
- Command-line examples
- Code examples
- Inline code
- Tables
- Admonitions
- reStructuredText syntax

---

# Tamil Translation Standards

When translating documentation:

- Prefer natural Tamil over literal translation.
- Preserve the technical meaning.
- Avoid machine-translated text without human review.
- Keep terminology consistent throughout the project.
- Use transliteration where a widely accepted Tamil equivalent does not exist.
- Write in a neutral, educational, and professional tone.
- Do not mix multiple writing styles within the same document.

Consistency is more important than creativity.

---

# Commit Messages

Use meaningful commit messages.

Good examples:

```text
docs: translate tutorial/introduction.po

docs: translate library/functions.po

docs: review reference/datamodel.po

docs: improve glossary terminology

docs: fix formatting in tutorial/modules.po
```

Avoid vague messages such as:

```
Update

Changes

Fix

Done
```

---

# Opening a Pull Request

Before opening a Pull Request:

- Sync with the latest upstream branch.
- Ensure validation passes.
- Review your translation.
- Verify formatting.
- Check terminology consistency.

Provide a clear description of:

- What you translated
- What you reviewed
- Anything requiring reviewer attention

---

# Pull Request Checklist

- [ ] Translation completed
- [ ] Self-reviewed
- [ ] `msgfmt --check` passes
- [ ] No broken RST or Sphinx markup
- [ ] Code examples unchanged
- [ ] Formatting preserved
- [ ] Technical terminology is consistent
- [ ] Commit messages are descriptive
- [ ] GitHub Actions checks pass

---

# Review Process

Every Pull Request is reviewed before merging.

Reviewers will check:

- Translation quality
- Technical accuracy
- Terminology consistency
- Formatting
- Documentation style
- Build validation

Changes may be requested before approval.

---

# Common Mistakes

Please avoid:

- Translating Python keywords.
- Translating function or class names.
- Modifying code examples.
- Breaking Sphinx markup.
- Translating URLs.
- Using inconsistent terminology.
- Copying machine translations without review.
- Changing formatting unnecessarily.

---

# GitHub Workflows

This repository includes GitHub Actions to help validate contributions.

Before requesting a review, ensure all automated workflow checks complete successfully.

If a workflow fails, please review the logs and resolve the reported issues before requesting another review.

---

# Getting Help

Need assistance?

Please use:

- GitHub Discussions — for questions and community conversations.
- GitHub Issues — for reporting bugs or suggesting improvements.

Maintainers and contributors are happy to help.

---

# Code of Conduct

This project follows the **Contributor Covenant v2.1**.

By participating, you agree to uphold a respectful, inclusive, and welcoming environment for everyone.

Please read the full guidelines in:

`CODE_OF_CONDUCT.md`

---

# Useful Resources

- uContributing to Python Docs Tamil (ta)

  First of all, thank you for your interest in contributing to the **Tamil (\*\***`ta`\***\*) translation of the Python documentation**.

  The goal of this project is to make Python documentation accessible to the Tamil-speaking community by providing translations that are technically accurate, easy to understand, and consistent with the official Python documentation.

  ## This repository follows the **Python Documentation Translation Project**, **PEP 545**, and the general contribution practices of the Python Software Foundation (PSF).

  # Documentation Contribution Agreement

  Python's documentation is maintained by contributors from around the world.

  By contributing translations or improvements to this repository, you agree that your contributions may be distributed under the same licensing terms used by the official Python Documentation Translation Project.

  Contributors retain credit for their work, and accepted contributions may become part of the official Tamil translation of the Python documentation.

  ## By opening a Pull Request, you acknowledge and accept these contribution terms.

  # Who Can Contribute?

  Everyone is welcome.

  You can contribute by:
  - Translating documentation
  - Reviewing translations
  - Fixing grammar and readability
  - Improving terminology consistency
  - Reporting issues
  - Improving project documentation
  - Improving automation workflows
  - Helping new contributors
    No contribution is too small.

  ***

  # Before You Start

  Basic knowledge of the following is recommended:
  - Git
  - GitHub
  - Python
  - Markdown
  - reStructuredText (RST)
  - gettext (.po) files
    Recommended tools:
  - Git
  - Poedit (or any PO editor)
  - VS Code
  - GNU gettext utilities (`msgfmt`, `msgattrib`, `msginit`)

  ***

  # Repository Structure

  ```
  python-docs-ta/
  │
  ├── .github/
  │   ├── ISSUE_TEMPLATE/
  │   ├── workflows/
  │   └── PULL_REQUEST_TEMPLATE.md
  │
  ├── tutorial/
  ├── library/
  ├── reference/
  ├── using/
  ├── whatsnew/
  │
  ├── README.md
  ├── CONTRIBUTING.md
  ├── CODE_OF_CONDUCT.md
  ├── LICENSE
  └── PROJECT_REPORT.md

  ```

  ***

  # Getting Started

  ## 1. Fork the Repository

  ## Fork this repository to your GitHub account.

  ## 2. Clone your Fork

  ```
  git clone https://github.com/<your-username>/python-docs-ta.git
  cd python-docs-ta

  ```

  ***

  ## 3. Add the Upstream Repository

  ```
  git remote add upstream https://github.com/Terminal-Joint/python-docs-ta.git

  ```

  Verify:

  ```
  git remote -v

  ```

  ***

  ## 4. Create a Feature Branch

  Always create a new branch from the latest translation branch.

  ```
  git fetch upstream

  git checkout -b tutorial-introduction upstream/3.15

  ```

  Use a descriptive branch name.

  Examples:
  - tutorial-introduction
  - library-functions
  - glossary-update
  - review-reference
  - fix-typos

  ***

  # Translation Workflow

  ```
  Choose a .po file
          │
          ▼
  Translate
          │
          ▼
  Self Review
          │
          ▼
  Validate
          │
          ▼
  Commit
          │
          ▼
  Push
          │
          ▼
  Open Pull Request
          │
          ▼
  Maintainer Review
          │
          ▼
  Merge

  ```

  ***

  # Creating a New Translation File

  Generate a new `.po` file from the latest template.

  ```
  msginit \
    --locale=ta \
    --input=PATH_TO_TEMPLATE.pot \
    --output-file=PATH_TO_OUTPUT.po

  ```

  Example

  ```
  msginit \
    --locale=ta \
    --input=library/functions.pot \
    --output-file=library/functions.po

  ```

  ***

  # Validating Your Translation

  Check syntax.

  ```
  msgfmt --check FILE.po

  ```

  Statistics.

  ```
  msgfmt --statistics FILE.po

  ```

  List untranslated strings.

  ```
  msgattrib --untranslated FILE.po

  ```

  List translated strings.

  ```
  msgattrib --translated FILE.po

  ```

  ## Please ensure there are no validation errors before opening a Pull Request.

  # Translation Guidelines

  Our objective is **accuracy first, readability second, and consistency always**.

  ## Translate
  - Titles
  - Headings
  - Paragraphs
  - Notes
  - Warnings
  - User-facing descriptions
  - Comments inside examples
  - Table descriptions

  ***

  ## Never Translate

  ### Python Keywords

  ```
  if
  else
  elif
  for
  while
  class
  def
  return
  import
  from
  try
  except
  finally
  raise
  pass
  with
  yield
  lambda

  ```

  ***

  ### Python Identifiers

  Do not translate:
  - Function names
  - Class names
  - Module names
  - Package names
  - Variable names
  - Exception names
    Examples

  ```
  print
  len
  range
  list
  dict
  tuple
  set
  ValueError
  TypeError
  os
  sys
  json
  pathlib

  ```

  ***

  ### Documentation Markup

  Never modify Sphinx roles.

  ```
  :func:
  :class:
  :mod:
  :meth:
  :attr:
  :exc:
  :term:
  :ref:

  ```

  ***

  ### Preserve
  - URLs
  - File names
  - Package names
  - Version numbers
  - Command-line examples
  - Code examples
  - Inline code
  - Tables
  - Admonitions
  - reStructuredText syntax

  ***

  # Tamil Translation Standards

  When translating documentation:
  - Prefer natural Tamil over literal translation.
  - Preserve the technical meaning.
  - Avoid machine-translated text without human review.
  - Keep terminology consistent throughout the project.
  - Use transliteration where a widely accepted Tamil equivalent does not exist.
  - Write in a neutral, educational, and professional tone.
  - Do not mix multiple writing styles within the same document.
    Consistency is more important than creativity.

  ***

  # Commit Messages

  Use meaningful commit messages.

  Good examples:

  ```
  docs: translate tutorial/introduction.po

  docs: translate library/functions.po

  docs: review reference/datamodel.po

  docs: improve glossary terminology

  docs: fix formatting in tutorial/modules.po

  ```

  Avoid vague messages such as:

  ```
  Update

  Changes

  Fix

  Done

  ```

  ***

  # Opening a Pull Request

  Before opening a Pull Request:
  - Sync with the latest upstream branch.
  - Ensure validation passes.
  - Review your translation.
  - Verify formatting.
  - Check terminology consistency.
    Provide a clear description of:
  - What you translated
  - What you reviewed
  - Anything requiring reviewer attention

  ***

  # Pull Request Checklist
  - Translation completed
  - Self-reviewed
  - `msgfmt --check` passes
  - No broken RST or Sphinx markup
  - Code examples unchanged
  - Formatting preserved
  - Technical terminology is consistent
  - Commit messages are descriptive
  - GitHub Actions checks pass

  ***

  # Review Process

  Every Pull Request is reviewed before merging.

  Reviewers will check:
  - Translation quality
  - Technical accuracy
  - Terminology consistency
  - Formatting
  - Documentation style
  - Build validation
    Changes may be requested before approval.

  ***

  # Common Mistakes

  Please avoid:
  - Translating Python keywords.
  - Translating function or class names.
  - Modifying code examples.
  - Breaking Sphinx markup.
  - Translating URLs.
  - Using inconsistent terminology.
  - Copying machine translations without review.
  - Changing formatting unnecessarily.

  ***

  # GitHub Workflows

  This repository includes GitHub Actions to help validate contributions.

  Before requesting a review, ensure all automated workflow checks complete successfully.

  ## If a workflow fails, please review the logs and resolve the reported issues before requesting another review.

  # Getting Help

  Need assistance?

  Please use:
  - GitHub Discussions — for questions and community conversations.
  - GitHub Issues — for reporting bugs or suggesting improvements.
    Maintainers and contributors are happy to help.

  ***

  # Code of Conduct

  This project follows the **Contributor Covenant v2.1**.

  By participating, you agree to uphold a respectful, inclusive, and welcoming environment for everyone.

  Please read the full guidelines in:

  ## `CODE_OF_CONDUCT.md`

  # Useful Resources
  - Python Documentation
  - Python Developer Guide
  - Python Documentation Translation Guide
  - PEP 545
  - GNU gettext Documentation
  - Transifex Documentation

  ***

  # Thank You

  Every translation, review, correction, and suggestion helps make Python more accessible to millions of Tamil-speaking learners and developers.

  Thank you for helping grow the Tamil Python community (PyTamil) through open source.Python Documentation

- Python Developer Guide
- Python Documentation Translation Guide
- PEP 545
- GNU gettext Documentation
- Transifex Documentation

---

# Thank You

Every translation, review, correction, and suggestion helps make Python more accessible to millions of Tamil-speaking learners and developers.

Thank you for helping grow the Tamil Python community (PyTamil) through open source.
