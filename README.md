# setting_pyvis

You can't do this with barnes_hut or any specified algo, it seems.
https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html

Here is the usage case (very bottom):
https://pyvis.readthedocs.io/en/latest/tutorial.html


Lines 29-34 show you where to paste it. You generate the code after creating a map with show buttons. Under the buttons, you'll see the option to generate the JavaScript. Copy and paste that as a string into set_options()
