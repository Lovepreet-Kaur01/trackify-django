const toggleButton =
document.getElementById("theme-toggle");


// CHECK SAVED THEME

if(localStorage.getItem("theme") === "light"){

    document.body.classList.add("light-mode");

    toggleButton.innerHTML = "☀️";
}


toggleButton.addEventListener("click", () => {

    document.body.classList.toggle("light-mode");


    // SAVE THEME

    if(
        document.body.classList.contains(
            "light-mode"
        )
    ){

        localStorage.setItem(
            "theme",
            "light"
        );

        toggleButton.innerHTML = "☀️";

    }

    else{

        localStorage.setItem(
            "theme",
            "dark"
        );

        toggleButton.innerHTML = "🌙";
    }

});