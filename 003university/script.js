let attemps = 0;

let computer = 0;
let medicine = 0;
let marketing = 0;
let arts = 0;

let send = document.getElementById("send");

send.addEventListener("click", login)

function login() {
    let user = document.getElementById("user").value;
    let password = document.getElementById("password").value;

    if (attemps === 2) {
        let blocked = document.getElementById("blocked");
        invalid.style.display = "none";
        blocked.style.display = "block";
        document.getElementById("user").value = "";
        document.getElementById("password").value = "";
    } else if (user === "1" && password === "1") {
        let form = document.getElementById("form");
        form.style.display = "none"
        document.getElementById("selection").style.display = "block"
    } else {
        let invalid = document.getElementById("invalid");
        invalid.style.display = "block";
        document.getElementById("user").value = "";
        document.getElementById("password").value = "";
        attemps ++
    }
}

let register = document.getElementById("register");
register.addEventListener("click", selection)

function selection() {
    document.getElementById("selection").style.display = "none"
    check()
}

function check() {
    if(document.getelement("selection)")) {
        function 

    }
}




