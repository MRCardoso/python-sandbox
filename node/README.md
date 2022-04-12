### Node theadpool single test
```
    for default are created 4 threads to work into threadpool
    this default value can be change the 'process.env.UV_THREADPOOL_SIZE'
    but remember, the process running into the threadpool, still use the Core resource of CPU/cores, so be carreful with this configuration
    how many threadpool, more will be required of your CPU/cores, that mean your response time will be bigger
     
    por padrao sao criados 4 threads para trabalhar com processo na threadpool.
    na chamada do processo(fs.readFile), sao feito duas chamadas em disco
    1 - acessa disco para obter stats do arquivo
    2 - acessa disco para obter o conteudo do arquivo e retornar
    como esse processo de leitura de disco pode durar "eternamente", a thread do (fs.readFile) é liberada para outros processo...
    dependendo de quantos outros processos ainda irão usar a threadpool, a operacao de fs pode demorar muito mais do que geralmente iria,
    por ficar 'esperando' uma thread disponivel para terminar a operacao,
    Caso seja apenas 3 processo que consumam a threadpool, mais fs.readFile, o processo de fs.readFile sera o primero a ser concluido.
    do contrario, quando mais processo forem consumir a theadpool, maior sera o tempo de conclusao da operacao(fs.readFile)
    caso seja fs.readFile + 4 doHash(), fs.readFile sera p 3 a ser concluido
    caso seja fs.readFile + 5 doHash(), fs.readFile sera p 4 a ser concluido
    caso seja fs.readFile + 6 doHash(), fs.readFile sera p 5 a ser concluido
    e assim por diante...
    esta metricas podem oscilar dependendo do SO(quantidade de cores) e o proprio tempo de resposta para acesso a disco
```
### runing 3 doHash()
```Shell
node multithead.js
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
$ node multithead.sj 4
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