"""Execute release notebooks locally with repository sample files substituted for GitHub URLs."""
from pathlib import Path
import json
import os
import traceback

os.environ.setdefault("MPLBACKEND", "Agg")
ROOT = Path(__file__).resolve().parents[1]
URLS = {
    "https://raw.githubusercontent.com/GSIS-DS/research-method-data-science/main/data/sample/mini_country_indicators.csv":
        str(ROOT / "data/sample/mini_country_indicators.csv"),
    "https://raw.githubusercontent.com/GSIS-DS/research-method-data-science/main/data/sample/fictional_interview_excerpts.csv":
        str(ROOT / "data/sample/fictional_interview_excerpts.csv"),
}

failures = []
for path in sorted(ROOT.rglob("*.ipynb")):
    namespace = {"__name__": "__main__"}
    notebook = json.loads(path.read_text(encoding="utf-8"))
    try:
        for cell in notebook["cells"]:
            if cell.get("cell_type") != "code":
                continue
            source = cell.get("source", "")
            source = "".join(source) if isinstance(source, list) else source
            for remote, local in URLS.items():
                source = source.replace(remote, Path(local).as_posix())
            exec(compile(source, str(path), "exec"), namespace)
        print(f"PASS {path.relative_to(ROOT)}")
    except Exception:
        failures.append(str(path.relative_to(ROOT)))
        traceback.print_exc()

if failures:
    raise SystemExit("Notebook execution failures: " + ", ".join(failures))
