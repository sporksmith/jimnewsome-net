---
layout: post
title: "In-Repository Documentation"
date: 2012-07-04 11:31
comments: true
categories: 
published: true
---

Introduction
============

Two popular places to keep documentation for programming projects are:

1. In `README` files in the code repository.
2. In a separate wiki.

In this article, I propose that a compelling way to manage
documentation is to combine the two: to write the documentation as
markdown files in the code repository itself, and to publish those
pages in a wiki-like format.

I also share my experience doing this on a SourceForge-hosted project,
where it is already quite straight-forward to do this, and could be
made even more convenient with only a few minor tweaks to
SourceForge's Allura platform.


Why Markdown?
=============

[Markdown](http://daringfireball.net/projects/markdown/), as defined
by its inventor Mark Gruber:

> “Markdown” is two things: (1) a plain text formatting syntax; and
> (2) a software tool, written in Perl, that converts the plain text
> formatting to HTML.

There are other plain text formatting syntaxes and tools, but Markdown
seems to have the most momentum, perhaps because of its
natural-looking syntax. Since its inception, many tools have been
created to parse Markdown files and convert them to formats suitable
for publishing, such as `html` and `pdf`. (One of my favorites is
[pandoc](http://johnmacfarlane.net/pandoc/), which also adds some
useful
[extensions](http://johnmacfarlane.net/pandoc/README.html#pandocs-markdown)).

There are many tools for publishing a whole site or wiki from
Markdown-generated files, and several project-hosting platforms
include support for Markdown-based wikis and for rendering
in-repository Markdown files, including SourceForge's Allura platform.

Why In-Repository?
==================

The software engineering principle of
[Don't Repeat Yourself](http://en.wikipedia.org/wiki/Don't_repeat_yourself)
applies equally well to documentation. There should be only
one canonical place for documentation. Having documentation in two
places (such as in a wiki and in in-repository README files) will tend
to result in them getting out of sync, and more than likely one of
those will rot.

Given that the canonical source of the documentation should only be in
one place, in the code repository itself seems ideal.

* Keeping them somewhere other than the code repository implies no
  documentation in the repository other than a URL to that other
  location. That leaves a user with a checkout with no documentation
  in offline situations. Also if you have an old checkout of the code
  the URL may lead nowhere at all. With the in-repository model, if
  you have a checkout of the repository you always have the relevant
  documentation right there.
* Documentation versions are kept synchronized with code versions.

    * A feature branch that changes behavior can also update the
      documentation. The behavior changes and documentation changes
      can be merged atomically.

    * If you have an old checkout or an archive tarball of the code,
      you also have the version of the documentation that applies to
      that exact version.

* In-repository documentation sources can be edited with external
  editors, rather than browser text windows. (This is also possible
  with some alternative ways of managing documentation, but not
  currently in Allura's wiki tool)

In-Repository Documentation with SourceForge's Allura Platform
==============================================================

While there are a number of tools for publishing a git repository of
Markdown files as a web site, to my knowledge they are intended for
use with a dedicated repository, and not with a repository that
primarily holds something else (code) and has the documentation
sprinkled throughout as markdown files. It might be possible to use
existing tools to support this use-case though, and in particular I've
managed to use SourceForge's
[Allura platform](https://sourceforge.net/p/allura/)'s git-repository
web-view-tool for this purpose.

In-repository documentation in the XMHF project
-----------------------------------------------

The documentation in the [XMHF](http://xmhf.org) is in markdown files
in the code repository itself. Documentation is placed in the
file-system near the relevant component, with a top-level README.md
for the whole repository and for each component.

    ├── COPYING.md
    ├── README.md
    ├── libbaremetal/
    │   └── README.md
    ├── lockdown/
    │   └── README.md
    ├── tee-cred/
    │   └── README.md
    ├── tee-sdk/
    │   └── README.md
    ├── trustvisor/
    │   ├── doc/
    │   │   ├── building-trustvisor.md
    │   │   ├── installing-trustvisor.md
    │   │   └── nv-storage.md
    │   └── README.md
    └── xmhf/
        ├── doc/
        │   ├── amt-serial-over-lan.md
        │   ├── building-xmhf.md
        │   ├── configuring-grub.md
        │   ├── custom-linux-kernels.md
        │   ├── debugging-xmhf.md
        │   ├── hardware-requirements.md
        │   └── installing-xmhf.md
        └── README.md

The documentation is viewable in html format through SourceForge's web
view of the
[xmhf repository](https://sourceforge.net/p/xmhf/xmhf/). The html
conversion is done transparently by SourceForge's Allura platform.

Suggested improvements
======================

The usability of this technique could be improved a lot with some
small changes to the Allura platform.

Shortcut syntax for relative links
----------------------------------

The vanilla Markdown syntax for title-less links is:

    [Text](URL)

Within the repository, linking to other files within the repository is
largely redundant. It would be nice to support the abbreviated

    [path/to/header.h] is a header file specifying...

as a shortcut for:

    [path/to/header.h](path/to/header.h) is a header file specifying...

I've filed
[ticket #4472](https://sourceforge.net/p/allura/tickets/4472/)
requesting that extension.

It would be even nicer if the platform indexed the locations of other
markdown files within the repository, allowing for a similar syntax as
"artifact links" in the wiki. i.e., it would be nice to allow:

    [Installing XMHF]

as a shortcut for:

    [Installing XMHF](xmhf/doc/installing-xmhf.md)


Support for linking to most recent version of a file
----------------------------------------------------

There is currently no permanent link that always points to the most
recent version of a file in a repository. For example, suppose I want
to a link to `installing-xmhf.md`. I can link to the current
most-recent version of it as follows:
<https://sourceforge.net/p/xmhf/xmhf/ci/515d200b1914731871ee312a0bd6e8b9fc412100/tree/xmhf/doc/installing-xmhf.md>. However,
after that document is updated, the link will still point to the exact
same (now deprecated) version of the file.

It would be better if I could link to the most recent with something
like:
<https://sourceforge.net/p/xmhf/xmhf/current/tree/xmhf/doc/installing-xmhf.md>

[Ticket 4130](https://sourceforge.net/p/allura/tickets/4130/) requests this feature.

Support for Markdown extensions
-------------------------------

The Allura platform extends Markdown to support things like tables and
code highlighting... except in the repository viewer. It currently
uses a different Markdown processor there that only recognizes vanilla
Markdown. [Ticket 4474](https://sourceforge.net/p/allura/tickets/4474/)
requests unifying the markdown parsers for consistency.

It would be even nicer if Allura incorporated some of
[pandoc's markdown extensions](http://johnmacfarlane.net/pandoc/README.html#pandocs-markdown),
such as definition lists, multi-line tables, footnotes, citations, and
internal links.

Other Tools and Platforms
=========================

Gitit
-----

I briefly experimented with [Gitit](http://gitit.net/). By default it
looks in a special sub-directory for markdown files, but it can be
configured to use the root directory instead by modifying the
`repository-path` variable. Unfortunately it mandates that all pages
end with the suffix `.page`, rather than recognizing other suffixes
like `.md`. I couldn't find a way to configure this, though presumably
it would only require a trivial change to the code.

GitHub
------

[GitHub](http://github.com)'s repository viewer also renders markdown
files. Unfortunately, it appears that creating a relative link from
the root README to other files in the repository is ***impossible***,
and [not likely to be
added](https://github.com/github/markup/issues/84).

Another possibility I haven't looked into is to use [GitHub
Pages](http://pages.github.com/). That feature publishes Markdown
files from a branch named `gh-pages`, using
[jekyll](https://github.com/mojombo/jekyll/). My impression is that
the intended usage is for the `gh-pages` branch to diverge from code
branches at the first commit, and not contain the code
itself. However, I don't think there's anything to stop one from
keeping `gh-pages` synchronized with master; i.e., having the markdown
files mixed with the code.
