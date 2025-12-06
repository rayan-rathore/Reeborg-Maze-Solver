🧠 Reeborg Maze & Hurdle Solver

A single Python algorithm that solves some Reeborg challenges:

Hurdle 1

Hurdle 2

Hurdle 3

Hurdle 4

The Maze

This solution uses the right-hand rule and structured control flow to navigate any maze-like environment. Although this project started as part of a learning challenge, the final algorithm ended up being flexible enough to handle every obstacle scenario.

📌 Why This Repo Exists

I originally solved hurdles 1–4 separately.
I didn’t save the earlier versions — but I discovered something better:

My maze algorithm actually passes all the hurdle challenges too.

So instead of multiple small scripts, this repository contains one general-purpose navigation algorithm.

🚀 Features

Works on both maze and hurdle challenges

Uses helper functions (turn_right(), go_ahead())

Implements structured logic:

prioritize right side

then check front

turn left if blocked

Avoids infinite loops

Clean and readable Python code

📂 Project Files
universal_solver.py   # final working solution
screenshots/          # proof of completion for all tasks
README.md             # project documentation

🖼 Screenshots

Here are the challenge completions:
(See the screenshots/ folder in this repo.)

Hurdle 1

Hurdle 2

Hurdle 3

Hurdle 4

Maze

🧩 Logic Summary

The algorithm follows this priority:

1️⃣ If right side is clear → turn right + move
2️⃣ Else if front is clear → move forward
3️⃣ Else if blocked → turn left

continuous movement without getting stuck.

📘 What I Learned

How loops and conditional logic control movement

How to build helper functions to simplify logic

Importance of condition order

Debugging infinite loops

Foundations of algorithmic thinking

💬 Feedback

If you have suggestions or want to share your own Reeborg solutions, feel free to open an issue or fork the repo!
