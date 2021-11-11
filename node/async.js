// OS's async features, what node std function use it? almost everithing around networking for all OS's, some other stuff is OS specific
// tasks using OS are reflected in the 'pendingOSTasks'
const https = require('https')
const Timer = require('./Timer')
const timer = new Timer()

const doRequest = (next) => {
    https.request('https://www.google.com', res => {
        res.on('data', () => {})
        res.on('end', next)
    })
    .end()
}

doRequest(() => console.log(`1: ${timer.elapseTime}`))
doRequest(() => console.log(`2: ${timer.elapseTime}`))
doRequest(() => console.log(`3: ${timer.elapseTime}`))
doRequest(() => console.log(`4: ${timer.elapseTime}`))
doRequest(() => console.log(`5: ${timer.elapseTime}`))
doRequest(() => console.log(`6: ${timer.elapseTime}`))