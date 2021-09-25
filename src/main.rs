fn constant_coeficient_general(xa:f64, ya:f64, xb:f64, yb:f64){

}

fn linear_coeficient_general(xa:f64, ya:f64, xb:f64, yb:f64){

}

fn angular_coeficient_general(xa:f64, ya:f64, xb:f64, yb:f64){
 
}

fn general_equation(xa:f64, ya:f64, xb:f64, yb:f64){
    let _angular_coeficient: () = angular_coeficient_general(xa, ya, xb, yb);
    let _linear_coeficient: () = linear_coeficient_general(xa, ya, xb, yb);
    let _constant_coeficient: () = linear_coeficient_general(xa, ya, xb, yb);
}

fn linear_coeficient_reduced(xa:f64, ya:f64, xb:f64, yb:f64){
    let yb_ya:f64 = yb - ya;
    let xb_xa:f64 = xb - xa;
    let angular_coeficient:f64 = yb_ya / xb_xa;
    let mut linear_coeficient = angular_coeficient * xa;
    linear_coeficient = linear_coeficient + ya;
    let mut value: String;
    if linear_coeficient > 0.0{
        value = "";
    }else if linear_coeficient < 0.0{
        value = "";
    }else{
        value = "";
    }
    return value;
}

fn angular_coeficient_reduced(xa:f64, ya:f64, xb:f64, yb:f64){
    let yb_ya:f64 = yb - ya;
    let xb_xa:f64 = xb - xa;
    let mut angular_coeficient:f64 = yb_ya / xb_xa;
    let mut value: String;
    if angular_coeficient > 0.0{
        value = angular_coeficient.to_string() + "x";
    }else if angular_coeficient < 0.0{
        value = angular_coeficient.to_string() + "x";
    }else{
        value = angular_coeficient.to_string() + "x";
    }
    return value;
}

fn reduced_equation(xa:f64, ya:f64, xb:f64, yb:f64){
    let _angular_coeficient: () = angular_coeficient_reduced(xa, ya, xb, yb);
    let _linear_coeficient: () = linear_coeficient_reduced(xa, ya, xb, yb);
}

fn main() {
    let xa:f64 = 1.5;
    let ya:f64 = 2.5;
    let xb:f64 = 5.5;
    let yb:f64 = 6.5;
    let _reduced_equation: () = reduced_equation(xa, ya, xb, yb);
    let _general_equation: () = general_equation(xa, ya, xb, yb);
}