// example of closure

function main(a){
    function add(b){
        console.log(a+b);
    }
    console.log(a);
    return add
}
const finalRes = main(5);
finalRes(10);