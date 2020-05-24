#!/bin/bash

# Based on https://stackoverflow.com/a/22638823

gitmtim(){
    local f
    for f
    do
        status=`git status -s -- "$f"`
        if [ -n "$status" ]
        then
            echo "Dirty: $f"
            exit 1
        fi
        # I suspect this command is the bottleneck, since it means doing a
        # linear search through history for every input file. Might be better
        # To do a single linear search while collecting the mtimes of each file
        # in the input set, but that's a bit more complex.
        mtime=`git log --pretty=%at -n1 -- "$f"`
        if [ -z "$mtime" ]
        then
            echo "Couldn't get mtime: $f"
            exit 1
        fi
        touch -d @0$mtime "$f"
    done
}
gitmtim "$@"
