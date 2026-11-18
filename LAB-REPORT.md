# Lab Report: Assignment 4

**Course:** DevOps for Cloud Computing (CSC418)
**Project:** Student Task Manager, version control with Git and GitHub
**Student:** M-Zayn-Abbas

---

## 1. Git vs GitHub, and the purpose of add, commit and push

**Git** is a version control tool that runs on my own computer. It records
snapshots of the project so I can see what changed, when and why, and go
back to an older version if needed. **GitHub** is a website that hosts Git
repositories online. It adds collaboration features on top of Git, such as
Issues, Pull Requests, code review, Actions and Releases.

- `git add` moves changes into the **staging area**, so I choose exactly
  which changes go into the next commit.
- `git commit` saves the staged changes as a **snapshot in my local
  history**, with a message explaining the change.
- `git push` **uploads my local commits** to the remote repository on GitHub
  so others can see them.

## 2. Why branches and Pull Requests are used, and what causes merge conflicts

A **branch** is a separate line of development. I built each feature
(`feature/add-task`, `feature/complete-task`, `feature/delete-task`) on its
own branch, so unfinished work never broke `main`, and each feature could be
tested and reviewed on its own.

A **Pull Request** asks for a branch to be merged into `main`. It shows the
changed files, lets teammates add review comments, runs the automated tests,
and links the work to an Issue. Code only reaches `main` after it has been
checked.

A **merge conflict** happens when two branches change the **same lines of
the same file** in different ways, starting from the same parent commit. Git
cannot decide which version is correct, so it stops and asks a person to
choose. In this lab, `status/in-development` and `status/testing` both
changed the `Project status:` line in README.md, which caused the conflict.

## 3. fetch vs pull, merge vs rebase

- `git fetch` **downloads** new commits from the remote but does **not**
  change my working files. I can inspect them first.
- `git pull` is `fetch` **plus** `merge`: it downloads the commits and
  immediately merges them into my current branch.

- `git merge` combines two branches by creating a **merge commit**. The full
  history is kept, including when the branches split and joined.
- `git rebase` **replays my commits on top of** another branch, so the
  history becomes one straight line. It looks cleaner, but it rewrites
  commit IDs, so it should not be used on branches others are already using.

## 4. How GitHub Issues and Actions help a development team

**Issues** work as a to-do list and bug tracker for the team. Each Issue
describes one piece of work, has labels (enhancement, documentation,
testing), and can be assigned to a person. Writing `Closes #1` in a PR links
it and closes the Issue automatically when the PR is merged, so everyone
knows what is finished.

**GitHub Actions** automates tasks. My workflow (`.github/workflows/tests.yml`)
runs the unit tests on every push to `main` and every Pull Request to `main`.
If a change breaks something, the PR shows a red cross before it is merged.
This catches bugs early and saves the team from testing by hand.

## 5. A difficulty I faced and how I solved it

When I merged the second status branch into `main`, Git stopped with
`CONFLICT (content): Merge conflict in README.md`, and the file contained
`<<<<<<<`, `=======` and `>>>>>>>` markers. At first it was not clear which
part belonged to which branch. I read the markers: the part under `HEAD` was
the version already on `main`, and the part after `=======` came from
`status/testing`. I wrote one final status line, deleted the markers, made
sure the rest of the README was unchanged, then ran `git add README.md` and
`git commit` to complete the merge.

I also had a failing GitHub Actions run: my delete test expected 2 tasks
after deleting one of two, which is wrong. The red run showed the exact
assertion (`AssertionError: 1 != 2`). I corrected the expected value to 1,
pushed again, and the next run passed.
