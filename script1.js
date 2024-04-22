// function

// function -> it is block of code that performs a specific task.

// types of function


// 1 function without argument and without return value.

function check1(){
    console.log(5);
}
check1()

// 2 function with argument and without return value.
function check2(a){
    console.log(a);
}
check2(5)
// 3 function without argument and with return value.
function check3(){
    let num = 16;
   let count=0;
    for(let a=1;a<=num;a++){
        if(num%a==0){
            count+=1;
        }
    }
    if(count==1){
        return "Not a prime number"
    }
    else{
        return "Prime number"
    }
}
let res = check3()
console.log(res);
// 4 function with argument andd with with return value.

