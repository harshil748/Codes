fn main() {
    // Basic printing with println! (adds a newline)
    println!("Hello, world!");
    
    // Basic printing with print! (no newline)
    print!("Hello, ");
    print!("Rust!\n");
    
    // Printing variables
    let name = "Rust";
    let version = 2023;
    println!("Programming in {} in {}", name, version);
    
    // Printing with named parameters
    println!("Language: {language}, Year: {year}", language = name, year = version);
    
    // Printing with debug formatting
    let numbers = vec![1, 2, 3];
    println!("Debug output: {:?}", numbers);
    println!("Pretty debug output: {:#?}", numbers);
    
    // Error stream printing
    eprintln!("This goes to stderr");
}
