extern crate beginner_tools;
use beginner_tools::input;
use straight::Straight;

mod straight;

fn main() {
    
    let xa: f64 = loop {
        if let Ok(n) = input("Input xa value: ") {
            break n
        };
        println!("Invalid value! Input a float number. Try again.");
    };

    let ya: f64 = loop {
        if let Ok(n) = input("Input yb value: ") {
            break n
        };
        println!("Invalid value! Input a float number. Try again.");
    };

    let xb: f64 = loop {
        if let Ok(n) = input("Input yb value: ") {
            break n
        };
        println!("Invalid value! Input a float number. Try again.");
    };

    let yb: f64 = loop {
        if let Ok(n) = input("Input yb value: ") {
            break n
        };
        println!("Invalid value! Input a float number. Try again.");
    };

    let reduced: Straight = straight::Straight {xa, ya, xb, yb};

    let general: Straight = straight::Straight {xa, ya, xb, yb};

    reduced.reduced();
    general.general();

}