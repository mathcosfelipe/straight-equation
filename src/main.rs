fn constant_coeficient_general(xa:f64, ya:f64, xb:f64, yb:f64){
    let first_main_diagonal:f64 = xb * ya * -1.0;
    let third_secondary_diagonal:f64 = xa * yb;
    let mut sum_c:f64 = first_main_diagonal + third_secondary_diagonal;
    let value:String;
    if sum_c > 0.0{
        value = format!(" + {}", sum_c.to_string());
    }else if sum_c < 0.0{
        value = format!(" - {}", (sum_c * -1.0).to_string());
    }else{
        value = format!();
    }
}

fn linear_coeficient_general(xa:f64, xb:f64){
    let third_main_diagnoal:f64 = xa * -1.0; 
    let second_secondary_diagonal:f64 = xb;
    let mut sum_y:f64 = third_main_diagnoal + second_secondary_diagonal;
    let value:String;
    if sum_y > 0.0{
        value = format!(" + {}", sum_y.to_string());
    }else if sum_y < 0.0{
        value = format!(" - {}", (sum_y * -1.0).to_string());
    }else{
        value = format!();
    }
}

fn angular_coeficient_general(ya:f64, yb:f64){
    let second_main_diagonal:f64 = yb * -1.0;
    let first_secondary_diagonal:f64 = ya;
    let mut sum_x:f64 = second_main_diagonal + first_secondary_diagonal;
    let value:String;
    if sum_x > 0.0{
        value = format!("{}", sum_x.to_string());
    }else if sum_x < 0.0{
        value = format!("- {}", (sum_x * -1.0).to_string());
    }else{
        value = format!();
    }
}

fn general_equation(xa:f64, ya:f64, xb:f64, yb:f64){
    let angular_coeficient: () = angular_coeficient_general(ya, yb);
    let linear_coeficient: () = linear_coeficient_general(xa, xb);
    let constant_coeficient: () = constant_coeficient_general(xa, ya, xb, yb);
    let general_equation: String = format!("The general equation is {:?}{:?}{:?}", angular_coeficient, linear_coeficient, constant_coeficient);
}   

fn linear_coeficient_reduced(xa:f64, ya:f64, xb:f64, yb:f64){
    let yb_ya:f64 = yb - ya;
    let xb_xa:f64 = xb - xa;
    let angular_coeficient:f64 = yb_ya / xb_xa;
    let mut linear_coeficient = angular_coeficient * xa;
    linear_coeficient = linear_coeficient + ya;
    let value: String;
    if linear_coeficient > 0.0{
        value = format!(" + {}", linear_coeficient.to_string());
    }else if linear_coeficient < 0.0{
        value = format!(" - {}", (linear_coeficient * -1.0).to_string());
    }else{
        value = format!();
    }
}

fn angular_coeficient_reduced(xa:f64, ya:f64, xb:f64, yb:f64){
    let yb_ya:f64 = yb - ya;
    let xb_xa:f64 = xb - xa;
    let mut angular_coeficient:f64 = yb_ya / xb_xa;
    let value: String;
    if angular_coeficient > 0.0{
        value = format!("{}", angular_coeficient.to_string());
    }else if angular_coeficient < 0.0{
        value = format!("- {}", (angular_coeficient * -1.0).to_string());
    }else{
        value = format!();
    }
}

fn reduced_equation(xa:f64, ya:f64, xb:f64, yb:f64){
    let angular_coeficient: () = angular_coeficient_reduced(xa, ya, xb, yb);
    let linear_coeficient: () = linear_coeficient_reduced(xa, ya, xb, yb);
    let reduced_equation: String = format!("The reduced equation is {:?}{:?}", angular_coeficient, linear_coeficient);
}

fn main() {
    let xa:f64 = 1.5;
    let ya:f64 = 2.5;
    let xb:f64 = 5.5;
    let yb:f64 = 6.5;
    let reduced_equation: () = reduced_equation(xa, ya, xb, yb);
    let general_equation: () = general_equation(xa, ya, xb, yb);
    println!("{:?}", reduced_equation);
    println!("{:?}", general_equation);
}