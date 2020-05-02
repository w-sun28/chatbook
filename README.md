# chatbook
Python-based summary and keyword extractor and question answering system   about a document's content

##INSTALL
See the ```requirements.txt``` file if installing directly. To make an editable package locally, use

```
pip3 install -e .
```
To embed in a system as is, from ```pypi.org``` use

```
pip3 install -U chatbook
```

##USAGE:

This lightweight version of the [doctalk](https://github.com/ptarau/pytalk) package assumes that files have been pre-processesed by ```doctalk``` from .txt or .pdf files into .json files. With minimal dependencies (networkx and nltk) and memory requeirements this package is planned to be exposed as a Web App or as an Alexa skill.

```
python3 -i

>>> from chatbook.talk import run_with
>>> run_with(fname)
```
This activates dialog about document in ```<fname>.txt``` with questions in ```<fname>_quests.txt```

See some examples at : 

[https://github.com/ptarau/chatbook](https://github.com/ptarau/chatbook) , where, after installing the system, you can run

```
python3 -i tests.py
>>> go()
```

To play with various parameter settings, edit the ```chatbook/params.py``` file.

### Web App
To use the included ``docbot``` Web app, after installing ```Flask``` and ```waitress```, run the ```app.py``` file in directory ```docbot``` with ```python3 app.py```. 

The docbot uses a JSON-based API, documented in ```chatbook/api.py```. In fact, this is the simplest way to integrate the summarizer and the dialog agent into a production system.

