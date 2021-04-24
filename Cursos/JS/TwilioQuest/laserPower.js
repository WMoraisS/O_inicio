var nums = [1, 2, 3, 4, 5, 6]
var power = calculatePower(nums)

function calculatePower(nums) {
    var total = 0
    nums.forEach(value => {
       total = total + (value * 2)
       console.log(value)
    });
    
    return total
}

console.log(power)