import array # с ним массивы красивее

baseText = (                                # статичные кружочки
    "[Events]\n"
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
    " F,0,351327,,1,0\n"
)

osufile = None # эта переменная должна присваивать путь к файлу .osu
osbfile = None # это то что редачится
resourcefolder = None
hitobjects = False # не понял что это ибо в коде оно по большей части для галочки даже в исходнике
fileselected = False
scanned = False # тригер того что файл выбрался и тем самым создает папку с текстурками ( я не добавил эту функцию)
filesadded = False
loopcount = None
check1 = None
check2 = None

def generate_storyboard():
    global osbfile, hitobjects, fileselected, osufile  # я хуй знает надо не надо но пусть будет глобальные переменные
    if fileselected and not hitobjects:  # тут мне чат жпт ебанул хз работает не работает
        with open(osbfile, 'w') as file:
            file.write(baseText)
        
        readCRINGE = []  # ну типа МАСИИИИИИИИИИИИИИИИИВ
        timing = []
        colour = []
        spinner = [] # хз нахуй оно надо если оно даже не читается адам сиякты
        
        
        with open(osufile, 'r') as file:
            lines = file.readlines()  # Читаем строки 
            for line in lines:
                line = line.strip()  # Убираю пробелы но пока не понял надо или нет!!!!!!!!!!!!!!!!!!!!!!!
                elements = line.split(',')  # хихи хаха запятые
                readCRINGE.append(elements)  # хихи хаха массив
                
                # тут должен был быть режим DT но мне лень её делать, там еще с таймингами ебаться
                
                timingnotdone = 0 # эта переменная относится к режиму DT мб кто то захочет это сделать 
                timingdone = timing
                
                if loopcount % 2 != 0:
                    check1 = timingdone
                else:
                    check2 = timingdone

                loopcount+1
                
                # внизу по названию сам понимаешь какие круглишки там
                
                redcircle = (
                    "Sprite,Foreground,Centre,\"SB\\taikohitcircle.png\",0,197\n"
                    " MX,0," + timingnotdone + "," + timingdone + ",280\n"
                    " MY,0," + timingnotdone + "," + timingdone + ",-640,400\n"
                    " F,0," + timingdone + ",,1,0\n"
                    " S,0," + timingdone + ",,0.456\n"
                    " C,0," + timingdone + ",,235,69,44\n"
                    "Sprite,Foreground,Centre,\"SB\\taikohitcircleoverlay.png\",0,197\n"
                    " MX,0," + timingnotdone + "," + timingdone + ",280\n"
                    " MY,0," + timingnotdone + "," + timingdone + ",-640,400\n"
                    " F,0," + timingdone + ",,1,0\n"
                    " S,0," + timingdone + ",,0.456\n"
                )

                redbig = (
                    "Sprite,Foreground,Centre,\"SB\\taikohitcircle.png\",0,197\n"
                    " MX,0," + timingnotdone + "," + timingdone + ",360\n"
                    " MY,0," + timingnotdone + "," + timingdone + ",-640,400\n"
                    " F,0," + timingdone + ",,1,0\n"
                    " S,0," + timingdone + ",,0.456\n"
                    " C,0," + timingdone + ",,235,69,44\n"
                    "Sprite,Foreground,Centre,\"SB\\taikohitcircleoverlay.png\",0,197\n"
                    " MX,0," + timingnotdone + "," + timingdone + ",360\n"
                    " MY,0," + timingnotdone + "," + timingdone + ",-640,400\n"
                    " F,0," + timingdone + ",,1,0\n"
                    " S,0," + timingdone + ",,0.456\n"
                )

                bluecircle = (
                    "Sprite,Foreground,Centre,\"SB\\taikohitcircle.png\",0,197\n"
                    " MX,0," + timingnotdone + "," + timingdone + ",200\n"
                    " MY,0," + timingnotdone + "," + timingdone + ",-640,400\n"
                    " F,0," + timingdone + ",,1,0\n"
                    " S,0," + timingdone + ",,0.456\n"
                    " C,0," + timingdone + ",,67,142,172\n"
                    "Sprite,Foreground,Centre,\"SB\\taikohitcircleoverlay.png\",0,197\n"
                    " MX,0," + timingnotdone + "," + timingdone + ",200\n"
                    " MY,0," + timingnotdone + "," + timingdone + ",-640,400\n"
                    " F,0," + timingdone + ",,1,0\n"
                    " S,0," + timingdone + ",,0.456\n"
                )

                bluebig = (
                    "Sprite,Foreground,Centre,\"SB\\taikohitcircle.png\",0,197\n"
                    " MX,0," + timingnotdone + "," + timingdone + ",440\n"
                    " MY,0," + timingnotdone + "," + timingdone + ",-640,400\n"
                    " F,0," + timingdone + ",,1,0\n"
                    " S,0," + timingdone + ",,0.456\n"
                    " C,0," + timingdone + ",,67,142,172\n"
                    "Sprite,Foreground,Centre,\"SB\\taikohitcircleoverlay.png\",0,197\n"
                    " MX,0," + timingnotdone + "," + timingdone + ",440\n"
                    " MY,0," + timingnotdone + "," + timingdone + ",-640,400\n"
                    " F,0," + timingdone + ",,1,0\n"
                    " S,0," + timingdone + ",,0.456\n"
                )

                bluestream = (
                    "Sprite,Foreground,Centre,\"SB\\taikohitcircle.png\",0,197\n"
                    " MX,0," + timingnotdone + "," + timingdone + ",200\n"
                    " MY,0," + timingnotdone + "," + timingdone + ",-480,465\n"
                    " F,0," + timingdone + ",,1,0\n"
                    " S,0," + timingdone + ",,0.456\n"
                    " C,0," + timingdone + ",,67,142,172\n"
                    "Sprite,Foreground,Centre,\"SB\\taikohitcircleoverlay.png\",0,197\n"
                    " MX,0," + timingnotdone + "," + timingdone + ",200\n"
                    " MY,0," + timingnotdone + "," + timingdone + ",-480,465\n"
                    " F,0," + timingdone + ",,1,0\n"
                    " S,0," + timingdone + ",,0.456\n"
                )
                
                # очень кривая логика счета что куда сувать, но зато сука работает 
                
                if spinner[0] != 48:
                    loopcount -= 1  # Уменьшаем loopcount на 1, хз нахуя
                elif colour == "12" or colour == "6":
                    with open(osbfile, 'a') as file:
                        file.write(bluebig + bluecircle)  # Запись в файл (остальные не буду обозначать)
                elif colour == "4":
                    with open(osbfile, 'a') as file:
                        file.write(redbig + redcircle)
                elif loopcount > 1:
                    if colour == "8" or colour == "2": 
                        if check1 - check2 < 100:
                            with open(osbfile, 'a') as file:
                                file.write(bluestream)
                                loopcount -= 1  # Уменьшаем loopcount на 1, мой сын Гитлер
                                check1 = check2
                        else:
                            with open(osbfile, 'a') as file:
                                file.write(bluecircle)
                    elif colour == "0":
                        with open(osbfile, 'a') as file:
                            file.write(redcircle)
            
            # тут надо функцию спавна текстурок и как я понял .osb файла, надо же что то редачить. Не сделал ибо законектить интерфейс может быть не удобным

            # а еще нужна функция "Selection", та же самая хуйня



                
                

