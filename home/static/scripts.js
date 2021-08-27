timer();

function timer(){
    var currentTime = new Date()
    var hours = currentTime.getHours()
    var minutes = currentTime.getMinutes()
    var seconds = currentTime.getSeconds()
    if (seconds < 10){
        seconds = '0' + seconds
    }
    if (minutes < 10){
        minutes = '0' + minutes
    }
    st_r = hours + ':' + minutes + ':' + seconds + ' ';
    if (hours > 11){
        st_r += 'PM';
    }else {
        st_r += 'AM';
    }
    document.getElementById('datetime').innerHTML = st_r;
    setTimeout(timer, 1000);
}
