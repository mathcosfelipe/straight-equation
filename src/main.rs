mod reduced_equation;

use reduced_equation::reduced_equation;

fn main(){
    let xa:f64 = 10.5;
    let ya:f64 = 20.5;
    let xb:f64 = 30.5;
    let yb:f64 = 40.5;
    
    let reduced_equation:() = reduced_equation::reduced_equation(xa, ya, xb, yb);
    println!("The reduced equation is {:?}", reduced_equation);
}