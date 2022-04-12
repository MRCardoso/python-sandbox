### Node theadpool single test
    for default are created 4 threads to work into threadpool
    this default value can be change the 'process.env.UV_THREADPOOL_SIZE'
    but remember, the process running into the threadpool, still use the Core resource of CPU/cores, so be carreful with this configuration
    how many threadpool, more will be required of your CPU/cores, that mean your response time will be bigger
    when is call a process to access hard-disc, are make 2 call to the HD
    1 - Access HD to get the stats of the file
    2 - Access HD to get the content of the file and return it
    how this reading process in the disc can last "forever", the thread allocated for 'fs.readFile' is release for another process to use...
    At this moment, the output(console.log) may be different, according to the amount of the processes to be executed in threadpool
    in short words....
    If the total of threads to be executed into the threadpool it's the same size as the threadpool size, the readFile will be the first log
    otherwise, the more processes running into threadpool, greather the waiting time of the readFile to be concluded
    e.g fs.readFile + 3 doHash(), fs will be the first log
    e.g fs.readFile + 4 doHash(), fs will be the thrid log
    e.g fs.readFile + 5 doHash(), fs will be the quarter log
    e.g fs.readFile + 6 doHash(), fs will be the fifth log
    and so on...
    this example may be change, according the SO resources (core size)
    remenber the https request, not running into the threadpool, it will be processed by the SO resources

### runing 3 doHash()
```Shell
node multithread.js
```
### Output
```
FS: 11
Http: 249
Hash: 490
Hash: 496
Hash: 509
```

### runing 4 doHash()
```Shell
$ node multithread.js 4
```
### Output
```
Http: 495
Hash: 501
FS: 501
Hash: 511
Hash: 511
Hash: 513

```