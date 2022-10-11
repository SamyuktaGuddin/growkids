$(document).ready(function() {
    console.log("login js file");
    $("#login").submit(function (event) {
        event.preventDefault();
        console.log("On Submit!");
    })
})