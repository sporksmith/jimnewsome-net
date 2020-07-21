title: Preserving mtimes in Pelican
date: 2020-05-24
status: draft

With [Pelican](https://blog.getpelican.com/), and probably other
static site generators, rebuilding the site regenerates every output
file.

That sets their mtime (modification time) to the current time.

That means when deploying to the server with rsync, rsync's heuristic of
comparing sizes and mtimes detects that every file has changed. Delta
compression means it still won't end up sending the actual contents of
unchanged files over the wire, but now both sides need to compute checksums of
every file.

It also means the server-side mtimes get updated as well. This can further
defeat other caching mechanisms, such as the
[If-Modified-Since](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Modified-Since)
HTTP request header.

## Getting mtimes from git

I keep my static site *and* generated output in a git repo, so I hacked up a
script to reset the mtimes to the date of the last commit where the content
changed before rsync'ing. This currently takes *more* total time than just
rsync'ing---I think due to doing a linear search through git's history for each
file---but does at least save the

## Using a shallow git repo
