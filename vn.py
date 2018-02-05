#!/usr/bin/env python
import click
from util import is_japanese
from glosbe import Glosbe
import crayons
from prompt_toolkit import prompt
from bs4 import BeautifulSoup

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
            phrase = prompt("[vn] > ")
            if is_japanese(phrase):
                frm = 'jpn'
                dst = 'eng'
            else:
                frm = 'eng'
                dst = 'jpn'
            if phrase == ':q':
                break
            if phrase == '' or phrase == None:
                click.echo('empty phrase')
                continue
            result = _translate(phrase, frm, dst)
            translations = result.get_translations()
            examples = result.get_examples()
            print_translations(translations, limit)
            print_examples(examples, frm, dst)
    else:
        if phrase == '' or phrase == None:
            click.echo('empty phrase')
            exit(1)
        if is_japanese(phrase):
            frm = 'jpn'
            dst = 'eng'
        else:
            frm = 'eng'
            dst = 'jpn'
        result = _translate(phrase, frm, dst)
        translations = result.get_translations()
        examples = result.get_examples()
    print_translations(translations, limit)
    print_examples(examples, frm, dst)




def print_examples(examples, frm, dst, limit=5):
    print (crayons.white("Example:"))
    for i, example in enumerate(examples):
        example = list(map(lambda x: BeautifulSoup(x, "lxml").get_text(), example))
        if frm == 'eng' and dst == 'jpn':
            print (crayons.white("\tENG - {}".format(example[0])))
            print (crayons.white("\tJPN - {}".format(example[1])))
        elif frm == 'jpn' and dst == 'eng':
            print (crayons.white("\tJPN - {}".format(example[0])))
            print (crayons.white("\tENG - {}".format(example[1])))
        if i > limit:
            break
        print()

def print_translations(translations, limit):
    print (crayons.white("Translation:"))
    for i, translation in enumerate(translations):
        print (crayons.white("\t - {}".format(translation)))
        if i > limit:
            break
        
    

def _translate(phrase, frm, dst):
    api = Glosbe(frm, dst)
    click.echo("translate... %s from %s to %s" % (crayons.red(phrase), crayons.blue(frm), crayons.blue(dst)))
    api.translate(phrase, tm=True)
    return api

def main():
    cmd()

if __name__ == "__main__":
    main()
