use std::io::{stdin, stdout, Write};

fn constant_coeficient_general(xa:f64, ya:f64, xb:f64, yb:f64) -> String{
    let c_secondary_diagonal:f64 = xb * ya * -1.0;
    let c_main_diagnal:f64 = xa * yb;
    let constant_coeficient:f64 = c_main_diagnal + c_secondary_diagonal;
    let value:String;
    if constant_coeficient < 0.0{
        value = format!(" - {}", (constant_coeficient * -1.0).to_string());
    }else if constant_coeficient > 0.0{
        value = format!(" + {}", (constant_coeficient).to_string())
    }else{
        value = format!("");
    }
    return value;
}

fn linear_coeficient_general(xa:f64, xb:f64) -> String{
    let y_secondary_diagonal:f64 = xa * -1.0;
    let y_main_diagonal:f64 = xb;
    let linear_coeficient:f64 = y_main_diagonal + y_secondary_diagonal;
    let value:String;
    if linear_coeficient < 0.0{
        value = format!(" - {}y", (linear_coeficient * -1.0).to_string());
    }else if linear_coeficient > 0.0{
        value = format!(" + {}y", (linear_coeficient).to_string());
    }else{
        value = format!("");
    }
    return value;
}

fn angular_coeficient_general(ya:f64, yb:f64) -> String{
    let x_secondary_diagonal:f64 = yb * -1.0;
    let x_main_diagonal:f64 = ya;
    let angular_coeficient:f64 = x_main_diagonal + x_secondary_diagonal;
    let value:String;
    if angular_coeficient < 0.0{
        value = format!(" - {}x", (angular_coeficient * -1.0).to_string());
    }else if angular_coeficient > 0.0{
        value = format!(" - {}x", (angular_coeficient).to_string());
    }else{
        value = format!("");
    }
    return value;
}

fn linear_coeficient_reduced(xa:f64, ya:f64, xb:f64, yb:f64) -> String{
    let ya_yb:f64 = ya - yb;
    let xa_xb:f64 = xa - xb;
    let angular_coeficient:f64 = ya_yb / xa_xb;
    let angular_coeficient_xa:f64 = angular_coeficient * xa;
    let linear_coeficient:f64 = angular_coeficient_xa + ya;
    let value:String;
    if linear_coeficient < 0.0{
        value = format!(" - {}", (linear_coeficient * -1.0).to_string());
    }else if linear_coeficient > 0.0{
        value = format!(" + {}", (linear_coeficient).to_string());
    }else{
        value = format!("");
    }
    return value;
}

fn angular_coeficient_reduced(xa:f64, ya:f64, xb:f64, yb:f64) -> String{
    let ya_yb:f64 = ya - yb;
    let xa_xb:f64 = xa - xb;
    let angular_coeficient:f64 = ya_yb / xa_xb;
    let value:String;
    if angular_coeficient < 0.0{
        value = format!(" - {}x", (angular_coeficient * -1.0).to_string());
    }else if angular_coeficient > 0.0{
        value = format!(" {}x", (angular_coeficient).to_string());
    }else{
        value = format!("");
    
    }
    return value;
}

fn general_equation(xa:f64, ya:f64, xb:f64, yb:f64) -> String{
    let angular_coeficient:String = angular_coeficient_general(ya, yb);
    let linear_coeficient:String = linear_coeficient_general(xa, xb);
    let constant_coeficient:String = constant_coeficient_general(xa, ya, xb, yb);
    let general_equation:String = (format!("The general equation is: {}{}{}", angular_coeficient, linear_coeficient, constant_coeficient)).to_string();
    return  general_equation;
}

fn reduced_equation(xa:f64, ya:f64, xb:f64, yb:f64) -> String{
    let angular_coeficient:String = angular_coeficient_reduced(xa, ya, xb, yb);
    let linear_coeficient:String = linear_coeficient_reduced(xa, ya, xb, yb);
    let reduced_equation: String = (format!("The reduced equation is: {}{}", angular_coeficient, linear_coeficient)).to_string();
    return reduced_equation;
}

fn main() {
    let mut xa: String = String::new();
    print!("Inform XA value: ");
    let _error = stdout().flush();
    stdin().read_line(&mut xa).expect("Did not enter a correct string!");
    let xa: f64 = xa.trim().parse().expect("Invalid input.");
    let mut ya:String = String::new();
    print!("Inform YA value: ");
    let _error = stdout().flush();
    stdin().read_line(&mut ya).expect("Did not enter a correct string!");
    let ya: f64 = ya.trim().parse().expect("Invalid input.");
    let mut xb: String = String::new();
    print!("Inform XB value: ");
    let _error = stdout().flush();
    stdin().read_line(&mut xb).expect("Did not enter a correct string!");
    let xb: f64 = xb.trim().parse().expect("Invalid input.");
    let mut yb: String = String::new();
    print!("Inform YB value: ");
    let _error = stdout().flush();
    stdin().read_line(&mut yb).expect("Did not enter a correct string!");
    let yb: f64 = yb.trim().parse().expect("Invalid input.");
    let reduced_equation:String = reduced_equation(xa, ya, xb, yb);
    let general_equation:String = general_equation(xa, ya, xb, yb);
    println!("{}", reduced_equation);
    println!("{}", general_equation);
}