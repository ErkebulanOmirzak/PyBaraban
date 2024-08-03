mod ffi; // Подключение модуля ffi

use gtk4::prelude::*;
use gtk4::{Application, ApplicationWindow, Builder, Button, CheckButton, Entry};
use native_dialog::FileDialog;

fn main() {
    let app = Application::builder()
        .application_id("com.example.TaiBaran")
        .build();

    app.connect_activate(build_ui);

    app.run();
}

fn build_ui(app: &Application) {
    // Загрузка интерфейса из файла Glade
    let glade_src = include_str!("ui.glade");
    let builder = Builder::from_string(glade_src);

    // Основное окно
    let window: ApplicationWindow = builder
        .object("main_window")
        .expect("Не удалось получить main_window");

    // Строка для пути к файлу
    let file_entry: Entry = builder
        .object("file_entry")
        .expect("Не удалось получить file_entry");

    // Кнопка A
    let open_button: Button = builder
        .object("open_button")
        .expect("Не удалось получить open_button");

    let file_entry_clone = file_entry.clone();
    open_button.connect_clicked(move |_| {
        // Диалог для выбора файла
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
    let generate_button: Button = builder
        .object("generate_button")
        .expect("Не удалось получить generate_button");

    let file_entry_for_generate = file_entry.clone();
    let _check_button: CheckButton = builder
        .object("check_button")
        .expect("Не удалось получить check_button");

    generate_button.connect_clicked(move |_| {
        println!("Торпеда пошла");

        // Пример использования FFI
        let osufile = file_entry_for_generate.text().to_string();
        let osbfile = "output.osb";
        let resourcefolder = "resources/image";
        
        match crate::ffi::generate_storyboard_rust(&osufile, osbfile, resourcefolder) {
            Ok(_) => println!("Storyboard generated successfully"),
            Err(e) => eprintln!("Error generating storyboard: {}", e),
        }
    });

    // Показать окно
    window.set_application(Some(app));
    window.show();
}
