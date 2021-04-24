var resp = process.argv[2]

getLaserSetting(resp)

function getLaserSetting(resp) {
    if (resp == 'please') {
        return 'OFF'
    } else {
        return 'ON'
    }
}