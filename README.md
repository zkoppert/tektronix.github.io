[![TekMonogram](https://tektronix.github.io/media/tekmonogram.png)](https://github.com/tektronix)

# tektronix.github.io [![Tektronix](https://tektronix.github.io/media/TEK-opensource_badge.svg)](https://github.com/tektronix) ![Builds](https://travis-ci.com/tektronix/tektronix.github.io.svg?branch=master)

A landing page for Tektronix Github Repos

## Maintainers

- [Zack Koppert](https://github.com/zkoppert)

## Local builds

1. Install a full Ruby development environment

   - [macOS](https://jekyllrb.com/docs/installation/macos/)
   - [Ubuntu Linux](https://jekyllrb.com/docs/installation/ubuntu/)
   - [Other Linux distros](https://jekyllrb.com/docs/installation/other-linux)
   - [Windows](https://jekyllrb.com/docs/installation/windows/)

2. Install Jekyll and bundler gems
   `gem install jekyll bundler`
3. Change into your repo if not already there
   `cd tektronix.github.io/`
4. Build the site and make it available on a local server
   `bundle exec jekyll serve`
5. Now browse to http://localhost:4000

## Testing

The following steps are performed as a part of CI. If you want to run them locally, do this:

- Install prettier and run `prettier --write *.md` then check the git diff for prettier's changes.
- Follow local build installation instructions above. Then run `bundle exec jekyll build` to ensure the site buidls.
