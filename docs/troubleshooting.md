# Troubleshooting

1. Copy the exact first error message.
2. Identify the first cell or step that failed.
3. Check account, internet connection, spelling, file extension, and folder.
4. In Colab choose **Runtime → Restart session and run all**.
5. Confirm required files were uploaded to the current session.
6. Compare expected column names and actual names with `df.columns`.
7. Do not repeatedly authorize unfamiliar access prompts.
8. Ask for help with the notebook link, step number, expected result, actual result, and error text.

A GitHub 404 may mean a wrong address or missing permission. A Drive save does not update GitHub.
A Colab session reset removes temporary files and variables.

## Colab reports a GitHub API 404

If the message refers to `api.github.com/repos/GSIS-DS/research-method-data-science/contents`, first
check the repository visibility. GitHub returns 404 for private content when Colab is not authorized
to read it. The notebook path can still be correct. Until the course repository is public, download
the `.ipynb` file from GitHub and upload it to Colab, or use Colab's GitHub authorization flow if your
account has repository access. Never paste a GitHub access token into a notebook.
