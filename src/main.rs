use std::io;

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

fn reduced_equation(xa:f64, ya:f64, xb:f64, yb:f64) -> String{
    let angular_coeficient:String = angular_coeficient_reduced(xa, ya, xb, yb);
    let linear_coeficient:String = linear_coeficient_reduced(xa, ya, xb, yb);
    let reduced_equation: String = (format!("The reduced equation is: {:?}{:?}", angular_coeficient, linear_coeficient)).to_string();
    return reduced_equation;
}

fn main(){
    
    let mut xa = String::new();
    io::stdin().read_line(&mut xa).expect("Failed to read input.");
    let xa: f64 = xa.trim().parse().expect("Invalid input.");
    
    let mut ya = String::new();
    io::stdin().read_line(&mut ya).expect("Failed to read input.");
    let ya: f64 = ya.trim().parse().expect("Invalid input.");
    
    let mut xb = String::new();
    io::stdin().read_line(&mut xb).expect("Failed to read input.");
    let xb: f64 = xb.trim().parse().expect("Invalid input.");

    let mut yb = String::new();
    io::stdin().read_line(&mut yb).expect("Failed to read input.");
    let yb: f64 = yb.trim().parse().expect("Invalid input.");

    let reduced_equation:String = reduced_equation(xa, ya, xb, yb);

    println!("{:?}", reduced_equation);

}