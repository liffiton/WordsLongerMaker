# WordsLongerMaker

WordsLongerMaker takes your words and makes them longer!

That is, it uses [WordNet](http://wordnet.princeton.edu/) data to find synonyms for every word in your text, replacing each word with the longest synonym it can find.  Instant longerfication!

## Dependencies

WordsLongerMaker is written in Python 3.

For language-processing, it uses [NLTK](http://www.nltk.org/) with the
``averaged_perceptron_tagger``, ``punkt``, ``universal_tagset``, and
``wordnet`` data installed:

    pip3 install nltk

You can download the required NLTK data using its built-in downloader:

    python3
    >>> import nltk
    >>> nltk.download()

The web interface uses [Bottle](http://bottlepy.org/) and any [server supported by Bottle](http://bottlepy.org/docs/dev/deployment.html#switching-the-server-backend).  The code here uses ``gunicorn``, but any other server, including the default server provided in ``bottle`` itself, will work.

    pip3 install bottle

## Usage

Once all dependencies are installed, simply run:

    ./weblongermaker.py

Point your browser to port 8080, and start making your words longer!
