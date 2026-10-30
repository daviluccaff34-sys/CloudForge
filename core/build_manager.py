import json
import os
from datetime import datetime, timezone
from pathlib import Path

VERSION = "0.1.0"
OUTPUT = Path("dist")


def main():
    print("================================")
    print("       CLOUDFORGE ENGINE")
    print("================================")

    OUTPUT.mkdir(exist_ok=True)

    build = {
        "project": "CloudForge",
        "version": VERSION,
        "type": "test-build",
        "status": "success",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "commit": os.getenv("GITHUB_SHA", "local"),
        "runner": os.getenv("RUNNER_OS", "local")
    }

    with open(OUTPUT / "build-info.json", "w") as file:
        json.dump(build, file, indent=4)

    with open(OUTPUT / "BUILD.txt", "w") as file:
        file.write("CloudForge build completed successfully!\n")
        file.write(f"Version: {VERSION}\n")

    print("Build completed!")
    print("Artifacts generated in dist/")


if __name__ == "__main__":
    main()
