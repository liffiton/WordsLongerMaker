#!/usr/bin/env python3

import bottle

import wordslongermaker


@bottle.get('/', template='index')
def make_longer():
    text = bottle.request.query.text
    if text:
        longer = wordslongermaker.make_longer_all(text)
        return {'text': text, 'longer': longer}
    else:
        return {'text': '', 'longer': ''}


def main():
    bottle.run()


if __name__ == '__main__':
    main()
