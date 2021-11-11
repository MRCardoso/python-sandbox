class Timer {
    constructor(){
        this.reset()
    }
    
    reset() {
        this.initial = this.nowTime
        return this
    }

    get nowTime(){ return Date.now() }
    get initialTime(){ return this.initial }
    get elapseTime() { return this.nowTime - this.initial }
}

module.exports = Timer