function SwitchCase(somestring) {
    // Please write your code here.
    var new_str = ""
    for (let i = 0; i<somestring.length; i++){
        if (i % 2 == 0) {
            new_str+=somestring[i].toUpperCase()
        }
        else {
            new_str+=somestring[i].toLowerCase()
        }
    }
    return new_str
}
console.log(SwitchCase("asdfASDFASD$!"))

function weirdBUG(some_str) {
    // var some_str = "asdfasfads"
    var some_empty_str1 =""
    var some_empty_str2 =""
    for (let i = 0; i<some_str.length; i++){
        some_empty_str1 += some_str[i].toUpperCase()
    }
    for (let i = 0; i<some_str.length; i++){
        some_empty_str2 = some_empty_str2 + some_str[i].toLowerCase()
    }
    console.log(some_empty_str1)
    console.log(some_empty_str2)
    return some_empty_str1 + "VS" + some_empty_str2
}
weirdBUG("dsalfjasdAD")



// solution = function(str) {
//     for (let i =0; i<str.length; i++){ if (i%2){str[i]=str[i].toUpperCase()} else{str[i]=str[i].toLowerCase()} }