mod angular_coeficient_reduced;
mod linear_coeficient_reduced;

pub fn reduced_equation(xa:f64, ya:f64, xb:f64, yb:f64){
    let angular_coeficient:() = angular_coeficient_reduced::angular_coeficient_reduced(xa, ya, xb, yb);
    let linear_coeficient_reduced:() = linear_coeficient_reduced::linear_coeficient_reduced(xa, ya, xb, yb);
}