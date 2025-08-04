# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Mujaheed Khan
#
# This file is part of the gifs4docs project.
# You may use, distribute, and modify this code under the terms of the MIT
# license. See the LICENSE file in the project root for more information.


import subprocess
from pathlib import Path
import shlex


def test_output_file(tmp_path):
    """Verify that feedback is saved into output text file."""

    input = Path("tests") / "example_swift_package" / "Package.swift"
    output = tmp_path / "output.txt"

    command = f"./swift_pkg_consultant.py -p {input} -o {output}"
    commandlets = shlex.split(command)

    subprocess.run(commandlets, check=True)

    # Assert the GIF was created
    assert output.exists()
    assert output.stat().st_size > 0


def test_analyse():
    """Simply analyze the swift package."""

    input = Path("tests") / "example_swift_package" / "Package.swift"
    commandlets = shlex.split(f"./swift_pkg_consultant.py -p {input}")
    result = subprocess.run(commandlets,
                            capture_output=True,
                            text=True,
                            check=True
                            )

    # Capture stdout text
    output = result.stdout.strip()

    assert "SwiftPM Health Score" in output
