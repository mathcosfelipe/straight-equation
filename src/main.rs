fn angular_coeficient_general(xa: f64, ya: f64, xb: f64, yb: f64){
    let _yb_ya: f64 = yb - ya;
    let _xb_xa: f64 = xb - xa;
}

fn linear_coeficient_general(xa: f64, ya: f64, xb: f64, yb: f64){
    let _yb_ya: f64 = yb - ya;
    let _xb_xa: f64 = xb - xa;
}

fn constant_coeficient_general(xa: f64, ya: f64, xb: f64, yb: f64){
    let _yb_ya: f64 = yb - ya;
    let _xb_xa: f64 = xb - xa;
}

fn linear_coeficient_reduced(xa: f64, ya: f64, xb: f64, yb: f64){
    let yb_ya: f64 = yb - ya;
    let xb_xa: f64 = xb - xa;
    let linear_coeficient: f64 = yb_ya / xb_xa;

    if linear_coeficient < 0.0{
    }else if linear_coeficient > 0.0{

    }else{

    }
}

fn angular_coeficient_reduced(xa: f64, ya: f64, xb: f64, yb: f64){
    let yb_ya: f64 = yb - ya;
    let xb_xa: f64 = xb - xa;
    let angular_coeficient: f64 = yb_ya / xb_xa;
    
    if angular_coeficient < 0.0{
    }else if angular_coeficient > 0.0{

    }else{

    }
    
}

fn general_equation(xa: f64, ya: f64, xb: f64, yb: f64){
    let _angular_coeficient: () = angular_coeficient_general(xa, ya, xb, yb);
    let _linear_coeficient: () = linear_coeficient_general(xa, ya, xb, yb);
    let _constant_coeficient: () = constant_coeficient_general(xa, ya, xb, yb);
}

fn reduced_equation(xa: f64, ya: f64, xb: f64, yb: f64){
    let _angular_coeficient: () = angular_coeficient_reduced(xa, ya, xb, yb);
    let _linear_coeficient: () = linear_coeficient_reduced(xa, ya, xb, yb);
}

fn main(){
    let xa: f64 = 5.5;
    let ya: f64 = 10.5;
    let xb: f64 = 15.5;
    let yb: f64 = 20.5;
    let _reduced_equation = reduced_equation(xa, ya, xb, yb);
    let _general_equation = general_equation(xa, ya, xb, yb);
}