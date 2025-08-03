# swift_pkg_consultant

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![LLM Powered](https://img.shields.io/badge/LLM-Ollama%20%7C%20LLaMA3-blue.svg)](https://ollama.ai)
[![SwiftPM](https://img.shields.io/badge/SwiftPM-Inspector-informational)](https://swift.org/package-manager/)
[![Built by Mujaheed Khan](https://img.shields.io/badge/built%20by-mujasoft-blueviolet)](https://github.com/mujasoft)

---

**`swift_pkg_consultant`** is a CLI tool that uses a local LLM (e.g. `llama3` via [Ollama](https://ollama.ai)) to analyze your `Package.swift` and provide:

- ✅ SwiftPM best practice recommendations
- 🧠 AI-enhanced modularity + metadata suggestions
- 📊 A SwiftPM Health Score out of 100
- 🖥️ Clean, terminal-friendly output (powered by `rich`)

This is built for Swift developers who want better insights into their package structure — fast, local, and human-readable.

---

## 📸 Demo

> _Terminal output from a real Swift package analysis:_

![Demo](./demo.gif)  
_(or replace with screenshot if needed)_

---

## 🛠 Installation

```bash
git clone https://github.com/mujasoft/swift_pkg_consultant.git
cd swift_pkg_consultant
pip install .
```

Requires:
- Python 3.9+
- [Ollama](https://ollama.ai) installed and running (`ollama serve`)
- A downloaded model like `llama3` or `codellama` (`ollama run llama3`)

---

## 🚀 Usage

### Analyze a SwiftPM package

```bash
swift_pkg_consultant analyse -p ./Package.swift
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

## ⚙️ Options

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
📦 Package: MujaTools
✅ 2 targets, 1 product, 1 dependency

⚠️ No platform declaration
⚠️ No test target for 'MujaCore'
💡 Consider modularizing Utility logic

SwiftPM Health Score: 78/100
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

© 2025 Mujaheed Khan

---

## ✨ Built by [@mujasoft](https://github.com/mujasoft)

Open to feedback, contributions, and collaboration — especially if you're working on Swift, dev tools, or AI-infra!

