# DocForge

A small, dependency-free Python CLI to generate a Markdown project inventory from source files. An **Open Heightz** initiative founded by **Clesh TN Maluleka**.

## Quick start
Python 3.10+ recommended.

```bash
python docforge.py ./my-project --output PROJECT_OVERVIEW.md
python -m unittest discover -s tests
```

The script lists supported source files and extracts Python module/class/function names using the standard-library AST parser. It does **not** send code to remote services. Output is intentionally limited and is **not** a replacement for reviewed documentation.

## Safety
Inspect generated Markdown before publication. The CLI skips hidden directories, common build directories and symlinked files, and refuses to overwrite an existing output unless `--force` is supplied. Avoid scanning projects containing sensitive information.

See LICENSE, AUTHORS.md, NOTICE.md, CONTRIBUTING.md, SECURITY.md and ROADMAP.md.
