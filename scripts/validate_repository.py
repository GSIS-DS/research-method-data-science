from pathlib import Path
import ast, json, re, sys

root=Path(__file__).resolve().parents[1]
errors=[]
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
for p in root.rglob("*"):
    if p.is_file() and p.stat().st_size == 0: errors.append(f"empty file: {p.relative_to(root)}")
if errors:
    print("\n".join(errors)); sys.exit(1)
print("Repository validation passed.")
