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
check the repository address and notebook path. The course repository is public, so access does not
require GitHub authorization. Confirm that the URL uses the `GSIS-DS` organization, the
`research-method-data-science` repository, and the `main` branch. If needed, download the `.ipynb`
file from GitHub and upload it to Colab. Never paste a GitHub access token into a notebook.
