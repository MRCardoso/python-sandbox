const https = require('https')
const crypto = require('crypto')
const fs = require('fs')
const Timer = require('./Timer')
const timer = new Timer()
let totalHash = parseInt(process.argv[2])
if (isNaN(totalHash)) {
    totalHash = 3
}

const doRequest = (next) => {
    https.request('https://www.google.com', res => {
        res.on('data', () => {})
        res.on('end', next)
    })
    .end()
}
const doHash = () => {
    crypto.pbkdf2('a', 'b', 100000, 512, 'sha512', () => {
        console.log(`Hash: ${timer.elapseTime}`)
    })
}

doRequest(() => console.log(`Http: ${timer.elapseTime}`))

fs.readFile('multithread.js','utf8', () => {
    console.log(`FS: ${timer.elapseTime}`)
})

for (let i = 0; i < totalHash; i++) {
    doHash()
}