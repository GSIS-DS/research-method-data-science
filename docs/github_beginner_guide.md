# Git and GitHub: a beginner guide

**Git** records versions of files. **GitHub** is an online service that stores and shares Git
repositories. A **repository** is the project folder together with its version history. A **commit**
is a named saved version, not merely pressing Save. A **branch** is a separate line of development.
Think of Git as a labeled revision history and GitHub as the shared online cabinet holding it.

## Level 1: required browser and Colab workflow

1. Open the [course repository](https://github.com/GSIS-DS/research-method-data-science).
   **You should see:** folders and a course description.
2. Select a folder name to browse; select a filename to read it.
3. Select a notebook ending in `.ipynb`, then its **Open in Colab** badge.
4. In Colab select **File → Save a copy in Drive**. This is your editable Drive copy.
5. To download it, select **File → Download → Download .ipynb**.
6. Upload or submit only through the channel named on the assignment, normally Cyber Campus.
7. Verify location: the Colab title shows Drive status; the GitHub page shows the public repository.
   Saving in Drive does not update GitHub.

## Level 2: saving from Colab to GitHub

Use this only when an assignment explicitly asks.

1. In Colab select **File → Save a copy in GitHub**.
2. Authorize GitHub only after checking the requested account and permissions.
3. Select your personal project repository—not the course repository.
4. Confirm the filename and folder. Avoid replacing a different notebook.
5. Write a commit message describing the change, for example `Document missing-value decisions`.
6. Save, then open GitHub in a new tab and verify the file and commit message appear.

Never commit passwords, API keys, personal data, interview recordings, identifiable responses, or
licensed/restricted datasets.

## Level 3: optional local Git workflow

Open a terminal only if you are comfortable doing so.

```bash
git clone REPOSITORY_URL
git status
git add PATH_TO_FILE
git commit -m "Describe the change"
git pull
git push
```

- `clone` creates a local copy.
- `status` reports changed files.
- `add` selects a change for the next named version.
- `commit` creates that named local version.
- `pull` brings remote changes to the local copy.
- `push` sends local commits to GitHub.

If a command reports a conflict, stop, preserve both versions, and ask for help.
