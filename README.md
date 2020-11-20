# openfiles_exporter
Counter of files opened by a specific linux user

### Specify the list of users with the respective processes to identify

``` yaml
# Configuration File 'configuration.yml'
---
- users:
    - jboss: ['java']
    - another_user: ['process1', 'process2', '...']
```

### Start the collector by the following way
#### Using Python directly
> Requires python 3

_Install dependencies_
```
pip install -r requirements.txt
```
_Start the process and leave it running in the background_
```
python collector.py </dev/null >> logexp.txt 2>&1 & echo $! > pidexp.txt
```
#### Using Python with virtual environment
> Requires python 3 and virtualenv


_Initialize virtual environment_
```
virtualenv -p python3 venv
source venv/bin/activate
```

_Install dependencies_
```
(venv) pip install -r requirements.txt
```
_Start the process with a script_
```
(venv) ./startcollector.py
```

#### The pid of the process is stored in the following directory
```
pidexp.txt
```

#### You can observe any eventuality in the following log
```
logexp.txt
```

### In your browser
Go to the http://hostname:5633/

```
# TYPE Count_OpenFiles gauge
Count_OpenFiles{limit="open files",pid="23690",user="jboss"} 2885.0
Count_OpenFiles{limit="open files",pid="23619",user="jboss"} 342.0
Count_OpenFiles{limit="open files",pid="23593",user="jboss"} 32.0
```