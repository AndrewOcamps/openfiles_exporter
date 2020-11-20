import time
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
from getLimits import OpenFiles
import yaml
import os

def read_configuration(config_file):
  with open(config_file, 'r') as f:
    try:
      configuration = yaml.safe_load(f)
      for config in configuration:
        users = config['users']

      return users

    except yaml.YAMLError as exc:
      return exc

class CustomCollector(object):
    def __init__(self):
      pass

    def collect(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        users = read_configuration(os.path.join(basedir, 'configuration.yml'))
        try:
          if users != None:
            for user in range(len(users)):
              user_pid = users[user]
              for userName in user_pid:
                for processName in range(len(user_pid[userName])):
                  openfiles = OpenFiles(user_pid[userName][processName]).count()
                  g = GaugeMetricFamily("Count_OpenFiles", 'Help text', labels=['limit', 'user', 'pid'])
                  for pid in openfiles:
                   g.add_metric(["open files", userName, pid], openfiles[pid])
                  yield g
          else:
            raise TypeError
        except TypeError:
          print('Some error in configuration file!')

if __name__ == '__main__':
    start_http_server(5633)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)

