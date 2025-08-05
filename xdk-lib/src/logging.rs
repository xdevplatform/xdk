use colored::*;

pub fn info(message: &str) {
    println!("{}", message);
}

pub fn success(message: &str) {
    println!("{}", message.green());
}

#[allow(dead_code)]
pub fn warn(message: &str) {
    eprintln!("{}", message.yellow());
}

pub fn error(message: &str) {
    eprintln!("{}", message.red());
}

#[macro_export]
macro_rules! log_info {
    ($($arg:tt)*) => { $crate::logging::info(&format!($($arg)*)) };
}

#[macro_export]
macro_rules! log_success {
    ($($arg:tt)*) => { $crate::logging::success(&format!($($arg)*)) };
}

#[macro_export]
macro_rules! log_warn {
    ($($arg:tt)*) => { $crate::logging::warn(&format!($($arg)*)) };
}

#[macro_export]
macro_rules! log_error {
    ($($arg:tt)*) => { $crate::logging::error(&format!($($arg)*)) };
}
