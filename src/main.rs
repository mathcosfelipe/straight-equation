extern crate beginner_tools;
use beginner_tools::input;

mod straight;
use straight::Straight;

fn main() {
    
    let xa: f64 = loop {
        if let Ok(xa_validation) = input("Input xa value: ") {
            break xa_validation
        };
        println!("Invalid value! Input a float number. Try again.");
    };

    let ya: f64 = loop {
        if let Ok(ya_validation) = input("Input yb value: ") {
            break ya_validation
        };
        println!("Invalid value! Input a float number. Try again.");
    };

    let xb: f64 = loop {
        if let Ok(xb_validation) = input("Input yb value: ") {
            break xb_validation
        };
        println!("Invalid value! Input a float number. Try again.");
    };

    let yb: f64 = loop {
        if let Ok(yb_validation) = input("Input yb value: ") {
            break yb_validation
        };
        println!("Invalid value! Input a float number. Try again.");
    };

    let reduced: Straight = straight::Straight {xa, ya, xb, yb};

    let general: Straight = straight::Straight {xa, ya, xb, yb};

    reduced.reduced();
    general.general();

}