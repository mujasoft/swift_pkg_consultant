# swift_pkg_consultant

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![LLM Powered](https://img.shields.io/badge/LLM-Ollama%20%7C%20LLaMA3-blue.svg)](https://ollama.ai)
[![SwiftPM](https://img.shields.io/badge/SwiftPM-Inspector-informational)](https://swift.org/package-manager/)

---

**`swift_pkg_consultant`** is a CLI tool that uses a local LLM (e.g. `llama3` via [Ollama](https://ollama.ai)) to analyze your `Package.swift` and provide:

- SwiftPM best practice recommendations
- A SwiftPM Health Score out of 100
- Clean, terminal-friendly output (powered by `rich`)

This is built for Swift developers who want better insights into their package structure. 

---

## Demo

![Demo](./Demo.gif)  
---

## Why this exists?

I wanted a tool that can work offline and help me improve, review and audit the quality of packages without having to
go online.

## Installation

```bash
git clone https://github.com/mujasoft/swift_pkg_consultant.git
cd swift_pkg_consultant
pip3 install -r rquirements.txt
```

Requires:
- Python 3.9+.
- [Ollama](https://ollama.ai) installed and running.
- A downloaded model like `llama3`.
---

## Usage

### Analyze a SwiftPM package

```bash
swift_pkg_consultant -p ./Package.swift # default output filename
```

### Output to file

```bash
swift_pkg_consultant analyse -p ./Package.swift -o review.txt
```

### Only show health score

```bash
swift_pkg_consultant analyse -p ./Package.swift --score-only
```

---

## Options

| Flag | Description |
|------|-------------|
| `-p, --package` | Path to your `Package.swift` (required) |
| `-o, --output`  | Output file path for the review (default: `review.txt`) |
| `-m, --model`   | LLM model to use (default: `llama3`) |
| `-q, --quiet-mode` | Suppress terminal output |
| `-s, --score-only` | Only display the SwiftPM Health Score |

---

## 📦 Example Output

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

## 📄 License

This project is licensed under the [MIT License](LICENSE).

© 2025 Mujaheed Khan

---

## ✨ Built by [@mujasoft](https://github.com/mujasoft)

Open to feedback, contributions, and collaboration — especially if you're working on Swift, dev tools, or AI-infra!

