with open("test.txt", "w")as file:
    file.writelines(["안녕하세요.",\
        "중바꿈이 될까요",\
        "안될까요?",\
        "띄어쓰기라도 하지 않을까요?"])

    file.writelines([True, 273, "문자열"])