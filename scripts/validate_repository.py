from pathlib import Path
import ast, json, re, sys

root=Path(__file__).resolve().parents[1]
errors=[]
notebook_index=(root/"notebooks/README.md").read_text(encoding="utf-8")
readme=(root/"README.md").read_text(encoding="utf-8")
expected_weights={
    "Research workflow labs and participation": "10%",
    "Literature review and research proposal": "15%",
    "Midterm practical assessment": "25%",
    "Qualitative research exercise": "15%",
    "Final examination assignment—individual research project": "35%",
}
general_weights={
    "Class participation": "10%",
    "Individual assignments": "10%",
    "Group activities": "20%",
    "Midterm examination — Week 8": "25%",
    "Final individual research project — Week 16": "35%",
}
for component, weight in expected_weights.items():
    if f"| {component} | {weight} |" not in readme:
        errors.append(f"README assessment mismatch: {component} must be {weight}")
for component, weight in general_weights.items():
    if f"| {component} | {weight} |" not in readme:
        errors.append(f"README general assessment mismatch: {component} must be {weight}")
for p in root.rglob("*.md"):
    text=p.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://","https://","#","mailto:")): continue
        clean=target.split("#",1)[0]
        if clean and not (p.parent/clean).resolve().exists():
            errors.append(f"broken link: {p.relative_to(root)} -> {target}")
for p in root.rglob("*.ipynb"):
    try:
        nb=json.loads(p.read_text(encoding="utf-8"))
        if nb.get("nbformat") != 4: errors.append(f"notebook format: {p.relative_to(root)}")
        joined=" ".join("".join(c.get("source",[])) if isinstance(c.get("source"),list) else c.get("source","") for c in nb["cells"])
        for required in ("Learning objectives","Estimated time","Reproducibility test","Attribution"):
            if required not in joined: errors.append(f"{p.relative_to(root)} missing {required}")
        expected="https://colab.research.google.com/github/GSIS-DS/research-method-data-science/blob/main/"+p.relative_to(root).as_posix()
        if expected not in joined: errors.append(f"{p.relative_to(root)} has incorrect Colab link")
        for cell in nb["cells"]:
            if cell.get("cell_type") == "code":
                source=cell.get("source","")
                source="".join(source) if isinstance(source,list) else source
                ast.parse(source)
    except Exception as exc: errors.append(f"invalid notebook {p.relative_to(root)}: {exc}")
course_notebooks=list((root/"notebooks").rglob("*.ipynb"))
if len(course_notebooks) != 17:
    errors.append(f"expected 17 course notebooks under notebooks/, found {len(course_notebooks)}")
for p in course_notebooks:
    relative=p.relative_to(root/"notebooks").as_posix()
    if relative not in notebook_index:
        errors.append(f"notebook missing from index: {relative}")
for p in root.rglob("*"):
    if p.is_file() and p.stat().st_size == 0: errors.append(f"empty file: {p.relative_to(root)}")
if errors:
    print("\n".join(errors)); sys.exit(1)
print("Repository validation passed.")
