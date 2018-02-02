#!/usr/bin/env python
import click
from util import is_japanese
from glosbe import Glosbe
import crayons
from prompt_toolkit import prompt

@click.group()
def cmd():
    pass

@cmd.command(help="translate [phrase]")
@click.argument('phrase', required=False)
@click.option("--interactive", "-i", is_flag=True, help='interactive mode')
@click.option("--from", "-f", 'frm', default="jpn", help='language of phrase to translate, values: ISO 693-3 three letter language code')
@click.option("--dest", "-d", 'dst', default="eng", help='destination language, values: ISO 693-3 three letter language code')
@click.option("--limit", "-l", "limit", default=10, help='output limit')
def translate(interactive, phrase, frm, dst, limit):
    if interactive:
        click.echo(':q quit')
        while (True):
            phrase = prompt("> ")
            if phrase == ':q':
                break
            if phrase == '' or phrase == None:
                click.echo('empty phrase')
            result = _translate(phrase, frm, dst)
            result.show_translation(limit=limit)
    else:
        if phrase == '' or phrase == None:
            click.echo('empty phrase')
            exit(1)
        result = _translate(phrase, frm, dst)
        result.show_translation(limit=limit)


def _translate(phrase, frm, dst):
    # text is japanese
    if is_japanese(phrase):
        frm = 'jpn'
        dst = 'eng'
    else:
        frm = 'eng'
        dst = 'jpn'

    api = Glosbe(frm, dst)
    click.echo("translate... %s from %s to %s" % (crayons.red(phrase), crayons.blue(frm), crayons.blue(dst)))
    api.translate(phrase)
    return api

def main():
    cmd()

if __name__ == "__main__":
    main()
