const form = document.getElementById('myForm')
const jsonOutput = document.getElementById('jsonOutput')

//create an event to coonnnet the form to the send button
form.addEventListener("submit", function(event){
    event.preventDefault()
    const fname = document.getElementById("fname").value
    const lname = document.getElementById("lname").value

    const data = {
        firstname: fname,
        lastname: lname
    }
    //display the data on html page when send button is pressed
    jsonOutput.innerHTML = JSON.stringify(data)

})