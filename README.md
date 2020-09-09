#locustes

How to run
============

1. Locust is available on PyPI and can be installed with pip
    1) for Python 2.7:
        $ python -m pip install locustio

    2) for Python 3:
        python3 -m pip install locustio

2. Once Locust is installed, a locust command should be available in your shell
   To see available options, run:

    $ locust --help

  Locust supports Python 2.7, 3.4, 3.5, and 3.6.

3. To run Locust. run
    $ locust -f locust_files/my_locust_file.py --host=http://example.com

4. Once you’ve started Locust using one of the above command lines,
   you should open up a browser and point it to http://127.0.0.1:8089


