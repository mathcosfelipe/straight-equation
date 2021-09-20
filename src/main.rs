mod reduced_equation;
mod general_equation;

fn main() {
    let xa:f64 = 1.5;
    let ya:f64 = 2.5;
    let xb:f64 = 4.5;
    let yb:f64 = 5.5; 
    let _reduced_equation: () = reduced_equation::reduced_equation(xa, ya, xb, yb);
    let _general_equation: () = general_equation::general_equation(xa, ya, xb, yb);

    // println!("The reduced equation is {}", reduced_equation);
    // println!("The general equation is {}", general_equation);

}