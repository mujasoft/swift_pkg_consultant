# swift_pkg_consultant

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![LLM Powered](https://img.shields.io/badge/LLM-Ollama%20%7C%20LLaMA3-blue.svg)](https://ollama.ai)
[![SwiftPM](https://img.shields.io/badge/SwiftPM-Inspector-informational)](https://swift.org/package-manager/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)


---

A tool built for Swift developers who want better insights into their package structure using AI.

It uses a local LLM to analyze your `Package.swift` and provide:

- SwiftPM best practice recommendations
- A SwiftPM Health Score out of 100
- Suggestions

---

## Demo

![Demo](./Demo.gif)  
---

## Why this exists?
As a developer, I often need quick insights into the health and structure of my Swift packages. I prefer local, offline-first tools with a special preference for ones I can integrate easily into CI pipelines like Jenkins. This project was built to make it simple to review and share SwiftPM feedback with teammates, without relying on cloud-based LLMs.

### Ideal for

- SwiftPM library authors
- Devs publishing reusable modules
- Teams auditing internal Swift packages

## Installation

```bash
git clone https://github.com/mujasoft/swift_pkg_consultant.git
cd swift_pkg_consultant
pip3 install -r requirements.txt
```

Requires:
- Python 3.9+.
- [Ollama](https://ollama.ai) installed and running.
- A downloaded model like `llama3`.
---

## Usage

### Analyze a SwiftPM package

```bash
swift_pkg_consultant -p ./Package.swift
```

### Output to file

```bash
swift_pkg_consultant -p ./Package.swift -o review.txt
```

### Only show health score

```bash
swift_pkg_consultant -p ./Package.swift --score-only
```

---

## Options

| Flag | Description |
|------|-------------|
| `-p, --package` | Path to your `Package.swift` (required) |
| `-o, --output`  | Output file path for the review. (optional) |
| `-m, --model`   | LLM model to use (default: `llama3`) |
| `-q, --quiet-mode` | Suppress all terminal output |
| `-s, --score-only` | Only display the SwiftPM Health Score |

---

## Example Output

```bash
╭────────────────────────────────────────────────────────────────────────── Review Made for "tests/example_swift_package/Package.swift" ───────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                                                                  │
│  **SwiftPM Review**                                                                                                                                                                                              │
│                                                                                                                                                                                                                  │
│  The Swift package for MujaTools appears to be a good starting point, but there are some areas that can be improved upon. Here's a breakdown of the findings:                                                    │
│                                                                                                                                                                                                                  │
│  ### Potential Problems or Omissions                                                                                                                                                                             │
│                                                                                                                                                                                                                  │
│  * The `swift-tools-version` declaration specifies version 5.9, which may not be compatible with the latest Swift compiler versions. It's recommended to use the latest supported version (e.g.,                 │
│  `swift-tools-version:6.0`) for future-proofing.                                                                                                                                                                 │
│  * There is no explicit `description` property defined for the package or its products. This makes it harder for users to understand what the package does and why they might want to include it in their        │
│  project.                                                                                                                                                                                                        │
│  * The `platforms` declaration only includes macOS (v12) and iOS (v15), which may limit the package's usefulness on other platforms.                                                                             │
│                                                                                                                                                                                                                  │
│  ### Recommendations                                                                                                                                                                                             │
│                                                                                                                                                                                                                  │
│  * **Modularity**: Consider breaking down the `MujaCore` target into smaller, more focused modules or subtargets. This will make it easier to reuse individual components in other projects.                     │
│  * **Platform Support**: Expand the `platforms` declaration to include support for watchOS and tvOS, if applicable.                                                                                              │
│  * **Testing**: While there is a test target (`MujaCoreTests`) defined, consider adding more specific testing metadata (e.g., `.testTarget(name: "MujaCoreTests", dependencies: ["MujaCore"], executable:        │
│  true)`). This will help users understand how to run the tests and what they cover.                                                                                                                              │
│  * **Plugins**: If the package provides plugins or extensions for other packages or frameworks, consider defining them as separate targets within this package.                                                  │
│                                                                                                                                                                                                                  │
│  ### Suggested Improvements                                                                                                                                                                                      │
│                                                                                                                                                                                                                  │
│  * Add a `description` property to provide a brief summary of what the package does:                                                                                                                             │
│  ```swift                                                                                                                                                                                                        │
│  let package = Package(                                                                                                                                                                                          │
│      name: "MujaTools",                                                                                                                                                                                          │
│      description: "A collection of tools and libraries for Muja development",                                                                                                                                    │
│      // ...                                                                                                                                                                                                      │
│  )                                                                                                                                                                                                               │
│  ```                                                                                                                                                                                                             │
│  * Consider adding platform-specific metadata (e.g., `.platforms([.watchOS(.v7), .tvOS(.v15)])`) to support additional platforms.                                                                                │
│                                                                                                                                                                                                                  │
│  ### SwiftPM Health Score                                                                                                                                                                                        │
│                                                                                                                                                                                                                  │
│  SwiftPM Health Score: 42/100                                                                                                                                                                                    │
│                                                                                                                                                                                                                  │
│  The package has a solid foundation, but there are opportunities for improvement in terms of modularity, platform support, and testing. By addressing these areas, the package can become more robust and        │
│  easier to maintain.                                                                                                                                                                                             │
│                                                                                                                                                                                                                  │
│  **Recommendation**: Continue to review and refine the package configuration to improve its overall health score.                                                                                                │
│                                                                                                                                                                                                                  │
╰────────────────────────────────────────────────────────────────────────────────────── LLM Powered Improvements by "llama3" ──────────────────────────────────────────────────────────────────────────────────────╯

WARNING: Please double-check since LLMs can still make mistakes.

Output saved to: review.txt

```

---
## Related Projects
Here are some other developer tools in the mujasoft toolbox:

- [readme_consultant](https://github.com/mujasoft/readme_consultant)
Uses local LLMs to analyze and improve your GitHub README.md files for clarity, completeness, and appeal.
- [gif4docs](https://github.com/mujasoft/gif4docs)
A CLI tool for converting videos to optimized GIFs which are perfect for README demos and documentation.
- [brewgen](https://github.com/mujasoft/brewgen)
Generates brew install-friendly formulas for your Python or CLI tools with minimal config which are designed to help you ship CLI tools like a pro.

---

## Caveats
- Responses may vary across runs due to LLM non-determinism.
- Tested only with llama3 on a MacBook Pro (M1, 16GB RAM).
- Other models and environments have not been tested and may produce inconsistent results.

## To-do
- Add a `rewrite` option
- Add a `dump-to-json` option
- Add some automated tests with pytest

## License

This project is licensed under the [MIT License](LICENSE).

---