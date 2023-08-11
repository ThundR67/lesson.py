# Option
```rust
enum Option<T> {
    Some(T),
    None,
}

let a: Option<i32> = Some(5);
let hello: Option<&str> = None;
```
In rust, Option is an enum with two variants. It can either have some value, or be None. It is used to represent the presence or absence of a value.

# How To Use Option
```rust
fn divide(numerator: f64, denominator: f64) -> Option<f64> {
    if denominator == 0.0 {
        return None;
    }
    
    Some(numerator / denominator)
}
```
This division function will return None if denominator is 0.
Otherwise it will return the value wrapped in Some.

# Unwrap Method
```rust
let wrapped_result = divide(4.0, 2.0);
let result = wrapped_result.unwrap();
println!("{result}"); // 2.0
```
You cannot straight away use option returned by divide. You must handle the option. Easiest way is to use unwrap method. This will give you the inner result.


# Unwrap Panic
```rust
let wrapped_result = divide(4.0, 0.0);
let result = wrapped_result.unwrap();
println!("{result}"); 
// thread 'main' panicked 
// `Option::unwrap()` on a `None` value'
```
However, it will panic if the option is None. So use it only if the whole program is useless without the value. Like when loading a config file.

# Match
```rust
let result = divide(4.0, 2.0);
match result {
    Some(x) => println!("Result -> {x}"),
    None => println!("Division Failed"),
}
// Result -> 2.0
```
One safe way is to use match.

# Unwrap_or Method
```rust
let wrapped_result = divide(4.0, 2.0);
let result = wrapped_result.unwrap_or(0.0);
println!("{result}"); // 2.0


let wrapped_result = divide(4.0, 0.0);
let result = wrapped_result.unwrap_or(0.0);
println!("{result}"); // 0.0
```
Other safe way is to use unwrap or method. It will return the actual value if the option is Some. Otherwise it will return the default value passed to it.

# Unwrap_or_else Method
```rust
let wrapped_result = divide(4.0, 0.0);
let result = wrapped_result.unwrap_or_else(|| {
    println!("Division Failed");
    0.0
});
println!("{result}");
// Division Failed
// 0.0
```
You can use unwrap or else method. This will run the closure passed to it if the option is None and return its output.

# If Let Syntax
```rust
if let Some(result) = divide(4.0, 2.0) {
    println!("{result}");
} else {
    println!("Division Failed");
}
// 2.0
```
You can use if let statement to run code if the option is Some. You can then use else to run code if the option is None.

# Expect
```rust
let wrapped_result = divide(4.0, 0.0);
let result = wrapped_result.expect("Division Failed");
println!("{result}");
// thread 'main' panicked at 'Division Failed'
```
Lastly, you can use expect method. It is similar to using unwrap but it panics with custom message if the option is None.
