let control = 0;

function drawer(){
    var in_box = document.getElementById("in");
    var up_box = document.getElementById("up");


    if(control == 0){
        in_box.style.transform = "translateX(100%)";
        up_box.style.transform = "translateY(-100%)";
        control = 1;

    }
    else{
        in_box.style.transform = "translateX(0%)";
        up_box.style.transform = "translateY(0%)";
        control = 0;
    }
    
}

function drawer_mini(){

    var up_box = document.getElementById("up");
    var descrp = document.getElementById("main_box");
    


        up_box.style.display = "flex";
        descrp.style.transform = "translateY(-85%)";

        descrp.style.background = "transparent";
        descrp.style.border = "none";
}

function pasw_vision(side){
    
    var icon_up = document.getElementById("icon_up")
    var icon_in = document.getElementById("icon_in")

    var input_up = document.getElementById("uPas");
    var input_in = document.getElementById("iPas");


    

    if(side=='upas'  ){
        if(input_up.type== "password"){
            input_up.type = "text";
            icon_up.src = "./static/eyehidden.png";
            
        }
        else if(input_up.type = "text"){
            input_up.type = "password";
            icon_up.src = "./static/eyevisible.png";
        }
    }
    else if(side=='ipas'){
        if(input_up.type== "password"){
            input_up.type = "text";
            icon_in.src = "./static/eyehidden.png";
            
        }
        else if(input_up.type = "text"){
            input_up.type = "password";
            icon_in.src = "./static/eyevisible.png";
        }
    }


}