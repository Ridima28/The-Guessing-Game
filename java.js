let userinput = document.getElementById("userinput");
let gameresult = document.getElementById("gameresult");
let number = Math.ceil(Math.random()*100);


function buttonCheck(){
    let guessnumber = parseInt(userinput.value);

    if (guessnumber === number) {
        gameresult.textContent="Congratulations You Guessed The Correct Number!!";
        gameresult.style.backgroundColor = "#22870039";



    }else if (guessnumber <number){
        gameresult.textContent = "Guess Is Too Low, Try Higher Number!";
        gameresult.style.backgroundColor = "#9eff9dff";
    } else if (guessnumber > number) {
        gameresult.textContent= "Guess Is Too High, Try Lower Number!";
        gameresult.style.backgroundColor = "#9eff9dff";
    } else{
        gameresult.textContent = "Enter A Valid Number!";
        gameresult.style.backgroundColor = "#9eff9df";
    }
}