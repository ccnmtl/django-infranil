# django-infranil

[![Build Status](https://travis-ci.org/ccnmtl/django-infranil.png)](https://travis-ci.org/ccnmtl/django-infranil)
[![Coverage Status](https://coveralls.io/repos/github/ccnmtl/django-infranil/badge.svg?branch=master)](https://coveralls.io/github/ccnmtl/django-infranil?branch=master)

Infranil can be thought of as `TemplateView` on steroids. It allows
you to servce up a directory of Django templates with a minimum of
ceremony and configuration.

## Motivation

Sometimes you just have some random pages that need to be part of your
application. Nothing complicated, just some good old HTML for the most
part. No real structure, just miscellaneous additional content that
needs to sit alongside your main application functionality.

A CMS like Mezzanine or Wagtail would do the job, but seems like a lot
of overhead to pull in for a couple basic pages. There isn't any real,
consistent *structure* to these pages, so automatically generating
navigation won't help much; you'll end up manually overriding more of
the CMS functionality than you use.

Flatpages might work. But maybe the pages have just a bit more
complicated markup and javascript in them than you're comfortable
editing through a textarea. And maybe the nature of these pages really
lend themselves to being files on disk managed by version control
rather than stored in your database.

You could make an 'html' directory in your static media and have them
served straight from there. But maybe you really want just a *little*
bit of dynamicism; you've already got a nice base template with your
site's overall styling and it would be nice to be able to inherit from
that. Or you want access to the `request.user` so you can keep your
global navbar working on the pages. Or you've got a custom templatetag
that provides some functionality that would be really nice to have
here.

At this point, you'll probably start using Django's built-in
`TemplateView` and set up a bunch of them in your `urls.py`. If it's
just a handful, that's fine. Too many and it becomes a chore,
especially if you're mainly a designer rather than a programmer and
the parts of Django outside of templates are a little frightening and
confusing. Now you're missing the good/bad old days of simple PHP apps
where you just drop a file in a directory and pull it up in a browser,
sprinkling in a bit of dynamic functionality just where you need it.

This is what Infranil is for. You set up one URL route pointing at a
directory of simple templates and it does the rest.

## Basic Usage

    $ pip install django-infranil

Add `infranil` to your `INSTALLED_APPS`.

In your `urls.py`, you add:

    from infranil.views import InfranilView
    ...
    (r'^infranil/(?P<path>.*)$', InfranilView.as_view()),

Make an `infranil` directory in your project's templates directory. In
there, add a `foo.html` file with normal Django template syntax. Now
you can access that page at `/infranil/foo/`. Bob's your uncle.

## Details

There are only a couple rules that you'll need to keep in mind to
understand how Infranil maps URL paths to files in your template
directory.

First, when the URL has a path like `foo/`, Infranil will first look
for `foo.html`. If it doesn't find that, it will look for
`foo/index.html`. If it doesn't find either of those, you get a
404. Additional subdirectories are OK and follow normal
rules. `foo/bar/baz/' will map to `foo/bar/baz.html` or
`foo/bar/baz/index.html`.

Obviously, the `.html` extension doesn't go in the URL. File
extensions really have no place in modern web app URLs.

The only other thing to know is that Infranil is also very restrictive
on what characters you can have in the filename. This is mainly to
avoid any security issues where, eg an attacker might try to request
`../../../etc/passwd` or otherwise break out of the designated
template directory and get your app to serve up files that it
shouldn't.

So, to make sure that can't happen. Infranil allows *only*
alphanumerics, hyphens, and forward slashes in the
URL/filenames. Anything else is stripped out automatically. This is
really in line with best practices for naming files on unix systems
anyway.

You can also override the base template directory when you instantiate
the view:

    (r'^infranil/(?P<path>.*)$',
     InfranilView.as_view(base_dir="somewhere_else")),

This is particularly handy if you want to have multiple Infranil
instances at different paths:

    (r'^one/(?P<path>.*)$',
     InfranilView.as_view(base_dir="infranil_one")),
    (r'^two/(?P<path>.*)$',
     InfranilView.as_view(base_dir="infranil_two")),

Of course, `InfranilView` is a basic Django class-based view, so you
can subclass it, combine it with mixins, etc.

## Suggestions

Infranil combined with
[django-flatblocks](https://github.com/funkybob/django-flatblocks) is
a powerful combination. If they're both set up, you've got the basics
of a rudimentary CMS with full control over which parts are
user-editable through the web and which parts are designer controlled
and in version control.

## Infranil?

Yeah, the name is super nerdy. I had the idea for this library when
pondering the solution space of flatblocks and flatpages. An 'infranil
manifold' in Riemannian Geometry is an "[almost flat](http://en.wikipedia.org/wiki/Almost_flat_manifold)" manifold.

