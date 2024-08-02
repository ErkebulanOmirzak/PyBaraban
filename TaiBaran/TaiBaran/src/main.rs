mod ffi; // Подключение модуля ffi

use gtk4::prelude::*;
use gtk4::{Application, ApplicationWindow, Box, Button, CheckButton, Entry};
use native_dialog::FileDialog;

fn main() {
    let app = Application::builder()
        .application_id("com.example.TaiBaran")
        .build();

    app.connect_activate(build_ui);

    app.run();
}

fn build_ui(app: &Application) {
    // Основное окно
    let window = ApplicationWindow::builder()
        .application(app)
        .title("TaiBaran")
        .default_width(300)
        .default_height(200)
        .build();

    // Основной контейнер
    let vbox = Box::new(gtk4::Orientation::Vertical, 10);

    // Строка для пути к файлу
    let file_entry = Entry::new();
    file_entry.set_placeholder_text(Some("маршрут до параши"));

    // Кнопка A
    let open_button = Button::with_label("Дифу блядь сюда мне");
    let file_entry_clone = file_entry.clone(); // Создание клона для замыкания
    open_button.connect_clicked(move |_| {
        // диалог для выбора файла
        match FileDialog::new()
            .add_filter("osu! Files", &["osu"])
            .show_open_single_file() 
        {
            Ok(Some(path)) => file_entry_clone.set_text(path.to_str().unwrap()),
            Ok(None) => println!("Э бля дифа где"),
            Err(e) => eprintln!("Фу бля: {}", e),
        }
    });

    // Кнопка B
    let generate_button = Button::with_label("Высрать");
    let file_entry_for_generate = file_entry.clone(); // Создание клона для замыкания
    generate_button.connect_clicked(move |_| {
        println!("Торпеда пошла");

        // Пример использования FFI
        let osufile = file_entry_for_generate.text().to_string(); // Исправлено
        let osbfile = "output.osb";
        let resourcefolder = "resources/image";
        
        match crate::ffi::generate_storyboard_rust(&osufile, osbfile, resourcefolder) {
            Ok(_) => println!("Storyboard generated successfully"),
            Err(e) => eprintln!("Error generating storyboard: {}", e),
        }
    });

    // Галочка
    let check_button = CheckButton::with_label("спидозник ебаный");

    // элементы в контейнере
    vbox.append(&file_entry);
    vbox.append(&open_button);
    vbox.append(&generate_button);
    vbox.append(&check_button);

    // рожаем контейнер в основное окно
    window.set_child(Some(&vbox));
    window.show();
}
