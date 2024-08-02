// storyboard_generator.cpp

#include <iostream>
#include <fstream>
#include <string>

extern "C" {
    // Прототипы функций
    int generate_storyboard(const char* osufile, const char* osbfile, const char* resourcefolder);
}

// Вспомогательная функция для записи текста в файл
void write_to_file(const std::string& filename, const std::string& text) {
    std::ofstream file(filename, std::ios::app); // Открытие файла для добавления текста
    if (file.is_open()) {
        file << text;
        file.close();
    } else {
        std::cerr << "Не удалось открыть файл для записи: " << filename << std::endl;
    }
}

int generate_storyboard(const char* osufile, const char* osbfile, const char* resourcefolder) {
    // Преобразуем входные параметры в строки
    std::string osu_file(osufile);
    std::string osb_file(osbfile);
    std::string resource_folder(resourcefolder);

    // Основной текст storyboard
    const std::string basetext = "[Events]\n"
        "//Background and Video events\n"
        "//Storyboard Layer 0 (Background)\n"
        "//Storyboard Layer 1 (Fail)\n"
        "//Storyboard Layer 2 (Pass)\n"
        "//Storyboard Layer 3 (Foreground)\n"
        "Sprite,Foreground,Centre,\"SB\\approachcircle.png\",0,0\n"
        " M,0,0,,200,400\n"
        " F,0,0,,0,1\n"
        " S,0,0,,0.51\n"
        " F,0,351327,,1,0\n"
        "Sprite,Foreground,Centre,\"SB\\taikobigcircle.png\",0,0\n"
        " M,0,0,,200,400\n"
        " F,0,0,,0,1\n"
        " S,0,0,,0.48\n"
        " C,0,0,,211,211,211\n"
        " F,0,351327,,1,0\n"
        "Sprite,Foreground,Centre,\"SB\\approachcircle.png\",0,0\n"
        " M,0,0,,280,400\n"
        " F,0,0,,0,1\n"
        " S,0,0,,0.51\n"
        " F,0,351327,,1,0\n"
        "Sprite,Foreground,Centre,\"SB\\taikobigcircle.png\",0,0\n"
        " M,0,0,,280,400\n"
        " F,0,0,,0,1\n"
        " S,0,0,,0.48\n"
        " C,0,0,,211,211,211\n"
        " F,0,351327,,1,0\n"
        "Sprite,Foreground,Centre,\"SB\\approachcircle.png\",0,0\n"
        " M,0,0,,360,400\n"
        " F,0,0,,0,1\n"
        " S,0,0,,0.51\n"
        " F,0,351327,,1,0\n"
        "Sprite,Foreground,Centre,\"SB\\taikobigcircle.png\",0,0\n"
        " M,0,0,,360,400\n"
        " F,0,0,,0,1\n"
        " S,0,0,,0.48\n"
        " C,0,0,,211,211,211\n"
        " F,0,351327,,1,0\n"
        "Sprite,Foreground,Centre,\"SB\\approachcircle.png\",0,0\n"
        " M,0,0,,440,400\n"
        " F,0,0,,0,1\n"
        " S,0,0,,0.51\n"
        " F,0,351327,,1,0\n"
        "Sprite,Foreground,Centre,\"SB\\taikobigcircle.png\",0,0\n"
        " M,0,0,,440,400\n"
        " F,0,0,,0,1\n"
        " S,0,0,,0.48\n"
        " C,0,0,,211,211,211\n"
        " F,0,351327,,1,0\n";

    // Записываем базовый текст в .osb файл
    write_to_file(osb_file, basetext);

    // Чтение .osu файла
    std::ifstream osu_file_stream(osu_file);
    if (!osu_file_stream.is_open()) {
        std::cerr << "Не удалось открыть .osu файл: " << osu_file << std::endl;
        return 1; // Код ошибки
    }

    std::string line;
    bool hitobjects = false;
    int loopcount = 0;

    while (std::getline(osu_file_stream, line)) {
        if (line == "[HitObjects]") {
            hitobjects = true;
            continue;
        }

        if (hitobjects) {
            // Разделяем строку на элементы
            size_t pos = 0;
            std::string token;
            std::string elements[6];
            int i = 0;
            while ((pos = line.find(',')) != std::string::npos) {
                token = line.substr(0, pos);
                elements[i++] = token;
                line.erase(0, pos + 1);
            }
            elements[i] = line;

            // Извлекаем данные
            std::string timing = elements[2];
            std::string colour = elements[4];
            std::string spinner = elements[5];

            int timing_not_done;
            if (false /* Проверка на DTCheckBox */) {
                timing_not_done = std::stoi(timing) - 1800;
            } else {
                timing_not_done = std::stoi(timing) - 1200;
            }
            int timing_done = std::stoi(timing);

            loopcount++;

            // Формируем текст для разных типов hitobject
            std::string redcircle = "Sprite,Foreground,Centre,\"SB\\taikohitcircle.png\",0,197\n"
                " MX,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",280\n"
                " MY,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",-640,400\n"
                " F,0," + std::to_string(timing_done) + ",,1,0\n"
                " S,0," + std::to_string(timing_done) + ",,0.456\n"
                " C,0," + std::to_string(timing_done) + ",,235,69,44\n"
                "Sprite,Foreground,Centre,\"SB\\taikohitcircleoverlay.png\",0,197\n"
                " MX,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",280\n"
                " MY,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",-640,400\n"
                " F,0," + std::to_string(timing_done) + ",,1,0\n"
                " S,0," + std::to_string(timing_done) + ",,0.456\n";

            std::string redbig = "Sprite,Foreground,Centre,\"SB\\taikohitcircle.png\",0,197\n"
                " MX,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",360\n"
                " MY,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",-640,400\n"
                " F,0," + std::to_string(timing_done) + ",,1,0\n"
                " S,0," + std::to_string(timing_done) + ",,0.456\n"
                " C,0," + std::to_string(timing_done) + ",,235,69,44\n"
                "Sprite,Foreground,Centre,\"SB\\taikohitcircleoverlay.png\",0,197\n"
                " MX,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",360\n"
                " MY,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",-640,400\n"
                " F,0," + std::to_string(timing_done) + ",,1,0\n"
                " S,0," + std::to_string(timing_done) + ",,0.456\n";

            std::string bluecircle = "Sprite,Foreground,Centre,\"SB\\taikohitcircle.png\",0,197\n"
                " MX,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",200\n"
                " MY,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",-640,400\n"
                " F,0," + std::to_string(timing_done) + ",,1,0\n"
                " S,0," + std::to_string(timing_done) + ",,0.456\n"
                " C,0," + std::to_string(timing_done) + ",,67,142,172\n"
                "Sprite,Foreground,Centre,\"SB\\taikohitcircleoverlay.png\",0,197\n"
                " MX,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",200\n"
                " MY,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",-640,400\n"
                " F,0," + std::to_string(timing_done) + ",,1,0\n"
                " S,0," + std::to_string(timing_done) + ",,0.456\n";

            std::string bluebig = "Sprite,Foreground,Centre,\"SB\\taikohitcircle.png\",0,197\n"
                " MX,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",440\n"
                " MY,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",-640,400\n"
                " F,0," + std::to_string(timing_done) + ",,1,0\n"
                " S,0," + std::to_string(timing_done) + ",,0.456\n"
                " C,0," + std::to_string(timing_done) + ",,67,142,172\n"
                "Sprite,Foreground,Centre,\"SB\\taikohitcircleoverlay.png\",0,197\n"
                " MX,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",440\n"
                " MY,0," + std::to_string(timing_not_done) + "," + std::to_string(timing_done) + ",-640,400\n"
                " F,0," + std::to_string(timing_done) + ",,1,0\n"
                " S,0," + std::to_string(timing_done) + ",,0.456\n";

            // Вставляем соответствующий текст в .osb файл
            if (colour == "1") {
                write_to_file(osb_file, redcircle);
            } else if (colour == "2") {
                write_to_file(osb_file, redbig);
            } else if (colour == "3") {
                write_to_file(osb_file, bluecircle);
            } else if (colour == "4") {
                write_to_file(osb_file, bluebig);
            }
        }
    }

    osu_file_stream.close();
    return 0; // Успешное завершение
}
