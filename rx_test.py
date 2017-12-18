from rx import Observable
items = ["2017/10/13", "2016/01/02", "2000/11/12"]

(Observable.from_(items)
          .flat_map(lambda s: Observable.from_(s.split("/")))
          .map(lambda s: int(s))
          .subscribe(lambda s: print(s)))

print()

(Observable.from_(items)
          .map(lambda s: Observable.from_(s.split("/")))
          .concat_all()
          .map(lambda s: int(s))
          .subscribe(lambda s: print(s)))

print()

(Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])
           .group_by(lambda s: len(s))
           .flat_map(lambda grp: grp.to_list())
           .subscribe(lambda s: print(s)))
print()
(Observable.from_(["Bravo", "Charlie", "Tango", "Foxtrot"])
           .flat_map(lambda s: Observable.from_(s))
           .map(lambda s: s.lower())
           .distinct()
           .subscribe(lambda s: print(s)))

print()

from urllib.request import urlopen
def read_request(link):
    f = urlopen(link)
    return (Observable.from_(f)
                      .map(lambda s: s.decode('utf-8').strip()))
read_request('https://goo.gl/rIaDyM').subscribe(lambda s: print(s))

print()

import time
source = Observable.from_(["Alpha", "Beta", "Gamma", "Epsilon"]).publish().auto_connect(2)
source.subscribe(lambda s: print("Subscript 1: {}".format(s)))
time.sleep(1)
source.subscribe(lambda s: print("Subscript 2: {}".format(s)))
#source.connect()

