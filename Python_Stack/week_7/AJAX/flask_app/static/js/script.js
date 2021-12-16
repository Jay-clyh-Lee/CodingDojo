async function getCoderData() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch("https://api.github.com/users/jay-clyh-lee");
    // We then need to convert the data into JSON format.
    var coderData = await response.json();
    return coderData;
}
console.log(getCoderData());

// fetch("https://api.github.com/users/jay-clyh-lee")
//     .then(response => response.json() )
//     .then(coderData => console.log(coderData) )
//     .catch(err => console.log(err) )

