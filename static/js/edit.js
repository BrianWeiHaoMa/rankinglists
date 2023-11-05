const editButton = document.getElementById("my-edit-button");
if (editButton) {
    editButton.isToggled = false; 
    editButton.addEventListener("click", function() {
        buttons = document.getElementsByClassName("my-hidden-button");
        if (this.isToggled) {
            this.isToggled = false;
            for (let button of buttons) {
                button.classList.add("d-none");
            }
        } else {
            this.isToggled = true;
            for (let button of buttons) {
                button.classList.remove("d-none");
            }
        }
    });    
}
