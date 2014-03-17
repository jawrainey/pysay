# pysay

pysay is a small command-line utility that uses the [forvo API](http://api.forvo.com/) to provide audio playback of a word _or_ phrase in their native language. It was written as a replacement for the `say` command provided by OSX with a native language alternative.

## Installation

You will need to [sign up](http://api.forvo.com/plans-and-pricing/free/) to forvo and replace the contents of `APIKEY` in `pysay.py` with your key.

    git clone http://github.com/jawrainey/pysay.git ~/pysay
    cd ~/pysay && chmod +x pysay.py
    mv pysay.py /usr/local/bin/pysay #Note the removal of extension

## Usage

To hear audio playback of a desired word, run `pysay` and pass in the desired word:

    pysay schmetterling

To hear a phrase you must surround it with quotations:

    pysay "auf wiedersehen"

You can hear alternative pronunciations by modifying the `action` option:

    pysay schmetterling --action=word-pronunciations

If you prefer to hear words in a male or female voice, pass in the `sex` option:

    pysay здравствуйте --sex=f

## Requirements

- Python 2.7 or greater is required to make use of [argparse](https://pypi.python.org/pypi/argparse).

I have opted to use `mplayer` as there is no built-in audio player on Linux. This can be installed through `apt-get`:

    sudo apt-get install mplayer

## Contributing

If you have any suggestions for improvements, feel free to open an [issue](https://github.com/jawrainey/pysay/issues)
or make a [pull request](https://github.com/jawrainey/pysay/pulls).

## License

pysay is licensed under the [MIT License.](https://github.com/jawrainey/pysay/blob/master/LICENSE.txt)
