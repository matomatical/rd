My paper collection is growing, and I need to manage it. This is a tool
to help me access papers.

Overview
--------

A script `rd` takes a search term and searches all the papers in my various
storage locations. It identifies matches and presents them as a list. Then
it asks which ones to open, by hexadecimal identifiers.

Installation:

* Put the Python script 'rd' on path somehow (I have a folder on my path,
  from which I symlink to everything I want on my path)
* Configure the paths to be searched for papers at the top of the script

Usage:

* Run the command `rd` with a query argument like `Turing` or `Turing1937`.
* The tool will search for files in the configured paths, recursively,
  looking for prefix matches (filenames like `Turing*` or `Turing1937*` in
  this case).
* The tool will display a list of results, for example for `Turing` query:
    ```
    % rd Turing
    found 7 matches
    0 Turing+Copeland2004 - The essential Turing seminal writings
    1 Turing1937 - On Computable Numbers, with an Application to t
    2 Turing1938correction - On Computable Numbers, with an Applic
    3 Turing1939 - Systems of Logic Based on Ordinals.pdf
    4 Turing1948 - Rounding-off errors in matrix processes.pdf
    5 Turing1950 - Computing Machinery and Intelligence.pdf
    6 Turing2009 - Computing Machinery and Intelligence.pdf
    ```
* The tool will ask `open?`
  Respond with a whitespace-separated list of indexes (e.g. `1 2`) and it
  will open these files for you.


Note:
The intended use case is for opening papers, but actually the tool searches
all files. This has two implications:

1. Probably best to keep the list of paths to paths that actually have mostly
   papers, and not a lot of extra files (for example, whole drives, or
   directories with .git directories) because these would slow down the
   (very naive) search. Future versions can deal with this if it becomes an
   issue.
2. On the other hand, this tool can be used for opening anything you like!
   It doesn't have to be a paper.

History of methods of accessing papers
--------------------------------------

1. Kept them in folders, specific to project. This worked for first few
   projects, first hundred or so papers, no time pressure causing me to fall
   behind on sorting papers.

2. Kept them in Zotero categories. This worked for a few months, but
   eventually you start to lose track of which papers you have and where they
   are, and the interface is awful.

3. Back to file system. This time, every paper has a unique identifier based
   on author names and years, and it's at the start of the filename. The
   following script in my profile finds and opens papers:

   ```
    # read a paper
    function rd () {
        find "/Volumes/Discworld/nexus/library/readings/" "/Users/matt/unsorted/" -name $1"*" -print0 \
            | xargs -0ptL1 open
        # -print0 causes find to terminate each line with \0
        # -0 causes xargs to use \0 as a command delimeter
        # -L 1 causes xargs to call the utility (open) once with each argument
        #    separately (rather than once with all arguments, for example)
        # -p causes xargs to ask for confirmation before running each command
        # -t causes xargs to print the commands as they are executed (redundant
        #    with p)
    }
    ```

    It actually works pretty well, but when there are multiple papers it's
    annoying to control with a sequence of y/n (having to refocus after each
    y because the opened pdf steals focus).
    
    Also, one time, somehow, it tried to open every pdf on my harddrive one
    after another, and, well, that was pretty much hell!
