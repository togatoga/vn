#!/usr/bin/env python
import click
from util import is_japanese
from glosbe import Glosbe
import crayons

@click.group()
def cmd():
    pass

@cmd.command(help="A simple translation tool in terminal.")
@click.option("--from", "-f", 'frm', default="jpn")
@click.option("--dest", "-d", 'dst', default="eng")
@click.argument('phrase')
def translate(phrase, frm, dst):
    # text is japanese
    if is_japanese(phrase):
        frm = 'jpn'
        dst = 'eng'
    else:
        frm = 'eng'
        dst = 'jpn'
    api = Glosbe(frm, dst)
    print ("translate... %s from %s to %s" % (crayons.red(phrase), crayons.blue(frm), crayons.blue(dst)))
    api.translate(phrase)
    print ('-------------------------Result-------------------------')
    api.show_translation()

def main():
    cmd()

if __name__ == "__main__":
    main()
