# Google Colab beginner guide

A notebook combines readable **text cells** and executable **code cells**. Select a cell's Run
triangle or press Shift+Enter. Execution order matters because later cells may use values created
earlier. When uncertain, choose **Runtime → Restart session and run all**.

## Safe workflow

1. Open a GitHub notebook through its **Open in Colab** badge.
2. Select **File → Save a copy in Drive**.
3. Run cells from top to bottom.
4. Read outputs and answer interpretation prompts.
5. Restart and run all before submission.

Files uploaded with the Files panel usually live only in the temporary Colab session and may
disappear when it ends. Google Drive can be mounted with:

```python
from google.colab import drive
drive.mount("/content/drive")
```

Mount only when necessary, review permissions, and never expose private Drive paths in public work.
Upload only deidentified, permitted data. Use **File → Download** for `.ipynb`; use the Files panel
menu to download generated `.csv` or figure files.

## Common errors

- `NameError`: a required earlier cell was not run, or a name was misspelled.
- `FileNotFoundError`: the file is absent or its name/path differs.
- `KeyError`: a requested table column does not exist exactly as written.
- `ModuleNotFoundError`: a package needs installation or is unavailable.
- Session disconnected: reconnect; temporary variables/files may need recreation.
- Results changed after restart: execution order or an unrecorded random process affected them.

See [troubleshooting](troubleshooting.md) for a diagnostic checklist.
