"Curious memory consumption of pandas.unique()"
===============================================

This repo contains code and data for this [Stack Overflow question asked by @ead][so].

The test case is the same as their original code, however the bench for running is different;
in order to use more data points in a sane time, the bench preloads numpy and pandas, then `fork`s
off for each `n`.  In addition, it uses `resource.getrusage()` internally.

The data in `stats-lnx*.txt` was generated by running in Docker:

```
$ docker run -it python:3.7 -v $(pwd):/a
$ pip install pandas numpy
$ cd /a
$ python bench2.py | tee -a /a/stats-lnx.txt
```

The data in `stats-osx.txt` was generated in macOS.

```
python bench2.py --step-delta=2000 | tee -a stats-osx.txt
```

Charts can be generated with `python show.py --input=stats-osx.txt`.

[so]: https://stackoverflow.com/questions/51485816/curious-memory-consumtion-of-pandas-unique/51715694?noredirect=1#comment90400811_51715694
