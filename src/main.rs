extern crate beginner_tools;
use beginner_tools::input;

struct Straight {
    xa: f64,
    ya: f64,
    xb: f64,
    yb: f64
}

pub fn angular_reduced(xa: f64, ya: f64, xb: f64, yb: f64) -> f64 {
    (yb - ya) / (xb - xa)
}

pub fn linear_reduced(xa: f64, ya: f64, xb: f64, yb: f64) -> f64 {
    ((yb - ya) / (xb - xa)) * xa + ya
}

pub fn angular_general(ya: f64, yb: f64) -> f64 {
    yb * -1.0 + ya
}

pub fn linear_general(xa: f64, xb: f64) -> f64 {
    xa * -1.0 + xb
}

pub fn constant_general(xa: f64, ya: f64, xb: f64, yb: f64) -> f64 {
    xb * ya * -1.0 + xa * yb
}

impl Straight {
    
    fn reduced(&self){

        let angular: f64 = angular_reduced(self.xa, self.ya, self.xb, self.yb);
        let linear: f64 = linear_reduced(self.xa, self.ya, self.xb, self.yb);
        let angular_string: String;
        let linear_string: String;

        if angular < 0.0 {
            angular_string = format!("- {}x", (angular * -1.0).to_string());
        } else if angular > 0.0 {
            angular_string = format!("{}x", angular.to_string());
        } else {
            angular_string = format!("");
        }

        if linear < 0.0 {
            linear_string = format!(" - {}", (linear * -1.0).to_string());
        } else if linear > 0.0 {
            linear_string = format!(" + {}", linear.to_string());
        } else {
            linear_string = format!("");
        }

        println!("The reduced equation is: {}{}", angular_string, linear_string);

    }

    fn general(&self) {

        let angular: f64 = angular_general(self.ya, self.yb);
        let linear: f64 = linear_general(self.xa, self.xb);
        let constant: f64 = constant_general(self.xa, self.ya, self.xb, self.yb);
        let angular_string: String;
        let linear_string: String;
        let constant_string: String;

        if angular < 0.0 {
            angular_string = format!("- {}x", (angular * -1.0).to_string());
        } else if angular > 0.0 {
            angular_string = format!("{}x", angular.to_string());
        } else {
            angular_string = format!("");
        }

        if linear < 0.0 {
            linear_string = format!(" - {}y", (linear * -1.0).to_string());
        } else if linear > 0.0 {
            linear_string = format!(" + {}y", linear.to_string());
        } else {
            linear_string = format!("");
        }

        if constant < 0.0 {
            constant_string = format!(" - {}", (constant * -1.0).to_string());
        } else if constant > 0.0 {
            constant_string = format!(" + {}", constant.to_string());
        } else {
            constant_string = format!("");
        }

        println!("The general equation is: {}{}{}", angular_string, linear_string, constant_string);

    }

}

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

    let reduced: Straight = Straight {
        xa: xa,
        ya: ya,
        xb: xb,
        yb: yb
    };

    let general: Straight = Straight {
        xa: xa,
        ya: ya,
        xb: xb,
        yb: yb
    };

    reduced.reduced();
    general.general();

}