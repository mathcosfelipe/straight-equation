fn linear_coeficient(xa:f64, ya:f64, xb:f64, yb:f64){
    let yb_ya:f64 = yb - ya;
    let xb_xa:f64 = xb - xa;
    let angular_coeficient:f64 = yb_ya / xb_xa;
    let angular_coeficient_ya:f64 = angular_coeficient * ya;
    let mut value:f64 = angular_coeficient_ya + ya;
    let linear_coeficient:String;
    if value < 0.0{
        linear_coeficient = format!(" - {}", (value * -1.0).to_string());
    }else if value > 0.0{
        linear_coeficient = format!(" + {}", value.to_string());
    }else{
        linear_coeficient = format!("");
    }
}

pub fn angular_coeficient(xa:f64, ya:f64, xb:f64, yb:f64){
    let yb_ya:f64 = yb - ya;
    let xb_xa:f64 = xb - xa;
    let mut value:f64 = yb_ya / xb_xa;
    let angular_coeficient:String;
    if value < 0.0{
        angular_coeficient = format!(" - {}", (value * -1.0).to_string());
    }else if value > 0.0 {
        angular_coeficient = format!("{}", (value).to_string());
    }else{
        angular_coeficient = format!("");
    }
}

pub fn reduced_equation(xa:f64, ya:f64, xb:f64, yb:f64){
    let angular_coeficient:() = angular_coeficient(xa, ya, xb, yb);
    let linear_coeficient: () = linear_coeficient(xa, ya, xb, yb);
    let reduced_equation: String = format!("{:?} {:?}", angular_coeficient, linear_coeficient);
}