fn main() {
    // папка с C++ исходниками
    println!("cargo:rerun-if-changed=cpp");

    // билд C++ исходников
    cc::Build::new()
        .cpp(true)
        .files(vec!["cpp/storyboard_generator.cpp"]) // Указываем файлы для компиляции
        .include("cpp") // Указываем папку с заголовками, если есть
        .compile("storyboard_generator");

    // что надо пересобирать если изменится папка cpp
    println!("cargo:rerun-if-changed=cpp/storyboard_generator.cpp");
}