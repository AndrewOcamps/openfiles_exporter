# openfiles_exporter
Counter of files opened by a specific linux user

### Start the collector by the following way
```
./startcollector.sh
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