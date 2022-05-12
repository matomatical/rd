My paper collection is growing, and I need to manage it. This is a tool
to help me access papers.

Plan
----

A script `rd` takes a search term and searches all the papers in my various
storage locations. It identifies matches and presents them as a list. Then
it asks which ones to open, by hexadecimal identifiers.

Let's go!


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
