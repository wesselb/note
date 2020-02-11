# Note: Simple and Quick Note Taking System

## Installation

Clone and enter the repo.

```bash
git clone https://github.com/wesselb/note
cd note
```
Add the `bin` directory to your path. Replace `~/.bash_profile` with the appropriate file if necessary.

```bash
echo "export PATH=\"\$PATH:`pwd`/bin\"" >> ~/.bash_profile
```

## Make a Note

Suppose that today's date is 2020-01-01 and the time is 14:00.

```bash
note Meeting with someone
```

Then a file is created at `/path/to/repo/notes/2020-01-01.md` and opened in `vim`:

```
# [14:00] Meeting with someone
<position-of-cursor>
```

## Search Notes

```bash
search
```

This will list the headers of all notes for you to search through with `fzf`. The result is opened at the right line in `vim`.
