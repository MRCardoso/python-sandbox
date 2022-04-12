const validateTime = (value) => /^([0-1][0-9]|2[0-4]):([0-5][0-9])(:[0-5][0-9])?$/.test(value)
const vs = {}
const validPeriods = () => {
    for(let i = 0; i<23;i++){
        for(let j = 0; j<=59;j++) {
            const value = String(i).padStart(2, "0") + ":" + String(j).padStart(2, "0");
            vs[value] = validateTime(value)
        }
    }
    console.table(vs)
}
let normalizeTime = (raw) => {
    let values = raw.split(":")

    if(values.length < 2) {
        for (let i = values.length; i < 2; i++) {
            values[i] = "00"
        }
    }
    values = values.map(h => {
        const fillRight = /^\d_$/.test(h)
        const current = h.replace(/[^0-9]/ig, '')
        return current[fillRight ? "padEnd" : "padStart"](2, "0")
    })
    
    let hours = (/^([0-1][0-9]|2[0-3])?$/.test(values[0]) ? values[0] : "00")
    let minutes = (/^([0-5][0-9])?$/.test(values[1]) ? values[1]: "00")
    return [hours, minutes]
}
const params = process.argv.slice(2)
const time = (params[0] || "00:00")
console.log(validateTime(time))
console.log(normalizeTime(time))
// console.table(Object.keys(vs).filter(k => vs[k] === false)) // invalid hours