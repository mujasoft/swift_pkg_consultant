#!/usr/bin/env python3
# MIT License

# Copyright (c) 2025 Mujaheed Khan

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import sys

import ollama
import typer

from rich import print
from rich.console import Console
from rich.panel import Panel


app = typer.Typer(
    help="AI powered tool to review swift package info"
)

console = Console()


def read_text(filepath):
    """Given a filepath, returns contents of file.

    Args:
        filepath (str): Path to file to read.

    Returns:
        str: Contents of file.
    """

    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def is_model_available(model_name: str) -> bool:
    """Check if specified model is available in local Ollama."""

    try:
        models = ollama.list().get("models", [])
        return any(m.model.startswith(model_name) for m in models)

    # Catch alls are not usually the way to go but its better to fail
    # early.
    except Exception as e:
        console.print(f"[bold red]ERROR:[/] Could not connect to Ollama: {e}")
        raise typer.Exit(code=1)


def send_prompt_to_LLM(prompt: str, model: str = "llama3") -> str:
    """Sends prompt to specified LLM and returns output.

    Args:
        prompt (str): Block of text containg prompt.
        model (str, optional): Name of model. Defaults to "llama3".

    Returns:
        str: response from LLM.
    """

    with console.status("[bold green]Analyzing your swift package ...[/]"):
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
    return response['message']['content']


def validate_setup(package):
    """Ensure package parameter is valid.

    Args:
        package (str): path to 'Package.swift'.
    """

    if package is None:
        sys.exit("ERROR: You must specify a repo directory.")

    if not os.path.exists(package):
        sys.exit(f"ERROR: \"{package}\" does not exist.")

    if not package.endswith(".swift"):
        console.print(f"[bold red]ERROR:[/] Expected a `.swift` file."
                      f" Got: {package}")
        raise typer.Exit(code=1)


@app.command()
def analyse(
    package: str = typer.Option(None, "--package", "-p",
                                help="Mandatory. Location of where the "
                                     "packaged is located."),
    output: str = typer.Option(None, "--output", "-o",
                               help="Location of where to save "
                                    "report in a .txt file."),
    model: str = typer.Option("llama3", "--model", "-m",
                              help="Name of model."),
    enable_quiet_mode: bool = typer.Option(False, "--quiet-mode", "-q",
                                           help="Choose to suppress all"
                                                " output."),
    score_only: bool = typer.Option(False, "--score-only", "-s",
                                    help="Choose to only display score."),
                             ):
    """Uses LLM to review a Package.swift file."""

    # Not always needed to save output.
    if output is not None:
        if not output.endswith(".txt"):
            output += ".txt"

    validate_setup(package)

    # Ensure model is ready
    if not is_model_available(model):
        console.print(f"[bold red]ERROR:[/] Model \"{model}\" not found "
                      "in Ollama.")
        console.print(f"[bold yellow]Hint:[/] Run [italic]ollama run {model}"
                      "[/] to download and start it.")
        raise typer.Exit(code=1)

    # Extract contents of package.
    package_text = read_text(package)

    prompt = f"""
You are a senior Apple tools engineer with deep expertise in Swift Package
Manager (SwiftPM). You’ve been asked to review a Swift package configuration
for structure, clarity, and best practices.

Please:
1. Identify potential problems or omissions.
2. Recommend improvements for modularity, platform support, testing, or
plugins.
3. Suggest missing metadata such as descriptions or platform declarations.
4. Use markdown-style formatting and a kind, professional tone.
5. Conclude with a 'SwiftPM Health Score' out of 100.
   Like 'SwiftPM Health Score: 28/100'
6. Dont speak in the first person.

Here is the Swift package:

{package_text}

Now, provide your analysis.
"""

    # Try a couple times for resilience.
    no_of_attempts = 3
    for x in range(no_of_attempts):
        results = send_prompt_to_LLM(prompt, model)

        if len(results) != 0:
            break

    if not enable_quiet_mode:

        # Sometimes the format is not the same so the regex may need updates
        # down the line.
        if score_only:
            match = re.search(r'\*?\*?SwiftPM Health Score:\*?\*?\s*(\d+/\d+)', results)
            if match:
                score_str = match.group(0)
                score_str = score_str.replace("*", "")
                print(score_str)
            else:
                print(results)
                print("[bold red]Could not find health score in output.[/]")
            raise typer.Exit()
        else:
            console.print(
                Panel.fit(
                    results.strip(),
                    title=f'[bold cyan]Review Made for "{package}"',
                    subtitle=f'[green]LLM Powered Improvements by "{model}"',
                    border_style="bright_green",
                    padding=(1, 2),
                    style="blue")
                    )

    # Start writing results to file.
    if output is not None:
        with open(output, 'w') as f:
            f.write(results)

    if not enable_quiet_mode:
        print()
        console.print("[bold yellow]WARNING: Please double-check since LLMs"
                      " can still make mistakes.[/]")

        print()
        console.print(f"[bold cyan]Output saved to:[/] {output}")


if __name__ == "__main__":
    app()
