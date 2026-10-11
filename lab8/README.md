# Lab 8: Vim Editor

## Basics
- Vim comes preinstalled on macOS (verified with `vim --version`)
- Created `file.txt`, opened with `vim file.txt`
- Entered Insert mode (`i`), typed sample text
- Deleted a line in Normal mode with `dd`
- Deleted all content with `:%d`
- Saved with `:w`, confirmed save message
- Quit with `:q` / saved and quit with `:wq`

## Task: Additional commands explored
- `yy` / `p` — yank (copy) and paste a line
- `u` / `Ctrl+r` — undo / redo
- `/word` + `n` — search and jump to next match
- `gg` / `G` — jump to top / bottom of file
- `dw` — delete a word
- `x` — delete a character
- `:set number` — show line numbers
- `v` — Visual mode for selecting text
- `:wq!` / `:q!` — force save+quit / quit without saving
